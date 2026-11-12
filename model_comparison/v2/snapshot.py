"""v2 추가 자료 스냅샷. v1 스냅샷은 그대로 두고, 그 옆에 추가 자료 폴더를 만든다.

    # 스냅샷 담당(공유 DB 보유자): v1 스냅샷이 있어야 함
    uv run --extra prices python -m model_comparison.v2.snapshot export --garak ..\\garak_arrivals.jsonl
    # 받은 사람
    uv run python -m model_comparison.v2.snapshot check

data/snapshots/fv-v2-extra-20261031/
- asos_station_daily.csv  관측소별 ASOS 일자료(주산지 관측소만), 마감일까지
- garak_arrivals_daily.csv 가락시장 경매 후 반입물량(톤), 실험 5개 품목, 마감일까지
- item_station.csv         품목 → 주산지 관측소(stations.py)
- manifest.json            v1 스냅샷 ID·manifest SHA-256, 파일별 SHA-256·행 수

v1 스냅샷 파일을 복사하지 않으므로 v1 입력(가격·달력 등)은 v1과 바이트 단위로 같다.
"""
import argparse
import csv
import json
import os
import sys
from datetime import date
from pathlib import Path

from model_comparison.v2.stations import GARAK_ITEM, ITEM_STATIONS
from tools import snapshot as v1
from tools import standard

ROOT = Path(__file__).resolve().parents[2]
V1_DIR = ROOT / 'data' / 'snapshots' / standard.DATA_VERSION
EXTRA_ID = 'fv-v2-extra-20261031'
EXTRA_DIR = ROOT / 'data' / 'snapshots' / EXTRA_ID
COLUMNS = {
    'asos_station_daily.csv': ('stn_id', 'obs_date', 'avg_ta', 'min_ta', 'max_ta', 'sum_rn', 'avg_rhm', 'sum_ss_hr'),
    'garak_arrivals_daily.csv': ('arrival_date', 'item', 'ton'),
    'item_station.csv': ('item', 'stn_id', 'stn_name', 'role'),
}
ASOS_FIELDS = ('avgTa', 'minTa', 'maxTa', 'sumRn', 'avgRhm', 'sumSsHr')


def write(out: Path, name: str, rows) -> dict:
    with open(out / name, 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f, lineterminator='\n')
        writer.writerow(COLUMNS[name])
        count = 0
        for row in rows:
            writer.writerow([v1.cell(v) for v in row])
            count += 1
    return {'sha256': v1.sha256(out / name), 'rows': count}


def garak_rows(path: Path, cutoff: date):
    """jsonl(하루 × 품목) → (날짜, 실험 품목, 톤). 자료가 있는 날 그 품목 행이 없으면 0톤(미반입)."""
    wanted = {name: item for item, name in GARAK_ITEM.items()}
    days, totals = set(), {}
    with open(path, encoding='utf-8') as f:
        for line in f:
            record = json.loads(line)
            day = date.fromisoformat(record['date'])
            if day > cutoff or not record.get('ITM_NM'):
                continue  # 품목이 하나도 없는 날 = 자료 없음(0톤이 아님)
            days.add(day)
            item = wanted.get(record.get('ITM_NM'))
            if item:
                totals[day, item] = totals.get((day, item), 0.0) + float(record.get('SUM_TOT') or 0)
    return [(day, item, round(totals.get((day, item), 0.0), 4)) for day in sorted(days) for item in standard.ITEMS]


def asos_rows(url: str, cutoff: date, stations):
    from sqlalchemy import create_engine, text

    query = text("""
        SELECT entity_code, observed_on, payload FROM external_observation
        WHERE dataset = 'ASOS_DAILY' AND observed_on <= :cutoff AND entity_code = ANY(:stations)
        ORDER BY entity_code::int, observed_on, id""")
    latest = {}
    with create_engine(url, hide_parameters=True).connect() as connection:
        for code, day, payload in connection.execute(query, {'cutoff': cutoff, 'stations': [str(s) for s in stations]}):
            latest[int(code), day] = payload  # 같은 날 여러 판이면 마지막(최신) 판
    for (stn, day), payload in sorted(latest.items()):
        yield (stn, day, *[payload.get(k) for k in ASOS_FIELDS])


