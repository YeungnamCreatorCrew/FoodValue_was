"""격리된 임시 DB에서 냉장고 API를 검증한다. 실제 .env DB는 사용하지 않는다."""
from datetime import date, timedelta
from decimal import Decimal
from types import SimpleNamespace

import pytest
from sqlalchemy import create_engine, text
from sqlalchemy.orm import Session
from sqlalchemy.pool import StaticPool

from app.services import fridge_service, receipt_service


@pytest.fixture
def api(monkeypatch):
    # 테스트 설정은 fixture 종료 시 복구한다. 기존 .env의 비밀값은 출력하지 않는다.
    for key, value in {
        'DATABASE_URL': 'sqlite://', 'JWT_SECRET_KEY': 't' * 48,
        'S3_ENDPOINT_URL': 'http://localhost:9000', 'S3_REGION': 'us-east-1',
        'S3_BUCKET': 'test', 'S3_ACCESS_KEY': 'test', 'S3_SECRET_KEY': 'test-secret',
        'S3_PUBLIC_BASE_URL': 'http://localhost:9000/test',
    }.items():
        monkeypatch.setenv(key, value)
    from app.core.config import get_settings
    get_settings.cache_clear()
    from fastapi import FastAPI
    from fastapi.testclient import TestClient
    from app.core.db import get_db
    from app.core.deps import get_current_user
    from app.routers.fridge import router
    from app.main import validation_error_handler
    from fastapi.exceptions import RequestValidationError
    from app.core.limits import ImageUploadSizeLimit

    engine = create_engine('sqlite://', poolclass=StaticPool, connect_args={'check_same_thread': False})
    # SQLite용 테스트 DDL: PostgreSQL의 identity/JSONB 대신 INTEGER/JSON 사용.
    statements = [
        'CREATE TABLE users(id INTEGER PRIMARY KEY)',
        '''CREATE TABLE item(id INTEGER PRIMARY KEY, name TEXT, category TEXT, default_unit TEXT,
        default_storage TEXT, food_type TEXT DEFAULT 'RAW', grams_per_unit NUMERIC,
        density_g_per_ml NUMERIC, price_source TEXT, price_code TEXT, price_unit_label TEXT, is_price_listed INTEGER DEFAULT 1,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)''',
        '''CREATE TABLE item_alias(id INTEGER PRIMARY KEY, item_id INTEGER, alias TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)''',
        '''CREATE TABLE fridge_ingredient(id INTEGER PRIMARY KEY, user_id INTEGER, item_id INTEGER,
        display_name TEXT, quantity NUMERIC CHECK(quantity >= 0), initial_quantity NUMERIC,
        unit TEXT, storage TEXT, food_type TEXT DEFAULT 'RAW', purchased_at DATE,
        grams_per_unit NUMERIC, purchase_price INTEGER, deleted_at TIMESTAMP,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        CHECK(quantity <= initial_quantity))''',
        '''CREATE TABLE ingredient_usage(id INTEGER PRIMARY KEY, fridge_ingredient_id INTEGER,
        used_amount NUMERIC, grams_used NUMERIC, reason TEXT, memo TEXT, used_at DATE,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)''',
        '''CREATE TABLE item_nutrition(id INTEGER PRIMARY KEY, item_id INTEGER, edible_ratio NUMERIC,
        carbohydrate_g NUMERIC, protein_g NUMERIC, fat_g NUMERIC, sodium_mg NUMERIC,
        sugars_g NUMERIC, cholesterol_mg NUMERIC, source TEXT, basis TEXT DEFAULT '100G')''',
        '''CREATE TABLE fridge_receipt(id INTEGER PRIMARY KEY, user_id INTEGER, purchased_at DATE,
        candidates JSON, confirmed_at TIMESTAMP, created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)''',
        "INSERT INTO users VALUES (1), (2)",
        "INSERT INTO item(id,name,category,default_unit,default_storage,food_type,grams_per_unit,price_source) VALUES (1,'두부','ETC','모','FRIDGE','PROCESSED',300,'CHAMGA')",
        "INSERT INTO item_alias(item_id,alias) VALUES(1,'찌개두부')",
        "INSERT INTO item_nutrition(item_id,edible_ratio,carbohydrate_g,protein_g,fat_g,sodium_mg,sugars_g,cholesterol_mg,source) VALUES(1,100,2,10,5,10,0,0,'MFDS')",
    ]
    with engine.begin() as conn:
        for statement in statements:
            conn.execute(text(statement))
    application = FastAPI()
    application.add_middleware(ImageUploadSizeLimit)
    application.add_exception_handler(RequestValidationError, validation_error_handler)
    application.include_router(router, prefix='/api/v1')

    def db():
        with Session(engine, expire_on_commit=False) as session:
            yield session

    actor = SimpleNamespace(id=1)
    application.dependency_overrides[get_db] = db
    application.dependency_overrides[get_current_user] = lambda: actor
    with TestClient(application) as client:
        yield client, engine, actor, application
    engine.dispose()
    get_settings.cache_clear()


