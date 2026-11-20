"""수집 → 적재 → 예측 통합 검증. 가짜 Open API 응답을 사용하고 생성한 데이터만 정리한다."""
import os
import random
from datetime import date, timedelta
from decimal import Decimal
from types import SimpleNamespace

import pytest
from sqlalchemy import text
from sqlalchemy.orm import Session

from app import price_backtest, price_pipeline
from app.collectors import data_go_kr, ecos, kamis, kosis
from app.collectors.records import windows
from app.repositories import covariate_repository, series_repository
from app.services import collection_service, warehouse_service
from app.services.collection_service import Credentials
from app.services.fridge_service import today
from tests.test_fridge_postgres import local

pytestmark = pytest.mark.skipif(os.getenv('FOODVALUE_TEST_POSTGRES') != '1', reason='로컬 PostgreSQL 명시 실행 필요')
DAYS = 480
RETAIL_PRICE = ("SELECT d.price FROM price_daily d JOIN price_series s ON s.id=d.series_id "
                "WHERE s.item_id=:id AND s.market='RETAIL' AND d.price_date=:d")
RUN_COUNT = 'SELECT count(*) FROM price_model_run WHERE series_id IN (SELECT id FROM price_series WHERE item_id=:id)'
CREDENTIALS = Credentials('kamis-key', 'kamis-id', 'portal-key', 'kosis-key', 'ecos-key')


class FakeApis:
    """도매가가 소매가를 5일 앞서는 합성 시장. 실제 시장 관계를 입증하지 않는다."""

    def __init__(self, station, code='246-00-04'):
        self.start = today() - timedelta(days=DAYS - 1)
        rng = random.Random(3)
        level, drift, self.wholesale = 1000.0, 0, []
        for index in range(DAYS + 5):
            if index % 15 == 0:
                drift = rng.choice([-25, -12, 12, 25])
            level = max(300, level + drift + rng.gauss(0, 5))
            self.wholesale.append(level)
        self.retail = [round(1.5 * self.wholesale[i] + rng.gauss(0, 3)) for i in range(DAYS)]
        self.station = station
        self.code = code
        self.calls = []
        self.overrides = {}

    def days(self, first, last):
        day = max(first, self.start)
        while day <= min(last, today()):
            yield day, (day - self.start).days
            day += timedelta(days=1)

    def __call__(self, url, params):
        self.calls.append(url)
        if url == kamis.URL and params.get('action') == kamis.DAILY_ACTION:
            assert params['p_cert_key'] == 'kamis-key'
            day = date.fromisoformat(params['p_regday'])
            index = (day - self.start).days
            if not 0 <= index < DAYS:
                return {'data': ['001']}
            retail = params['p_product_cls_code'] == '01'
            price = self.overrides.get(day, self.retail[index] if retail else round(self.wholesale[index + 5]))
            row = {'item_name': '대파', 'item_code': params['p_item_category_code'][0] + '00', 'kind_code': '', 'rank_code': '',
                   'day1': f'당일 ({day.month:02d}/{day.day:02d})', 'dpr1': f'{price:,}'}
            return {'data': {'error_code': '000', 'item': [row, {**row, 'item_code': self.code[:3],
                                                                 'kind_code': self.code[4:6], 'rank_code': self.code[7:]}]}}
        if url == kamis.URL:
            assert params['p_cert_key'] == 'kamis-key'
            retail = params['p_productclscode'] == '01'
            rows = [{'countyname': '평균', 'yyyy': str(d.year), 'regday': d.strftime('%m/%d'), 'kindname': '대파(1kg)',
                     'price': f'{self.overrides.get(d, self.retail[i] if retail else round(self.wholesale[i + 5])):,}'}
                    for d, i in self.days(date.fromisoformat(params['p_startday']), date.fromisoformat(params['p_endday']))]
            return {'data': {'error_code': '000', 'item': rows}}
        if url == data_go_kr.ASOS_URL:
            first, last = (date(int(v[:4]), int(v[4:6]), int(v[6:])) for v in (params['startDt'], params['endDt']))
            rows = [{'tm': d.isoformat(), 'stnId': params['stnIds'], 'stnNm': '테스트', 'avgTa': '15.0',
                     'minTa': '10.0', 'maxTa': '20.0', 'sumRn': '' if i % 3 else '4.5', 'avgRhm': '60', 'sumSsHr': '7'}
                    for d, i in self.days(first, last)]
            return {'response': {'header': {'resultCode': '00'}, 'body': {'items': {'item': rows}, 'totalCount': len(rows)}}}
        if url.startswith(ecos.BASE_URL + '/ecos-key/'):
            first, last = (date(int(v[:4]), int(v[4:6]), int(v[6:])) for v in url.split('/')[-3:-1])
            rows = [{'TIME': d.strftime('%Y%m%d'), 'DATA_VALUE': f'{1300 + i % 50:.1f}', 'UNIT_NAME': '원',
                     'ITEM_NAME1': '원/미국달러(매매기준율)'} for d, i in self.days(first, last) if d.weekday() < 5]
            return {'StatisticSearch': {'list_total_count': len(rows), 'row': rows}}
        if url == kosis.URL:
            assert params['apiKey'] == 'kosis-key'
            return [{'PRD_DE': str(y), 'DT': str(300000 + y), 'UNIT_NM': '톤', 'LST_CHN_DE': f'{y + 1}-10-28',
                     'ITM_NM': '대파:생산량'} for y in range(int(params['startPrdDe']), int(params['endPrdDe']) + 1)
                    if y < today().year]
        if url == data_go_kr.VILAGE_URL:
            day = date(int(params['base_date'][:4]), int(params['base_date'][4:6]), int(params['base_date'][6:]))
            rows = [{'category': 'TMP', 'fcstDate': (day + timedelta(days=1)).strftime('%Y%m%d'),
                     'fcstTime': f'{h:02d}00', 'fcstValue': '12'} for h in range(24)]
            rows += [{'category': 'TMX', 'fcstDate': (day + timedelta(days=1)).strftime('%Y%m%d'), 'fcstTime': '1500',
                      'fcstValue': '34.0' if params['nx'] == 60 else '20.0'}]
            return {'response': {'header': {'resultCode': '00'}, 'body': {'items': {'item': rows}, 'totalCount': len(rows)}}}
        if url == data_go_kr.HOLIDAY_URL:
            year, month = int(params['solYear']), int(params['solMonth'])
            rows = [{'locdate': int(f'{year}{month:02d}05'), 'dateName': '추석' if month == 9 else '테스트휴일',
                     'isHoliday': 'Y', 'dateKind': '01'}] if month in (5, 9) else []
            items = {'item': rows} if rows else ''
            return {'response': {'header': {'resultCode': '00'}, 'body': {'items': items, 'totalCount': len(rows)}}}
        raise AssertionError(url)


