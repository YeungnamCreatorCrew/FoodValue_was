"""수집 원천을 V2 정형 테이블로 정제·적재한다. 같은 키는 갱신하므로 몇 번 실행해도 결과가 같다.

| 테이블 | 근거 자료 |
| --- | --- |
| weather_daily(ACTUAL) | 전국 ASOS 관측소 일자료(external_observation)의 관측소 평균·특보 기준 비율 |
| weather_daily(FORECAST) | 단기예보 17개 시·도 대표 격자의 최신 발표본 평균. 오늘 이후 날짜만 덮어씀 |
| calendar_day | 공휴일(KASI)을 수집한 연도의 모든 날짜. 음력은 천문연 자료 기반 korean-lunar-calendar로 변환 |
| calendar_event | 공휴일 이름이 설날·추석인 연속 기간 |
| exchange_rate_daily | ECOS 731Y001 일별 원/미국달러 매매기준율 |
| item_production | KOSIS 농작물생산조사 연간 전국 생산량(톤, 확정치) |
| price_daily | 가격 계열(소매·도매)별 KAMIS 원본(external_observation)의 최신 버전 |
| price_change_history | 계열별 price_daily의 같은 날 기준 1~7일 뒤 변동률 |
| event_item_weight(LEARNED) | 소매 계열 price_change_history(7일)와 calendar_event로 계산한 품목별 명절 가격 압력 |

원천에 없는 값은 만들지 않는다. 가락 반입량(ARRIVAL)·KREI 전망은 원천 수집기가 없어 적재하지 않는다.
"""
from collections import defaultdict
from datetime import date, timedelta
from decimal import ROUND_HALF_UP, Decimal
from statistics import mean
from zoneinfo import ZoneInfo

from sqlalchemy import func, select
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.orm import Session

from app.collectors import data_go_kr, ecos, kamis, kosis
from app.collectors.http import number
from app.models.external import ExternalObservation
from app.models.prediction_input import (CalendarDay, CalendarEvent, EventItemWeight, ExchangeRateDaily, ItemProduction,
                                         PriceChangeHistory, WeatherDaily)
from app.core.constants import COLD_MIN_TEMP, HEAT_MAX_TEMP, HEAVY_RAIN_MM
from app.models.price import RETAIL, PriceDaily
from app.repositories import covariate_repository, series_repository
from app.repositories.covariate_repository import latest_versions
from app.services.exogenous import event_weight
from app.services.fridge_service import today

MAX_CARRY_DAYS = 7  # 휴장일 기준가는 직전 거래일 가격을 최대 7일까지 사용
EVENTS = {'설날': 'SEOLLAL', '추석': 'CHUSEOK'}
EVENT_EFFECT_BEFORE, EVENT_EFFECT_AFTER = 14, 3  # 명절 D-14 ~ 종료 D+3
MAX_CHANGE_RATE = Decimal('9999.99')  # NUMERIC(6,2)
CHUNK = 500
SEOUL = ZoneInfo('Asia/Seoul')


def _decimal(value, places='0.1'):
    return None if value is None else Decimal(str(value)).quantize(Decimal(places), rounding=ROUND_HALF_UP)


def _upsert(db, model, rows, constraint, keys):
    for offset in range(0, len(rows), CHUNK):
        statement = insert(model).values(rows[offset:offset + CHUNK])
        update = {column: statement.excluded[column] for column in rows[0] if column not in keys}
        db.execute(statement.on_conflict_do_update(constraint=constraint, set_=update))
    return len(rows)


