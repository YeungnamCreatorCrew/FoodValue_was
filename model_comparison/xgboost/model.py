"""XGBoost — 모델 비교 실험(기준서 v1) 제출용. 담당 A(명구).

운영 모델(app/services/price_prediction.py, direct-xgb-v5-huber)의 학습 방식을 기준서 인터페이스로 옮겼다.
- 전략: 시점 h(1~7)마다 따로 학습하는 직접 모델 7개
- 학습 대상: 변화율 y[d+h] / v[d] − 1 (가격 수준이 학습 범위를 벗어나도 한쪽으로 묶이지 않게)
- 예측 가격: current × (1 + 예측 변화율)
- 특징: 공통 로더의 base_v1 15개 중 시점마다 상수인 horizon을 뺀 14개
- 운영 모델에 있던 후보 선택·VALIDATED 관문·naive 복귀·가중 결합은 넣지 않는다(실패 시 naive 대체는 공통 평가기가 함)

결정적 실행(§1.3): tree_method='hist', n_jobs=4, random_state=seed.
"""
import numpy as np

# v5 운영 기본값(model_comparison/xgboost/README_MODEL.md). 튜닝은 설정 파일의 params로 덮어쓴다.
DEFAULT_PARAMS = {'n_estimators': 60, 'max_depth': 2, 'learning_rate': .05, 'subsample': 1.0, 'colsample_bytree': 1.0,
                  'min_child_weight': 10, 'reg_lambda': 10.0, 'objective': 'reg:pseudohubererror', 'huber_slope': .02}
FIXED = {'tree_method': 'hist', 'n_jobs': 4}
DROP_FEATURES = ('horizon',)


class XGBModel:
    def __init__(self, **params):
        fixed = {k: params.pop(k) for k in list(params) if k in FIXED}
        if fixed and fixed != {k: FIXED[k] for k in fixed}:
            raise ValueError(f'결정적 실행 옵션은 바꿀 수 없음: {FIXED}')
        unknown = set(params) - set(DEFAULT_PARAMS)
        if unknown:
            raise ValueError(f'모르는 파라미터: {sorted(unknown)}')
        self.params = {**DEFAULT_PARAMS, **params}
        if self.params['objective'] != 'reg:pseudohubererror':
            self.params.pop('huber_slope')  # 다른 손실에서는 쓰지 않는 값(경고만 나고 결과는 같음)

    def fit(self, history, seed: int) -> None:
        from xgboost import XGBRegressor

        names = list(history.feature_names)
        self.columns = [i for i, name in enumerate(names) if name not in DROP_FEATURES]
        self.current = names.index('current')
        features = np.asarray(history.features, dtype=float)
        targets = np.asarray(history.targets, dtype=float)
        horizons = np.asarray(history.horizons)
        change = targets / features[:, self.current] - 1
        self.models = {}
        for h in sorted(set(horizons.tolist())):
            rows = horizons == h
            model = XGBRegressor(**self.params, **FIXED, random_state=seed)
            model.fit(features[rows][:, self.columns], change[rows])
            self.models[h] = model

    def predict(self, inputs) -> list[float | None]:
        out = []
        for h in sorted(inputs.features):
            model = self.models.get(h)
            if model is None:
                out.append(None)
                continue
            row = np.asarray(inputs.features[h], dtype=float)
            change = float(model.predict(row[self.columns][None, :])[0])
            out.append(float(row[self.current]) * (1 + change))
        return out
