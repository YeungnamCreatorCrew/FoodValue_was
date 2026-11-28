"""Round-trip a handoff in a disposable LOCAL schema with different item IDs.

Only uses 127.0.0.1 DB_*; never uses DATABASE_URL or SUPABASE_DATABASE_URL.
"""
import contextlib
import io
import json
import re
import uuid
from pathlib import Path
from types import SimpleNamespace

from dotenv import load_dotenv
from sqlalchemy import text

from app.core.db import make_engine
from tools.catalog_expansion import ROOT, engine_for, import_bundle, report_for


def main():
    load_dotenv(ROOT / '.env')
    local = engine_for(SimpleNamespace(database_env=None, allow_shared=False))
    schema = 'catalog_transfer_' + uuid.uuid4().hex[:12]
    target = make_engine(local.url.update_query_dict({'options': f'-csearch_path={schema}'}))
    folder = ROOT / 'handoff/siknal-20-20261128'
    try:
        with local.begin() as connection:
            connection.exec_driver_sql(f'CREATE SCHEMA "{schema}"')
        def version(path):
            return tuple(map(int, re.match(r'V(\d+)(?:_(\d+))?__', path.name).groups(default='0')))
        migrations = sorted((ROOT / 'db/migration').glob('V*.sql'), key=version)
        with target.begin() as connection:
            cursor = connection.connection.driver_connection.cursor()
            for migration in migrations:
                cursor.execute(migration.read_text(encoding='utf-8-sig'))
        with contextlib.redirect_stdout(io.StringIO()):
            import_bundle(target, folder, build_indicators=False)
        before = counts(target)
        with contextlib.redirect_stdout(io.StringIO()):
            import_bundle(target, folder, build_indicators=False)
        after = counts(target)
        assert before == after, (before, after)
        expected = json.loads((folder / 'verification.json').read_text(encoding='utf-8'))
        actual = report_for(target)
        assert actual['listed_items'] == 15
        assert len(actual['series']) == 30
        normalize = lambda report: {(r['name'], r['market']): (r['observations'], str(r['first_date']), str(r['last_date'])) for r in report['series']}
        assert normalize(actual) == normalize(expected), 'Portable import must preserve per-series dates and counts'
        with target.connect() as connection:
            assert connection.scalar(text('SELECT max(id) FROM item')) == 15
        from app.services import indicator_batch_service
        result = indicator_batch_service.run(target, 1)
        assert result['status'] == 'SUCCESS'
        print(json.dumps({'status': 'PASS', 'different_item_ids': True, 'repeat_import_counts': after,
                          'all_30_series_match': True, 'indicator_generation': result['status']}))
    finally:
        target.dispose()
        # Only the random schema created above is removed; public and all data stay intact.
        with local.begin() as connection:
            connection.exec_driver_sql(f'DROP SCHEMA IF EXISTS "{schema}" CASCADE')
        local.dispose()


def counts(engine):
    with engine.connect() as connection:
        return {table: connection.scalar(text(f'SELECT count(*) FROM {table}'))
                for table in ('item', 'item_alias', 'price_series', 'external_observation', 'price_daily')}


if __name__ == '__main__':
    main()
