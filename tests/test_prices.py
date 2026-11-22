import json
from datetime import date, timedelta

import pytest
from sqlalchemy import event, text

from app.routers.prices import router
from app.services import price_service
from tests.test_fridge import api

ROOT='/api/v1/prices'
DAY=date(2026,10,8)


@pytest.fixture
def prices(api,monkeypatch):
    client,engine,actor,application=api
    application.include_router(router,prefix='/api/v1')
    monkeypatch.setattr(price_service,'today',lambda:DAY)
    # 공개 조회는 토큰 없음, 로그인 조회만 테스트 사용자를 반환한다.
    from app.core.deps import get_optional_user
    from fastapi import Header,HTTPException
    def optional(authorization:str | None=Header(None)):
        if authorization=='Bearer test':
            return actor
        if authorization:
            raise HTTPException(401,'인증 실패')
        return None
    application.dependency_overrides[get_optional_user]=optional
    statements=[
        '''CREATE TABLE price_series(id INTEGER PRIMARY KEY,item_id INTEGER,source TEXT DEFAULT 'KAMIS',market TEXT,
        item_code TEXT,kind_code TEXT,rank_code TEXT,unit_quantity NUMERIC,unit TEXT,created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)''',
        '''CREATE TABLE price_daily(id INTEGER PRIMARY KEY,series_id INTEGER,price_date DATE,price INTEGER,
        observation_id INTEGER,created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)''',
        '''CREATE TABLE price_model_run(id INTEGER PRIMARY KEY,series_id INTEGER,base_date DATE,data_date DATE,
        status TEXT,model_name TEXT,model_version TEXT,quality TEXT,metrics JSON,error_code TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,finished_at TIMESTAMP)''',
        '''CREATE TABLE price_forecast(id INTEGER PRIMARY KEY,target_date DATE,
        predicted_price INTEGER,lower_price INTEGER,upper_price INTEGER,model_run_id INTEGER,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)''',
        '''CREATE TABLE price_insight(id INTEGER PRIMARY KEY,recommendation TEXT,
        buy_after_days INTEGER,expected_saving INTEGER,mape NUMERIC,factors JSON,summary JSON,summary_generator TEXT,
        summary_model TEXT,summary_prompt_version TEXT,model_run_id INTEGER,created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)''',
        '''CREATE TABLE price_forecast_explanation(model_run_id INTEGER PRIMARY KEY,horizon_days INTEGER,method TEXT,
        current_price NUMERIC,damping NUMERIC,base_price NUMERIC,predicted_price INTEGER,created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)''',
        '''CREATE TABLE price_forecast_factor(id INTEGER PRIMARY KEY,model_run_id INTEGER,feature TEXT,feature_value REAL,
        contribution NUMERIC,history JSON,created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)''',
        "INSERT INTO item(id,name,category,default_unit,default_storage,food_type,price_source,price_unit_label) VALUES(2,'대파','VEGETABLE','단','FRIDGE','RAW','KAMIS','1kg')",
        # 계열 1: 대파 소매(가격·예측 있음), 계열 2: 두부 소매(자료 없음), 계열 3: 대파 도매(자료 없음)
        "INSERT INTO price_series(id,item_id,market,item_code,kind_code,rank_code,unit_quantity,unit) VALUES(1,2,'RETAIL','211','00','01',1,'kg')",
        "INSERT INTO price_series(id,item_id,market,item_code,kind_code,rank_code,unit_quantity,unit) VALUES(2,1,'RETAIL','999','00','01',300,'g')",
        "INSERT INTO price_series(id,item_id,market,item_code,kind_code,rank_code,unit_quantity,unit) VALUES(3,2,'WHOLESALE','211','00','01',1,'kg')",
        "INSERT INTO item_alias(item_id,alias) VALUES(2,'흙대파')",
        "INSERT INTO price_model_run(id,series_id,base_date,data_date,status,model_name,model_version,quality,metrics,finished_at) VALUES(1,1,'2026-10-08','2026-10-08','SUCCESS','XGBOOST','test','VALIDATED','{}',CURRENT_TIMESTAMP)",
        "INSERT INTO price_insight(recommendation,buy_after_days,expected_saving,mape,factors,model_run_id) VALUES('BUY_LATER',7,70,3,'[]',1)",
    ]
    with engine.begin() as conn:
        for statement in statements:
            conn.execute(text(statement))
        for offset,price in ((0,1000),(-7,1100),(-10,1150)):
            conn.execute(text("INSERT INTO price_daily(series_id,price_date,price) VALUES(1,:day,:p)"),{'day':DAY+timedelta(days=offset),'p':price})
        for h in range(1,8):
            conn.execute(text("INSERT INTO price_forecast(target_date,predicted_price,lower_price,upper_price,model_run_id) VALUES(:target,:p,:low,:high,1)"),
                         {'target':DAY+timedelta(days=h),'p':1000-h*10,'low':900-h*10,'high':1100-h*10})
    yield client,engine,actor