@pytest.fixture
def pipeline(local, monkeypatch):
    client, engine, item_id, _, _ = local
    with engine.connect() as conn:
        name = conn.scalar(text('SELECT name FROM item WHERE id=:id'), {'id': item_id})
    monkeypatch.setitem(kosis.PRODUCTION_SERIES, name, ('DT_1ET0291', 'T44'))  # 테스트 품목을 대파 시계열에 연결
    station = str(90000 + random.randint(0, 9999))
    code = f'2{item_id % 100:02d}-99-04'  # 품종 99: 실데이터 계열(예: 246-00-04)과 겹치지 않게
    with engine.begin() as conn:
        conn.execute(text("UPDATE item SET food_type='RAW',price_source='KAMIS',price_unit_label='1kg' WHERE id=:id"),
                     {'id': item_id})
        for market in ('RETAIL', 'WHOLESALE'):
            conn.execute(text('INSERT INTO price_series(item_id,market,item_code,kind_code,rank_code,unit_quantity,unit) '
                              "VALUES(:id,:market,:item,'99','04',1,'kg')"), {'id': item_id, 'market': market, 'item': code[:3]})
        conn.execute(text("""INSERT INTO item_weather_station(item_id,station_code,station_name,producing_region,
            mapping_status,share,rationale) VALUES(:id,:station,'테스트','테스트 주산지','VERIFIED',1,'통합 테스트')"""),
                     {'id': item_id, 'station': station})
    apis = FakeApis(station, code)
    with engine.connect() as conn:
        before = conn.scalar(text('SELECT coalesce(max(id),0) FROM external_collection_run'))
    try:
        yield client, engine, item_id, apis
    finally:
        with engine.begin() as conn:
            # price_daily가 원본 행을 참조하므로 계열 자료를 먼저 지운다.
            series = 'SELECT id FROM price_series WHERE item_id=:id'
            runs = f'SELECT id FROM price_model_run WHERE series_id IN ({series})'
            for table in ('price_forecast_factor', 'price_forecast_explanation', 'price_insight', 'price_forecast'):
                conn.execute(text(f'DELETE FROM {table} WHERE model_run_id IN ({runs})'), {'id': item_id})
            conn.execute(text(f'DELETE FROM backtest_run WHERE series_id IN ({series})'), {'id': item_id})
            for table in ('price_model_run', 'price_daily', 'price_change_history'):
                conn.execute(text(f'DELETE FROM {table} WHERE series_id IN ({series})'), {'id': item_id})
            # 공휴일은 품목과 무관한 공용 원천이다. 이 테스트 중 생성된 수집 실행이 넣은 행만 지운다.
            conn.execute(text('DELETE FROM external_observation WHERE collection_run_id > :before'), {'before': before})
            conn.execute(text('DELETE FROM external_collection_run WHERE id > :before'), {'before': before})
            for table in ('item_weather_station', 'item_production', 'event_item_weight', 'price_series'):
                conn.execute(text(f'DELETE FROM {table} WHERE item_id=:id'), {'id': item_id})


