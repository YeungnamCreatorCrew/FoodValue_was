"""수집 원천을 V2 정형 테이블로 정제·적재한다. 같은 키는 갱신하므로 몇 번 실행해도 결과가 같다.

| 테이블 | 근거 자료 |
| --- | --- |
| weather_daily(ACTUAL) | 전국 ASOS 관측소 일자료(external_observation)의 관측소 평균·특보 기준 비율 |
| weather_daily(FORECAST) | 단기예보 17개 시·도 대표 격자의 최신 발표본 평균. 오늘 이후 날짜만 덮어씀 |
| calendar_day | 공휴일(KASI)을 수집한 연도의 모든 날짜. 음력은 천문연 자료 기반 korean-lunar-calendar로 변환 |
| calendar_event | 공휴일 이름이 설날·추석인 연속 기간 |
| item_production | KOSIS 농작물생산조사 연간 전국 생산량(톤, 확정치) |
| price_change_history | price_daily(NATIONAL)의 같은 날 기준 1~7일 뒤 변동률 |

원천에 없는 값은 만들지 않는다. 가락 반입량(ARRIVAL)·KREI 전망·이벤트 가중치는 원천 수집기가 없어 적재하지 않는다.
"""
from collections import defaultdict
from datetime import date, timedelta
from decimal import ROUND_HALF_UP, Decimal
from statistics import mean
from zoneinfo import ZoneInfo

from sqlalchemy import func, select
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.orm import Session

from app.collectors import data_go_kr, kosis
from app.collectors.http import number
from app.models.external import ExternalObservation
from app.models.prediction_input import CalendarDay, CalendarEvent, ItemProduction, PriceChangeHistory, WeatherDaily
from app.models.price import PriceDaily
from app.repositories.covariate_repository import latest_versions

HEAT_MAX_TEMP = 33.0  # 폭염: 일 최고 33℃ 이상
HEAVY_RAIN_MM = 80.0  # 호우: 일 강수 80mm 이상
COLD_MIN_TEMP = -12.0  # 한파: 일 최저 -12℃ 이하
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


# ---------------------------------------------------------------- price_change_history
def change_history_rows(item_id: int, prices: dict[date, int], since: date | None = None):
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
                rows[key] = {'item_id': item_id, 'region': 'NATIONAL', 'price_year': day.year, 'month_day': month_day,
                             'horizon_days': horizon, 'base_price': prices[base], 'change_rate': rate}
        day += timedelta(days=1)
    return list(rows.values())


def refresh_price_change_history(engine, item_ids, since: date | None = None):
    total = 0
    with Session(engine) as db:
        for item_id in item_ids:
            # 휴장일 이월을 위해 기준일 이전 7일까지 함께 읽는다.
            query = select(PriceDaily.price_date, PriceDaily.price).where(PriceDaily.item_id == item_id,
                                                                         PriceDaily.region == 'NATIONAL')
            if since:
                query = query.where(PriceDaily.price_date >= since - timedelta(days=MAX_CARRY_DAYS))
            rows = change_history_rows(item_id, dict(db.execute(query).all()), since)
            if rows:
                total += _upsert(db, PriceChangeHistory, rows, 'uk_price_change_history',
                                 {'item_id', 'region', 'price_year', 'month_day', 'horizon_days'})
        db.commit()
    return total


def refresh(engine, item_ids, *, weather_start: date, weather_end: date, since: date | None = None):
    """파이프라인에서 수집 직후 호출한다. 테이블별 적재 행 수를 반환한다."""
    result = {}
    for name, task in (('weather_daily', lambda: refresh_weather_daily(engine, weather_start, weather_end)),
                       ('weather_forecast', lambda: refresh_weather_forecast(engine)),
                       ('calendar', lambda: dict(zip(('calendar_day', 'calendar_event'), refresh_calendar(engine)))),
                       ('item_production', lambda: refresh_item_production(engine, item_ids)),
                       ('price_change_history', lambda: refresh_price_change_history(engine, item_ids, since))):
        try:
            value = task()
            result.update(value if isinstance(value, dict) else {name: value})
        except Exception as error:
            result[name] = {'status': 'FAILED', 'errorCode': type(error).__name__}
    return result