def test_public_list_filter_search_sort(prices):
    client,_,_=prices
    result=client.get(ROOT+'/items').json()
    assert result['total']==2
    row=next(x for x in result['items'] if x['id']==2)
    assert row['currentPrice']==1000 and row['weeklyChangePercent']==-9.09
    assert row['forecastPrice']==930 and row['status']=='READY'
    assert row['market']=='RETAIL' and row['seriesId']==1 and row['unitLabel']=='1kg'
    assert client.get(ROOT+'/items?keyword=흙대파').json()['total']==1
    assert client.get(ROOT+'/items',params={'keyword':'%'}).json()['total']==0
    assert client.get(ROOT+'/items?category=VEGETABLE&size=1').json()['total']==1
    assert client.get(ROOT+'/items?sort=change').json()['items'][0]['id']==2


def test_detail_forecast_consistency_and_private_inventory(prices):
    client,_,actor=prices
    detail=client.get(ROOT+'/items/2').json()
    forecast=client.get(ROOT+'/items/2/forecast').json()
    assert detail['forecast']==forecast
    assert detail['item']['forecastPrice']==forecast['points'][-1]['predictedPrice']
    assert detail['fridge'] is None
    client.post('/api/v1/fridge/items',json={'itemId':2,'displayName':'대파','quantity':'.5',
                'unit':'단','storage':'FRIDGE','purchasedAt':'2026-10-01'})
    assert client.get(ROOT+'/items/2',headers={'Authorization':'Bearer test'}).json()['fridge']['quantities']=={'단':'0.500'}
    actor.id=2
    assert client.get(ROOT+'/items/2',headers={'Authorization':'Bearer test'}).json()['fridge']['ingredientCount']==0
    assert client.get(ROOT+'/items/2',headers={'Authorization':'Bearer wrong'}).status_code==401


def test_history_preserves_missing_dates(prices):
    client,_,_=prices
    result=client.get(ROOT+'/items/2/history?days=14')
    assert result.status_code==200
    rows=result.json()['points']
    assert len(rows)==14 and rows[-1]['price']==1000 and rows[-2]['price'] is None
    assert client.get(ROOT+'/items/2/history?days=15').status_code==400


def test_history_long_periods(prices):
    client,_,_=prices
    for days in (180,365):
        rows=client.get(ROOT+f'/items/2/history?days={days}').json()['points']
        assert len(rows)==days and rows[-1]['price']==1000
    assert client.get(ROOT+'/items/2/history?days=120').status_code==400
    assert client.get(ROOT+'/items/2/history?days=366').status_code==400


def test_empty_stale_partial_results(prices):
    client,engine,_=prices
    assert client.get(ROOT+'/items/1').json()['item']['status']=='NO_DATA'
    assert client.get(ROOT+'/items/1/forecast').json()['points']==[]
    with engine.begin() as conn:
        conn.execute(text("INSERT INTO price_model_run(id,series_id,base_date,status) VALUES(2,1,'2026-10-08','FAILED')"))
    result=client.get(ROOT+'/items/2/forecast').json()
    assert result['modelRunId']==1 and result['latestAttemptStatus']=='FAILED'
    with engine.begin() as conn:
        conn.execute(text('DELETE FROM price_forecast WHERE id=(SELECT max(id) FROM price_forecast)'))
    assert client.get(ROOT+'/items/2/forecast').json()['points']==[]


