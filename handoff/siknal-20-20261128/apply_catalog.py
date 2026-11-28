"""20품목 확장: 로컬 등록·KAMIS 적재·지표 생성·이름 기반 공유 DB 이관.

기본 접속은 .env DB_*로 만든 127.0.0.1이다. DATABASE_URL을 기본으로 읽지 않는다.
공유 DB 쓰기는 --database-env SUPABASE_DATABASE_URL --allow-shared를 명시해야 한다.
"""
import argparse
import gzip
import json
import os
import re
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import date, timedelta
from decimal import Decimal
from pathlib import Path

from dotenv import load_dotenv
from sqlalchemy import URL, select, text
from sqlalchemy.engine import make_url
from sqlalchemy.orm import Session

import sys
sys.path.insert(0, str(Path.cwd()))

from app.collectors import kamis
from app.collectors.http import fetch_json
from app.collectors.records import Batch, Record
from app.core.db import make_engine
from app.models.item import Item
from app.models.price import PriceSeries
from app.services import collection_service, warehouse_service

ROOT = Path.cwd()
SPEC_PATH = Path(__file__).resolve().with_name('catalog.json')
SPEC = json.loads(SPEC_PATH.read_text(encoding='utf-8'))
NAMES = [item['name'] for item in SPEC['items']]


def quote(value):
    return "'" + str(value).replace("'", "''") + "'"


def unit_parts(label):
    match = re.fullmatch(r'(\d+(?:\.\d+)?)(.+)', label)
    if not match:
        raise ValueError('INVALID_UNIT')
    return Decimal(match[1]), match[2]


def registration_sql():
    statements = ['-- 15개 신규 품목. ID를 고정하지 않고 이름·시장으로 연결하며 기존 계열은 덮어쓰지 않는다.']
    for item in SPEC['items']:
        name = quote(item['name'])
        statements.append(f"INSERT INTO item (name,category,default_unit,default_storage,price_source,price_unit_label,is_price_listed) VALUES ({name},{quote(item['category'])},'g','FRIDGE','KAMIS',{quote(item['retail'])},TRUE) ON CONFLICT (name) DO NOTHING;")
        code, kind, rank = item['code'].split('-')
        for market, key in (('RETAIL', 'retail'), ('WHOLESALE', 'wholesale')):
            quantity, unit = unit_parts(item[key])
            statements.append(f"INSERT INTO price_series (item_id,source,market,item_code,kind_code,rank_code,unit_quantity,unit) SELECT id,'KAMIS',{quote(market)},{quote(code)},{quote(kind)},{quote(rank)},{quantity},{quote(unit)} FROM item WHERE name={name} ON CONFLICT (item_id,market) DO NOTHING;")
            statements.append(f"DO $$ BEGIN IF NOT EXISTS (SELECT 1 FROM item i JOIN price_series s ON s.item_id=i.id WHERE i.name={name} AND i.is_price_listed AND i.category={quote(item['category'])} AND i.price_source='KAMIS' AND s.market={quote(market)} AND s.source='KAMIS' AND s.item_code={quote(code)} AND s.kind_code={quote(kind)} AND s.rank_code={quote(rank)} AND s.unit_quantity={quantity} AND s.unit={quote(unit)}) THEN RAISE EXCEPTION USING MESSAGE = 'CATALOG_CONFLICT: ' || {name}; END IF; END $$;")
        for alias in item['aliases']:
            statements.append(f"INSERT INTO item_alias (item_id,alias) SELECT id,{quote(alias)} FROM item WHERE name={name} ON CONFLICT (alias) DO NOTHING;")
            statements.append(f"DO $$ BEGIN IF EXISTS (SELECT 1 FROM item_alias a JOIN item i ON i.id=a.item_id WHERE a.alias={quote(alias)} AND i.name<>{name}) THEN RAISE EXCEPTION 'ALIAS_CONFLICT'; END IF; END $$;")
    return '\n'.join(statements)


def engine_for(args):
    env = dict(os.environ)
    if args.database_env:
        raw = env.get(args.database_env)
        if not raw:
            raise ValueError('DATABASE_ENV_MISSING')
        url = make_url(raw)
    else:
        url = URL.create('postgresql+psycopg', username=env['DB_USER'], password=env['DB_PASSWORD'],
                         host='127.0.0.1', port=int(env.get('DB_PORT', '5432')), database=env['DB_NAME'])
    if url.host not in ('127.0.0.1', 'localhost', '::1') and not args.allow_shared:
        raise ValueError('SHARED_DATABASE_REQUIRES_ALLOW_SHARED')
    if args.allow_shared and not args.database_env:
        raise ValueError('SHARED_DATABASE_REQUIRES_EXPLICIT_ENV')
    # SQLAlchemy hides bound values; never print a connection URL or raw DB exception.
    return make_engine(url, pool_size=3, max_overflow=0)


