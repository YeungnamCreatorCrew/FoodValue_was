"""원천 → V2 정형 테이블 정제 규칙. DB 없이 행 생성만 검증한다."""
from datetime import date, timedelta
from decimal import Decimal

import pytest

from app.services import warehouse_service as warehouse


def test_weather_aggregate_uses_station_mean_and_alert_ratios():
    readings = [
        {'avgTa': '30.0', 'maxTa': '35.0', 'minTa': '25.0', 'sumRn': '', 'avgRhm': '70', 'sumSsHr': '10'},
        {'avgTa': '20.0', 'maxTa': '25.0', 'minTa': '15.0', 'sumRn': '100.0', 'avgRhm': '90', 'sumSsHr': None},
        {'avgTa': None, 'maxTa': None, 'minTa': '-13.0', 'sumRn': '20.0', 'avgRhm': None, 'sumSsHr': '2'},
    ]
    row = warehouse.aggregate_weather(readings)
    assert row['avg_temp'] == Decimal('25.0') and row['max_temp'] == Decimal('30.0')
    assert row['min_temp'] == Decimal('9.0')  # (25 + 15 - 13) / 3
    assert row['precipitation'] == Decimal('40.0')  # 빈 강수량은 0mm
    assert row['sunshine_hours'] == Decimal('6.0')
    assert row['heat_station_ratio'] == Decimal('50.00')  # 최고기온 있는 2곳 중 1곳
    assert row['heavy_rain_station_ratio'] == Decimal('33.33')
    assert row['cold_station_ratio'] == Decimal('33.33')
    assert row['station_count'] == 3
    assert warehouse.aggregate_weather([]) is None


def test_calendar_rows_lunar_holidays_and_market_closure():
    pytest.importorskip('korean_lunar_calendar')
    holidays = {date(2026, 9, 24): ['추석'], date(2026, 9, 25): ['추석'], date(2026, 9, 26): ['추석'],
                date(2026, 10, 3): ['개천절'], date(2026, 10, 5): ['대체공휴일', '대체공휴일']}
    rows = {row['cal_date']: row for row in warehouse.calendar_rows(holidays, {2026})}
    assert len(rows) == 365
    chuseok = rows[date(2026, 9, 25)]
    assert (chuseok['lunar_month'], chuseok['lunar_day'], chuseok['is_lunar_leap']) == (8, 15, False)
    assert chuseok['is_holiday'] and chuseok['is_market_closed'] and chuseok['day_of_week'] == 5
    # KAMIS 미조사일: 토·일과 모든 공휴일(대체공휴일 포함)
    assert rows[date(2026, 10, 3)]['is_holiday'] and rows[date(2026, 10, 3)]['is_market_closed']  # 토요일 개천절
    assert rows[date(2026, 10, 4)]['is_market_closed'] and not rows[date(2026, 10, 4)]['is_holiday']  # 일요일
    assert rows[date(2026, 10, 10)]['is_market_closed']  # 토요일
    assert rows[date(2026, 10, 5)]['holiday_name'] == '대체공휴일' and rows[date(2026, 10, 5)]['is_market_closed']
    assert not rows[date(2026, 10, 6)]['is_market_closed']  # 평일
    leap = {row['cal_date']: row for row in warehouse.calendar_rows({}, {2023})}[date(2023, 3, 22)]
    assert (leap['lunar_month'], leap['lunar_day'], leap['is_lunar_leap']) == (2, 1, True)


def test_event_rows_group_consecutive_holidays():
    holidays = {date(2026, 2, 16): ['설날'], date(2026, 2, 17): ['설날'], date(2026, 2, 18): ['설날'],
                date(2026, 9, 24): ['추석'], date(2026, 9, 26): ['추석'], date(2026, 9, 25): ['추석'],
                date(2026, 5, 5): ['어린이날']}
    rows = sorted(warehouse.event_rows(holidays), key=lambda row: row['start_date'])
    assert [(r['event_code'], r['name'], r['start_date'], r['end_date']) for r in rows] == [
        ('SEOLLAL', '2026 설날', date(2026, 2, 16), date(2026, 2, 18)),
        ('CHUSEOK', '2026 추석', date(2026, 9, 24), date(2026, 9, 26))]
    assert rows[1]['effect_start_date'] == date(2026, 9, 10) and rows[1]['effect_end_date'] == date(2026, 9, 29)