def test_query_count_does_not_grow_per_item(prices):
    client,engine,_=prices
    def count():
        calls=[]
        def listener(*args):
            calls.append(1)
        event.listen(engine,'before_cursor_execute',listener)
        try:
            assert client.get(ROOT+'/items').status_code==200
        finally:
            event.remove(engine,'before_cursor_execute',listener)
        return len(calls)
    first=count()
    with engine.begin() as conn:
        for i in range(3,13):
            conn.execute(text("INSERT INTO item(id,name,category,default_unit,default_storage,food_type,price_source) VALUES(:id,:name,'VEGETABLE','g','FRIDGE','RAW','KAMIS')"),{'id':i,'name':f'품목{i}'})
            conn.execute(text("INSERT INTO price_series(id,item_id,market,item_code,kind_code,rank_code,unit_quantity,unit) VALUES(:id,:id,'RETAIL',:code,'00','01',1,'kg')"),{'id':i+10,'code':f'{i+100}'})
    assert count()==first


def test_snapshot_reads_one_consistent_statement(prices):
    _,engine,_=prices
    from app.repositories.price_repository import snapshot
    from sqlalchemy.orm import Session
    calls=[]
    def listener(*args):
        calls.append(1)
    event.listen(engine,'before_cursor_execute',listener)
    try:
        with Session(engine) as db:
            run,points,guide=snapshot(db,1,DAY)
            assert len(points)==7 and guide.model_run_id==run.id
            assert all(point.model_run_id==run.id for point in points)
        assert len(calls)==1
    finally:
        event.remove(engine,'before_cursor_execute',listener)


@pytest.mark.parametrize('path',['/items/0','/items/9223372036854775808','/items?size=51','/items?category=INVALID'])
def test_input_validation(prices,path):
    assert prices[0].get(ROOT+path).status_code==400


def test_missing_item_and_factors(prices):
    client,_,_=prices
    assert client.get(ROOT+'/items/999').status_code==404
    assert client.get(ROOT+'/items/2/factors').json()['baseDate']=='2026-10-08'


def test_stale_and_baseline_states(prices,monkeypatch):
    client,engine,_=prices
    monkeypatch.setattr(price_service,'today',lambda:DAY+timedelta(days=3))
    assert client.get(ROOT+'/items/2/forecast').json()['status']=='STALE'
    monkeypatch.setattr(price_service,'today',lambda:DAY)
    with engine.begin() as conn:
        conn.execute(text("UPDATE price_model_run SET quality='BASELINE' WHERE id=1"))
    assert client.get(ROOT+'/items/2/forecast').json()['status']=='BASELINE'


def test_wholesale_market_is_separate_series(prices):
    client,_,_=prices
    rows=client.get(ROOT+'/items?market=WHOLESALE').json()['items']
    assert [(r['id'],r['market'],r['seriesId'],r['status']) for r in rows]==[(2,'WHOLESALE',3,'NO_DATA')]
    forecast=client.get(ROOT+'/items/2/forecast?market=WHOLESALE').json()
    assert forecast['seriesId']==3 and forecast['points']==[]
    assert client.get(ROOT+'/items/1?market=WHOLESALE').status_code==404
    assert client.get(ROOT+'/items/2?market=FARM').status_code==400


