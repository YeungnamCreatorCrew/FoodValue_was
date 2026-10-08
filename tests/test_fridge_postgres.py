"""FOODVALUE_TEST_POSTGRES=1일 때만 로컬 PostgreSQL에서 실행. 생성한 데이터만 정리한다."""
import os
import secrets
import uuid
from concurrent.futures import ThreadPoolExecutor
from threading import Barrier
from pathlib import Path
from types import SimpleNamespace

import pytest
from sqlalchemy import make_url, select, text
from sqlalchemy.orm import Session

from app.models.fridge import FridgeIngredient, FridgeReceipt, IngredientUsage, Item
from app.schemas.fridge import Consume, IngredientCreate, ReceiptConfirm
from app.services import fridge_service as service, receipt_service

pytestmark = pytest.mark.skipif(os.getenv('FOODVALUE_TEST_POSTGRES') != '1', reason='로컬 PostgreSQL 명시 실행 필요')


@pytest.fixture
def local(monkeypatch):
    from dotenv import load_dotenv
    load_dotenv()
    url = os.getenv('DATABASE_URL', '')
    parsed = make_url(url)
    if parsed.get_backend_name() != 'postgresql' or parsed.host not in ('localhost', '127.0.0.1', '::1'):
        pytest.fail('이 테스트는 로컬 PostgreSQL만 허용합니다')
    if not os.getenv('JWT_SECRET_KEY'):
        monkeypatch.setenv('JWT_SECRET_KEY', secrets.token_urlsafe(48))
    # 이미지 업로드를 호출하지 않는다. 누락된 S3 설정만 테스트 프로세스 안에서 보완한다.
    for key, value in {'S3_ENDPOINT_URL':'http://localhost:9000', 'S3_REGION':'us-east-1',
                       'S3_BUCKET':'test', 'S3_ACCESS_KEY':'test', 'S3_SECRET_KEY':'test-secret',
                       'S3_PUBLIC_BASE_URL':'http://localhost:9000/test'}.items():
        if not os.getenv(key):
            monkeypatch.setenv(key, value)
    from app.core.config import get_settings
    get_settings.cache_clear()
    from sqlalchemy import create_engine
    from fastapi.testclient import TestClient
    from app.main import app
    engine = create_engine(url, pool_pre_ping=True)
    tag = uuid.uuid4().hex[:12]
    item_id = None
    users = []
    try:
        with engine.begin() as conn:
            count = conn.scalar(text("SELECT count(*) FROM information_schema.tables WHERE table_schema='public' AND table_type='BASE TABLE' AND table_name <> 'flyway_schema_history'"))
            assert count == 22
            assert conn.scalar(text("SELECT count(*) FROM information_schema.columns WHERE table_schema='public' AND table_name='fridge_ingredient' AND column_name='expires_at'")) == 0
            item_id = conn.scalar(text('''INSERT INTO item(name,category,default_unit,default_storage,food_type,grams_per_unit)
                VALUES(:name,'ETC','모','FRIDGE','PROCESSED',300) RETURNING id'''), {'name':f'pg-test-{tag}'})
            conn.execute(text('''INSERT INTO item_nutrition(item_id,edible_ratio,protein_g,carbohydrate_g,fat_g,sodium_mg,sugars_g,cholesterol_mg,source)
                VALUES(:id,100,10,2,5,10,0,0,'MFDS')'''), {'id':item_id})
        with TestClient(app) as client:
            headers = []
            for i in range(2):
                body = {'email':f'pg-fridge-{tag}-{i}@example.com','nickname':f'pg{tag}{i}','password':'password123'}
                result = client.post('/api/v1/auth/signup', json=body)
                assert result.status_code == 201, result.text
                token = client.post('/api/v1/auth/login', json=body).json()['accessToken']
                header = {'Authorization':f'Bearer {token}'}
                users.append(client.get('/api/v1/users/me',headers=header).json()['id'])
                headers.append(header)
            yield client, engine, item_id, users, headers
    finally:
        with engine.begin() as conn:
            for user_id in users:
                conn.execute(text('DELETE FROM fridge_receipt WHERE user_id=:id'), {'id':user_id})
                conn.execute(text('DELETE FROM fridge_ingredient WHERE user_id=:id'), {'id':user_id})
                conn.execute(text('DELETE FROM users WHERE id=:id'), {'id':user_id})
            # 가입 후 테스트 예외가 나도 정확한 UUID 이메일만 정리한다.
            conn.execute(text('DELETE FROM users WHERE email IN (:a,:b)'),
                         {'a':f'pg-fridge-{tag}-0@example.com','b':f'pg-fridge-{tag}-1@example.com'})
            if item_id:
                conn.execute(text('DELETE FROM item WHERE id=:id'), {'id':item_id})
        engine.dispose()
        get_settings.cache_clear()


ROOT = '/api/v1/fridge'


def body(item_id):
    return {'itemId':item_id,'displayName':'테스트 두부','quantity':'1','unit':'모',
            'storage':'FRIDGE','purchasedAt':str(service.today())}