def kamis_expectation(apis):
    """(적재될 일수, 요청 수). 최근 PERIOD_LIMIT_DAYS일은 기간 API, 그 이전은 평일만 일별 API로 받는다."""
    boundary = today() - timedelta(days=kamis.PERIOD_LIMIT_DAYS)
    older = [d for d, _ in apis.days(apis.start, boundary - timedelta(days=1)) if d.weekday() < 5]
    recent = [d for d, _ in apis.days(boundary, today())]
    return len(older) + len(recent), len(older) + len(list(windows(boundary, today(), kamis.WINDOW_DAYS)))


def collect(engine, item_id, apis, **kwargs):
    results = collection_service.collect(engine, [item_id], fetch=apis, credentials=CREDENTIALS, **kwargs)
    return {(row['source'], row['dataset']): row for row in results}


def test_collect_store_dedupe_and_revision(pipeline):
    _, engine, item_id, apis = pipeline
    first = collect(engine, item_id, apis, start=apis.start)
    assert {key: row['status'] for key, row in first.items()} == {
        ('KAMIS', 'RETAIL_DAILY'): 'SUCCESS', ('KAMIS', 'WHOLESALE_DAILY'): 'SUCCESS',
        ('KMA', 'ASOS_DAILY'): 'SUCCESS', ('KMA', 'VILAGE_FCST_DAILY'): 'SUCCESS', ('KASI', 'HOLIDAY'): 'SUCCESS',
        ('KOSIS', 'CROP_PRODUCTION'): 'SUCCESS', ('ECOS', 'EXCHANGE_RATE_DAILY'): 'SUCCESS'}
    kamis_days, kamis_requests = kamis_expectation(apis)
    assert first[('KAMIS', 'RETAIL_DAILY')]['inserted'] == kamis_days
    # 주산지 관측소 + 전국 집계 관측소. ASOS는 전일까지
    assert first[('KMA', 'ASOS_DAILY')]['received'] == (len(data_go_kr.NATIONAL_STATIONS) + 1) * (DAYS - 1)
    with engine.connect() as conn:
        counts = dict(conn.execute(text('SELECT s.market, count(d.id) FROM price_series s JOIN price_daily d ON d.series_id=s.id '
                                        'WHERE s.item_id=:id GROUP BY 1'), {'id': item_id}).all())
        assert counts == {'RETAIL': kamis_days, 'WHOLESALE': kamis_days}
        assert conn.scalar(text(RETAIL_PRICE), {'id': item_id, 'd': today()}) == apis.retail[-1]
        assert conn.scalar(text('SELECT count(*) FROM price_daily d JOIN price_series s ON s.id=d.series_id '
                                'WHERE s.item_id=:id AND d.observation_id IS NULL'), {'id': item_id}) == 0
        run = conn.execute(text('SELECT status,request_count,records_received,records_inserted,finished_at FROM external_collection_run WHERE id=:id'),
                           {'id': first[('KAMIS', 'WHOLESALE_DAILY')]['runId']}).one()
        assert run[0] == 'SUCCESS' and run[1] == kamis_requests and run[2] == run[3] == kamis_days and run[4] is not None
    # 같은 내용의 재수집은 새 행을 만들지 않는다.
    again = collect(engine, item_id, apis, start=apis.start)
    assert all(row['inserted'] == 0 for row in again.values())
    # 원천이 값을 수정하면 새 버전을 보존하고 예측 대상 가격도 갱신한다.
    apis.overrides[today()] = 4321
    revised = collect(engine, item_id, apis)
    assert revised[('KAMIS', 'RETAIL_DAILY')]['inserted'] == 1
    assert revised[('KAMIS', 'RETAIL_DAILY')]['startDate'] == (today() - timedelta(days=14)).isoformat()
    with engine.connect() as conn:
        assert conn.scalar(text(RETAIL_PRICE), {'id': item_id, 'd': today()}) == 4321
        assert conn.scalar(text("SELECT count(*) FROM external_observation WHERE item_id=:id AND dataset='RETAIL_DAILY' AND observed_on=:d"),
                           {'id': item_id, 'd': today()}) == 2
    with Session(engine) as db:
        covariates = covariate_repository.load(db, series_repository.get(db, item_id), apis.start, today(), today() + timedelta(days=7))
    assert len(covariates.counterpart) == kamis_days and len(covariates.weather) == DAYS - 1
    assert covariates.weather[today() - timedelta(days=1)]['sumRn'] in (0.0, 4.5)
    assert date(today().year, 9, 5) in covariates.holidays and today().year in covariates.holiday_years


