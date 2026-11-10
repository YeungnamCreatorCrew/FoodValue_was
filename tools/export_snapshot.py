"""실험 데이터 스냅샷 내보내기(기준서 §2.2, §9). 공유 DB 보유자(스냅샷 담당)만 실행한다.

    uv run --extra prices python -m tools.export_snapshot            # .env의 DATABASE_URL, KOSIS_API_KEY 사용
    uv run --extra prices python -m tools.export_snapshot --exclude-item 깐마늘   # 팀이 품목을 빼기로 했을 때

결과: data/snapshots/<DATA_VERSION>/ (Git에 올리지 않음. 압축해 팀 공유 드라이브로 배포)
- 관측 자료는 마감일(DATA_CUTOFF)까지만 자른다. DB에 그 뒤 자료가 있어도 다시 수집할 필요 없다.
- 배추·무는 작형별 원본(price_daily_kind.csv)을 tools.loader.merge_kinds로 한 번 이어 붙여 price_daily_merged.csv로 둔다.
- 생산량은 KOSIS에서 실험 품목 매핑(깐마늘→마늘, 배추·무 작형→배추·무)으로 받는다. DB의 item_production은 쓰지 않는다
  (작형별 품목·깐마늘은 이름이 KOSIS 키와 달라 비어 있다).
- 계열 품질(§2.1)을 계산해 manifest와 화면에 낸다. REVIEW·FAIL 계열은 팀이 포함 여부를 정한다.
"""
import argparse
import json
import os
import subprocess
import sys
from datetime import UTC, date, datetime
from pathlib import Path

from tools import loader, snapshot, standard
from tools.runtime import apply_environment

ROOT = Path(__file__).resolve().parents[1]

QUERIES = {
    'series': """
SELECT s.id, i.name, s.market, s.item_code, s.kind_code, s.rank_code, s.unit_quantity, s.unit
FROM price_series s JOIN item i ON i.id = s.item_id
WHERE i.name IN ('대파', '양파', '깐마늘') OR i.name LIKE '배추(%' OR i.name LIKE '무(%'
ORDER BY s.id""",
    'price_daily': """
SELECT d.series_id, d.price_date, d.price
FROM price_daily d JOIN price_series s ON s.id = d.series_id JOIN item i ON i.id = s.item_id
WHERE (i.name IN ('대파', '양파', '깐마늘') OR i.name LIKE '배추(%' OR i.name LIKE '무(%')
  AND d.price_date <= :cutoff
ORDER BY d.series_id, d.price_date""",
    'calendar_day': """
SELECT cal_date, day_of_week, is_holiday, holiday_name, lunar_month, lunar_day, is_lunar_leap, is_market_closed
FROM calendar_day WHERE cal_date BETWEEN DATE '2016-01-01' AND DATE '2027-12-31' ORDER BY cal_date""",
    'calendar_event': """
SELECT event_code, name, start_date, end_date, effect_start_date, effect_end_date
FROM calendar_event ORDER BY start_date, event_code""",
    'weather_daily': """
SELECT weather_date, avg_temp, max_temp, min_temp, precipitation, avg_humidity, sunshine_hours,
       heat_station_ratio, heavy_rain_station_ratio, cold_station_ratio, station_count
FROM weather_daily WHERE data_type = 'ACTUAL' AND weather_date <= :cutoff ORDER BY weather_date""",
    'exchange_rate_daily': """
SELECT rate_date, currency_code, rate, unit_label
FROM exchange_rate_daily WHERE rate_date <= :cutoff ORDER BY rate_date, currency_code""",
    'flyway': """
SELECT version, description, success FROM flyway_schema_history ORDER BY installed_rank""",
}


class SnapshotError(Exception):
    pass


def base_item(name: str):
    """DB 품목 이름 → (실험 품목, 작형 품목 여부). 배추(월동) → ('배추', True)."""
    if name in snapshot.DIRECT_ITEMS:
        return name, False
    for item in ('배추', '무'):
        if name.startswith(f'{item}('):
            return item, True
    raise SnapshotError(f'실험 품목이 아님: {name}')


