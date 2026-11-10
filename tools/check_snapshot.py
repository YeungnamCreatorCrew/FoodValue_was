"""스냅샷 수령 검사(기준서 §2.2, §9). 받은 사람 모두 실험 전에 실행한다.

    uv run python -m tools.check_snapshot data/snapshots/fv-snap-20261031-v1

확인: 스냅샷 ID·마감일·기준서 판, 파일별 SHA-256·행 수, 빠진/남는 파일, 열 이름, 마감일 뒤 관측 없음,
계열별 첫/마지막 관측일·관측 수, 기준일 목록 재계산, 배추·무 이어 붙이기 재계산·연도별 전환 횟수.
마지막 줄의 manifest SHA-256을 팀원끼리 대조한다(모두 같아야 같은 스냅샷).
"""
import argparse
import csv
import json
import sys
from datetime import date
from pathlib import Path

from tools import loader, snapshot, standard


def check(folder: Path):
    errors, lines = [], []
    manifest_path = folder / snapshot.MANIFEST
    if not manifest_path.exists():
        return [f'{snapshot.MANIFEST} 없음'], lines
    manifest = json.loads(manifest_path.read_text(encoding='utf-8'))

    expected = {'snapshot_id': standard.DATA_VERSION, 'cutoff': standard.DATA_CUTOFF.isoformat(),
                'standard_version': standard.STANDARD_VERSION, 'format_version': snapshot.FORMAT_VERSION}
    for key, value in expected.items():
        if manifest.get(key) != value:
            errors.append(f'manifest {key}={manifest.get(key)!r}, 기준서 값 {value!r}')
    cutoff = standard.DATA_CUTOFF

    present = {p.name for p in folder.iterdir() if p.is_file()} - {snapshot.MANIFEST}
    listed = set(manifest.get('files', {}))
    for name in sorted(set(snapshot.COLUMNS) - listed):
        errors.append(f'manifest에 {name} 항목 없음')
    for name in sorted(present - listed):
        errors.append(f'manifest에 없는 파일 {name}')
    for name in sorted(listed):
        info = manifest['files'][name]
        path = folder / name
        if not path.exists():
            errors.append(f'{name} 없음')
            continue
        digest, rows = snapshot.sha256(path), snapshot.count_rows(path)
        ok = digest == info['sha256'] and rows == info['rows']
        if digest != info['sha256']:
            errors.append(f'{name} SHA-256 다름({digest[:16]} ≠ {info["sha256"][:16]})')
        if rows != info['rows']:
            errors.append(f'{name} 행 수 다름({rows} ≠ {info["rows"]})')
        with open(path, encoding='utf-8', newline='') as f:
            header = tuple(next(csv.reader(f), ()))
        if name in snapshot.COLUMNS and header != snapshot.COLUMNS[name]:
            errors.append(f'{name} 열이 다름: {header}')
        lines.append(f'  {"OK " if ok else "ERR"} {name:26} {rows:>7}행  {digest[:16]}')
    if errors:
        return errors, lines

    tables = {name: loader.read_table(folder, name) for name in snapshot.COLUMNS}
    for name, column in snapshot.OBSERVATION_DATE.items():
        late = [r[column] for r in tables[name] if date.fromisoformat(r[column]) > cutoff]
        if late:
            errors.append(f'{name}에 마감일 {cutoff} 뒤 자료 {len(late)}행(예: {late[0]})')

    # 계열 정의·기간
    series = {int(r['series_id']): r for r in tables['price_series.csv']}
    if manifest.get('series_count') != len(series):
        errors.append(f'계열 수 {len(series)} ≠ manifest series_count {manifest.get("series_count")}')
    days = {}
    for r in tables['price_daily.csv']:
        days.setdefault(int(r['series_id']), set()).add(r['price_date'])
    for r in tables['price_daily_merged.csv']:
        days.setdefault(int(r['series_id']), set()).add(r['price_date'])
    if set(days) != set(series):
        errors.append(f'가격 자료의 계열 {sorted(days)} ≠ price_series.csv {sorted(series)}')
    by_id = {s['series_id']: s for s in manifest.get('series', [])}
    for sid in sorted(series):
        info, got = by_id.get(sid), days.get(sid, set())
        if not info or not got:
            errors.append(f'계열 {sid} manifest 정보 또는 자료 없음')
            continue
        actual = (min(got), max(got), len(got))
        if actual != (info['first_date'], info['last_date'], info['observations']):
            errors.append(f'계열 {sid} 기간·관측 수 {actual} ≠ manifest '
                          f'{(info["first_date"], info["last_date"], info["observations"])}')
        lines.append(f'  계열 {sid:>5} {info["item"]} {info["market"]:9} {actual[0]} ~ {actual[1]} {actual[2]}일 '
                     f'[{info["status"]}]')

    # 기준일 목록
    calendar = loader.read_calendar(folder)
    for name, built in snapshot.origin_lists(calendar).items():
        listed_days = [r['origin_date'] for r in tables[name]]
        if listed_days != [d.isoformat() for d in built]:
            errors.append(f'{name}가 calendar_day.csv로 다시 만든 목록과 다름')
    lines.append(f'  기준일 검증 {len(tables["origins_validation.csv"])} / 튜닝 {len(tables["origins_tune.csv"])} '
                 f'/ 시험 {len(tables["origins_test.csv"])}')

    # 이어 붙이기 재계산
    recomputed = loader.merge_from_kind_table(tables['price_daily_kind.csv'], calendar)
    want = [[snapshot.cell(v) for v in row] for row in snapshot.merged_rows_for_csv(recomputed)]
    have = [[r[c] for c in snapshot.COLUMNS['price_daily_merged.csv']] for r in tables['price_daily_merged.csv']]
    if want != have:
        first = next((i for i, (a, b) in enumerate(zip(want, have)) if a != b), min(len(want), len(have)))
        errors.append(f'price_daily_merged.csv가 이어 붙이기 재계산과 다름(행 {first + 1}부터, '
                      f'재계산 {len(want)}행 / 파일 {len(have)}행)')
    for sid, rows in recomputed.items():
        summary = loader.switch_summary(rows)
        stored = by_id.get(sid, {}).get('merge', {})
        if [list(s) for s in summary['switches']] != [list(s) for s in stored.get('switches', [])] \
                or summary['per_year'] != stored.get('per_year'):
            errors.append(f'계열 {sid} 전환일·연도별 전환 횟수가 manifest와 다름')
        lines.append(f'  이어 붙이기 {sid} 연도별 전환 {summary["per_year"]}')
    return errors, lines


def main(argv=None):
    parser = argparse.ArgumentParser(description='스냅샷 수령 검사')
    parser.add_argument('folder', type=Path)
    args = parser.parse_args(argv)
    if not args.folder.is_dir():
        parser.error(f'폴더가 없음: {args.folder}')
    errors, lines = check(args.folder)
    print(f'스냅샷 {args.folder}')
    for line in lines:
        print(line)
    for error in errors:
        print(f'  ERROR {error}')
    manifest = args.folder / snapshot.MANIFEST
    if manifest.exists():
        print(f'manifest SHA-256 {snapshot.sha256(manifest)}')
    print('결과: 통과' if not errors else f'결과: 실패 {len(errors)}건 — 실험을 시작하지 말고 스냅샷 담당에게 알리세요')
    return 1 if errors else 0


if __name__ == '__main__':
    sys.exit(main())