def test_missing_credentials_are_recorded_as_skipped(pipeline):
    _, engine, item_id, apis = pipeline
    results = collection_service.collect(engine, [item_id], fetch=apis, credentials=Credentials())
    assert {row['status'] for row in results} == {'SKIPPED'} and apis.calls == []
    assert {row['errorCode'] for row in results} == {'MISSING_KAMIS_CREDENTIALS', 'MISSING_DATA_GO_KR_KEY', 'MISSING_KOSIS_KEY',
                                                    'MISSING_ECOS_KEY'}


def test_full_pipeline_publishes_exogenous_forecast(pipeline):
    client, engine, item_id, apis = pipeline
    collect(engine, item_id, apis, start=apis.start)
    args = SimpleNamespace(item_ids=[item_id], start=None, end=None, collect_only=False, predict_only=True)
    output = price_pipeline.run(engine, args)
    assert price_pipeline.exit_code(output) == 0
    prediction = output['predictions'][0]
    with engine.connect() as conn:
        metrics = conn.scalar(text('SELECT metrics FROM price_model_run WHERE id=:id'), {'id': prediction['runId']})
    assert [(row['market'], row['status']) for row in output['predictions']] == [('RETAIL', 'SUCCESS'), ('WHOLESALE', 'SUCCESS')]
    assert prediction['status'] == 'SUCCESS', prediction
    assert prediction['model'] in ('XGBOOST_EXT', 'XGBOOST_WEIGHTED') and prediction['quality'] == 'VALIDATED', metrics['evaluation']
    detail = client.get(f'/api/v1/prices/items/{item_id}').json()
    metrics = detail['forecast']['metrics']
    # 전국 날씨·명절·환율은 공용 테이블이라 로컬 DB에 수집된 만큼 그룹이 더 붙을 수 있다. 이 테스트가 넣은 원천만 확인한다.
    assert {'COUNTERPART', 'WEATHER', 'CALENDAR'} <= set(metrics['externalGroups'])
    assert metrics['externalCoverage']['COUNTERPART'] == 1.0
    assert {'MARKET': ['COUNTERPART'], 'WEATHER': ['WEATHER'], 'CALENDAR': ['CALENDAR']}.items() <= \
        {k: [g for g in v if g in ('COUNTERPART', 'WEATHER', 'CALENDAR')] for k, v in metrics['weighting']['blocks'].items()}.items()
    assert all(0.0 <= value <= 1.0 for value in metrics['weighting']['weights'].values())
    observed = [factor['name'] for factor in detail['guide']['factors']]
    assert observed[:3] == ['최근 가격', '도매가격', '주산지 기상']
    # 학습 모델로 공개된 실행은 SHAP 설명이 함께 저장되고, 기대값 + 기여 합이 예측가와 맞는다.
    factors = client.get(f'/api/v1/prices/items/{item_id}/factors').json()
    assert factors['explained'] is True and factors['predictedPrice'] == detail['forecast']['points'][-1]['predictedPrice']
    assert abs(factors['basePrice'] + sum(f['contribution'] for f in factors['factors']) - factors['predictedPrice']) < 1 + .05 * len(factors['factors'])
    assert 'counterLast' in {f['id'] for f in factors['factors']} and factors['summary']['headline']
    history = client.get(f'/api/v1/prices/items/{item_id}/factors/current/history?days=14').json()
    assert history['points'] and history['points'][-1]['date'] == factors['baseDate']
    assert len(detail['forecast']['points']) == 7
    wholesale = client.get(f'/api/v1/prices/items/{item_id}/forecast?market=WHOLESALE').json()
    assert wholesale['market'] == 'WHOLESALE' and len(wholesale['points']) == 7
    assert wholesale['metrics']['externalCoverage']['COUNTERPART'] == 1.0  # 도매 예측의 상대 시장 = 소매


