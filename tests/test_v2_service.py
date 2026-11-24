from datetime import date

import pytest

from app.services import v2_calibration, v2_ensemble, v2_service
from app.services.price_prediction import InsufficientDataError


def test_combine_averages_only_available_members():
    got = v2_ensemble.combine({'A': [100.0] + [None] * 6, 'B': [200.0] * 7, 'C': [None] * 7})
    assert got == [150.0] + [200.0] * 6
    assert v2_ensemble.combine({'A': [None] * 7}) == [None] * 7


def test_series_key_only_experiment_series():
    assert v2_service.series_key('대파', 'KAMIS', 'RETAIL') == '대파|RETAIL'
    assert v2_service.series_key('배추', 'MERGED', 'WHOLESALE') == '배추|WHOLESALE'
    assert v2_service.series_key('배추(월동)', 'KAMIS', 'RETAIL') is None
    assert v2_service.series_key('토마토', 'KAMIS', 'RETAIL') is None


def test_enabled_reads_env(monkeypatch):
    monkeypatch.delenv(v2_service.ENV, raising=False)
    assert not v2_service.enabled()
    monkeypatch.setenv(v2_service.ENV, 'V2')
    assert v2_service.enabled()


def _calibration(verdict):
    bounds = {str(h): {'95': [0.9, 1.1], '80': [0.95, 1.05]} for h in range(1, 8)}
    return {'evaluationStart': '2024-11-01', 'evaluationEnd': '2025-10-31',
            'series': {'대파|RETAIL': {'verdict': verdict, 'mape': 3.0, 'naiveMape': 3.5, 'improvementPct': 14.3,
                                       'within5Pct': 80.0, 'points': 1700, 'intervals': bounds,
                                       'naiveIntervals': {str(h): {'95': [0.8, 1.2]} for h in range(1, 8)}}}}


def _forecast(prices):
    return {'대파|RETAIL': v2_ensemble.SeriesForecast(1, '대파', 'RETAIL', prices, {'XGBOOST': prices}, {})}


def test_prediction_validated_uses_ensemble_and_interval(monkeypatch):
    monkeypatch.setattr(v2_calibration, 'load', lambda: _calibration('VALIDATED'))
    monkeypatch.setattr(v2_service, 'forecasts', lambda engine, base: _forecast([1000.4] * 7))
    result = v2_service.prediction(None, '대파|RETAIL', date(2026, 11, 24), 950)
    assert result.model == 'V2_ENSEMBLE' and result.quality == 'VALIDATED'
    assert result.prices == [1000] * 7 and result.lower[0] == 900 and result.upper[0] == 1100
    assert result.metrics['evaluation']['V2_ENSEMBLE']['mape'] == 3.0 and result.metrics['validation']['within5Pct'] == 80.0


def test_prediction_baseline_keeps_last_price(monkeypatch):
    monkeypatch.setattr(v2_calibration, 'load', lambda: _calibration('BASELINE'))
    monkeypatch.setattr(v2_service, 'forecasts', lambda engine, base: _forecast([1000.0] * 7))
    result = v2_service.prediction(None, '대파|RETAIL', date(2026, 11, 24), 950)
    assert result.model == 'LAST_PRICE' and result.quality == 'BASELINE'
    assert result.prices == [950] * 7 and result.lower[0] == 760 and result.upper[0] == 1140


def test_prediction_missing_forecast_is_insufficient(monkeypatch):
    monkeypatch.setattr(v2_calibration, 'load', lambda: _calibration('VALIDATED'))
    monkeypatch.setattr(v2_service, 'forecasts', lambda engine, base: _forecast([None] * 7))
    with pytest.raises(InsufficientDataError):
        v2_service.prediction(None, '대파|RETAIL', date(2026, 11, 24), 950)
