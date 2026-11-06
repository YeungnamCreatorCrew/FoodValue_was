"""외부변수 묶음 가중치. 합성 오차로 신호·잡음·중복 묶음을 구분하는지 검증한다."""
import random

import numpy as np
import pytest

from app.services import weighting


def samples(count=700, signal=1.0, noise_scale=.02, duplicate=False, seed=3):
    """기준 예측의 오차 중 signal 비율만큼을 MARKET 전문가가 맞힌다. MACRO 전문가는 무관한 잡음이다."""
    rng = random.Random(seed)
    rows = []
    for index in range(count):
        origin, horizon = index // 7, index % 7 + 1
        base = rng.gauss(0, .02)
        shock = rng.gauss(0, .03)
        truth = base + shock + rng.gauss(0, noise_scale)
        experts = {'MARKET': base + signal * shock, 'MACRO': base + rng.gauss(0, .03)}
        if duplicate:
            experts['COPY'] = experts['MARKET']
        rows.append((origin, origin + horizon, horizon, truth, base, experts))
    return rows


def test_signal_block_is_weighted_and_noise_block_is_zero():
    result = weighting.choose(samples(), ['MARKET', 'MACRO'])
    assert result.values['MARKET'] > .8 and result.values['MACRO'] < .05
    assert result.kappa is not None and result.samples == 700


def test_pure_noise_gets_no_weight():
    result = weighting.choose(samples(signal=0.0), ['MARKET', 'MACRO'])
    assert result.values == {'MARKET': 0.0, 'MACRO': 0.0} and result.kappa is None


def test_duplicate_blocks_share_weight_without_double_counting():
    result = weighting.choose(samples(duplicate=True), ['MARKET', 'MACRO', 'COPY'])
    assert result.values['MARKET'] + result.values['COPY'] == pytest.approx(1.0, abs=.15)
    assert all(0.0 <= value <= 1.0 for value in result.values.values())


def test_too_few_samples_or_stale_window_gives_zero():
    rows = samples()
    assert weighting.choose(rows[:weighting.MIN_SAMPLES - 1], ['MARKET', 'MACRO']).values == {'MARKET': 0.0, 'MACRO': 0.0}
    # 1년보다 오래된 표본은 빠진다. 최근 표본만으로 부족하면 0.
    old = [(o, t, h, y, b, e) for o, t, h, y, b, e in rows[:300]] + [(o + 1000, t + 1000, h, y, b, e) for o, t, h, y, b, e in rows[300:320]]
    assert weighting.choose(old, ['MARKET', 'MACRO']).samples == 20


def test_solver_respects_box_and_combine_formula():
    rng = np.random.default_rng(0)
    deltas = rng.normal(size=(200, 2))
    residuals = deltas @ np.array([1.8, -.5]) + rng.normal(scale=.01, size=200)
    w = weighting.solve(deltas, residuals, 0.0)
    assert w[0] == pytest.approx(1.0) and w[1] == pytest.approx(0.0)
    assert weighting.Weights({'A': .5, 'B': 0.0}).combine(.10, {'A': .20, 'B': .90}) == pytest.approx(.15)