def production_rows(fetch_production, cutoff: date, items):
    """[(실험 품목, 연도, 톤, 사용 시작일)]. 사용 시작일 = Y+1년 6월 30일(§3.1). 마감일 이후에 쓸 수 있는 연도는 뺀다."""
    rows = []
    for item in items:
        for year, ton in sorted(fetch_production(snapshot.PRODUCTION_KEY[item]).items()):
            usable = date(year + 1, 6, 30)
            if usable <= cutoff:
                rows.append((item, year, ton, usable))
    return rows


def build(raw: dict, out: Path, *, cutoff: date, exclude_items=(), meta=None) -> dict:
    """DB에서 읽은 원자료로 스냅샷 폴더를 만든다. raw 키: series, price_daily, calendar_day, calendar_event,
    weather_daily, exchange_rate_daily, production, flyway(선택). 반환: manifest."""
    exclude = set(exclude_items)
    unknown = exclude - set(standard.ITEMS)
    if unknown:
        raise SnapshotError(f'모르는 품목: {sorted(unknown)}')
    if out.exists() and any(out.iterdir()):
        raise SnapshotError(f'{out}이 비어 있지 않음. 다른 폴더를 주거나 지운 뒤 다시 실행')
    out.mkdir(parents=True, exist_ok=True)

    calendar = [(r[0], bool(r[7])) for r in raw['calendar_day']]
    survey = sorted(d for d, closed in calendar if not closed)

    # 계열 정의: 대파·양파·깐마늘은 DB id 그대로, 배추·무는 (품목, 시장)별 가상 id
    direct, kind_source = {}, {}
    for sid, name, market, item_code, kind_code, rank_code, quantity, unit in raw['series']:
        item, is_kind = base_item(name)
        if item in exclude:
            continue
        if is_kind:
            kind_source[sid] = (snapshot.MERGED_ID[item, market], kind_code, item_code, rank_code, quantity, unit)
        else:
            direct[sid] = (item, market, item_code, kind_code, rank_code, quantity, unit)
    merged_def = {}
    for source, (mid, kind, item_code, rank_code, quantity, unit) in sorted(kind_source.items()):
        entry = merged_def.setdefault(mid, {'item_code': item_code, 'rank_code': rank_code,
                                            'unit': (snapshot.cell(quantity), unit), 'sources': []})
        if entry['unit'] != (snapshot.cell(quantity), unit) or entry['item_code'] != item_code:
            raise SnapshotError(f'{standard.MERGED_SERIES[mid]} 작형별 단위·코드가 다름(§2.1: 이어 붙이지 않고 팀에 알림)')
        entry['sources'].append((source, kind))

    daily, kinds = [], []
    for sid, day, price in raw['price_daily']:
        if day > cutoff:
            raise SnapshotError(f'마감일 이후 자료가 쿼리에서 걸러지지 않음: {sid} {day}')
        if sid in direct:
            daily.append((sid, day, price))
        elif sid in kind_source:
            kinds.append((kind_source[sid][0], sid, kind_source[sid][1], day, price))
    kinds.sort(key=lambda r: (r[0], r[3], r[2]))
    merged = {}
    for mid in sorted(merged_def):
        obs = [(day, kind, price, source) for m, source, kind, day, price in kinds if m == mid]
        merged[mid] = loader.merge_kinds(obs, survey)

    series_rows = [(sid, *spec, '') for sid, spec in sorted(direct.items())]
    for mid, entry in sorted(merged_def.items()):
        item, market = standard.MERGED_SERIES[mid]
        sources = ';'.join(str(s) for s, _ in entry['sources'])
        series_rows.append((mid, item, market, entry['item_code'], '', entry['rank_code'], *entry['unit'], sources))
    if not series_rows:
        raise SnapshotError('내보낼 계열이 없음')

    included_items = [i for i in standard.ITEMS if i not in exclude]
    files = {
        'price_series.csv': series_rows,
        'price_daily.csv': daily,
        'price_daily_kind.csv': kinds,
        'price_daily_merged.csv': snapshot.merged_rows_for_csv(merged),
        'calendar_day.csv': raw['calendar_day'],
        'calendar_event.csv': raw['calendar_event'],
        'weather_daily.csv': raw['weather_daily'],
        'exchange_rate_daily.csv': raw['exchange_rate_daily'],
        'item_production.csv': [r for r in raw['production'] if r[0] in included_items],
    }
    for name, days in snapshot.origin_lists(calendar).items():
        files[name] = [(d,) for d in days]

    manifest_files = {}
    for name in snapshot.COLUMNS:
        rows = snapshot.write_csv(out, name, files[name])
        manifest_files[name] = {'sha256': snapshot.sha256(out / name), 'rows': rows}

    # 계열 통계·품질
    days_by_series = {}
    for sid, day, _ in daily:
        days_by_series.setdefault(sid, set()).add(day)
    for mid, rows in merged.items():
        days_by_series[mid] = {r.price_date for r in rows}
    series_info = []
    for row in series_rows:
        sid = row[0]
        days = days_by_series.get(sid)
        if not days:
            raise SnapshotError(f'계열 {sid} {row[1]} {row[2]}에 관측이 없음')
        info = {'series_id': sid, 'item': row[1], 'market': row[2],
                'code': f'{row[3]}-{row[4] or "작형별"}-{row[5]}', 'unit': f'{row[6]} {row[7]}',
                **snapshot.series_quality(days, survey, cutoff)}
        if sid in merged:
            info['source_series'] = [{'source_series_id': s, 'kind_code': k} for s, k in merged_def[sid]['sources']]
            info['merge'] = loader.switch_summary(merged[sid])
            info['monthly_observations'] = snapshot.monthly_counts(days)
        series_info.append(info)

    kind_months = {}
    for mid, source, kind, day, _ in kinds:
        item = standard.MERGED_SERIES[mid][0]
        months = kind_months.setdefault(item, {}).setdefault(kind, set())
        months.add(day.month)
    meta = meta or {}
    manifest = {
        'format_version': snapshot.FORMAT_VERSION,
        'snapshot_id': standard.DATA_VERSION,
        'standard_version': standard.STANDARD_VERSION,
        'cutoff': cutoff.isoformat(),
        'created_at': meta.get('created_at'),
        'git_sha': meta.get('git_sha'),
        'git_dirty': meta.get('git_dirty'),
        'flyway': [{'version': v, 'description': d, 'success': bool(s)} for v, d, s in raw.get('flyway', [])],
        'series_count': len(series_rows),
        'excluded_items': sorted(exclude),
        'files': manifest_files,
        'series': series_info,
        'kind_priority_by_month': {str(m): k for m, k in standard.KIND_PRIORITY_BY_MONTH.items()},
        'kind_observed_months': {item: {k: sorted(v) for k, v in sorted(ks.items())}
                                 for item, ks in sorted(kind_months.items())},
        'production_mapping': {i: snapshot.PRODUCTION_KEY[i] for i in included_items},
        'notes': meta.get('notes', []),
        'queries': {name: ' '.join(q.split()) for name, q in QUERIES.items()},
    }
    with open(out / snapshot.MANIFEST, 'w', encoding='utf-8', newline='\n') as f:
        json.dump(manifest, f, ensure_ascii=False, indent=2)
        f.write('\n')
    return manifest


