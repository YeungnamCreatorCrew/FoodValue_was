import os
from concurrent.futures import ThreadPoolExecutor
from datetime import timedelta
from threading import Event

import pytest
from sqlalchemy import text

from app.services import price_batch_service as batch
from app.services.fridge_service import today
from app.services.price_prediction import InsufficientDataError, Prediction
from tests.test_fridge_postgres import local

pytestmark=pytest.mark.skipif(os.getenv('FOODVALUE_TEST_POSTGRES')!='1',reason='로컬 PostgreSQL 명시 실행 필요')
ROOT='/api/v1/prices'


@pytest.fixture
def pricing(local):
    client,engine,item_id,users,headers=local
    with engine.begin() as conn:
        conn.execute(text("UPDATE item SET food_type='RAW',price_source='KAMIS',price_code=:code,price_unit_label='1kg' WHERE id=:id"),{'id':item_id,'code':f'test-{item_id}'})
        rows=[{'id':item_id,'day':today()-timedelta(days=479-i),'price':1000} for i in range(480)]
        conn.execute(text("INSERT INTO price_daily(item_id,region,price_date,price) VALUES(:id,'NATIONAL',:day,:price)"),rows)
    try:
        yield local
    finally:
        with engine.begin() as conn:
            for table in ('price_insight','price_forecast','price_model_run','price_daily'):
                conn.execute(text(f'DELETE FROM {table} WHERE item_id=:id'),{'id':item_id})


def fake_prediction():
    return Prediction('LAST_PRICE','BASELINE',[1000]*7,[950]*7,[1050]*7,
                      {'evaluation':{'LAST_PRICE':{'mape':0,'mae':0,'samples':100}},'intervals':[]})


def test_real_training_and_public_api(pricing):
    client,engine,item_id,_,_=pricing
    result=batch.run(engine,item_id)
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
    client,engine,item_id,_,_=pricing
    monkeypatch.setattr(batch,'predict',lambda *args:fake_prediction())
    first=batch.run(engine,item_id)
    second=batch.run(engine,item_id)
    assert first['runId']!=second['runId']
    with engine.connect() as conn:
        assert conn.scalar(text('SELECT count(*) FROM price_forecast WHERE item_id=:id'),{'id':item_id})==7
        assert conn.scalar(text('SELECT count(*) FROM price_insight WHERE item_id=:id'),{'id':item_id})==1
    def insufficient(*args):
        raise InsufficientDataError('test')
    monkeypatch.setattr(batch,'predict',insufficient)
    assert batch.run(engine,item_id)['status']=='INSUFFICIENT_DATA'
    forecast=client.get(f'{ROOT}/items/{item_id}/forecast').json()
    assert forecast['modelRunId']==second['runId'] and forecast['latestAttemptStatus']=='INSUFFICIENT_DATA'
    def invalid(*args):
        result=fake_prediction()
        result.prices[0]=0
        return result
    monkeypatch.setattr(batch,'predict',invalid)
    with pytest.raises(Exception):
        batch.run(engine,item_id)
    forecast=client.get(f'{ROOT}/items/{item_id}/forecast').json()
    assert forecast['modelRunId']==second['runId'] and len(forecast['points'])==7
    assert forecast['latestAttemptStatus']=='FAILED'


def test_advisory_lock_rejects_concurrent_batch_and_releases(pricing,monkeypatch):
    _,engine,item_id,_,_=pricing
    entered,release=Event(),Event()
    def blocked(*args):
        entered.set()
        assert release.wait(timeout=15)
        return fake_prediction()
    monkeypatch.setattr(batch,'predict',blocked)
    with ThreadPoolExecutor(max_workers=1) as pool:
        future=pool.submit(batch.run,engine,item_id)
        try:
            assert entered.wait(timeout=10)
            with pytest.raises(batch.BatchBusyError):
                batch.run(engine,item_id)
        finally:
            release.set()
        assert future.result(timeout=15)['status']=='SUCCESS'
    monkeypatch.setattr(batch,'predict',lambda *args:fake_prediction())
    assert batch.run(engine,item_id)['status']=='SUCCESS'


def test_invalid_scope_and_untrained_run(pricing):
    client,engine,item_id,_,_=pricing
    with pytest.raises(ValueError):
        batch.run(engine,item_id,today()+timedelta(days=1))
    with engine.begin() as conn:
        conn.execute(text('DELETE FROM price_daily WHERE item_id=:id'),{'id':item_id})
    assert batch.run(engine,item_id)['status']=='INSUFFICIENT_DATA'
    result=client.get(f'{ROOT}/items/{item_id}/forecast').json()
    assert result['status']=='INSUFFICIENT_DATA' and result['points']==[]
