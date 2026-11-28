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
            conn.execute(text(f'DELETE FROM price_forecast_factor WHERE model_run_id IN ({runs})'),{'id':series_id})
            conn.execute(text(f'DELETE FROM price_forecast_explanation WHERE model_run_id IN ({runs})'),{'id':series_id})
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


def _track_prediction(track,price):
    model='STRUCT' if track=='STRUCT' else 'V2_ENSEMBLE'
    return Prediction(model,'VALIDATED',[price]*7,[price-50]*7,[price+50]*7,
                      {'evaluation':{model:{'mape':4.0}},'modelVersion':f'test-{track.lower()}','modelTrack':track})


def test_struct_track_is_saved_and_served_in_same_format(pricing,monkeypatch):
    client,engine,item_id,series_id=pricing
    from app.services import v2_service
    monkeypatch.setattr(batch,'_v2_key',lambda db,series:'대파|RETAIL')
    monkeypatch.setattr(v2_service,'struct_enabled',lambda:True)
    monkeypatch.setattr(v2_service,'prediction',lambda engine,key,base,last,track='ENSEMBLE':
                        _track_prediction(track,1100 if track=='STRUCT' else 1200))
    result=batch.run(engine,series_id)
    assert result['status']=='SUCCESS' and result['track']=='ENSEMBLE'
    assert result['struct']['status']=='SUCCESS' and result['struct']['model']=='STRUCT'
    default=client.get(f'{ROOT}/items/{item_id}/forecast').json()
    struct=client.get(f'{ROOT}/items/{item_id}/forecast?model=STRUCT').json()
    assert default['modelTrack']=='ENSEMBLE' and default['modelName']=='V2_ENSEMBLE' and default['points'][-1]['predictedPrice']==1200
    assert struct['modelTrack']=='STRUCT' and struct['modelName']=='STRUCT' and struct['points'][-1]['predictedPrice']==1100
    assert set(default)==set(struct)  # 같은 응답 형식
    detail=client.get(f'{ROOT}/items/{item_id}?model=STRUCT').json()
    assert detail['item']['forecastPrice']==1100 and detail['forecast']['modelTrack']=='STRUCT'
    listing=client.get(f'{ROOT}/items?keyword=pg-test&model=STRUCT').json()
    assert any(row['id']==item_id and row['forecastPrice']==1100 for row in listing['items'])
    assert client.get(f'{ROOT}/items/{item_id}/factors?model=STRUCT').json()['modelTrack']=='STRUCT'
    assert client.get(f'{ROOT}/items/{item_id}/forecast?model=OTHER').status_code==400

    # struct가 실패해도 앙상블 실행은 성공으로 남고, struct 화면은 이전 struct 실행을 유지한다.
    def struct_fails(engine,key,base,last,track='ENSEMBLE'):
        if track=='STRUCT':
            raise RuntimeError('boom')
        return _track_prediction(track,1300)
    monkeypatch.setattr(v2_service,'prediction',struct_fails)
    again=batch.run(engine,series_id)
    assert again['status']=='SUCCESS' and again['struct']=={'track':'STRUCT','status':'FAILED','errorCode':'RuntimeError'}
    struct=client.get(f'{ROOT}/items/{item_id}/forecast?model=STRUCT').json()
    assert struct['points'][-1]['predictedPrice']==1100 and struct['latestAttemptStatus']=='FAILED'
    assert client.get(f'{ROOT}/items/{item_id}/forecast').json()['latestAttemptStatus']=='SUCCESS'


def test_struct_track_without_runs_is_no_forecast_not_ensemble(pricing,monkeypatch):
    client,engine,item_id,series_id=pricing
    monkeypatch.setattr(batch,'predict',lambda *args,**kwargs:fake_prediction())
    result=batch.run(engine,series_id)
    assert 'struct' not in result
    struct=client.get(f'{ROOT}/items/{item_id}/forecast?model=STRUCT').json()
    assert struct['status']=='NO_FORECAST' and struct['points']==[] and struct['latestAttemptStatus'] is None


def test_struct_factors_are_saved_and_served_with_real_struct_output(pricing,monkeypatch):
    """실험 스냅샷 2025-06-02 대파 소매 struct 예측(실제 항 분해)을 저장하고 /factors?model=STRUCT로 다시 읽는다."""
    from tests.test_struct_service import SNAPSHOT, REFIT_DAY
    if not SNAPSHOT.exists():
        pytest.skip('실험 스냅샷이 없음(Git 밖)')
    from app.services import price_summary, struct_service, v2_service
    from tools import loader
    client,engine,item_id,series_id=pricing
    monkeypatch.setenv(price_summary.LLM_ENV,'0')
    real=struct_service.forecast(loader.Snapshot(SNAPSHOT),REFIT_DAY,log=lambda *_:None)[1]
    monkeypatch.setattr(batch,'_v2_key',lambda db,series:'대파|RETAIL')
    monkeypatch.setattr(v2_service,'struct_enabled',lambda:True)
    real_prediction=v2_service.prediction
    def prediction(engine,key,base,last,track='ENSEMBLE'):
        if track=='ENSEMBLE':
            return _track_prediction(track,1200)
        return real_prediction(engine,key,base,last,track)
    monkeypatch.setattr(v2_service,'prediction',prediction)
    monkeypatch.setattr(v2_service,'forecasts',lambda engine,base,log=print,track='ENSEMBLE':{'대파|RETAIL':real})
    result=batch.run(engine,series_id)
    assert result['struct']['status']=='SUCCESS' and result['struct']['quality']=='VALIDATED'
    factors=client.get(f'{ROOT}/items/{item_id}/factors?model=STRUCT').json()
    assert factors['explained'] and factors['method']=='STRUCT_TERM_SHARE' and factors['modelName']=='STRUCT'
    assert {f['id'] for f in factors['factors']}<={'counter_change7','target_counter_ratio','struct_season',
                                                  'target_in_event_window','target_prev_day_holiday'}
    assert factors['basePrice']==factors['currentPrice']
    assert factors['basePrice']+sum(f['contribution'] for f in factors['factors'])==pytest.approx(factors['predictedPrice'],abs=1)
    assert factors['summary']['generator']=='TEMPLATE' and 'SHAP' not in str(factors['summary'])
    season=next(f for f in factors['factors'] if f['id']=='struct_season')
    assert season['hasHistory'] is False and season['category']=='CALENDAR'
    # 추이는 저장된 90일 값. 예측 입력은 2025-06-02 스냅샷이고 실행 기준일은 오늘이라 API 기간 필터 대신 저장값을 본다.
    with engine.connect() as conn:
        stored=conn.scalar(text("SELECT history FROM price_forecast_factor WHERE model_run_id=:id AND feature='counter_change7'"),
                           {'id':result['struct']['runId']})
    assert len(stored)==90 and stored[-1]['date']==REFIT_DAY.isoformat()
    history=client.get(f'{ROOT}/items/{item_id}/factors/counter_change7/history?model=STRUCT')
    assert history.status_code==200 and history.json()['factorId']=='counter_change7'
    assert client.get(f'{ROOT}/items/{item_id}/factors').json()['explained'] is False  # 앙상블(가짜 예측)은 설명 없음