def test_price_change_history_carries_closed_days_without_fake_zero():
    start = date(2026, 1, 5)  # 월요일. 주말(10, 11일) 결측
    prices = {start + timedelta(days=i): 1000 + i * 10 for i in range(5)}
    prices[date(2026, 1, 12)] = 1200
    rows = {(r['month_day'], r['horizon_days']): r for r in warehouse.change_history_rows(1, prices)}
    assert rows[('01-05', 1)]['change_rate'] == Decimal('1.00') and rows[('01-05', 1)]['base_price'] == 1000
    # 토요일 기준가는 금요일 가격, 1일 뒤(일요일)는 새 거래가 없어 제외, 2일 뒤 월요일은 포함
    assert rows[('01-10', 2)]['base_price'] == 1040 and ('01-10', 1) not in rows
    assert rows[('01-10', 2)]['change_rate'] == Decimal('15.38')
    assert ('01-09', 1) not in rows and ('01-09', 2) not in rows  # 금→토·일
    assert rows[('01-09', 3)]['change_rate'] == Decimal('15.38')
    assert all(r['region'] == 'NATIONAL' and r['item_id'] == 1 for r in rows.values())
    since = {r['month_day'] for r in warehouse.change_history_rows(1, prices, since=date(2026, 1, 9))}
    assert min(since) == '01-09'


def test_price_change_history_merges_leap_day_into_feb_28():
    prices = {date(2024, 2, 27): 100, date(2024, 2, 28): 110, date(2024, 2, 29): 120, date(2024, 3, 1): 150}
    rows = warehouse.change_history_rows(1, prices)
    feb = [r for r in rows if r['month_day'] == '02-28' and r['horizon_days'] == 1]
    assert len(feb) == 1 and feb[0]['base_price'] == 110  # 같은 해 02-28 행이 우선
    assert not any(r['month_day'] == '02-29' for r in rows)


def test_forecast_aggregate_skips_points_without_temperature():
    points = [{'tmpMean': 10.0, 'tmx': 34.0, 'tmn': 5.0, 'pcpSum': 90.0, 'rehMean': 60.0},
              {'tmpMean': None, 'tmx': 20.0, 'tmn': -13.0, 'pcpSum': None, 'rehMean': None},
              {'tmpMean': None, 'tmx': None, 'tmn': None, 'pcpSum': 1.0}]
    row = warehouse.aggregate_forecast(points)
    assert row['station_count'] == 2 and row['sunshine_hours'] is None
    assert (row['avg_temp'], row['max_temp'], row['min_temp']) == (Decimal('10.0'), Decimal('27.0'), Decimal('-4.0'))
    assert (row['heat_station_ratio'], row['cold_station_ratio'], row['heavy_rain_station_ratio']) == (
        Decimal('50.00'), Decimal('50.00'), Decimal('100.00'))
    assert warehouse.aggregate_forecast([{'pcpSum': 1.0}]) is None


def test_production_rows_from_kosis_observations():
    from types import SimpleNamespace
    observation = SimpleNamespace(item_id=3, payload={'DT': '440715'}, units={'volume': '톤'},
                                  period_start=date(2025, 1, 1), period_end=date(2025, 12, 31))
    other_unit = SimpleNamespace(item_id=3, payload={'DT': '10'}, units={'volume': 'ha'},
                                 period_start=date(2025, 1, 1), period_end=date(2025, 12, 31))
    assert warehouse.production_rows([observation, other_unit]) == [{
        'item_id': 3, 'measure_type': 'PRODUCTION', 'period_type': 'YEAR', 'period_start': date(2025, 1, 1),
        'period_end': date(2025, 12, 31), 'volume': Decimal('440715.0'), 'volume_unit': 'TON',
        'is_estimate': False, 'source': 'KOSIS'}]


def test_exchange_rows():
    from types import SimpleNamespace
    row = SimpleNamespace(observed_on=date(2026, 11, 4), entity_code='USD', payload={'DATA_VALUE': '1,390.5'},
                          units={'rate': '원'})
    assert warehouse.exchange_rows([row]) == [{'rate_date': date(2026, 11, 4), 'currency_code': 'USD',
                                               'rate': Decimal('1390.5000'), 'unit_label': '원', 'source': 'ECOS'}]