def test_backtest_reproduces_past_forecasts_read_only(pipeline):
    _, engine, item_id, apis = pipeline
    collect(engine, item_id, apis, start=apis.start)
    with engine.connect() as conn:
        runs_before = conn.scalar(text(RUN_COUNT), {'id': item_id})
    dates = [today() - timedelta(days=21), today() - timedelta(days=14)]
    output, records = price_backtest.run(engine, item_id, dates, workers=2)
    assert [run['status'] for run in output['runs']] == ['SUCCESS', 'SUCCESS']
    assert output['summary']['overall']['points'] == len(records) == 14  # 가짜 자료는 매일 가격이 있음
    # 기준일 이후 가격은 입력에 쓰지 않는다: 각 행의 현재가는 그 기준일의 가격이다.
    first = date.fromisoformat(records[0]['baseDate'])
    assert records[0]['currentPrice'] == apis.retail[(first - apis.start).days]
    with engine.connect() as conn:
        assert conn.scalar(text(RUN_COUNT), {'id': item_id}) == runs_before
    saved = price_backtest.save(engine, output, records, start=dates[0], end=dates[-1], every=7, note='통합 테스트')
    with engine.begin() as conn:
        assert conn.scalar(text('SELECT count(*) FROM backtest_point WHERE backtest_run_id=:id'), {'id': saved}) == 14
        assert conn.scalar(text('SELECT count(*) FROM backtest_origin WHERE backtest_run_id=:id'), {'id': saved}) == 2
        conn.execute(text('DELETE FROM backtest_run WHERE id=:id'), {'id': saved})


GLOBAL_TABLES = ('weather_daily', 'calendar_day', 'calendar_event', 'exchange_rate_daily')


