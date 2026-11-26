import os
from concurrent.futures import ThreadPoolExecutor
from datetime import timedelta
from threading import Event

import pytest
from sqlalchemy import text

from app.services import price_batch_service as batch
from app.core.dates import today
from app.services.price_prediction import InsufficientDataError, Prediction
from tests.price_postgres_fixture import local

pytestmark=pytest.mark.skipif(os.getenv('FOODVALUE_TEST_POSTGRES')!='1',reason='로컬 PostgreSQL 명시 실행 필요')
ROOT='/api/v1/prices'


@pytest.fixture
def pricing(local):
    _,engine,item_id=local
    with engine.begin() as conn:
        conn.execute(text("UPDATE item SET food_type='RAW',price_source='KAMIS',price_unit_label='1kg' WHERE id=:id"),{'id':item_id})
        # 실데이터 계열과 겹치지 않도록 품종·등급 코드를 99로 둔다.
        series_id=conn.scalar(text("INSERT INTO price_series(item_id,market,item_code,kind_code,rank_code,unit_quantity,unit) "
                                   "VALUES(:id,'RETAIL',:code,'99','99',1,'kg') RETURNING id"),{'id':item_id,'code':f'{item_id%1000:03d}'})
        rows=[{'id':series_id,'day':today()-timedelta(days=479-i),'price':1000} for i in range(480)]
        conn.execute(text("INSERT INTO price_daily(series_id,price_date,price) VALUES(:id,:day,:price)"),rows)
    try:
        yield (*local,series_id)
    finally:
        with engine.begin() as conn:
            runs='SELECT id FROM price_model_run WHERE series_id=:id'
            conn.execute(text(f'DELETE FROM price_insight WHERE model_run_id IN ({runs})'),{'id':series_id})
            conn.execute(text(f'DELETE FROM price_forecast WHERE model_run_id IN ({runs})'),{'id':series_id})
            for table in ('price_model_run','price_daily'):
                conn.execute(text(f'DELETE FROM {table} WHERE series_id=:id'),{'id':series_id})
            conn.execute(text('DELETE FROM price_series WHERE id=:id'),{'id':series_id})


def fake_prediction():
    return Prediction('LAST_PRICE','BASELINE',[1000]*7,[950]*7,[1050]*7,
                      {'evaluation':{'LAST_PRICE':{'mape':0,'mae':0,'samples':100}},'intervals':[]})


def test_real_training_and_public_api(pricing):
    client,engine,item_id,series_id=pricing
    result=batch.run(engine,series_id)
    assert result['status']=='SUCCESS' and result['quality']=='BASELINE'
    response=client.get(f'{ROOT}/items/{item_id}')
    assert response.status_code==200,response.text
    detail=response.json()
    assert len(detail['forecast']['points'])==7
    assert detail['item']['forecastPrice']==detail['forecast']['points'][-1]['predictedPrice']==1000
    assert detail['guide']['recommendation']=='HOLD'
    assert detail['forecast']['metrics']['evaluation']['LAST_PRICE']['mape']==0
    assert client.get(f'{ROOT}/items/{item_id}/history?days=30').status_code==200


def test_retry_failure_preserves_previous_result_and_no_duplicates(pricing,monkeypatch):
    client,engine,item_id,series_id=pricing
    monkeypatch.setattr(batch,'predict',lambda *args,**kwargs:fake_prediction())
    first=batch.run(engine,series_id)
    second=batch.run(engine,series_id)
    assert first['runId']!=second['runId']
    with engine.connect() as conn:
        # 실행마다 예측 7개·가이드 1개가 따로 남는다(같은 날 재실행이 이전 실행을 지우지 않음).
        runs='SELECT id FROM price_model_run WHERE series_id=:id'
        assert conn.scalar(text(f'SELECT count(*) FROM price_forecast WHERE model_run_id IN ({runs})'),{'id':series_id})==14
        assert conn.scalar(text(f'SELECT count(*) FROM price_insight WHERE model_run_id IN ({runs})'),{'id':series_id})==2
    def insufficient(*args,**kwargs):
        raise InsufficientDataError('test')
    monkeypatch.setattr(batch,'predict',insufficient)
    assert batch.run(engine,series_id)['status']=='INSUFFICIENT_DATA'
    forecast=client.get(f'{ROOT}/items/{item_id}/forecast').json()
    assert forecast['modelRunId']==second['runId'] and forecast['latestAttemptStatus']=='INSUFFICIENT_DATA'
    def invalid(*args,**kwargs):
        result=fake_prediction()
        result.prices[0]=0
        return result
    monkeypatch.setattr(batch,'predict',invalid)
    with pytest.raises(Exception):
        batch.run(engine,series_id)
    forecast=client.get(f'{ROOT}/items/{item_id}/forecast').json()
    assert forecast['modelRunId']==second['runId'] and len(forecast['points'])==7
    assert forecast['latestAttemptStatus']=='FAILED'


def test_advisory_lock_rejects_concurrent_batch_and_releases(pricing,monkeypatch):
    _,engine,item_id,series_id=pricing
    entered,release=Event(),Event()
    def blocked(*args,**kwargs):
        entered.set()
        assert release.wait(timeout=15)
        return fake_prediction()
    monkeypatch.setattr(batch,'predict',blocked)
    with ThreadPoolExecutor(max_workers=1) as pool:
        future=pool.submit(batch.run,engine,series_id)
        try:
            assert entered.wait(timeout=10)
            with pytest.raises(batch.BatchBusyError):
                batch.run(engine,series_id)
        finally:
            release.set()
        assert future.result(timeout=15)['status']=='SUCCESS'
    monkeypatch.setattr(batch,'predict',lambda *args,**kwargs:fake_prediction())
    assert batch.run(engine,series_id)['status']=='SUCCESS'


def test_invalid_scope_and_untrained_run(pricing):
    client,engine,item_id,series_id=pricing
    with pytest.raises(ValueError):
        batch.run(engine,series_id,today()+timedelta(days=1))
    with engine.begin() as conn:
        conn.execute(text('DELETE FROM price_daily WHERE series_id=:id'),{'id':series_id})
    assert batch.run(engine,series_id)['status']=='INSUFFICIENT_DATA'
    result=client.get(f'{ROOT}/items/{item_id}/forecast').json()
    assert result['status']=='INSUFFICIENT_DATA' and result['points']==[]