def read_database(url: str, cutoff: date) -> dict:
    from sqlalchemy import create_engine, text

    engine = create_engine(url, pool_pre_ping=True, hide_parameters=True)
    raw = {}
    with engine.connect() as connection:
        for name, query in QUERIES.items():
            raw[name] = [tuple(r) for r in connection.execute(text(query), {'cutoff': cutoff})]
    raw['series'] = [tuple(r) for r in raw['series']]
    return raw


def kosis_fetcher(key: str):
    from app.collectors import http, kosis

    def fetch(name: str) -> dict:
        batch = kosis.collect(http.fetch_json, key=key, items=[(None, name)],
                              start_year=standard.COLLECT_START.year - 1, end_year=date.today().year)
        if batch.partial_error or not batch.records:
            raise SnapshotError(f'KOSIS 생산량({name})을 받지 못함: {batch.partial_error or "자료 없음"}')
        return {r.period_start.year: http.number(r.payload['DT']) for r in batch.records}
    return fetch


def git_state():
    def run(*args):
        return subprocess.run(['git', *args], cwd=ROOT, capture_output=True, text=True, check=False).stdout.strip()
    return run('rev-parse', 'HEAD') or None, bool(run('status', '--porcelain', '--untracked-files=no'))


def print_summary(manifest, out):
    print(f'스냅샷 {manifest["snapshot_id"]} → {out}')
    print(f'계열 N={manifest["series_count"]}  마감일 {manifest["cutoff"]}  Git {str(manifest["git_sha"])[:10]}')
    for s in manifest['series']:
        line = (f'  [{s["status"]:6}] {s["series_id"]:>5} {s["item"]} {s["market"]:9} {s["first_date"]} ~ {s["last_date"]}'
                f'  {s["observations"]}일  2023~ {s["coverage_from_2023"]:.1%}')
        if 'merge' in s:
            line += f'  연도별 전환 {s["merge"]["per_year"]}'
        print(line)
        for note in s['notes']:
            print(f'           - {note}')
        for first, last, length in s['missing_runs_from_2023']:
            print(f'           - 결측 {first} ~ {last} ({length}조사일)')
    for name, info in manifest['files'].items():
        print(f'  {name:26} {info["rows"]:>7}행  {info["sha256"][:16]}')
    review = [s for s in manifest['series'] if s['status'] != 'PASS']
    if review:
        print(f'\n※ REVIEW/FAIL 계열 {len(review)}개: 팀이 포함 여부를 정하세요. 품목을 빼려면 --exclude-item <품목>으로 다시 만듭니다.')
    print(f'\n배포: {out} 폴더를 압축해 공유 드라이브에 올리고, 받는 사람은 python -m tools.check_snapshot {out}')


