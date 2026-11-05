import math
import random
from datetime import date, timedelta

import pytest

from app.services import price_prediction as model
from app.services.exogenous import (CALENDAR_FEATURES, EVENT_FEATURES, NATIONAL_WEATHER_FEATURES, WEATHER_FEATURES,
                                    WHOLESALE_FEATURES, Covariates, EventWindow, ExogenousFeatures, event_weight)

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
    assert result.model in ('XGBOOST_EXT', 'XGBOOST_WEIGHTED') and result.quality == 'VALIDATED'
    evaluation = result.metrics['evaluation']
    assert evaluation[result.model]['mape'] < evaluation['XGBOOST']['mape']
    assert evaluation[result.model]['mape'] < evaluation['LAST_PRICE']['mape']
    assert result.metrics['candidates'] == ['LAST_PRICE', 'MEAN_7', 'XGBOOST', 'XGBOOST_EXT', 'XGBOOST_WEIGHTED']
    assert result.metrics['featureSets']['XGBOOST_EXT'][-len(WHOLESALE_FEATURES):] == WHOLESALE_FEATURES
    assert result.metrics['externalCoverage'] == {'WHOLESALE': 1.0}
    # 묶음이 하나면 전문가 모델은 XGBOOST_EXT와 같고, 도매가 묶음의 가중치가 학습된다.
    assert result.metrics['weighting']['blocks'] == {'MARKET': ['WHOLESALE']}
    assert result.metrics['weighting']['weights']['MARKET'] > .5
    assert len(result.prices) == 7


def test_uninformative_external_source_is_not_forced():
    pytest.importorskip('xgboost')
    rows = [(START + timedelta(days=i), 1000) for i in range(480)]
    noise = random.Random(1)
    wholesale = {day: 500 + noise.random() * 100 for day, _ in rows}
    result = model.predict(rows, rows[-1][0], Covariates(wholesale=wholesale))
    assert result.model == 'LAST_PRICE' and result.quality == 'BASELINE'
    assert 'XGBOOST_EXT' in result.metrics['evaluation']
    assert result.metrics['weighting']['weights'] == {'MARKET': 0.0}


def random_fx(days, seed=2):
    rng, rate, fx = random.Random(seed), 1300.0, {}
    for day in days:
        rate *= math.exp(rng.gauss(0, .005))
        fx[day] = rate
    return fx


def test_noise_block_gets_zero_weight_while_signal_block_is_kept():
    pytest.importorskip('xgboost')
    retail, wholesale = leading_series()
    result = model.predict(retail, retail[-1][0], Covariates(wholesale=wholesale, fx=random_fx([d for d, _ in retail])))
    weighting = result.metrics['weighting']
    assert weighting['blocks'] == {'MARKET': ['WHOLESALE'], 'MACRO': ['FX']}
    assert weighting['weights']['MARKET'] > .5 and weighting['weights']['MACRO'] == 0.0
    assert result.model in ('XGBOOST_EXT', 'XGBOOST_WEIGHTED') and result.quality == 'VALIDATED'


def national_row(temp, heat=0.0, rain=0.0):
    return {'avgTemp': temp, 'precipitation': rain, 'heatRatio': heat, 'heavyRainRatio': 0.0, 'coldRatio': 0.0}


def test_structured_sources_respect_publication_lag():
    national = {START + timedelta(days=i): national_row(10.0, heat=50.0) for i in range(120)}
    fx = {START + timedelta(days=i): 1300.0 + i for i in range(120)}
    days, _, features = build(Covariates(national_weather=national, fx=fx))
    origin = 60
    before = features.vector(origin, 2)
    for offset in range(origin, 120):
        national[START + timedelta(days=offset)] = national_row(40.0, heat=100.0)
        fx[START + timedelta(days=offset)] = 99999.0
    _, _, edited = build(Covariates(national_weather=national, fx=fx))
    assert edited.vector(origin, 2) == before
    assert before[:len(NATIONAL_WEATHER_FEATURES)][:4] == [10.0, 0.0, 3.5, 14.0]  # 7일·28일 동안 관측소 절반이 폭염
    assert before[-2] == pytest.approx(1359 / 1352 - 1) and before[-1] == pytest.approx(1359 / 1331 - 1)
    assert features.blocks == {'WEATHER': ['NATIONAL_WEATHER'], 'MACRO': ['FX']}


def test_production_is_used_only_after_assumed_publication():
    covariates = Covariates(production={2022: 100.0, 2023: 120.0})
    rows = [(date(2024, 1, 1) + timedelta(days=i), 1000) for i in range(400)]
    days, values, _, _ = model.normalize(rows, rows[-1][0])
    features = ExogenousFeatures(days, values, covariates)
    # 2024-06-29에는 2023년 값이 아직 공개 전(가정)이라 최신은 2022년. 2021년이 없어 증감을 만들 수 없다.
    assert math.isnan(features.vector(days.index(date(2024, 6, 29)), 1)[0])
    assert features.vector(days.index(date(2024, 6, 30)), 1) == [pytest.approx(.2)]  # 2023 / 2022 - 1
    covariates.production[2021] = 80.0
    features = ExogenousFeatures(days, values, covariates)
    assert features.vector(days.index(date(2024, 6, 29)), 1) == [pytest.approx(.25)]  # 2022 / 2021 - 1