# ---------------------------------------------------------------- weather_daily
def aggregate_weather(readings: list[dict]):
    """관측소별 ASOS 일자료 → 전국 1행. 관측소 단순 평균이며 면적·인구 가중을 하지 않는다."""
    columns = defaultdict(list)
    for payload in readings:
        for key in ('avgTa', 'maxTa', 'minTa', 'avgRhm', 'sumSsHr'):
            value = number(payload.get(key))
            if value is not None:
                columns[key].append(value)
        # 무강수일은 강수량이 빈 값으로 온다. 관측 행이 있으면 0mm로 본다.
        columns['sumRn'].append(number(payload.get('sumRn')) or 0.0)
    if not readings:
        return None

    def avg(key):
        return _decimal(mean(columns[key])) if columns[key] else None

    def ratio(key, test):
        values = columns[key]
        return _decimal(sum(test(v) for v in values) / len(values) * 100, '0.01') if values else None

    return {'avg_temp': avg('avgTa'), 'max_temp': avg('maxTa'), 'min_temp': avg('minTa'),
            'precipitation': avg('sumRn'), 'avg_humidity': avg('avgRhm'), 'sunshine_hours': avg('sumSsHr'),
            'heat_station_ratio': ratio('maxTa', lambda v: v >= HEAT_MAX_TEMP),
            'heavy_rain_station_ratio': ratio('sumRn', lambda v: v >= HEAVY_RAIN_MM),
            'cold_station_ratio': ratio('minTa', lambda v: v <= COLD_MIN_TEMP),
            'station_count': len(readings)}


def refresh_weather_daily(engine, start: date, end: date):
    with Session(engine) as db:
        rows = latest_versions(db, ExternalObservation.source == data_go_kr.KMA, ExternalObservation.dataset == data_go_kr.ASOS,
                       ExternalObservation.entity_code.in_(data_go_kr.NATIONAL_STATIONS),
                       ExternalObservation.observed_on.between(start, end))
        by_day = defaultdict(list)
        for row in rows:
            by_day[row.observed_on].append(row.payload)
        records = [{'weather_date': day, 'data_type': 'ACTUAL', **aggregate_weather(readings)}
                   for day, readings in sorted(by_day.items())]
        count = _upsert(db, WeatherDaily, records, 'uk_weather_daily', {'weather_date', 'data_type'}) if records else 0
        db.commit()
    return count


def aggregate_forecast(points: list[dict]):
    """대표 격자별 일 예보 요약 → 전국 FORECAST 1행. 일조시간은 예보 항목이 없어 NULL.

    기온 값이 하나도 없는 날(발표 직후 마지막 날처럼 예보 시간이 일부뿐인 날)은 None을 반환한다.
    """
    points = [p for p in points if any(p.get(key) is not None for key in ('tmpMean', 'tmx', 'tmn'))]
    if not points:
        return None

    def values(key):
        return [p[key] for p in points if p.get(key) is not None]

    def avg(key):
        data = values(key)
        return _decimal(mean(data)) if data else None

    def ratio(key, test):
        data = values(key)
        return _decimal(sum(test(v) for v in data) / len(data) * 100, '0.01') if data else None

    return {'avg_temp': avg('tmpMean'), 'max_temp': avg('tmx'), 'min_temp': avg('tmn'), 'precipitation': avg('pcpSum'),
            'avg_humidity': avg('rehMean'), 'sunshine_hours': None,
            'heat_station_ratio': ratio('tmx', lambda v: v >= HEAT_MAX_TEMP),
            'heavy_rain_station_ratio': ratio('pcpSum', lambda v: v >= HEAVY_RAIN_MM),
            'cold_station_ratio': ratio('tmn', lambda v: v <= COLD_MIN_TEMP), 'station_count': len(points)}


def refresh_weather_forecast(engine):
    """가장 최근 발표본으로 오늘 이후 날짜의 FORECAST 행을 덮어쓴다. 지난 날짜의 예보 행은 마지막 예보로 남긴다."""
    with Session(engine) as db:
        issued = db.scalar(select(func.max(ExternalObservation.issued_at)).where(
            ExternalObservation.source == data_go_kr.KMA, ExternalObservation.dataset == data_go_kr.VILAGE))
        if issued is None:
            return 0
        rows = latest_versions(db, ExternalObservation.source == data_go_kr.KMA,
                               ExternalObservation.dataset == data_go_kr.VILAGE, ExternalObservation.issued_at == issued,
                               ExternalObservation.observed_on >= issued.astimezone(SEOUL).date())
        by_day = defaultdict(list)
        for row in rows:
            by_day[row.observed_on].append(row.payload)
        records = [{'weather_date': day, 'data_type': 'FORECAST', **row} for day, row in
                   sorted((day, aggregate_forecast(points)) for day, points in by_day.items()) if row]
        count = _upsert(db, WeatherDaily, records, 'uk_weather_daily', {'weather_date', 'data_type'}) if records else 0
        db.commit()
    return count