ROOT = '/api/v1/fridge'


def register(client, **overrides):
    body = {'itemId': 1, 'displayName': '두부', 'quantity': '1', 'unit': '모',
            'storage': 'FRIDGE', 'purchasedAt': str(fridge_service.today()), **overrides}
    return client.post(ROOT + '/items', json=body)


def test_crud_consumption_and_preserved_history(api):
    client, engine, actor, _ = api
    created = register(client)
    assert created.status_code == 201
    row = created.json()
    assert row['gramsPerUnit'] == '300.000' and row['foodType'] == 'PROCESSED'
    assert row['priceAvailable'] is True and 'expiresAt' not in row
    path = f"{ROOT}/items/{row['id']}"
    body = {'reason': 'USE', 'amount': '0.25', 'usedAt': str(fridge_service.today())}
    assert client.post(path + '/consume', json=body).json()['quantity'] == '0.750'
    assert client.post(path + '/consume', json={**body, 'amount': '1'}).status_code == 400
    history = client.get(path + '/usage').json()
    assert history['total'] == 1 and history['items'][0]['gramsUsed'] == '75.000'
    actor.id = 2
    assert client.get(path).status_code == 404
    assert client.patch(path, json={'displayName': '도용'}).status_code == 404
    assert client.post(path + '/consume', json=body).status_code == 404
    assert client.get(ROOT + '/items').json()['total'] == 0
    actor.id = 1
    assert client.patch(path, json={'purchasePrice': 2000}).status_code == 200
    assert client.delete(path).status_code == 204
    assert client.get(path).status_code == 404
    with engine.connect() as conn:
        assert conn.scalar(text('SELECT count(*) FROM ingredient_usage')) == 1
        assert conn.scalar(text('SELECT count(*) FROM fridge_ingredient WHERE deleted_at IS NOT NULL')) == 1


def test_finish_discard_and_summary(api):
    client, _, _, _ = api
    row = register(client).json()
    path = f"{ROOT}/items/{row['id']}"
    assert client.get(ROOT + '/summary').json()['total'] == 1
    assert client.post(path + '/consume', json={'reason':'FINISH','usedAt':str(fridge_service.today())}).json()['quantity'] == '0.000'
    assert client.get(ROOT + '/items').json()['total'] == 0
    assert client.get(ROOT + '/items?include_empty=true').json()['total'] == 1
    assert client.get(ROOT + '/summary').json()['total'] == 0
    assert client.post(path + '/consume', json={'reason':'DISCARD','usedAt':str(fridge_service.today())}).status_code == 400


@pytest.mark.parametrize('overrides', [
    {'quantity':0}, {'quantity':'0.0001'}, {'quantity':'NaN'}, {'unit':'상자'},
    {'displayName':'   '}, {'itemId':999}, {'unit':'g','gramsPerUnit':2},
    {'purchasedAt':str(fridge_service.today() + timedelta(days=1))},
])
def test_invalid_input(api, overrides):
    assert register(api[0], **overrides).status_code == 400