def register(engine):
    with engine.begin() as connection:
        connection.exec_driver_sql(registration_sql())
    return catalog_series(engine)


def catalog_series(engine):
    with Session(engine) as db:
        rows = db.execute(select(Item.name, PriceSeries).join(PriceSeries, Item.id == PriceSeries.item_id)
                          .where(Item.name.in_(NAMES)).order_by(Item.name, PriceSeries.market)).all()
        result = [{'name': name, 'item_id': s.item_id, 'series_id': s.id, 'market': s.market,
                   'code': s.code, 'unit': s.unit_label} for name, s in rows]
    if len(result) != 30:
        raise ValueError('EXPECTED_30_NEW_SERIES_REGISTER_FIRST')
    return result


def store_records(engine, series, records, start, end, requests=0, partial_error=None):
    dataset = kamis.MARKET_DATASETS[series['market']]
    return collection_service.run_dataset(engine, kamis.SOURCE, dataset, start, end,
                                         lambda: Batch(records, requests, partial_error))


def collect_recent(engine, end):
    series = catalog_series(engine)
    start = end - timedelta(days=364)
    def collect_one(row):
        dataset = kamis.MARKET_DATASETS[row['market']]
        batch = kamis.collect(fetch_json, code=row['code'], dataset=dataset, item_id=row['item_id'],
                              unit_label=row['unit'], start=start, end=end,
                              cert_key=os.environ['KAMIS_CERT_KEY'], cert_id=os.environ['KAMIS_CERT_ID'])
        if any(not start <= record.observed_on <= end for record in batch.records):
            raise ValueError('SOURCE_RETURNED_DATES_OUTSIDE_REQUEST')
        result = store_records(engine, row, batch.records, start, end, batch.requests, batch.partial_error)
        print(json.dumps({'stage': 'recent', 'name': row['name'], 'market': row['market'], **result}, ensure_ascii=False), flush=True)
        if batch.partial_error:
            raise ValueError('RECENT_COLLECTION_PARTIAL_RETRY')
    with ThreadPoolExecutor(max_workers=2) as pool:
        for future in as_completed([pool.submit(collect_one, row) for row in series]):
            future.result()
    warehouse_service.refresh_price_daily(engine, sorted({s['item_id'] for s in series}), since=start)


def collect_history(engine, start, end, cache, comparison_only=False):
    series = catalog_series(engine)
    groups = {}
    for row in series:
        groups.setdefault((row['market'], row['code'][0] + '00'), []).append(row)
    cache.mkdir(parents=True, exist_ok=True)
    days = list(kamis.survey_days(start, end))
    if comparison_only:
        windows = [(end.replace(year=year) - timedelta(days=27), end.replace(year=year))
                   for year in range(end.year - 5, end.year)]
        days = [day for day in days if any(first <= day <= last for first, last in windows)]
    # Recent observations first; cache makes an interrupted run resumable.
    tasks = [(market, category, day) for day in reversed(days) for market, category in groups]
    found = {s['series_id']: [] for s in series}
    errors = []
    def fetch_one(task):
        market, category, day = task
        target = cache / f'{market}-{category}-{day.isoformat()}.json.gz'
        if target.exists():
            with gzip.open(target, 'rt', encoding='utf-8') as handle:
                payload = json.load(handle)
        else:
            sample = groups[market, category][0]
            params = kamis.daily_params(sample['code'], kamis.MARKET_DATASETS[market], day,
                                        os.environ['KAMIS_CERT_KEY'], os.environ['KAMIS_CERT_ID'])
            payload = kamis._trim(fetch_json(kamis.URL, params, timeout=20, retries=2))
            kamis._rows(payload)  # Never cache a failed/authentication response.
            with gzip.open(target, 'wt', encoding='utf-8') as handle:
                json.dump(payload, handle, ensure_ascii=False)
        records = []
        for row in groups[market, category]:
            # Refuse historic unit changes instead of silently mixing incomparable prices.
            source_rows = kamis._rows(payload)
            code = kamis.parse_code(row['code'])
            match = next((r for r in source_rows if (r.get('item_code'), r.get('kind_code'), r.get('rank_code')) == (code['item'], code['kind'], code['rank'])), None)
            if match and match.get('unit') and str(match['unit']).replace(' ', '') != row['unit']:
                raise ValueError('HISTORIC_UNIT_MISMATCH')
            records.extend((row['series_id'], r) for r in kamis.parse_daily(payload, row['code'], kamis.MARKET_DATASETS[market], row['item_id'], row['unit'], day))
        return records
    with ThreadPoolExecutor(max_workers=4) as pool:
        futures = {pool.submit(fetch_one, task): task for task in tasks}
        for count, future in enumerate(as_completed(futures), 1):
            try:
                for sid, record in future.result():
                    found[sid].append(record)
            except Exception as error:
                task = futures[future]
                errors.append({'market': task[0], 'category': task[1], 'date': task[2].isoformat(), 'error': type(error).__name__})
            if count % 100 == 0 or count == len(tasks):
                print(json.dumps({'stage': 'history', 'done': count, 'total': len(tasks), 'observations': sum(map(len, found.values())), 'errors': len(errors)}), flush=True)
    for row in series:
        store_records(engine, row, found[row['series_id']], start, end)
    warehouse_service.refresh_price_daily(engine, sorted({s['item_id'] for s in series}), since=start)
    (cache / 'errors.json').write_text(json.dumps(errors, indent=2), encoding='utf-8')
    if errors:
        raise ValueError(f'HISTORY_PARTIAL_{len(errors)}_RETRY_WITH_CACHE')


