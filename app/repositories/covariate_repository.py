"""예측용 외부 원천을 읽는다.

- external_observation: 도매가·주산지 기상·공휴일. 같은 원천 키의 여러 버전 중 최신 수집본을 사용한다.
- V2 정형 테이블: weather_daily(ACTUAL)·calendar_event·price_change_history·item_production·exchange_rate_daily.
공개 시점 규칙은 exogenous에서 적용한다. 여기서는 기간만 자른다.
"""
from collections import defaultdict
from datetime import date, timedelta

from sqlalchemy import func, select

from app.collectors import data_go_kr, kamis
from app.collectors.http import number
from app.models.external import ExternalObservation, ItemWeatherStation
from app.models.prediction_input import CalendarEvent, ExchangeRateDaily, ItemProduction, PriceChangeHistory, WeatherDaily
from app.services.exogenous import SEASONAL_YEARS, Covariates, EventWindow

WEATHER_KEYS = ('avgTa', 'minTa', 'maxTa', 'sumRn', 'avgRhm', 'sumSsHr')


def latest_versions(db, *conditions):
    """원천 키별 최신 버전만. 원천이 값을 수정하면 수정본을 사용한다."""
    ranked = (select(ExternalObservation.id, func.row_number().over(
        partition_by=(ExternalObservation.source, ExternalObservation.dataset, ExternalObservation.source_record_key),
        order_by=(ExternalObservation.retrieved_at.desc(), ExternalObservation.id.desc())).label('rank'))
        .where(*conditions).subquery())
    return db.scalars(select(ExternalObservation).join(ranked, ExternalObservation.id == ranked.c.id)
                      .where(ranked.c.rank == 1).order_by(ExternalObservation.observed_on)).all()


def wholesale(db, item_id, start: date, end: date):
    rows = latest_versions(db, ExternalObservation.source == kamis.SOURCE, ExternalObservation.dataset == kamis.WHOLESALE,
                   ExternalObservation.item_id == item_id, ExternalObservation.observed_on.between(start, end))
    result = {}
    for row in rows:
        price = number(row.payload.get('price'))
        if price and price > 0:
            result[row.observed_on] = price
    return result


def stations(db, item_id):
    return db.scalars(select(ItemWeatherStation).where(ItemWeatherStation.item_id == item_id,
                                                       ItemWeatherStation.mapping_status == 'VERIFIED')).all()


def _active(station, day):
    if station.valid_from and day < station.valid_from or station.valid_until and day > station.valid_until:
        return False
    return not station.months or day.month in station.months


def weather(db, item_id, start: date, end: date):
    """검증된 주산지 관측소만 사용한다. 비중(share)이 없으면 활성 관측소를 같은 비중으로 평균한다."""
    mapped = stations(db, item_id)
    if not mapped:
        return {}
    rows = latest_versions(db, ExternalObservation.source == data_go_kr.KMA, ExternalObservation.dataset == data_go_kr.ASOS,
                   ExternalObservation.entity_code.in_({s.station_code for s in mapped}),
                   ExternalObservation.observed_on.between(start, end))
    by_day = defaultdict(dict)
    for row in rows:
        by_day[row.observed_on][row.entity_code] = row.payload
    result = {}
    for day, readings in by_day.items():
        aggregate = {}
        for key in WEATHER_KEYS:
            weighted = []
            for station in mapped:
                payload = readings.get(station.station_code)
                if payload is None or not _active(station, day):
                    continue
                value = number(payload.get(key))
                if value is None and key == 'sumRn':
                    value = 0.0  # ASOS 일자료는 무강수일의 강수량을 빈 값으로 제공한다.
                if value is not None:
                    weighted.append((value, float(station.share) if station.share is not None else 1.0))
            total = sum(weight for _, weight in weighted)
            aggregate[key] = sum(v * w for v, w in weighted) / total if total > 0 else None
        if any(value is not None for value in aggregate.values()):
            result[day] = aggregate
    return result