def test_catalog_alias_filters_and_literal_search(api):
    client, _, _, _ = api
    assert client.get(ROOT + '/catalog?keyword=찌개두부').json()['total'] == 1
    register(client, displayName='두부_팩')
    register(client, displayName='두부1팩', storage='FREEZER')
    assert client.get(ROOT + '/items', params={'keyword':'두부_팩'}).json()['total'] == 1
    assert client.get(ROOT + '/items', params={'keyword':'%'}).json()['total'] == 0
    assert client.get(ROOT + '/items?storage=FREEZER').json()['total'] == 1
    assert client.get(ROOT + '/items?food_type=PROCESSED&size=1').json()['total'] == 2
    assert len(client.get(ROOT + '/items?size=1&page=2').json()['items']) == 1


def test_nutrition_uses_remaining_inventory(api):
    client, _, _, _ = api
    row = register(client).json()
    def protein():
        return next(n for n in client.get(ROOT + '/nutrition').json()['nutrients'] if n['name']=='protein')
    assert protein()['amount'] == 30 and protein()['shortfall'] == 25
    client.post(f"{ROOT}/items/{row['id']}/consume", json={'reason':'DISCARD','amount':'0.5','usedAt':str(fridge_service.today())})
    assert protein()['amount'] == 15
    register(client, itemId=None, unit='팩', gramsPerUnit=None)
    assert protein()['status'] == 'INCOMPLETE' and protein()['shortfall'] is None


def test_volume_nutrition_does_not_assume_density(api):
    client, engine, _, _ = api
    with engine.begin() as conn:
        conn.execute(text("UPDATE item_nutrition SET basis='100ML' WHERE item_id=1"))
    row = register(client, unit='L', quantity='0.5').json()
    assert row['gramsPerUnit'] is None
    nutrients = client.get(ROOT + '/nutrition').json()['nutrients']
    assert next(n for n in nutrients if n['name']=='protein')['amount'] == 50


def payload():
    return {'images':[{'inferResult':'SUCCESS','receipt':{'result':{
        'paymentInfo':{'date':{'formatted':{'value':'2026-10-01'}}},
        'subResults':[{'items':[{'name':{'text':'찌개두부','confidenceScore':0.9},
        'count':{'text':'1'},'price':{'price':{'text':'2,000'}}}]}]}}}]}


def test_ocr_confirm_atomic_and_single_use(api, monkeypatch):
    client, engine, actor, _ = api
    monkeypatch.setattr(receipt_service, 'recognize', lambda data: payload())
    result = client.post(ROOT + '/receipts', files={'file':('receipt.png',b'image','image/png')})
    assert result.status_code == 201
    receipt = result.json()
    assert receipt['purchasedAt'] == '2026-10-01'
    assert receipt['candidates'][0]['itemId'] == 1
    path = f"{ROOT}/receipts/{receipt['id']}"
    body = {'items':[{'itemId':1,'displayName':'두부','quantity':'1','unit':'모',
                     'storage':'FRIDGE','purchasedAt':'2026-10-02'}]}
    actor.id = 2
    assert client.get(path).status_code == 404
    assert client.post(path + '/confirm', json=body).status_code == 404
    actor.id = 1
    invalid = {'items':[body['items'][0],{**body['items'][0],'itemId':999}]}
    assert client.post(path + '/confirm', json=invalid).status_code == 400
    assert client.get(ROOT + '/items').json()['total'] == 0
    assert client.get(path).json()['confirmedAt'] is None
    assert client.post(path + '/confirm', json=body).status_code == 201
    assert client.post(path + '/confirm', json=body).status_code == 409
    assert client.get(ROOT + '/items').json()['total'] == 1