def indicators(engine):
    from app.services import indicator_batch_service
    for row in catalog_series(engine):
        if row['market'] == 'RETAIL':
            result = indicator_batch_service.run(engine, row['item_id'])
            print(json.dumps({'stage': 'indicators', 'name': row['name'], **result}, ensure_ascii=False), flush=True)


def export_bundle(engine, folder):
    folder.mkdir(parents=True, exist_ok=True)
    (folder / '01_register_items.sql').write_text('BEGIN;\n' + registration_sql() + '\nCOMMIT;\n', encoding='utf-8')
    (folder / 'catalog.json').write_text(json.dumps(SPEC, ensure_ascii=False, indent=2), encoding='utf-8')
    # Standalone handoff entry point; run it from the recipient's WAS checkout.
    entry = Path(__file__).read_text(encoding='utf-8')
    entry = entry.replace('from app.collectors import kamis', 'import sys\nsys.path.insert(0, str(Path.cwd()))\n\nfrom app.collectors import kamis', 1)
    entry = entry.replace('ROOT = Path.cwd()', 'ROOT = Path.cwd()')
    entry = entry.replace("SPEC_PATH = Path(__file__).resolve().with_name('catalog.json')", "SPEC_PATH = Path(__file__).resolve().with_name('catalog.json')")
    entry = entry.replace("default=Path(__file__).resolve().parent", 'default=Path(__file__).resolve().parent')
    (folder / 'apply_catalog.py').write_text(entry, encoding='utf-8')
    with engine.connect() as connection:
        rows = connection.execute(text('''SELECT i.name,s.market,s.item_code,s.kind_code,s.rank_code,
            o.source_record_key,o.payload,o.observed_on,o.units,o.entity_name,o.payload_sha256
            FROM external_observation o JOIN item i ON i.id=o.item_id
            JOIN price_series s ON s.item_id=i.id AND o.entity_code=concat(s.item_code,'-',s.kind_code,'-',s.rank_code)
             AND o.dataset=CASE s.market WHEN 'RETAIL' THEN 'RETAIL_DAILY' ELSE 'WHOLESALE_DAILY' END
            WHERE i.name=ANY(:names) AND o.source='KAMIS'
            ORDER BY i.name,s.market,o.observed_on,o.retrieved_at'''), {'names': NAMES}).mappings().all()
    portable = [dict(r, observed_on=r['observed_on'].isoformat()) for r in rows]
    with gzip.open(folder / '02_kamis_observations.json.gz', 'wt', encoding='utf-8') as handle:
        json.dump({'version': SPEC['version'], 'records': portable}, handle, ensure_ascii=False)
    report = report_for(engine)
    (folder / 'verification.json').write_text(json.dumps(report, ensure_ascii=False, indent=2, default=str), encoding='utf-8')
    print(json.dumps({'stage': 'export', 'observations': len(portable), 'folder': str(folder)}, ensure_ascii=False))


