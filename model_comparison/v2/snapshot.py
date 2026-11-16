"""v2 추가 자료 스냅샷. v1 스냅샷은 그대로 두고, 그 옆에 추가 자료 폴더를 만든다.

    # 스냅샷 담당(공유 DB 보유자): v1 스냅샷이 있어야 함
    uv run --extra prices python -m model_comparison.v2.snapshot export --garak ..\\garak_arrivals.jsonl
    # 스냅샷 담당: 원본 추출본을 검사한 뒤 정제본(실험용)을 만든다
    uv run python -m model_comparison.v2.snapshot check data/snapshots/fv-v2-extra-20261031
    uv run python -m model_comparison.v2.snapshot clean
    # 받은 사람: 정제본 폴더를 받아 검사(manifest SHA-256을 팀과 맞춘다)
    uv run python -m model_comparison.v2.snapshot check

data/snapshots/fv-v2-extra-20261031/     원본 추출본(가락 API 값 그대로). 실험에 직접 쓰지 않는다
data/snapshots/fv-v2-extra-20261031-r2/  정제본(실험 기본값). 원본에서 반입량 오입력 의심값만 빈 값으로 바꿈
- garak_excluded.csv       (정제본만) 뺀 값 목록: 날짜·품목·원래 톤·직전 중앙값·배수
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
import shutil
import statistics
import sys
from datetime import date
from pathlib import Path

from model_comparison.v2.stations import GARAK_ITEM, ITEM_STATIONS
from tools import snapshot as v1
from tools import standard

ROOT = Path(__file__).resolve().parents[2]
V1_DIR = ROOT / 'data' / 'snapshots' / standard.DATA_VERSION
RAW_ID = 'fv-v2-extra-20261031'  # 원본 추출본(export 결과). PR #42 v2 첫 결과는 이 판으로 냈다
RAW_DIR = ROOT / 'data' / 'snapshots' / RAW_ID
EXTRA_ID = 'fv-v2-extra-20261031-r2'  # 정제본(clean 결과) — 모든 v2 실험의 기본 입력
EXTRA_DIR = ROOT / 'data' / 'snapshots' / EXTRA_ID
# 반입량 오입력 판정: 그 품목 직전 반입일(0톤 제외) WINDOW개 중앙값의 RATIO배 초과 → 빈 값
GARAK_SPIKE_RATIO = 8
GARAK_SPIKE_WINDOW = 20
GARAK_SPIKE_MIN_HISTORY = 10  # 직전 값이 이보다 적으면 판정하지 않음
COLUMNS = {
    'asos_station_daily.csv': ('stn_id', 'obs_date', 'avg_ta', 'min_ta', 'max_ta', 'sum_rn', 'avg_rhm', 'sum_ss_hr'),
    'garak_arrivals_daily.csv': ('arrival_date', 'item', 'ton'),
    'item_station.csv': ('item', 'stn_id', 'stn_name', 'role'),
    'garak_excluded.csv': ('arrival_date', 'item', 'raw_ton', 'past_median', 'ratio'),
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


def drop_garak_spikes(tons: dict) -> dict:
    """(품목, 날짜) → 톤 에서 오입력 의심값을 찾는다. 반환: (품목, 날짜) → 직전 중앙값.

    직전 값만 보므로 날짜 t의 판정에 t 이후 자료가 들어가지 않는다(시점 규칙 유지). 의심값은 이후 기준에서 뺀다.
    근거(2026-11-16 가락 API data21 재조회, 원본 값 확인): 무 2021-11-26 14,762톤 = 한 도매법인 14,400톤
    (앞뒤 날 합계 360~377톤), 깐마늘(가락 '마늘') 2021-04-23·08-09·08-26·09-15 = 한 법인 168~1,319톤(평소 8~23톤).
    배수 8은 이 5건(최소 8.8배)과 다음으로 큰 정상값(6.5배) 사이로 잡았다.
    """
    dropped, history = {}, {}
    for item, day in sorted(tons):
        ton = tons[item, day]
        past = history.setdefault(item, [])
        if len(past) >= GARAK_SPIKE_MIN_HISTORY:
            median = statistics.median(past)
            if ton > GARAK_SPIKE_RATIO * median:
                dropped[item, day] = median
                continue
        if ton > 0:
            past.append(ton)
            del past[:-GARAK_SPIKE_WINDOW]
    return dropped


def clean(src: Path = RAW_DIR, out: Path = EXTRA_DIR) -> dict:
    """원본 추출본 → 정제본. 반입량 의심값의 ton만 빈 값으로 바꾸고 나머지 글자·파일은 그대로 둔다."""
    src, out = Path(src), Path(out)
    raw_manifest = json.loads((src / 'manifest.json').read_text(encoding='utf-8'))
    bad = [name for name, info in raw_manifest.get('files', {}).items()
           if not (src / name).exists() or v1.sha256(src / name) != info['sha256']]
    if bad:
        raise SystemExit(f'원본 추출본 SHA-256 불일치: {bad}')
    if out.exists() and any(out.iterdir()):
        raise SystemExit(f'{out}이 비어 있지 않음')
    out.mkdir(parents=True, exist_ok=True)
    with open(src / 'garak_arrivals_daily.csv', encoding='utf-8', newline='') as f:
        rows = list(csv.reader(f))
    header, body = rows[0], rows[1:]
    if tuple(header) != COLUMNS['garak_arrivals_daily.csv']:
        raise SystemExit(f'반입량 열이 다름: {header}')
    tons = {(item, date.fromisoformat(day)): float(ton) for day, item, ton in body}
    dropped = drop_garak_spikes(tons)
    files = {}
    with open(out / 'garak_arrivals_daily.csv', 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f, lineterminator='\n')
        writer.writerow(header)
        for day, item, ton in body:
            writer.writerow([day, item, '' if (item, date.fromisoformat(day)) in dropped else ton])
    files['garak_arrivals_daily.csv'] = {'sha256': v1.sha256(out / 'garak_arrivals_daily.csv'), 'rows': len(body)}
    excluded = [(day, item, v1.cell(tons[item, day]), v1.cell(round(median, 4)),
                 v1.cell(round(tons[item, day] / median, 1)))
                for (item, day), median in sorted(dropped.items(), key=lambda kv: (kv[0][1], kv[0][0]))]
    files['garak_excluded.csv'] = write(out, 'garak_excluded.csv', excluded)
    for name in raw_manifest['files']:
        if name not in files:
            shutil.copyfile(src / name, out / name)
            files[name] = raw_manifest['files'][name]
    manifest = {'extra_id': EXTRA_ID if out == EXTRA_DIR else out.name,
                'base_snapshot_id': raw_manifest['base_snapshot_id'],
                'base_manifest_sha256': raw_manifest['base_manifest_sha256'], 'cutoff': raw_manifest['cutoff'],
                'derived_from': {'extra_id': raw_manifest['extra_id'], 'manifest_sha256': v1.sha256(src / 'manifest.json')},
                'cleaning': {'garak_spike': {'rule': 'ton > ratio × median(직전 window개 반입일, 0톤 제외) → 빈 값',
                                             'ratio': GARAK_SPIKE_RATIO, 'window': GARAK_SPIKE_WINDOW,
                                             'min_history': GARAK_SPIKE_MIN_HISTORY, 'dropped': len(dropped)}},
                'files': dict(sorted(files.items()))}
    (out / 'manifest.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + '\n', encoding='utf-8', newline='\n')  # OS와 무관하게 LF → 누가 만들어도 같은 SHA
    for row in excluded:
        print('  제외', *row)
    print(f'정제본 → {out}\nmanifest SHA-256 {v1.sha256(out / "manifest.json")}')
    return manifest


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
    p_export.add_argument('--out', default=str(RAW_DIR))
    p_clean = sub.add_parser('clean', help='원본 추출본 → 정제본(반입량 오입력 의심값 제거)')
    p_clean.add_argument('--src', type=Path, default=RAW_DIR)
    p_clean.add_argument('--out', type=Path, default=EXTRA_DIR)
    p_check = sub.add_parser('check')
    p_check.add_argument('folder', nargs='?', type=Path, default=EXTRA_DIR)
    args = parser.parse_args(argv)
    if args.command == 'export':
        export(args)
        return 0
    if args.command == 'clean':
        clean(args.src, args.out)
        return 0
    errors = check(args.folder)
    for error in errors:
        print(f'  ERROR {error}')
    print(f'manifest SHA-256 {v1.sha256(args.folder / "manifest.json")}')
    print('결과: 통과' if not errors else f'결과: 실패 {len(errors)}건')
    return 1 if errors else 0


if __name__ == '__main__':
    sys.exit(main())