def holidays(db, start: date, end: date):
    rows = latest_versions(db, ExternalObservation.source == data_go_kr.KASI, ExternalObservation.dataset == data_go_kr.HOLIDAY,
                   ExternalObservation.observed_on.between(start, end))
    named = {row.observed_on: row.entity_name or '' for row in rows if row.payload.get('isHoliday') != 'N'}
    # 공휴일 자료를 실제로 수집한 연도만 달력 특징을 만든다. 미수집 연도를 '공휴일 없음'으로 보지 않는다.
    years = set(db.scalars(select(func.distinct(func.extract('year', ExternalObservation.period_start))).where(
        ExternalObservation.source == data_go_kr.KASI, ExternalObservation.dataset == data_go_kr.HOLIDAY,
        ExternalObservation.observed_on.between(start, end))).all())
    return named, {int(year) for year in years}


def _float(value):
    return None if value is None else float(value)


def national_weather(db, start: date, end: date):
    rows = db.scalars(select(WeatherDaily).where(WeatherDaily.data_type == 'ACTUAL',
                                                 WeatherDaily.weather_date.between(start, end))).all()
    return {row.weather_date: {'avgTemp': _float(row.avg_temp), 'precipitation': _float(row.precipitation),
                               'heatRatio': _float(row.heat_station_ratio),
                               'heavyRainRatio': _float(row.heavy_rain_station_ratio),
                               'coldRatio': _float(row.cold_station_ratio)} for row in rows}


def events(db, start: date, end: date):
    rows = db.scalars(select(CalendarEvent).where(CalendarEvent.effect_end_date >= start,
                                                  CalendarEvent.effect_start_date <= end)
                      .order_by(CalendarEvent.start_date)).all()
    return [EventWindow(row.event_code, row.start_date, row.end_date, row.effect_start_date, row.effect_end_date)
            for row in rows]


def change_history(db, item_id, start: date, end: date):
    """시점 → 기준일 → 변동률(분율). 02-28 행에는 윤년 02-29 기준이 합쳐져 있을 수 있다(같은 해 02-28 우선)."""
    rows = db.execute(select(PriceChangeHistory.price_year, PriceChangeHistory.month_day, PriceChangeHistory.horizon_days,
                             PriceChangeHistory.change_rate)
                      .where(PriceChangeHistory.item_id == item_id, PriceChangeHistory.region == 'NATIONAL',
                             PriceChangeHistory.price_year.between(start.year, end.year))).all()
    result = defaultdict(dict)
    for year, month_day, horizon, rate in rows:
        day = date(year, int(month_day[:2]), int(month_day[3:]))
        if start <= day <= end:
            result[horizon][day] = float(rate) / 100
    return dict(result)


def production(db, item_id):
    rows = db.execute(select(ItemProduction.period_start, ItemProduction.volume).where(
        ItemProduction.item_id == item_id, ItemProduction.measure_type == 'PRODUCTION',
        ItemProduction.period_type == 'YEAR', ItemProduction.is_estimate.is_(False))).all()
    return {start.year: float(volume) for start, volume in rows if volume and volume > 0}


def exchange_rate(db, start: date, end: date, currency='USD'):
    rows = db.execute(select(ExchangeRateDaily.rate_date, ExchangeRateDaily.rate).where(
        ExchangeRateDaily.currency_code == currency, ExchangeRateDaily.rate_date.between(start, end))).all()
    return {day: float(rate) for day, rate in rows}


def load(db, item_id, start: date, end: date, horizon_end: date):
    holiday_map, years = holidays(db, start, horizon_end)
    # 과거 같은 시기 변동률·명절 효과는 학습 시작보다 최대 5년 이전 자료까지 참고한다.
    history_start = date(start.year - SEASONAL_YEARS, 1, 1)
    return Covariates(wholesale=wholesale(db, item_id, start, end), weather=weather(db, item_id, start, end),
                      holidays=holiday_map, holiday_years=years,
                      national_weather=national_weather(db, start, end),
                      events=events(db, history_start - timedelta(days=60), horizon_end),
                      change_history=change_history(db, item_id, history_start, end),
                      production=production(db, item_id), fx=exchange_rate(db, start, end))