def add_explanation(engine):
    history=[{'date':(DAY-timedelta(days=d)).isoformat(),'value':0.02+d/1000} for d in range(89,-1,-1)]
    history[-8]['value']=None  # 7일 전 값이 결측이면 비교하지 않는다
    summary={'headline':'현재 1,000원인 대파 소매가격은 7일 후 930원으로 약 7.0% 낮아질 것으로 예측되었습니다.',
             'detail':'이번 예측에서 달력·계절은 하락 방향, 최근 가격 흐름은 상승 방향으로 작용했습니다.',
             'categories':{'CALENDAR':'달력·계절은 가격을 낮추는 방향으로 작용했습니다.','PRICE':'최근 가격 흐름은 높이는 방향입니다.'}}
    with engine.begin() as conn:
        conn.execute(text("UPDATE price_insight SET summary=:s,summary_generator='GEMINI' WHERE model_run_id=1"),{'s':json.dumps(summary,ensure_ascii=False)})
        conn.execute(text("INSERT INTO price_forecast_explanation VALUES(1,7,'XGBOOST_TREE_SHAP',1000,1,1010,930,CURRENT_TIMESTAMP)"))
        rows=[('current',1000,12.5,[{'date':DAY.isoformat(),'value':1000}]),('change7',-.05,-3.25,history),
              ('targetSeasonSin',.3,-60,[]),('targetSeasonCos',.9,-29.25,[]),('lag7',1100,0,[{'date':(DAY-timedelta(days=7)).isoformat(),'value':1100}])]
        for feature,value,contribution,points in rows:
            conn.execute(text("INSERT INTO price_forecast_factor(model_run_id,feature,feature_value,contribution,history) VALUES(1,:f,:v,:c,:h)"),
                         {'f':feature,'v':value,'c':contribution,'h':json.dumps(points)})


def test_factors_explain_published_run(prices):
    client,engine,_=prices
    add_explanation(engine)
    body=client.get(ROOT+'/items/2/factors').json()
    assert body['explained'] is True and body['unavailableReason'] is None
    assert (body['basePrice'],body['predictedPrice'],body['targetDate'])==(1010,930,'2026-10-15')
    assert [f['id'] for f in body['factors']]==['targetSeason','current','change7','lag7']
    season,current,change,lag=body['factors']
    assert season['contribution']==-89.2 and season['hasHistory'] is False and season['value'] is None
    assert change['value']==-5.0 and change['unit']=='%' and change['previousValue'] is None
    assert lag['direction']=='NEUTRAL' and (lag['previousValue'],lag['previousDate'])==(1100,'2026-10-01')
    assert current['label']=='현재 가격' and current['direction']=='UP'
    assert [(c['category'],c['direction'],c['description'] is not None) for c in body['categories']]==[('CALENDAR','DOWN',True),('PRICE','UP',True)]
    assert body['summary']['generator']=='GEMINI'
    detail=client.get(ROOT+'/items/2').json()
    assert detail['summary']['headline'].startswith('현재 1,000원') and detail['item']['aliases']==['흙대파']


def test_factor_history_window(prices):
    client,engine,_=prices
    add_explanation(engine)
    body=client.get(ROOT+'/items/2/factors/change7/history?days=14').json()
    assert body['unit']=='%' and len(body['points'])==14 and body['points'][-1]=={'date':DAY.isoformat(),'value':2.0}
    assert body['points'][-8]['value'] is None
    assert len(client.get(ROOT+'/items/2/factors/change7/history?days=90').json()['points'])==90
    assert client.get(ROOT+'/items/2/factors/targetSeason/history').status_code==404
    assert client.get(ROOT+'/items/2/factors/change7/history?days=20').status_code==400
    assert client.get(ROOT+'/items/2/factors/bad-id!/history').status_code in (400,404)


def test_factors_without_explanation(prices):
    client,engine,_=prices
    body=client.get(ROOT+'/items/2/factors').json()
    assert body['explained'] is False and body['unavailableReason']=='NOT_EXPLAINED' and body['factors']==[]
    with engine.begin() as conn:
        conn.execute(text("UPDATE price_model_run SET quality='BASELINE' WHERE id=1"))
    assert client.get(ROOT+'/items/2/factors').json()['unavailableReason']=='BASELINE_MODEL'
    assert client.get(ROOT+'/items/2/factors?market=WHOLESALE').json()['unavailableReason']=='NO_FORECAST'
    assert client.get(ROOT+'/items/2/factors/change7/history').status_code==404