# ---------------------------------------------------------------- calendar_day / calendar_event
def lunar(day: date):
    from korean_lunar_calendar import KoreanLunarCalendar
    calendar = KoreanLunarCalendar()
    if not calendar.setSolarDate(day.year, day.month, day.day):
        raise ValueError('음력 변환 범위를 벗어난 날짜입니다')
    return calendar.lunarMonth, calendar.lunarDay, bool(calendar.isIntercalation)


def calendar_rows(holidays: dict[date, list[str]], years):
    rows = []
    for year in sorted(years):
        day = date(year, 1, 1)
        while day.year == year:
            names = holidays.get(day, [])
            month, lunar_day, leap = lunar(day)
            # KAMIS 가격 미조사일(시세 결측이 정상인 날). 2025~2026년 KAMIS 도매·소매 실데이터에서
            # 결측일이 토·일과 모든 공휴일(대체공휴일 포함)과 정확히 일치함을 확인했다.
            closed = day.isoweekday() >= 6 or bool(names)
            rows.append({'cal_date': day, 'day_of_week': day.isoweekday(), 'is_holiday': bool(names),
                         'holiday_name': ','.join(dict.fromkeys(names))[:30] or None, 'lunar_month': month,
                         'lunar_day': lunar_day, 'is_lunar_leap': leap, 'is_market_closed': closed})
            day += timedelta(days=1)
    return rows


def event_rows(holidays: dict[date, list[str]]):
    rows = []
    for name, code in EVENTS.items():
        days = sorted(day for day, names in holidays.items() if name in names)
        groups = []
        for day in days:
            if groups and (day - groups[-1][-1]).days == 1:
                groups[-1].append(day)
            else:
                groups.append([day])
        for group in groups:
            rows.append({'event_code': code, 'name': f'{group[0].year} {name}', 'start_date': group[0],
                         'end_date': group[-1], 'effect_start_date': group[0] - timedelta(days=EVENT_EFFECT_BEFORE),
                         'effect_end_date': group[-1] + timedelta(days=EVENT_EFFECT_AFTER)})
    return rows


def refresh_calendar(engine):
    """공휴일을 수집한 연도만 채운다. 미수집 연도를 '공휴일 없음'으로 적재하지 않는다."""
    with Session(engine) as db:
        rows = latest_versions(db, ExternalObservation.source == data_go_kr.KASI, ExternalObservation.dataset == data_go_kr.HOLIDAY)
        holidays = defaultdict(list)
        for row in rows:
            if row.payload.get('isHoliday') != 'N' and row.entity_name:
                holidays[row.observed_on].append(row.entity_name)
        years = {day.year for day in holidays}
        days = calendar_rows(holidays, years)
        events = event_rows(holidays)
        if days:
            _upsert(db, CalendarDay, days, 'uk_calendar_day_cal_date', {'cal_date'})
        if events:
            _upsert(db, CalendarEvent, events, 'uk_calendar_event', {'event_code', 'start_date'})
        db.commit()
    return len(days), len(events)


# ---------------------------------------------------------------- item_production
def production_rows(observations):
    """KOSIS 연간 전국 생산량 → item_production(PRODUCTION, YEAR, 확정치)."""
    rows = []
    for row in observations:
        volume = number(row.payload.get('DT'))
        if volume is None or volume < 0 or (row.units or {}).get('volume') not in ('톤', None):
            continue
        rows.append({'item_id': row.item_id, 'measure_type': 'PRODUCTION', 'period_type': 'YEAR',
                     'period_start': row.period_start, 'period_end': row.period_end, 'volume': _decimal(volume),
                     'volume_unit': 'TON', 'is_estimate': False, 'source': 'KOSIS'})
    return rows


