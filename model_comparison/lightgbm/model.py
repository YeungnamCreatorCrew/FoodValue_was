"""LightGBM 가격 예측 모델 (담당 B, 기준서 v1 §9 인터페이스).

    uv run --extra prices python -m tools.run_backtest --config model_comparison/lightgbm/config.json \\
        --phase smoke --month 2025-01 --series 1,9001 --out runs

설정(params) 중 모델 쪽에서 해석하는 키 (나머지는 LightGBM 파라미터로 그대로 전달):
- target_transform: 'log_ratio'  log(y / current)   — 기본
                    'ratio'      y / current - 1
                    'level'      y (원 단위 그대로)
- strategy: 'direct_per_horizon'  시점 h(1~7)마다 모델 1개, horizon 특징 제외 — 기본
            'pooled_horizon'      시점 통합 모델 1개, horizon 특징 포함
- n_estimators: 부스팅 반복 수
- early_stopping_rounds: 0이면 끔. 쓰면 학습 표본의 마지막 20%(기준일 시간순)로 판단(§6)
- drop_features: 뺄 기본 특징 이름 목록 (예: ["days_since_kind_switch"])
- relative_features: true면 원 단위 특징을 current 대비 비율로 바꾼다(정보 추가 없음, 같은 15개 특징의 결정적 변환).
    lag1·lag7·lag14·lag28·mean7·mean28 → x / current - 1, volatility7 → volatility7 / current.
    트리는 학습 범위 밖 가격 수준으로 외삽하지 못하므로 수준 대신 상대값을 쓰게 한다. 기본 false
- keep_current: relative_features일 때 current(원) 자체를 특징으로 남길지. 기본 true

config.json의 최상위 target_transform·strategy는 params의 같은 키와 반드시 같게 둔다(기록용).
결정적 실행 옵션(deterministic·force_row_wise·num_threads=4·seed)은 항상 강제한다(§6).
"""
import numpy as np

from tools.runtime import OriginInputs, TrainingData

TRANSFORMS = ('log_ratio', 'ratio', 'level')
STRATEGIES = ('direct_per_horizon', 'pooled_horizon')
MODEL_KEYS = ('target_transform', 'strategy', 'n_estimators', 'early_stopping_rounds', 'drop_features',
              'relative_features', 'keep_current')
RELATIVE = ('lag1', 'lag7', 'lag14', 'lag28', 'mean7', 'mean28')
FORCED = {'deterministic': True, 'force_row_wise': True, 'num_threads': 4, 'verbosity': -1}


class LGBMModel:
    def __init__(self, **params):
        self.params = dict(params)
        self.transform = params.get('target_transform', 'log_ratio')
        self.strategy = params.get('strategy', 'direct_per_horizon')
        if self.transform not in TRANSFORMS:
            raise ValueError(f'target_transform={self.transform!r}, 가능: {TRANSFORMS}')
        if self.strategy not in STRATEGIES:
            raise ValueError(f'strategy={self.strategy!r}, 가능: {STRATEGIES}')
        self.n_estimators = int(params.get('n_estimators', 300))
        self.early_stopping = int(params.get('early_stopping_rounds', 0))
        self.drop = set(params.get('drop_features', []))
        self.relative = bool(params.get('relative_features', False))
        if self.relative and not params.get('keep_current', True):
            self.drop.add('current')
        self.lgb_params = {k: v for k, v in params.items() if k not in MODEL_KEYS}
        self.lgb_params.setdefault('objective', 'regression')
        self.boosters = {}

    # 특징·목표 변환 ----------------------------------------------------------------------
    def _columns(self, names):
        drop = set(self.drop)
        if self.strategy == 'direct_per_horizon':
            drop.add('horizon')  # 시점별 모델에서는 상수
        return [i for i, n in enumerate(names) if n not in drop]

    def _prepare(self, X, names):
        """원본 특징 행렬(n × 15) → 모델 입력. relative_features면 원 단위 열을 current 대비 값으로."""
        X = np.array(X, dtype=float)
        if self.relative:
            current = X[:, names.index('current')]
            for n in RELATIVE:
                i = names.index(n)
                X[:, i] = X[:, i] / current - 1.0
            i = names.index('volatility7')
            X[:, i] = X[:, i] / current
        return X[:, self.cols]

    def _to_target(self, y, current):
        if self.transform == 'log_ratio':
            return np.log(y / current)
        if self.transform == 'ratio':
            return y / current - 1.0
        return y

    def _from_target(self, z, current):
        if self.transform == 'log_ratio':
            return current * np.exp(z)
        if self.transform == 'ratio':
            return current * (1.0 + z)
        return z

    def _train(self, X, z, origins, seed):
        import lightgbm as lgb

        params = {**self.lgb_params, **FORCED, 'seed': seed}
        if self.early_stopping <= 0:
            return lgb.train(params, lgb.Dataset(X, z), num_boost_round=self.n_estimators)
        # 기준일 시간순 마지막 20%로 조기 종료 (같은 기준일이 학습·판단에 나뉘지 않게 기준일로 자름)
        unique = np.unique(origins)
        cut = unique[int(len(unique) * 0.8)]
        fit_mask = origins < cut
        train = lgb.Dataset(X[fit_mask], z[fit_mask])
        valid = lgb.Dataset(X[~fit_mask], z[~fit_mask], reference=train)
        return lgb.train(params, train, num_boost_round=self.n_estimators, valid_sets=[valid],
                         callbacks=[lgb.early_stopping(self.early_stopping, verbose=False)])

    # 인터페이스 ----------------------------------------------------------------------------
    def fit(self, history: TrainingData, seed: int) -> None:
        self.names = list(history.feature_names)
        self.cur = self.names.index('current')
        self.cols = self._columns(self.names)
        X_all = np.asarray(history.features, dtype=float)
        y = np.asarray(history.targets, dtype=float)
        h_all = np.asarray(history.horizons, dtype=int)
        origins = np.array([o.toordinal() for o in history.origins])
        z = self._to_target(y, X_all[:, self.cur])
        X = self._prepare(X_all, self.names)
        if self.strategy == 'pooled_horizon':
            self.boosters = {0: self._train(X, z, origins, seed)}
        else:
            self.boosters = {h: self._train(X[h_all == h], z[h_all == h], origins[h_all == h], seed)
                             for h in np.unique(h_all)}

    def predict(self, inputs: OriginInputs) -> list[float | None]:
        out = []
        for h in sorted(inputs.features):
            row = np.asarray(inputs.features[h], dtype=float)
            booster = self.boosters.get(0 if self.strategy == 'pooled_horizon' else h)
            if booster is None:
                out.append(None)
                continue
            z = booster.predict(self._prepare(row.reshape(1, -1), self.names))[0]
            out.append(float(self._from_target(z, row[self.cur])))
        return out
