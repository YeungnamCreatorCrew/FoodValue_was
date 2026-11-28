from decimal import Decimal
from types import SimpleNamespace

import pytest

from tools.catalog_expansion import NAMES, SPEC, engine_for, registration_sql, unit_parts


def test_catalog_is_twenty_distinct_items_and_fifteen_market_pairs():
    assert len(set(SPEC['existing']) | set(NAMES)) == 20
    assert len(NAMES) == len(set(NAMES)) == 15
    assert len({item['code'] for item in SPEC['items']}) == 15
    for item in SPEC['items']:
        for market in ('retail', 'wholesale'):
            quantity, unit = unit_parts(item[market])
            assert quantity > 0 and unit in ('g', 'kg', '개', '포기')


def test_retail_wholesale_quantities_are_not_assumed_identical():
    by_name = {item['name']: item for item in SPEC['items']}
    assert unit_parts(by_name['오이']['retail']) == (Decimal(10), '개')
    assert unit_parts(by_name['오이']['wholesale']) == (Decimal(50), '개')
    assert unit_parts(by_name['깻잎']['retail']) == (Decimal(50), 'g')
    assert unit_parts(by_name['깻잎']['wholesale']) == (Decimal(2), 'kg')


def test_shared_database_requires_explicit_opt_in(monkeypatch):
    monkeypatch.setenv('CATALOG_TEST_URL', 'postgresql+psycopg://example:placeholder@shared.example/postgres')
    with pytest.raises(ValueError, match='SHARED_DATABASE_REQUIRES_ALLOW_SHARED'):
        engine_for(SimpleNamespace(database_env='CATALOG_TEST_URL', allow_shared=False))


def test_default_target_uses_local_db_even_when_database_url_is_shared(monkeypatch):
    monkeypatch.setenv('DATABASE_URL', 'postgresql+psycopg://example:placeholder@shared.example/postgres')
    monkeypatch.setenv('DB_USER', 'local_test')
    monkeypatch.setenv('DB_PASSWORD', 'test')
    monkeypatch.setenv('DB_NAME', 'local_catalog')
    engine = engine_for(SimpleNamespace(database_env=None, allow_shared=False))
    try:
        assert engine.url.host == '127.0.0.1'
        assert engine.url.database == 'local_catalog'
    finally:
        engine.dispose()


def test_registration_is_repeatable_and_rejects_mapping_conflicts():
    sql = registration_sql()
    assert sql.count('INSERT INTO price_series') == 30
    assert 'ON CONFLICT (name) DO NOTHING' in sql
    assert sql.count('CATALOG_CONFLICT') == 30
    assert 'ON CONFLICT (item_id,market) DO NOTHING' in sql
    assert 'UPDATE ' not in sql
    assert 'DELETE ' not in sql