def refresh_item_production(engine, item_ids):
    with Session(engine) as db:
        rows = production_rows(latest_versions(db, ExternalObservation.source == kosis.SOURCE,
                                               ExternalObservation.dataset == kosis.DATASET,
                                               ExternalObservation.item_id.in_(item_ids)))
        if rows:
            _upsert(db, ItemProduction, rows, 'uk_item_production',
                    {'item_id', 'measure_type', 'period_type', 'period_start', 'is_estimate'})
        db.commit()
    return len(rows)


# ---------------------------------------------------------------- exchange_rate_daily
def exchange_rows(observations):
    rows = []
    for row in observations:
        rate = number(row.payload.get('DATA_VALUE'))
        if rate is None or rate <= 0 or row.observed_on is None:
            continue
        rows.append({'rate_date': row.observed_on, 'currency_code': row.entity_code, 'rate': _decimal(rate, '0.0001'),
                     'unit_label': ((row.units or {}).get('rate') or '원')[:30], 'source': 'ECOS'})
    return rows


def refresh_exchange_rate(engine, start: date, end: date):
    with Session(engine) as db:
        rows = exchange_rows(latest_versions(db, ExternalObservation.source == ecos.SOURCE,
                                             ExternalObservation.dataset == ecos.DATASET,
                                             ExternalObservation.observed_on.between(start, end)))
        if rows:
            _upsert(db, ExchangeRateDaily, rows, 'uk_exchange_rate_daily', {'rate_date', 'currency_code'})
        db.commit()
    return len(rows)


# ---------------------------------------------------------------- price_daily
def price_rows(series_id, observations):
    """KAMIS 원본 최신 버전 → price_daily. 가격이 없거나 0 이하인 행은 만들지 않는다."""
    rows = []
    for row in observations:
        price = number(row.payload.get('price'))
        if row.observed_on is None or price is None or price <= 0:
            continue
        rows.append({'series_id': series_id, 'price_date': row.observed_on, 'price': int(round(price)),
                     'observation_id': row.id})
    return rows


def refresh_price_daily(engine, item_ids, since: date | None = None):
    """계열 코드로 저장된 원본(키 '{코드}:{날짜}')만 읽는다. 코드를 바꾸면 이전 코드의 원본은 섞이지 않는다."""
    total = 0
    with Session(engine) as db:
        for series in series_repository.of_items(db, item_ids):
            conditions = [ExternalObservation.source == kamis.SOURCE, ExternalObservation.dataset == kamis.MARKET_DATASETS[series.market],
                          ExternalObservation.item_id == series.item_id,
                          ExternalObservation.source_record_key.like(f'{series.code}:%')]
            if since:
                conditions.append(ExternalObservation.observed_on >= since)
            rows = price_rows(series.id, latest_versions(db, *conditions))
            if rows:
                total += _upsert(db, PriceDaily, rows, 'uk_price_daily', {'series_id', 'price_date'})
        db.commit()
    return total


# ---------------------------------------------------------------- price_change_history
def change_history_rows(series_id: int, prices: dict[date, int], since: date | None = None):
    """기준일 d(달력의 모든 날)의 가격과 d+h(1~7)의 가격으로 변동률을 만든다.

    휴장일은 직전 거래일 가격을 최대 7일까지 사용한다. 목표일까지 새 거래가 없으면(같은 관측을 다시 쓰게 되면)
    0%를 만들어내지 않도록 그 표본은 제외한다. 윤년 2월 29일은 02-28로 합치며 같은 해 02-28 행이 우선한다.
    """
    if not prices:
        return []
    observed = sorted(prices)
    start, end = max(observed[0], since or observed[0]), observed[-1]
    carried, last = {}, None
    for offset in range((end - observed[0]).days + 1):
        day = observed[0] + timedelta(days=offset)
        if day in prices:
            last = day
        if last and (day - last).days <= MAX_CARRY_DAYS:
            carried[day] = last
    rows = {}
    day = start
    while day <= end:
        base = carried.get(day)
        if base:
            for horizon in range(1, 8):
                target = carried.get(day + timedelta(days=horizon))
                if not target or target <= base:
                    continue
                rate = Decimal((prices[target] - prices[base]) / prices[base] * 100).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
                if abs(rate) > MAX_CHANGE_RATE:
                    continue
                month_day = '02-28' if (day.month, day.day) == (2, 29) else day.strftime('%m-%d')
                key = (day.year, month_day, horizon)
                if key in rows and (day.month, day.day) == (2, 29):
                    continue
                rows[key] = {'series_id': series_id, 'price_year': day.year, 'month_day': month_day,
                             'horizon_days': horizon, 'base_price': prices[base], 'change_rate': rate}
        day += timedelta(days=1)
    return list(rows.values())