def test_real_api_inventory_nutrition_and_owner(local):
    client, engine, item_id, users, headers = local
    result = client.post(ROOT + '/items',json=body(item_id),headers=headers[0])
    assert result.status_code == 201, result.text
    ingredient_id = result.json()['id']
    path = f'{ROOT}/items/{ingredient_id}'
    assert client.get(path, headers=headers[1]).status_code == 404
    assert client.get(path).status_code == 401
    nutrient = client.get(ROOT + '/nutrition',headers=headers[0]).json()
    assert next(x for x in nutrient['nutrients'] if x['name']=='protein')['amount'] == 30
    result = client.post(path + '/consume',json={'reason':'USE','amount':'.5','usedAt':str(service.today())},headers=headers[0])
    assert result.status_code == 200, result.text
    assert result.json()['quantity'] == '0.500'
    assert client.get(path + '/usage',headers=headers[0]).json()['items'][0]['gramsUsed'] == '150.000'
    assert client.delete(path,headers=headers[0]).status_code == 204
    assert client.get(ROOT + '/items',headers=headers[0]).json()['total'] == 0
    with engine.connect() as conn:
        assert conn.scalar(text('SELECT count(*) FROM ingredient_usage WHERE fridge_ingredient_id=:id'),{'id':ingredient_id}) == 1


def test_concurrent_consumption_never_overdraws(local):
    client, engine, item_id, users, headers = local
    ingredient_id = client.post(ROOT + '/items',json=body(item_id),headers=headers[0]).json()['id']
    barrier = Barrier(2)
    def worker():
        with Session(engine,expire_on_commit=False) as db:
            barrier.wait(timeout=10)
            try:
                service.consume(db,SimpleNamespace(id=users[0]),ingredient_id,
                                Consume(reason='USE',amount='0.75',used_at=service.today()))
                return 'OK'
            except service.InvalidOperationError:
                return 'REJECTED'
    with ThreadPoolExecutor(max_workers=2) as pool:
        futures = [pool.submit(worker) for _ in range(2)]
        results = [f.result(timeout=20) for f in futures]
    assert sorted(results) == ['OK','REJECTED']
    with Session(engine) as db:
        assert str(db.get(FridgeIngredient,ingredient_id).quantity) == '0.250'
        assert len(db.scalars(select(IngredientUsage).where(IngredientUsage.fridge_ingredient_id==ingredient_id)).all()) == 1


def test_concurrent_receipt_confirmation_is_single_use(local):
    client, engine, item_id, users, headers = local
    with Session(engine) as db:
        receipt = FridgeReceipt(user_id=users[0],purchased_at=service.today(),candidates=[])
        db.add(receipt)
        db.commit()
        receipt_id = receipt.id
    barrier = Barrier(2)
    def worker():
        with Session(engine,expire_on_commit=False) as db:
            barrier.wait(timeout=10)
            try:
                receipt_service.confirm(db,SimpleNamespace(id=users[0]),receipt_id,
                                        ReceiptConfirm(items=[IngredientCreate.model_validate(body(item_id))]))
                return 'OK'
            except receipt_service.OcrError as error:
                assert error.status == 409
                return 'CONFLICT'
    with ThreadPoolExecutor(max_workers=2) as pool:
        results = [pool.submit(worker) for _ in range(2)]
        assert sorted(f.result(timeout=20) for f in results) == ['CONFLICT','OK']
    assert client.get(ROOT + '/items',headers=headers[0]).json()['total'] == 1


def test_all_migrations_on_empty_schema(local):
    _, engine, _, _, _ = local
    schema = 'fridge_migration_test_' + uuid.uuid4().hex
    folder = Path(__file__).resolve().parents[1] / 'db' / 'migration'
    def version(path):
        return tuple(int(part) for part in path.name.split('__')[0][1:].split('_'))
    with engine.connect() as conn:
        transaction = conn.begin()
        try:
            conn.exec_driver_sql(f'CREATE SCHEMA "{schema}"')
            conn.exec_driver_sql(f'SET LOCAL search_path TO "{schema}"')
            for path in sorted(folder.glob('V*__*.sql'), key=version):
                # 매개변수 없는 simple query로 여러 SQL 문을 한 파일 그대로 실행한다.
                with conn.connection.driver_connection.cursor() as cursor:
                    cursor.execute(path.read_text(encoding='utf-8'), prepare=False)
            assert conn.scalar(text("SELECT count(*) FROM information_schema.tables WHERE table_schema=:s AND table_type='BASE TABLE'"), {'s':schema}) == 22
            assert conn.scalar(text("SELECT count(*) FROM information_schema.columns WHERE table_schema=:s AND table_name='fridge_ingredient' AND column_name='expires_at'"), {'s':schema}) == 0
        finally:
            # 테이블·데이터·스키마 생성 모두 롤백한다. 기존 public 스키마에 영향 없음.
            transaction.rollback()
