"""external_observation에서 예측용 외부 원천을 읽는다. 같은 원천 키의 여러 버전 중 최신 수집본을 사용한다."""
from collections import defaultdict
from datetime import date

from sqlalchemy import func, select

from app.collectors import data_go_kr, kamis
from app.collectors.http import number
from app.models.external import ExternalObservation, ItemWeatherStation
from app.services.exogenous import Covariates

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


def load(db, item_id, start: date, end: date, horizon_end: date):
    holiday_map, years = holidays(db, start, horizon_end)
    return Covariates(wholesale=wholesale(db, item_id, start, end), weather=weather(db, item_id, start, end),
                      holidays=holiday_map, holiday_years=years)
