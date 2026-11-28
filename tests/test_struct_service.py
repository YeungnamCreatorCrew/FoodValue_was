import csv
import json
from datetime import date
from pathlib import Path

import pytest

from app.services import struct_service

SNAPSHOT = struct_service.ROOT / 'data' / 'snapshots' / 'fv-snap-20261031-v1'
RESULTS = struct_service.ROOT / 'model_comparison' / 'structural' / 'results' / 'val-t18' / 'predictions.csv'
PARAMS = struct_service.ROOT / 'model_comparison' / 'structural' / 'final_params_t18_20250602.json'
REFIT_DAY = date(2025, 6, 2)  # 월요일(실험 재학습일). 계수 사본이 남아 있는 날


@pytest.fixture(scope='module')
def refit_day():
    if not SNAPSHOT.exists():
        pytest.skip('실험 스냅샷이 없음(Git 밖)')
    from tools import loader
    snap = loader.Snapshot(SNAPSHOT)
    return snap, struct_service.forecast(snap, REFIT_DAY, log=lambda *_: None)


def test_service_forecast_matches_validation_run_on_refit_day(refit_day):
    _, result = refit_day
    expected = {}
    with open(RESULTS, encoding='utf-8', newline='') as f:
        for row in csv.DictReader(f):
            if row['origin_date'] == REFIT_DAY.isoformat():
                expected.setdefault(int(row['series_id']), []).append(float(row['predicted_price']) if row['status'] == 'OK' else None)
    assert set(expected) == set(result)
    for sid, prices in expected.items():
        assert result[sid].prices == prices, sid


def test_service_parameters_match_saved_coefficients(refit_day):
    _, result = refit_day
    saved = json.loads(PARAMS.read_text(encoding='utf-8'))
    for sid, p in saved.items():
        got = result[int(sid)].parameters
        assert got['kH'] == p['k_h'] and got['lambda'] == p['lambda']
        assert got['coef'] == pytest.approx(p['coef'], rel=1e-9, abs=1e-12)


def test_explanation_sums_to_prediction_and_wholesale_has_none(refit_day):
    snap, result = refit_day
    for sid, f in result.items():
        if snap.series[sid].market == 'WHOLESALE':
            assert f.explanation is None and f.explanation_error == ''
            continue
        e = f.explanation
        assert e is not None and e.method == struct_service.METHOD and e.base_price == e.current_price
        assert e.base_price + sum(e.contributions.values()) == pytest.approx(f.prices[6], abs=0.5)
        assert set(e.contributions) <= {'counter_change7', 'target_counter_ratio', struct_service.SEASON_FACTOR,
                                        'target_in_event_window', 'target_prev_day_holiday'}
        assert struct_service.SEASON_FACTOR not in e.history and len(e.history['counter_change7']) == 90


def test_market_comes_from_snapshot_not_experiment_ids():
    from types import SimpleNamespace
    snap = SimpleNamespace(series_ids=[60, 61, 9001], series={60: SimpleNamespace(market='RETAIL'), 61: SimpleNamespace(market='WHOLESALE'),
                                                              9001: SimpleNamespace(market='RETAIL')})
    params = struct_service.model_params(snap, {'params': {'wholesale_terms': []}})
    assert params['retail_series'] == [60, 9001] and params['wholesale_series'] == [61]