def test_seasonal_change_uses_only_realized_prior_years():
    origin_day = date(2026, 3, 10)
    history = {3: {date(2025, 3, 10): .10, date(2025, 3, 12): .20, date(2024, 3, 8): .30,
                   date(2023, 3, 20): 9.9,  # ±3일 밖
                   date(2026, 3, 8): 5.0}}  # 같은 해: 3월 11일 가격이 아직 확인되지 않음
    rows = [(origin_day - timedelta(days=99 - i), 1000) for i in range(100)]
    days, values, _, _ = model.normalize(rows, origin_day)
    features = ExogenousFeatures(days, values, Covariates(change_history=history))
    assert features.vector(len(days) - 1, 3) == [pytest.approx((.15 + .30) / 2)]
    assert math.isnan(features.vector(len(days) - 1, 1)[0])  # 시점 1의 자료 없음
    only_one_year = ExogenousFeatures(days, values, Covariates(change_history={3: {date(2025, 3, 10): .1}}))
    assert math.isnan(only_one_year.vector(len(days) - 1, 3)[0])


def chuseok_windows(years):
    return [EventWindow('CHUSEOK', date(y, 9, 20), date(y, 9, 22), date(y, 9, 6), date(y, 9, 25)) for y in years]


def chuseok_changes(years, bump):
    changes = {}
    for year in years:
        for k in range(120):
            day = date(year, 7, 1) + timedelta(days=k)
            changes[day] = .01 + (bump(year) if date(year, 9, 6) <= day <= date(year, 9, 25) else 0.0)
    return changes


def test_event_weight_is_shrunk_and_uses_only_finished_events():
    years = [2022, 2023, 2024, 2025]
    windows = chuseok_windows(years)
    steady = chuseok_changes(years, lambda y: .08)
    weight = event_weight(steady, windows, date(2026, 1, 1))
    assert weight == pytest.approx(math.tanh(.8))  # 해마다 같은 +8%p → 축소 없음
    mixed = chuseok_changes(years, lambda y: .08 if y % 2 else -.07)
    assert event_weight(mixed, windows, date(2026, 1, 1)) == 0.0  # 방향이 엇갈리면 0
    noisy = chuseok_changes(years, lambda y: {2022: .02, 2023: .10, 2024: .05, 2025: .07}[y])
    assert 0 < event_weight(noisy, windows, date(2026, 1, 1)) < math.tanh(.6)
    # 2025 추석 영향 기간의 7일 뒤 가격이 확인되기 전에는 2022~2024만 쓴다. 2개 연도 미만이면 None.
    assert event_weight(steady, windows, date(2025, 10, 1)) == pytest.approx(math.tanh(.8))
    assert event_weight(steady, windows, date(2023, 10, 1)) is None  # 2023 추석은 10/2에야 확인


def test_event_features_use_target_window_and_point_in_time_pressure():
    years = [2022, 2023, 2024]
    covariates = Covariates(events=chuseok_windows(years), holiday_years=set(years),
                            change_history={7: chuseok_changes(years, lambda y: .08)})
    rows = [(date(2022, 1, 1) + timedelta(days=i), 1000) for i in range(1050)]
    days, values, _, _ = model.normalize(rows, rows[-1][0])
    features = ExogenousFeatures(days, values, covariates)
    assert features.groups == ['CALENDAR', 'EVENT', 'SEASONAL'] and features.blocks['CALENDAR'] == ['CALENDAR', 'EVENT']
    def event(day, horizon):
        return features.group_vector(days.index(day), horizon, {'EVENT'})
    assert event(date(2024, 9, 1), 7) == [1.0, pytest.approx(math.tanh(.8))]  # 9/8 목표일은 영향 기간
    assert event(date(2024, 9, 1), 1) == [0.0, 0.0]
    assert event(date(2023, 9, 1), 7)[0] == 1.0 and math.isnan(event(date(2023, 9, 1), 7)[1])  # 과거 명절 1개뿐
    uncollected = ExogenousFeatures(days, values, Covariates(events=covariates.events, holiday_years={2022, 2023},
                                                             change_history=covariates.change_history))
    # 2024년 공휴일을 수집하지 않았으면 명절 기간 여부를 '아님'으로 단정하지 않는다.
    assert all(math.isnan(v) for v in uncollected.group_vector(days.index(date(2024, 9, 1)), 7, {'EVENT'}))
    assert len(EVENT_FEATURES) == 2