def import_bundle(engine, folder, *, build_indicators=True):
    with gzip.open(folder / '02_kamis_observations.json.gz', 'rt', encoding='utf-8') as handle:
        bundle = json.load(handle)
    if bundle['version'] != SPEC['version']:
        raise ValueError('BUNDLE_VERSION_MISMATCH')
    series = register(engine)
    for row in series:
        records = []
        for source in bundle['records']:
            if (source['name'], source['market']) != (row['name'], row['market']):
                continue
            code = '-'.join(source[k] for k in ('item_code', 'kind_code', 'rank_code'))
            if code != row['code'] or source['units'].get('unitLabel') != row['unit']:
                raise ValueError('BUNDLE_SERIES_MISMATCH')
            if collection_service.digest(source['payload']) != source['payload_sha256']:
                raise ValueError('BUNDLE_HASH_MISMATCH')
            records.append(Record(kamis.SOURCE, kamis.MARKET_DATASETS[row['market']], source['source_record_key'],
                source['payload'], observed_on=date.fromisoformat(source['observed_on']), entity_code=code,
                entity_name=source['entity_name'], units=source['units'], item_id=row['item_id']))
        if not records:
            raise ValueError('BUNDLE_MISSING_SERIES')
        result = store_records(engine, row, records, min(r.observed_on for r in records), max(r.observed_on for r in records))
        print(json.dumps({'stage': 'import', 'name': row['name'], 'market': row['market'], **result}, ensure_ascii=False), flush=True)
    warehouse_service.refresh_price_daily(engine, sorted({s['item_id'] for s in series}))
    if build_indicators:
        indicators(engine)


def report_for(engine):
    with engine.connect() as connection:
        data = connection.execute(text('''SELECT i.name,s.market,concat(s.item_code,'-',s.kind_code,'-',s.rank_code) AS code,
            s.unit_quantity,s.unit,count(d.id) AS observations,min(d.price_date) AS first_date,max(d.price_date) AS last_date
            FROM item i JOIN price_series s ON s.item_id=i.id LEFT JOIN price_daily d ON d.series_id=s.id
            WHERE i.name=ANY(:names) GROUP BY i.name,s.id ORDER BY i.name,s.market'''), {'names': NAMES}).mappings().all()
        listed = connection.execute(text("SELECT count(*) FROM item i WHERE i.is_price_listed AND EXISTS(SELECT 1 FROM price_series s WHERE s.item_id=i.id AND s.market='RETAIL')")).scalar_one()
        indicator_rows = connection.execute(text('''SELECT DISTINCT ON (i.name) i.name,r.status,r.as_of_date,r.data_date,
            (SELECT count(*) FROM price_indicator_card c WHERE c.run_id=r.id) AS cards
            FROM item i JOIN price_series s ON s.item_id=i.id JOIN price_indicator_run r ON r.series_id=s.id
            WHERE i.name=ANY(:names) AND s.market='RETAIL' ORDER BY i.name,r.as_of_date DESC,r.id DESC'''), {'names': NAMES}).mappings().all()
    return {'version': SPEC['version'], 'listed_items': listed, 'series': [dict(r) for r in data],
            'indicators': [dict(r) for r in indicator_rows],
            'coverage_note': '신규 품목은 최근 1년 일별 관측과 기준일 이전 5개 연도의 같은 28일 관측을 적재했습니다. 5년 연속 일별 이력은 아니며, 휴일·미조사·계절 품종 공백은 채우지 않습니다.',
            'forecast_note': '기존 v2 검증 대상은 5품목뿐입니다. 신규 품목에 검증 정확도·구매 권고를 복사하지 않습니다.'}


def main():
    load_dotenv(ROOT / '.env')
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('action', choices=('register', 'recent', 'history', 'comparison', 'indicators', 'export', 'import', 'report'))
    parser.add_argument('--database-env', help='담당자가 명시한 접속 환경 변수. 생략하면 DB_*의 로컬 DB')
    parser.add_argument('--allow-shared', action='store_true')
    parser.add_argument('--start', type=date.fromisoformat, default=date(2021, 10, 31))
    parser.add_argument('--end', type=date.fromisoformat, default=date(2026, 11, 27))
    parser.add_argument('--folder', type=Path, default=Path(__file__).resolve().parent)
    parser.add_argument('--cache', type=Path, default=ROOT / 'data/raw/catalog-20-kamis')
    args = parser.parse_args()
    engine = None
    try:
        engine = engine_for(args)
        if args.action == 'register':
            register(engine)
            print(json.dumps(report_for(engine), ensure_ascii=False, default=str))
        elif args.action == 'recent': collect_recent(engine, args.end)
        elif args.action in ('history', 'comparison'): collect_history(engine, args.start, args.end, args.cache, args.action == 'comparison')
        elif args.action == 'indicators': indicators(engine)
        elif args.action == 'export': export_bundle(engine, args.folder)
        elif args.action == 'import': import_bundle(engine, args.folder)
        else: print(json.dumps(report_for(engine), ensure_ascii=False, indent=2, default=str))
    except Exception as error:
        # Network/database exceptions can contain credentials. Only emit the error type.
        print(json.dumps({'status': 'FAILED', 'error': type(error).__name__,
                          'code': str(error) if isinstance(error, ValueError) else 'CHECK_CONFIGURATION_OR_SOURCE'}), flush=True)
        return 1
    finally:
        if engine is not None: engine.dispose()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
