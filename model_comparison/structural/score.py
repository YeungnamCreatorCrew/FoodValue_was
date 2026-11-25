"""구조적 가격 전달 모델 자체 채점(독립 트랙, PRD §11). 지표 정의는 기준서 §8과 같다.

기준서 §8과 같은 값이 나오도록 tools.evaluate의 points_for·summarize·result·adoption을 읽기 전용으로 재사용한다(수정 없음).
- policy(주 결과): 실패한 점은 naive로 대체. macro MAPE(계열별 MAPE의 단순 평균), naive 대비 개선율, rMAE, 계열 승,
  월 블록 부트스트랩 1,000회(시드 0), 시장별·계절별·시점별·작형 전환 세부
- model_only: 실패 점 제외(참고)

    # 실행 결과 채점(실행기가 끝에 자동으로도 부른다)
    uv run --extra prices python -m model_comparison.structural.score runs/struct/<실행 이름>

    # naive 자신을 채점(모델 없이 naive 수치만 확인. 튜닝 목록 naive macro MAPE 점검용)
    uv run --extra prices python -m model_comparison.structural.score --naive --origins tune
"""
import argparse
import csv
import hashlib
import json
import sys
from collections import defaultdict
from datetime import date, timedelta
from pathlib import Path

from tools import evaluate, loader, standard
from tools.validate_experiment import round_half_up

ROOT = Path(__file__).resolve().parents[2]
DEFAULT_SNAPSHOT = ROOT / 'data' / 'snapshots' / standard.DATA_VERSION
METRICS = 'metrics.json'


def read_rows(folder: Path):
    with open(Path(folder) / 'predictions.csv', encoding='utf-8', newline='') as f:
        return list(csv.DictReader(f))


def naive_rows(snap: loader.Snapshot, days, series_ids=None):
    """모델 대신 naive를 예측으로 낸 행(채점기가 naive 자신에게 naive 수치를 내는지 확인용)."""
    rows = []
    for sid in series_ids or snap.series_ids:
        for d in days:
            value = snap.naive(sid, d)
            for h in standard.HORIZONS:
                rows.append({'series_id': str(sid), 'origin_date': d.isoformat(),
                             'target_date': (d + timedelta(days=h)).isoformat(), 'horizon': str(h),
                             'status': 'OK' if value is not None else 'NO_INPUT',
                             'predicted_price': '' if value is None else str(round_half_up(value))})
    return rows


def evaluate_rows(rows, snap: loader.Snapshot, meta=None):
    """predictions 행들 -> metrics(dict). 같은 입력이면 같은 값(시간·메모리 같은 장비 값은 넣지 않는다)."""
    points = evaluate.points_for(rows, snap)
    ok = sum(p['ok'] for p in points)
    success_rate = ok / len(points) if points else 0.0
    n = len({int(r['series_id']) for r in rows})
    policy = evaluate.result(points, lambda p: p['pred'] if p['ok'] else p['naive'])
    status_counts = defaultdict(int)
    for r in rows:
        status_counts[r['status']] += 1
    return {
        **(meta or {}),
        'series_count': n, 'prediction_rows': len(rows), 'status_counts': dict(sorted(status_counts.items())),
        'evaluated_points': len(points), 'success_rate': evaluate.r6(success_rate),
        'results': {
            'policy': policy,
            'model_only': evaluate.result(points, lambda p: p['pred'] if p['ok'] else None, with_bootstrap=False),
        },
        'baselines': {
            'naive': evaluate.summarize(points, lambda p: p['naive']) | {'series': None},
            'mean7': evaluate.summarize(points, lambda p: p['mean7']) | {'series': None},
        },
        'adoption': evaluate.adoption(policy, success_rate, n),
    }


def write_metrics(folder: Path, snap: loader.Snapshot):
    folder = Path(folder)
    config = json.loads((folder / 'config.json').read_text(encoding='utf-8'))
    if config.get('kind') == 'smoke':
        raise ValueError(f'줄인 실행(smoke)은 채점하지 않음: {folder.name}')
    meta = {'name': config.get('name'), 'config_id': config.get('config_id'), 'kind': config.get('kind'),
            'origins': config.get('origins'), 'month': config.get('month'), 'data_version': config.get('data_version')}
    metrics = evaluate_rows(read_rows(folder), snap, meta)
    path = folder / METRICS
    with open(path, 'w', encoding='utf-8', newline='\n') as f:
        json.dump(metrics, f, ensure_ascii=False, indent=2, sort_keys=True)
        f.write('\n')
    return metrics, hashlib.sha256(path.read_bytes()).hexdigest()


def print_metrics(metrics):
    evaluate.print_metrics(metrics)


def main(argv=None):
    parser = argparse.ArgumentParser(description='구조적 가격 전달 모델 자체 채점(PRD §11)')
    parser.add_argument('folder', nargs='?', type=Path, help='runs/struct/<실행 이름>')
    parser.add_argument('--naive', action='store_true', help='naive 자신을 채점(기준일 목록 필요)')
    parser.add_argument('--origins', choices=('tune', 'validation'))
    parser.add_argument('--month')
    parser.add_argument('--snapshot', type=Path, default=DEFAULT_SNAPSHOT)
    args = parser.parse_args(argv)
    snap = loader.Snapshot(args.snapshot)
    if args.naive:
        if not args.origins:
            parser.error('--naive에는 --origins가 필요')
        days = snap.origins[args.origins]
        if args.month:
            days = [d for d in days if d.strftime('%Y-%m') == args.month]
        metrics = evaluate_rows(naive_rows(snap, days), snap, {'name': 'naive', 'origins': args.origins})
        print_metrics(metrics)
        print(f'naive macro MAPE {metrics["baselines"]["naive"]["macro_mape"]}%, 기준일 {len(days)}개, '
              f'평가 점 {metrics["evaluated_points"]}개')
        return 0
    if not args.folder:
        parser.error('folder 또는 --naive가 필요')
    try:
        metrics, digest = write_metrics(args.folder, snap)
    except ValueError as error:
        print(f'실패: {error}', file=sys.stderr)
        return 1
    print_metrics(metrics)
    print(f'metrics SHA-256 {digest}')
    return 0


if __name__ == '__main__':
    sys.exit(main())
