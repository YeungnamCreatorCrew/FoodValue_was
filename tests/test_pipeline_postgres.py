"""수집 → 적재 → 예측 통합 검증. 가짜 Open API 응답을 사용하고 생성한 데이터만 정리한다."""
import os
import random
from datetime import date, timedelta
from types import SimpleNamespace

import pytest
from sqlalchemy import text
from sqlalchemy.orm import Session

from app import price_pipeline
from app.collectors import data_go_kr, kamis
from app.repositories import covariate_repository
from app.services import collection_service
from app.services.collection_service import Credentials
from app.services.fridge_service import today
from tests.test_fridge_postgres import local

pytestmark = pytest.mark.skipif(os.getenv('FOODVALUE_TEST_POSTGRES') != '1', reason='로컬 PostgreSQL 명시 실행 필요')
DAYS = 480
CREDENTIALS = Credentials('kamis-key', 'kamis-id', 'portal-key')


class FakeApis:
    """도매가가 소매가를 5일 앞서는 합성 시장. 실제 시장 관계를 입증하지 않는다."""

    def __init__(self, station):
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
        self.calls = []
        self.overrides = {}

    def days(self, first, last):
        day = max(first, self.start)
        while day <= min(last, today()):
            yield day, (day - self.start).days
            day += timedelta(days=1)

    def __call__(self, url, params):
        self.calls.append(url)
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
        if url == data_go_kr.HOLIDAY_URL:
            year, month = int(params['solYear']), int(params['solMonth'])
            rows = [{'locdate': int(f'{year}{month:02d}05'), 'dateName': '추석' if month == 9 else '테스트휴일',
                     'isHoliday': 'Y', 'dateKind': '01'}] if month in (5, 9) else []
            items = {'item': rows} if rows else ''
            return {'response': {'header': {'resultCode': '00'}, 'body': {'items': items, 'totalCount': len(rows)}}}
        raise AssertionError(url)


@pytest.fixture
def pipeline(local):
    client, engine, item_id, _, _ = local
    station = str(90000 + random.randint(0, 9999))
    with engine.begin() as conn:
        conn.execute(text("""UPDATE item SET food_type='RAW',price_source='KAMIS',price_code=:code,price_unit_label='1kg'
            WHERE id=:id"""), {'id': item_id, 'code': f'2{item_id % 100:02d}-00-04'})
        conn.execute(text("""INSERT INTO item_weather_station(item_id,station_code,station_name,producing_region,
            mapping_status,share,rationale) VALUES(:id,:station,'테스트','테스트 주산지','VERIFIED',1,'통합 테스트')"""),
                     {'id': item_id, 'station': station})
    apis = FakeApis(station)
    with engine.connect() as conn:
        before = conn.scalar(text('SELECT coalesce(max(id),0) FROM external_collection_run'))
    try:
        yield client, engine, item_id, apis
    finally:
        with engine.begin() as conn:
            # 공휴일은 품목과 무관한 공용 원천이다. 이 테스트 중 생성된 수집 실행이 넣은 행만 지운다.
            conn.execute(text('DELETE FROM external_observation WHERE collection_run_id > :before'), {'before': before})
            conn.execute(text('DELETE FROM external_collection_run WHERE id > :before'), {'before': before})
            for table in ('price_insight', 'price_forecast', 'price_model_run', 'price_daily', 'item_weather_station'):
                conn.execute(text(f'DELETE FROM {table} WHERE item_id=:id'), {'id': item_id})


def collect(engine, item_id, apis, **kwargs):
    results = collection_service.collect(engine, [item_id], fetch=apis, credentials=CREDENTIALS, **kwargs)
    return {(row['source'], row['dataset']): row for row in results}


