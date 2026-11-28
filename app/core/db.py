from collections.abc import Iterator
from functools import lru_cache

from sqlalchemy import Engine, create_engine, event
from sqlalchemy.orm import DeclarativeBase, Session, sessionmaker

from app.core.config import get_settings
from app.core.constants import DB_POOL_SIZE, DB_POOL_TIMEOUT_SECONDS, DB_TIMEZONE


class Base(DeclarativeBase):
    pass


def make_engine(url, **kwargs) -> Engine:
    """DB 엔진. 서버·배치는 모두 이 함수로 만든다.

    PostgreSQL 접속마다 세션 타임존을 Asia/Seoul로 맞춘다. 공유 DB(Supabase)의 Session pooler는 DB·계정 기본값
    (ALTER DATABASE/ROLE ... SET timezone)과 접속 옵션(-c timezone)을 무시하고 UTC로 접속시키기 때문이다.
    이게 없으면 DB 기본값으로 채우는 created_at 등이 9시간 이르게 저장된다.
    """
    kwargs.setdefault('pool_pre_ping', True)
    kwargs.setdefault('hide_parameters', True)
    engine = create_engine(url, **kwargs)
    if engine.dialect.name == 'postgresql':
        @event.listens_for(engine, 'connect')
        def _set_timezone(dbapi_connection, _record):
            with dbapi_connection.cursor() as cursor:
                cursor.execute(f"SET TIME ZONE '{DB_TIMEZONE}'")
            dbapi_connection.commit()  # 트랜잭션 안의 SET은 롤백되면 사라지므로 바로 확정한다
    return engine


@lru_cache
def get_engine() -> Engine:
    """API 서버 엔진. 연결 수를 DB_POOL_SIZE로 고정한다(공유 DB 동시 접속 한도, constants 참고)."""
    return make_engine(get_settings().database_url, pool_size=DB_POOL_SIZE, max_overflow=0,
                       pool_timeout=DB_POOL_TIMEOUT_SECONDS)


@lru_cache
def _session_factory() -> sessionmaker[Session]:
    return sessionmaker(bind=get_engine(), expire_on_commit=False)


def get_db() -> Iterator[Session]:
    with _session_factory()() as session:
        yield session