def test_structured_tables_are_refreshed_idempotently(pipeline):
    _, engine, item_id, apis = pipeline
    with engine.connect() as conn:
        if any(conn.scalar(text(f'SELECT count(*) FROM {table}')) for table in GLOBAL_TABLES):
            pytest.skip('기존 전국 정형 데이터를 덮어쓰지 않도록 빈 테이블에서만 실행')
    try:
        collect(engine, item_id, apis, start=apis.start)
        first = warehouse_service.refresh(engine, [item_id], weather_start=apis.start, weather_end=today())
        again = warehouse_service.refresh(engine, [item_id], weather_start=apis.start, weather_end=today())
        assert first == again and first['weather_daily'] == DAYS - 1 and first['weather_forecast'] == 1
        with engine.connect() as conn:
            weather = conn.execute(text("SELECT avg_temp,max_temp,min_temp,station_count,heat_station_ratio FROM weather_daily "
                                        "WHERE weather_date=:d AND data_type='ACTUAL'"), {'d': today() - timedelta(days=1)}).one()
            assert tuple(weather) == (Decimal('15.0'), Decimal('20.0'), Decimal('10.0'),
                                      len(data_go_kr.NATIONAL_STATIONS), Decimal('0.00'))
            forecast = conn.execute(text("SELECT avg_temp,heat_station_ratio,station_count,sunshine_hours FROM weather_daily "
                                         "WHERE data_type='FORECAST'")).one()
            # 격자 (60, 120)·(60, 127) 두 곳만 최고 34℃
            assert tuple(forecast) == (Decimal('12.0'), Decimal('11.76'), len(data_go_kr.FORECAST_POINTS), None)
            years = conn.scalar(text('SELECT count(DISTINCT extract(year FROM cal_date)) FROM calendar_day'))
            assert conn.scalar(text('SELECT count(*) FROM calendar_day')) >= 365 * years
            chuseok = conn.execute(text("SELECT is_holiday,holiday_name,is_market_closed FROM calendar_day WHERE cal_date=:d"),
                                   {'d': date(today().year, 9, 5)}).one()
            assert tuple(chuseok) == (True, '추석', True)
            event = conn.execute(text("SELECT name,end_date,effect_start_date FROM calendar_event "
                                      "WHERE event_code='CHUSEOK' AND start_date=:d"), {'d': date(today().year, 9, 5)}).one()
            assert tuple(event) == (f'{today().year} 추석', date(today().year, 9, 5), date(today().year, 8, 22))
            production = conn.execute(text("SELECT period_start,period_end,volume,volume_unit,source FROM item_production "
                                           "WHERE item_id=:id ORDER BY period_start DESC LIMIT 1"), {'id': item_id}).one()
            last = today().year - 1
            assert tuple(production) == (date(last, 1, 1), date(last, 12, 31), Decimal(300000 + last), 'TON', 'KOSIS')
            assert first['item_production'] == conn.scalar(text('SELECT count(*) FROM item_production WHERE item_id=:id'), {'id': item_id})
            published = conn.scalar(text("SELECT publication_status FROM external_observation WHERE dataset='CROP_PRODUCTION' "
                                         "AND item_id=:id LIMIT 1"), {'id': item_id})
            assert published == 'SOURCE_PROVIDED'
            rate = conn.execute(text("SELECT count(*), max(rate_date), min(unit_label) FROM exchange_rate_daily "
                                     "WHERE currency_code='USD'")).one()
            weekdays = sum(1 for d, _ in apis.days(apis.start, today()) if d.weekday() < 5)
            assert rate[0] == weekdays == first['exchange_rate_daily'] and rate[2] == '원'
            history = conn.scalar(text('SELECT count(*) FROM price_change_history WHERE series_id IN '
                                       '(SELECT id FROM price_series WHERE item_id=:id)'), {'id': item_id})
            assert history == first['price_change_history'] and history > 0
            # 가짜 자료는 추석이 해마다 하나뿐이고 기간이 짧아 2개 연도 이상의 명절 효과가 없을 수 있다.
            learned = conn.scalar(text("SELECT count(*) FROM event_item_weight WHERE item_id=:id AND weight_source='LEARNED'"),
                                  {'id': item_id})
            assert learned == first['event_item_weight']
    finally:
        with engine.begin() as conn:
            for table in GLOBAL_TABLES:
                conn.execute(text(f'DELETE FROM {table}'))
            conn.execute(text('DELETE FROM price_change_history WHERE series_id IN (SELECT id FROM price_series WHERE item_id=:id)'),
                         {'id': item_id})
            conn.execute(text('DELETE FROM item_production WHERE item_id=:id'), {'id': item_id})
            conn.execute(text('DELETE FROM event_item_weight WHERE item_id=:id'), {'id': item_id})
