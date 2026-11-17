"""v2 통합 학습 모델. 10개 계열 표본을 한 모델이 함께 배운다.

인터페이스(통합 실행기 run_pooled가 부름)
    fit(features, targets, horizons, feature_names, seed)   features: (표본 × 특징), targets: 목표일 가격(원)
    predict(features, horizons) -> 가격(원) 배열            실패한 행은 nan

계열마다 가격 수준이 달라(깐마늘 1만 원대, 대파 3천 원대) 그대로 섞으면 안 되므로
- 학습 대상: 변화율 y / current − 1
- 가격 수준 특징(lag·평균·변동성·상대 시장 가격)은 current 대비 비율로, current는 log로 바꾼다

표본 가중(설정 params의 아래 키, XGBoost로 넘기지 않음)
- series_weight: None | 'balanced'(계열마다 가중 합 같게) | 'inv_scale'(계열 변화율 크기 |y|의 평균으로 나눔
                 → 변동 큰 도매 계열이 손실을 독차지하지 않게. 평가가 계열 macro 평균이라 맞춘다)
- halflife_days: 목표일이 학습 시점보다 이만큼 오래되면 가중 1/2(최근 가격 흐름을 더 따름). None이면 균등
"""
from typing import ClassVar

import numpy as np

PRICE_LEVEL = ('lag1', 'lag7', 'lag14', 'lag28', 'mean7', 'mean28', 'volatility7', 'counter_price')


def relative(features, names):
    """가격 수준 특징 → current 대비 비율, current → log(current). 원본 배열은 바꾸지 않는다."""
    x = np.array(features, dtype=np.float64, copy=True)
    cur = names.index('current')
    current = x[:, cur].copy()
    with np.errstate(all='ignore'):
        for name in PRICE_LEVEL:
            if name in names:
                j = names.index(name)
                x[:, j] = x[:, j] / current - (0 if name == 'volatility7' else 1)
        x[:, cur] = np.log(current)
    return x, current


def sample_weights(y, groups, ages, series_weight=None, halflife_days=None):
    """표본 가중(평균 1). 둘 다 없으면 None."""
    if (series_weight is None or groups is None) and (halflife_days is None or ages is None):
        return None
    w = np.ones(len(y))
    if series_weight is not None and groups is not None:
        for g in np.unique(groups):
            rows = groups == g
            if series_weight == 'balanced':
                w[rows] /= rows.sum()
            elif series_weight == 'inv_scale':
                w[rows] /= max(float(np.nanmean(np.abs(y[rows]))), 1e-4)
            else:
                raise ValueError(f'모르는 series_weight: {series_weight}')
    if halflife_days is not None and ages is not None:
        w *= 0.5 ** (np.asarray(ages, dtype=float) / float(halflife_days))
    return w * (len(w) / w.sum())


class PooledXGB:
    """시점별 직접 모델 7개(기본) 또는 시점 통합 모델 1개(strategy='pooled_horizon')."""

    DEFAULTS: ClassVar[dict] = {'n_estimators': 300, 'max_depth': 4, 'learning_rate': 0.05, 'subsample': 0.8,
                'colsample_bytree': 0.6, 'min_child_weight': 20, 'reg_lambda': 10.0, 'objective': 'reg:squarederror'}
    FIXED: ClassVar[dict] = {'tree_method': 'hist', 'n_jobs': 4}

    def __init__(self, strategy='direct_per_horizon', series_weight=None, halflife_days=None, **params):
        self.strategy = strategy
        self.series_weight = series_weight
        self.halflife_days = halflife_days
        self.params = {**self.DEFAULTS, **params}

    def _make_model(self, seed):
        from xgboost import XGBRegressor

        return XGBRegressor(**self.params, **self.FIXED, random_state=seed)

    def fit(self, features, targets, horizons, feature_names, seed, groups=None, ages=None):

        self.names = list(feature_names)
        x, current = relative(features, self.names)
        y = np.asarray(targets, dtype=float) / current - 1
        h = np.asarray(horizons)
        self.drop = [] if self.strategy == 'pooled_horizon' else [self.names.index('horizon')]
        keep = [j for j in range(x.shape[1]) if j not in self.drop]
        self.keep = keep
        weight = sample_weights(y, groups, ages, self.series_weight, self.halflife_days)
        self.models = {}
        groups = [None] if self.strategy == 'pooled_horizon' else sorted(set(h.tolist()))
        for g in groups:
            rows = np.ones(len(h), bool) if g is None else h == g
            model = self._make_model(seed)
            w = None if weight is None else weight[rows]
            model.fit(x[rows][:, keep], y[rows], sample_weight=w)
            self.models[g] = model

    def predict(self, features, horizons):
        x, current = relative(features, self.names)
        h = np.asarray(horizons)
        out = np.full(len(h), np.nan)
        for g, model in self.models.items():
            rows = np.ones(len(h), bool) if g is None else h == g
            if rows.any():
                out[rows] = current[rows] * (1 + model.predict(x[rows][:, self.keep]))
        return out

    def importance(self):
        """특징 중요도(gain) 평균 — 어떤 자료가 기여했는지 보기용."""
        names = [self.names[j] for j in self.keep]
        total = np.zeros(len(names))
        for model in self.models.values():
            score = model.get_booster().get_score(importance_type='total_gain')
            total += np.array([score.get(f'f{j}', 0.0) for j in range(len(names))])
        return dict(sorted(zip(names, total / max(len(self.models), 1)), key=lambda kv: -kv[1]))


class PooledLGBM(PooledXGB):
    """PooledXGB와 같은 대상·특징 변환·가중, 모델만 LightGBM."""

    DEFAULTS: ClassVar[dict] = {'n_estimators': 300, 'num_leaves': 15, 'max_depth': -1, 'learning_rate': 0.05,
                                'subsample': 0.8, 'subsample_freq': 1, 'colsample_bytree': 0.6,
                                'min_child_samples': 50, 'reg_lambda': 10.0, 'objective': 'regression'}
    FIXED: ClassVar[dict] = {'n_jobs': 4, 'verbose': -1}

    def _make_model(self, seed):
        from lightgbm import LGBMRegressor

        return LGBMRegressor(**self.params, **self.FIXED, random_state=seed)

    def importance(self):
        names = [self.names[j] for j in self.keep]
        total = np.zeros(len(names))
        for model in self.models.values():
            total += model.booster_.feature_importance(importance_type='gain')
        return dict(sorted(zip(names, total / max(len(self.models), 1)), key=lambda kv: -kv[1]))