def main(argv=None):
    parser = argparse.ArgumentParser(description='실험 데이터 스냅샷 내보내기(기준서 §2.2)')
    parser.add_argument('--out', type=Path, default=ROOT / 'data' / 'snapshots' / standard.DATA_VERSION)
    parser.add_argument('--exclude-item', action='append', default=[], choices=standard.ITEMS,
                        help='팀이 빼기로 한 품목(반복 가능)')
    args = parser.parse_args(argv)
    apply_environment()
    from dotenv import load_dotenv
    load_dotenv(ROOT / '.env')
    url, kosis_key = os.getenv('DATABASE_URL'), os.getenv('KOSIS_API_KEY')
    if not url:
        parser.error('.env에 DATABASE_URL이 필요합니다')
    if not kosis_key:
        parser.error('.env에 KOSIS_API_KEY가 필요합니다(생산량)')
    cutoff = standard.DATA_CUTOFF
    try:
        raw = read_database(url, cutoff)
        items = [i for i in standard.ITEMS if i not in args.exclude_item]
        raw['production'] = production_rows(kosis_fetcher(kosis_key), cutoff, items)
        sha, dirty = git_state()
        notes = ['깐마늘은 소매 258-01, 도매 258-03(대서)로 소매·도매 품종이 다름']
        if dirty:
            notes.append('내보낼 때 추적 파일에 커밋하지 않은 변경이 있었음')
        manifest = build(raw, args.out, cutoff=cutoff, exclude_items=args.exclude_item,
                         meta={'created_at': datetime.now(UTC).isoformat(timespec='seconds'),
                               'git_sha': sha, 'git_dirty': dirty, 'notes': notes})
    except SnapshotError as error:
        print(f'실패: {error}', file=sys.stderr)
        return 1
    print_summary(manifest, args.out)
    return 0


if __name__ == '__main__':
    sys.exit(main())
