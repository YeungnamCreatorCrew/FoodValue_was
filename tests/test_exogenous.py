import math
import random
from datetime import date, timedelta

import pytest

from app.services import price_prediction as model
from app.services.exogenous import (CALENDAR_FEATURES, WEATHER_FEATURES, WHOLESALE_FEATURES, Covariates,
                                    ExogenousFeatures)

START = date(2024, 1, 1)


def leading_series(count=480, lead=5, seed=7):
    """도매가가 소매가를 lead일 앞서는 합성 자료. 실제 시장의 선행 관계를 입증하는 자료가 아니다."""
    rng = random.Random(seed)
    level, drift, wholesale = 1000.0, 0, []
    for index in range(count + lead):
        if index % 15 == 0:
            drift = rng.choice([-25, -12, 12, 25])
        level = max(300, level + drift + rng.gauss(0, 5))
        wholesale.append(level)
    days = [START + timedelta(days=i) for i in range(count)]
    retail = [(day, round(1.5 * wholesale[i] + rng.gauss(0, 3))) for i, day in enumerate(days)]
    return retail, {day: wholesale[i + lead] for i, day in enumerate(days)}


def build(covariates, count=120):
    rows = [(START + timedelta(days=i), 1000 + i) for i in range(count)]
    days, values, _, _ = model.normalize(rows, rows[-1][0])
    return days, values, ExogenousFeatures(days, values, covariates)


def weather_row(value):
    return {'avgTa': value, 'minTa': value - 5, 'maxTa': value + 5, 'sumRn': 1.0, 'avgRhm': 60.0, 'sumSsHr': 5.0}


def test_external_inputs_respect_publication_lag():
    wholesale = {START + timedelta(days=i): 500.0 + i for i in range(120)}
    weather = {START + timedelta(days=i): weather_row(10.0) for i in range(120)}
    days, values, features = build(Covariates(wholesale=wholesale, weather=weather))
    origin = 60
    before = features.vector(origin, 3)
    # 예측 시작일 당일 이후의 값은 공개 전이므로 바뀌어도 입력이 같아야 한다.
    for offset in range(origin, 120):
        wholesale[START + timedelta(days=offset)] = 99999.0
        weather[START + timedelta(days=offset)] = weather_row(40.0)
    _, _, edited = build(Covariates(wholesale=wholesale, weather=weather))
    assert edited.vector(origin, 3) == before
    assert before[0] == 500.0 + origin - 1  # 전일 도매가
    assert before[WHOLESALE_FEATURES.index('wholesaleAge')] == 1.0


def test_missing_external_values_stay_missing():
    wholesale = {START + timedelta(days=i): 500.0 for i in range(30)}  # 이후 장기 결측
    _, _, features = build(Covariates(wholesale=wholesale))
    assert features.names == WHOLESALE_FEATURES
    assert all(math.isnan(value) for value in features.vector(90, 1))
    assert features.coverage([20, 90]) == {'WHOLESALE': 0.5}


def test_calendar_uses_target_date_and_only_collected_years():
    chuseok = date(2024, 9, 17)
    covariates = Covariates(holidays={chuseok: '추석', date(2024, 9, 16): '추석'}, holiday_years={2024})
    days, _, features = build(covariates, count=300)
    origin = days.index(date(2024, 9, 10))
    holiday, to_major, from_major = features.vector(origin, 6)  # 목표일 9/16
    assert (holiday, to_major, from_major) == (1.0, 0.0, 0.0)
    assert features.vector(origin, 1)[1] == 5.0
    assert features.names == CALENDAR_FEATURES
    # 2025년 공휴일은 수집하지 않았으므로 '공휴일 아님'으로 단정하지 않는다.
    late = Covariates(holidays={chuseok: '추석'}, holiday_years={2024})
    _, _, features = build(late, count=400)
    assert all(math.isnan(value) for value in features.vector(390, 7))


def test_weather_requires_enough_days():
    weather = {START + timedelta(days=i): weather_row(10.0) for i in range(50, 53)}  # 3일뿐
    _, _, features = build(Covariates(weather=weather))
    assert features.names == WEATHER_FEATURES
    assert all(math.isnan(value) for value in features.vector(54, 1))


@pytest.fixture(scope='module')
def exogenous_prediction():
    pytest.importorskip('xgboost')
    retail, wholesale = leading_series()
    return model.predict(retail, retail[-1][0], Covariates(wholesale=wholesale))


def test_informative_external_source_is_selected_and_validated(exogenous_prediction):
    result = exogenous_prediction
    assert result.model == 'XGBOOST_EXT' and result.quality == 'VALIDATED'
    evaluation = result.metrics['evaluation']
    assert evaluation['XGBOOST_EXT']['mape'] < evaluation['XGBOOST']['mape']
    assert evaluation['XGBOOST_EXT']['mape'] < evaluation['LAST_PRICE']['mape']
    assert result.metrics['candidates'] == ['LAST_PRICE', 'MEAN_7', 'XGBOOST', 'XGBOOST_EXT']
    assert result.metrics['featureSets']['XGBOOST_EXT'][-len(WHOLESALE_FEATURES):] == WHOLESALE_FEATURES
    assert result.metrics['externalCoverage'] == {'WHOLESALE': 1.0}
    assert len(result.prices) == 7


def test_uninformative_external_source_is_not_forced():
    pytest.importorskip('xgboost')
    rows = [(START + timedelta(days=i), 1000) for i in range(480)]
    noise = random.Random(1)
    wholesale = {day: 500 + noise.random() * 100 for day, _ in rows}
    result = model.predict(rows, rows[-1][0], Covariates(wholesale=wholesale))
    assert result.model == 'LAST_PRICE' and result.quality == 'BASELINE'
    assert 'XGBOOST_EXT' in result.metrics['evaluation']
