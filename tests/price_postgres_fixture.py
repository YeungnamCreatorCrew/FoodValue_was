import os
import uuid

import pytest
from sqlalchemy import create_engine, make_url, text


@pytest.fixture
def local():
    from dotenv import load_dotenv
    load_dotenv()
    url = os.getenv('DATABASE_URL', '')
    parsed = make_url(url)
    if parsed.get_backend_name() != 'postgresql' or parsed.host not in ('localhost', '127.0.0.1', '::1'):
        pytest.fail('The test requires local PostgreSQL')
    from fastapi.testclient import TestClient
    from app.main import app

    engine = create_engine(url, pool_pre_ping=True)
    tag = uuid.uuid4().hex[:12]
    item_id = None
    try:
        with engine.begin() as conn:
            item_id = conn.scalar(text('''INSERT INTO item(name,category,default_unit,default_storage,food_type,grams_per_unit)
                VALUES(:name,'ETC','kg','FRIDGE','RAW',1000) RETURNING id'''), {'name':f'pg-test-{tag}'})
        with TestClient(app) as client:
            yield client, engine, item_id
    finally:
        if item_id is not None:
            with engine.begin() as conn:
                conn.execute(text('DELETE FROM item WHERE id=:id'), {'id':item_id})
        engine.dispose()