def test_collect_store_dedupe_and_revision(pipeline):
    _, engine, item_id, apis = pipeline
    first = collect(engine, item_id, apis, start=apis.start)
    assert {key: row['status'] for key, row in first.items()} == {
        ('KAMIS', 'RETAIL_DAILY'): 'SUCCESS', ('KAMIS', 'WHOLESALE_DAILY'): 'SUCCESS',
        ('KMA', 'ASOS_DAILY'): 'SUCCESS', ('KASI', 'HOLIDAY'): 'SUCCESS'}
    assert first[('KAMIS', 'RETAIL_DAILY')]['inserted'] == DAYS
    assert first[('KMA', 'ASOS_DAILY')]['received'] == DAYS - 1  # ASOS는 전일까지
    with engine.connect() as conn:
        assert conn.scalar(text("SELECT count(*) FROM price_daily WHERE item_id=:id AND region='NATIONAL'"), {'id': item_id}) == DAYS
        latest = conn.scalar(text('SELECT price FROM price_daily WHERE item_id=:id AND price_date=:d'), {'id': item_id, 'd': today()})
        assert latest == apis.retail[-1]
        run = conn.execute(text('SELECT status,request_count,records_received,records_inserted,finished_at FROM external_collection_run WHERE id=:id'),
                           {'id': first[('KAMIS', 'WHOLESALE_DAILY')]['runId']}).one()
        assert run[0] == 'SUCCESS' and run[1] == 6 and run[2] == run[3] == DAYS and run[4] is not None
    # 같은 내용의 재수집은 새 행을 만들지 않는다.
    again = collect(engine, item_id, apis, start=apis.start)
    assert all(row['inserted'] == 0 for row in again.values())
    # 원천이 값을 수정하면 새 버전을 보존하고 예측 대상 가격도 갱신한다.
    apis.overrides[today()] = 4321
    revised = collect(engine, item_id, apis)
    assert revised[('KAMIS', 'RETAIL_DAILY')]['inserted'] == 1
    assert revised[('KAMIS', 'RETAIL_DAILY')]['startDate'] == (today() - timedelta(days=14)).isoformat()
    with engine.connect() as conn:
        assert conn.scalar(text('SELECT price FROM price_daily WHERE item_id=:id AND price_date=:d'), {'id': item_id, 'd': today()}) == 4321
        assert conn.scalar(text("SELECT count(*) FROM external_observation WHERE item_id=:id AND dataset='RETAIL_DAILY' AND observed_on=:d"),
                           {'id': item_id, 'd': today()}) == 2
    with Session(engine) as db:
        covariates = covariate_repository.load(db, item_id, apis.start, today(), today() + timedelta(days=7))
    assert len(covariates.wholesale) == DAYS and len(covariates.weather) == DAYS - 1
    assert covariates.weather[today() - timedelta(days=1)]['sumRn'] in (0.0, 4.5)
    assert date(today().year, 9, 5) in covariates.holidays and today().year in covariates.holiday_years


def test_missing_credentials_are_recorded_as_skipped(pipeline):
    _, engine, item_id, apis = pipeline
    results = collection_service.collect(engine, [item_id], fetch=apis, credentials=Credentials())
    assert {row['status'] for row in results} == {'SKIPPED'} and apis.calls == []
    assert {row['errorCode'] for row in results} == {'MISSING_KAMIS_CREDENTIALS', 'MISSING_DATA_GO_KR_KEY'}


def test_full_pipeline_publishes_exogenous_forecast(pipeline):
    client, engine, item_id, apis = pipeline
    collect(engine, item_id, apis, start=apis.start)
    args = SimpleNamespace(item_ids=[item_id], start=None, end=None, collect_only=False, predict_only=True)
    output = price_pipeline.run(engine, args)
    assert price_pipeline.exit_code(output) == 0
    prediction = output['predictions'][0]
    with engine.connect() as conn:
        metrics = conn.scalar(text('SELECT metrics FROM price_model_run WHERE id=:id'), {'id': prediction['runId']})
    assert prediction['status'] == 'SUCCESS', prediction
    assert prediction['model'] == 'XGBOOST_EXT' and prediction['quality'] == 'VALIDATED', metrics['evaluation']
    detail = client.get(f'/api/v1/prices/items/{item_id}').json()
    metrics = detail['forecast']['metrics']
    assert metrics['externalGroups'] == ['WHOLESALE', 'WEATHER', 'CALENDAR']
    assert metrics['externalCoverage']['WHOLESALE'] == 1.0
    names = [factor['name'] for factor in client.get(f'/api/v1/prices/items/{item_id}/factors').json()['factors']]
    assert names[:3] == ['최근 가격', '도매가격', '주산지 기상']
    assert len(detail['forecast']['points']) == 7