def refresh_price_change_history(engine, item_ids, since: date | None = None):
    total = 0
    with Session(engine) as db:
        for series in series_repository.of_items(db, item_ids):
            # 휴장일 이월을 위해 기준일 이전 7일까지 함께 읽는다.
            start = since - timedelta(days=MAX_CARRY_DAYS) if since else None
            rows = change_history_rows(series.id, dict(series_repository.prices(db, series.id, start)), since)
            if rows:
                total += _upsert(db, PriceChangeHistory, rows, 'uk_price_change_history',
                                 {'series_id', 'price_year', 'month_day', 'horizon_days'})
        db.commit()
    return total


# ---------------------------------------------------------------- event_item_weight
def event_weight_rows(item_id, changes7: dict[date, float], windows, as_of: date):
    """예측 모델(EVENT 특징)과 같은 함수로 오늘 기준 명절 가격 압력을 계산한다. 2개 연도 미만이면 만들지 않는다."""
    rows = []
    for code in EVENTS.values():
        weight = event_weight(changes7, [w for w in windows if w.code == code], as_of)
        if weight is not None:
            rows.append({'event_code': code, 'item_id': item_id, 'category': None,
                         'weight': _decimal(weight, '0.01'), 'weight_source': 'LEARNED'})
    return rows


def refresh_event_item_weight(engine, item_ids, as_of: date | None = None):
    """LEARNED 가중치만 갱신한다. 사람이 넣은 MANUAL 행은 덮어쓰지 않는다."""
    as_of = as_of or today()
    with Session(engine) as db:
        windows = covariate_repository.events(db, date(1900, 1, 1), as_of)
        rows = []
        for item_id, series in series_repository.by_items(db, item_ids, RETAIL).items():
            changes = covariate_repository.change_history(db, series.id, date(1900, 1, 1), as_of).get(7, {})
            rows += event_weight_rows(item_id, changes, windows, as_of)
        if rows:
            statement = insert(EventItemWeight).values(rows)
            db.execute(statement.on_conflict_do_update(
                constraint='uk_event_item_weight_item',
                set_={'weight': statement.excluded.weight, 'weight_source': statement.excluded.weight_source},
                where=EventItemWeight.weight_source == 'LEARNED'))
        db.commit()
    return len(rows)


def refresh(engine, item_ids, *, weather_start: date, weather_end: date, since: date | None = None):
    """파이프라인에서 수집 직후 호출한다. 테이블별 적재 행 수를 반환한다."""
    result = {}
    for name, task in (('price_daily', lambda: refresh_price_daily(engine, item_ids, since)),
                       ('weather_daily', lambda: refresh_weather_daily(engine, weather_start, weather_end)),
                       ('weather_forecast', lambda: refresh_weather_forecast(engine)),
                       ('calendar', lambda: dict(zip(('calendar_day', 'calendar_event'), refresh_calendar(engine)))),
                       ('item_production', lambda: refresh_item_production(engine, item_ids)),
                       ('exchange_rate_daily', lambda: refresh_exchange_rate(engine, weather_start, weather_end)),
                       ('price_change_history', lambda: refresh_price_change_history(engine, item_ids, since)),
                       ('event_item_weight', lambda: refresh_event_item_weight(engine, item_ids))):
        try:
            value = task()
            result.update(value if isinstance(value, dict) else {name: value})
        except Exception as error:
            result[name] = {'status': 'FAILED', 'errorCode': type(error).__name__}
    return result