def export(args):
    from dotenv import load_dotenv

    load_dotenv(ROOT / '.env')
    url = os.getenv('DATABASE_URL')
    if not url:
        raise SystemExit('.env에 DATABASE_URL이 필요합니다')
    base_manifest = V1_DIR / v1.MANIFEST
    if not base_manifest.exists():
        raise SystemExit(f'v1 스냅샷이 없음: {V1_DIR}')
    out = Path(args.out)
    if out.exists() and any(out.iterdir()):
        raise SystemExit(f'{out}이 비어 있지 않음')
    out.mkdir(parents=True, exist_ok=True)
    cutoff = standard.DATA_CUTOFF
    stations = sorted({s for rows in ITEM_STATIONS.values() for s, _, _ in rows})
    files = {
        'asos_station_daily.csv': write(out, 'asos_station_daily.csv', asos_rows(url, cutoff, stations)),
        'garak_arrivals_daily.csv': write(out, 'garak_arrivals_daily.csv', garak_rows(Path(args.garak), cutoff)),
        'item_station.csv': write(out, 'item_station.csv', [(item, s, name, role) for item, rows in ITEM_STATIONS.items()
                                                            for s, name, role in rows]),
    }
    manifest = {'extra_id': EXTRA_ID, 'base_snapshot_id': standard.DATA_VERSION,
                'base_manifest_sha256': v1.sha256(base_manifest), 'cutoff': cutoff.isoformat(), 'files': files}
    (out / 'manifest.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    for name, info in files.items():
        print(f'  {name:26} {info["rows"]:>7}행  {info["sha256"][:16]}')
    print(f'v2 추가 자료 → {out}\nmanifest SHA-256 {v1.sha256(out / "manifest.json")}')


def check(folder: Path = EXTRA_DIR, base: Path = V1_DIR) -> list[str]:
    errors = []
    manifest = json.loads((folder / 'manifest.json').read_text(encoding='utf-8'))
    if manifest.get('base_snapshot_id') != standard.DATA_VERSION:
        errors.append(f'v1 스냅샷 ID가 다름: {manifest.get("base_snapshot_id")}')
    if v1.sha256(base / v1.MANIFEST) != manifest.get('base_manifest_sha256'):
        errors.append('v1 스냅샷 manifest가 v2를 만들 때와 다름(v1 스냅샷부터 check_snapshot으로 확인)')
    for name, info in manifest.get('files', {}).items():
        path = folder / name
        if not path.exists():
            errors.append(f'{name} 없음')
        elif v1.sha256(path) != info['sha256']:
            errors.append(f'{name} SHA-256 다름')
    return errors


def main(argv=None):
    parser = argparse.ArgumentParser(description='v2 추가 자료 스냅샷')
    sub = parser.add_subparsers(dest='command', required=True)
    p_export = sub.add_parser('export')
    p_export.add_argument('--garak', required=True, help='가락시장 반입량 jsonl (fv_garak_collect.py 결과)')
    p_export.add_argument('--out', default=str(EXTRA_DIR))
    p_check = sub.add_parser('check')
    p_check.add_argument('folder', nargs='?', type=Path, default=EXTRA_DIR)
    args = parser.parse_args(argv)
    if args.command == 'export':
        export(args)
        return 0
    errors = check(args.folder)
    for error in errors:
        print(f'  ERROR {error}')
    print(f'manifest SHA-256 {v1.sha256(args.folder / "manifest.json")}')
    print('결과: 통과' if not errors else f'결과: 실패 {len(errors)}건')
    return 1 if errors else 0


if __name__ == '__main__':
    sys.exit(main())