def test_ocr_missing_configuration_and_body_limit(api, monkeypatch):
    client, _, _, _ = api
    monkeypatch.delenv('CLOVA_OCR_RECEIPT_URL', raising=False)
    monkeypatch.delenv('CLOVA_OCR_SECRET', raising=False)
    assert client.post(ROOT + '/receipts', files={'file':('a.png', b'\x89PNG\r\n\x1a\n')}).status_code == 503
    assert client.post(ROOT + '/receipts', content=b'x', headers={'Content-Length':str(6*1024*1024)}).status_code == 413


def test_patch_and_date_validation(api):
    client, _, _, _ = api
    row = register(client, unit='g', purchasedAt='2026-10-01').json()
    path = f"{ROOT}/items/{row['id']}"
    assert client.patch(path, json={}).status_code == 400
    assert client.patch(path, json={'storage':None}).status_code == 400
    assert client.patch(path, json={'gramsPerUnit':2}).status_code == 400
    assert client.post(path + '/consume', json={'reason':'USE','amount':'.1','usedAt':'2026-09-30'}).status_code == 400
    assert client.post(path + '/consume', json={'reason':'USE','amount':'.1','usedAt':'2026-10-02'}).status_code == 200
    assert client.patch(path, json={'purchasedAt':'2026-10-03'}).status_code == 400


def test_requires_authentication(api):
    from app.core.deps import get_current_user
    from fastapi import HTTPException
    client, _, _, application = api
    def unauthenticated():
        raise HTTPException(401, '인증이 필요합니다')
    application.dependency_overrides[get_current_user] = unauthenticated
    for path in ('/items', '/nutrition', '/summary', '/catalog', '/receipts/1'):
        assert client.get(ROOT + path).status_code == 401


def test_conversion_and_ocr_failure():
    assert fridge_service.conversion('kg', None, None) == 1000
    assert fridge_service.conversion('팩', None, SimpleNamespace(default_unit='모', grams_per_unit=300)) is None
    assert fridge_service.conversion('L', None, SimpleNamespace(density_g_per_ml=Decimal('1.03'))) == 1030
    with pytest.raises(receipt_service.OcrError):
        receipt_service.parse({'images':[{'inferResult':'FAILURE'}]})


def test_official_ocr_date_format():
    raw = payload()
    raw['images'][0]['receipt']['result']['paymentInfo']['date'] = {
        'text':'2026-10-01 (목)', 'formatted':{'year':'2026','month':'10','day':'01'}}
    candidates, day = receipt_service.parse(raw)
    assert day == date(2026, 10, 1)
    assert candidates[0]['purchasePrice'] == 2000


def test_nutrition_missing_weight_and_partial_nutrients(api):
    client, engine, _, _ = api
    row = register(client, unit='팩').json()
    result = client.get(ROOT + '/nutrition').json()
    assert result['excludedIngredients'][0]['reason'] == 'WEIGHT_UNKNOWN'
    client.patch(f"{ROOT}/items/{row['id']}", json={'gramsPerUnit':300})
    with engine.begin() as conn:
        conn.execute(text('UPDATE item_nutrition SET protein_g=NULL, sugars_g=0 WHERE item_id=1'))
    nutrients = {x['name']:x for x in client.get(ROOT + '/nutrition').json()['nutrients']}
    assert nutrients['protein']['complete'] is False
    assert nutrients['sugars']['complete'] is True and nutrients['sugars']['amount'] == 0


def test_ocr_user_date_override_and_bad_data(api, monkeypatch):
    client, _, _, _ = api
    monkeypatch.setattr(receipt_service, 'recognize', lambda data: payload())
    r = client.post(ROOT + '/receipts', data={'purchased_at':'2026-09-30'},
                    files={'file':('receipt.png', b'image')})
    assert r.json()['purchasedAt'] == '2026-09-30'
    monkeypatch.setattr(receipt_service, 'recognize', lambda data: {'images':[]})
    assert client.post(ROOT + '/receipts', files={'file':('a.png',b'image')}).status_code == 502
