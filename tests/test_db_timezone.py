import os

import pytest
from sqlalchemy import create_engine, text

from app.core.constants import DB_TIMEZONE
from app.core.db import make_engine

pytestmark = pytest.mark.skipif(os.getenv('FOODVALUE_TEST_POSTGRES') != '1', reason='로컬 PostgreSQL 명시 실행 필요')


@pytest.fixture
def utc_client(monkeypatch):
    """공유 DB pooler처럼 접속 때 UTC로 시작하는 세션을 만든다(libpq PGTZ = 접속 시 TimeZone 파라미터)."""
    from dotenv import load_dotenv
    load_dotenv()
    monkeypatch.setenv('PGTZ', 'UTC')
    return os.environ['DATABASE_URL']


def test_plain_engine_follows_startup_timezone(utc_client):
    engine = create_engine(utc_client)
    with engine.connect() as conn:
        assert conn.scalar(text('SHOW TIME ZONE')) == 'UTC'
    engine.dispose()


def test_make_engine_sets_seoul_even_after_rollback(utc_client):
    engine = make_engine(utc_client, pool_size=1, max_overflow=0)
    with engine.connect() as conn:
        assert conn.scalar(text('SHOW TIME ZONE')) == DB_TIMEZONE
        conn.rollback()
        assert conn.scalar(text('SHOW TIME ZONE')) == DB_TIMEZONE
    with engine.connect() as conn:  # 풀에서 다시 꺼낸 연결도 유지
        assert conn.scalar(text('SHOW TIME ZONE')) == DB_TIMEZONE
    engine.dispose()


def test_make_engine_on_sqlite_is_plain():
    engine = make_engine('sqlite://')
    with engine.connect() as conn:
        assert conn.scalar(text('select 1')) == 1
