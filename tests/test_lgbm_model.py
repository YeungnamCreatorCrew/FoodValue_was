"""LightGBM 모델(model_comparison/lightgbm) 단위 테스트. 가짜 데이터만 쓰고 스냅샷은 읽지 않는다.

    uv run --group dev --extra prices pytest tests/test_lgbm_model.py -q
"""
import json
from datetime import date, timedelta
from pathlib import Path

import numpy as np
import pytest

pytest.importorskip('lightgbm')

from model_comparison.lightgbm.model import LGBMModel  # noqa: E402
from tools import standard  # noqa: E402
from tools.runtime import OriginInputs, TrainingData  # noqa: E402

CONFIG = Path(__file__).resolve().parents[1] / 'model_comparison' / 'lightgbm' / 'config.json'
PRICE_COLS = ('current', 'lag1', 'lag7', 'lag14', 'lag28', 'mean7', 'mean28', 'volatility7')  # 원 단위 열


def config_params():
    return json.loads(CONFIG.read_text(encoding='utf-8'))['params']


def fake_rows(n_origins=200, scale=1.0, extra=(), seed=0):
    """가격 무작위 걸음으로 (기준일 × h=1..7) 학습 표본을 만든다. 열 순서는 base_v1 + extra."""
    rng = np.random.default_rng(seed)
    price = 3000 * np.exp(np.cumsum(rng.normal(0, 0.02, n_origins + 40)))
    names = list(standard.BASE_FEATURES) + list(extra)
    start = date(2020, 1, 1)
    feats, targets, horizons, origins = [], [], [], []
    for t in range(28, n_origins + 28):
        cur = price[t]
        base = {'current': cur, 'lag1': price[t - 1], 'lag7': price[t - 7], 'lag14': price[t - 14],
                'lag28': price[t - 28], 'mean7': price[t - 6:t + 1].mean(), 'mean28': price[t - 27:t + 1].mean(),
                'change7': cur / price[t - 7] - 1, 'volatility7': price[t - 6:t + 1].std(), 'price_age': 0,
                'days_since_kind_switch': 90}
        for h in range(1, 8):
            d = start + timedelta(days=t)
            row = dict(base, target_weekday=(d + timedelta(days=h)).weekday(), horizon=h,
                       target_season_sin=np.sin(2 * np.pi * (t + h) / 365.25),
                       target_season_cos=np.cos(2 * np.pi * (t + h) / 365.25))
            for i, name in enumerate(extra):
                row[name] = np.nan if (t + i) % 3 == 0 else rng.normal()  # 외부변수: 1/3이 결측
            values = [row[n] for n in names]
            for n in PRICE_COLS:
                values[names.index(n)] *= scale
            feats.append(values)
            targets.append(price[t + h] * scale)
            horizons.append(h)
            origins.append(d)
    return names, np.array(feats, dtype=float), np.array(targets), np.array(horizons), origins


def train_and_inputs(params, **kw):
    names, X, y, h, origins = fake_rows(**kw)
    last = origins[-1]
    train = [o < last for o in origins]
    history = TrainingData(series_id=1, as_of=last, features=X[train], targets=y[train], horizons=h[train],
                           origins=[o for o, keep in zip(origins, train) if keep], feature_names=names)
    test = ~np.array(train)
    inputs = OriginInputs(series_id=1, origin=last, feature_names=names,
                          features={int(hh): row for hh, row in zip(h[test], X[test])})
    model = LGBMModel(**params)
    model.fit(history, seed=42)
    return model, inputs


@pytest.mark.parametrize('strategy', ['direct_per_horizon', 'pooled_horizon'])
def test_predict_returns_seven_positive_prices(strategy):
    model, inputs = train_and_inputs({**config_params(), 'strategy': strategy})
    out = model.predict(inputs)
    assert len(out) == 7
    assert all(isinstance(v, float) and v > 0 for v in out)


def test_nan_in_extra_features_is_accepted():
    """2차 외부변수는 결측을 NaN 그대로 넘긴다(§5.2). LightGBM 기본 결측 처리로 학습·예측해야 한다."""
    model, inputs = train_and_inputs(config_params(), extra=standard.EXTRA_BUNDLES['MARKET'])
    for row in inputs.features.values():
        row[-4:] = np.nan  # 예측 입력의 외부변수가 모두 비어도
    out = model.predict(inputs)
    assert len(out) == 7 and all(np.isfinite(out))


def test_same_seed_gives_identical_predictions():
    a, inputs = train_and_inputs(config_params())
    b, _ = train_and_inputs(config_params())
    assert a.predict(inputs) == b.predict(inputs)


def test_relative_features_make_predictions_scale_with_price_level():
    """relative_features + keep_current=false + log_ratio: 가격 수준을 k배 하면 예측도 정확히 k배."""
    params = config_params()
    assert params['relative_features'] and not params['keep_current'] and params['target_transform'] == 'log_ratio'
    base, inputs = train_and_inputs(params, scale=1.0)
    scaled, inputs_k = train_and_inputs(params, scale=3.0)
    np.testing.assert_allclose(np.array(scaled.predict(inputs_k)), 3.0 * np.array(base.predict(inputs)), rtol=1e-9)


def test_missing_horizon_booster_returns_none():
    model, inputs = train_and_inputs(config_params())
    del model.boosters[7]
    out = model.predict(inputs)
    assert out[6] is None and all(v is not None for v in out[:6])


def test_config_top_level_matches_params():
    config = json.loads(CONFIG.read_text(encoding='utf-8'))
    assert config['target_transform'] == config['params']['target_transform']
    assert config['strategy'] == config['params']['strategy']
    assert config['params']['num_threads'] == 4 and config['params']['deterministic']


@pytest.mark.parametrize('bad', [{'target_transform': 'sqrt'}, {'strategy': 'recursive'}])
def test_invalid_options_raise(bad):
    with pytest.raises(ValueError):
        LGBMModel(**{**config_params(), **bad})
