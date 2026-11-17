"""v2 앙상블: 이미 끝난 실험 폴더 여러 개의 예측을 평균해 새 실험 폴더로 쓰고 같은 평가기로 채점한다.

모델을 다시 학습하지 않으므로 몇 초면 끝난다. 같은 기준일 목록·계열로 돌린 실험만 합칠 수 있다.

    uv run --extra prices python -m model_comparison.v2.ensemble experiments_v2/xgb-... experiments_v2/lgbm-... \\
        --name ens-xgb-lgbm [--weights 0.5,0.5] [--how mean|median]

- 같은 (계열, 기준일, 시점)에서 모든 실험이 OK일 때만 평균한다. 하나라도 실패면 그 점은 성공한 실험만으로 평균,
  모두 실패면 첫 실험의 상태를 그대로 쓴다(평가기가 naive로 대체).
- 가중치는 합이 1이 되도록 맞춘다. 기준일 목록 결과(tune)로 정한 가중치를 검증 전체에 그대로 쓴다.
"""
import argparse
import csv
import json
import sys
from datetime import date
from pathlib import Path

import numpy as np

from tools import evaluate, loader, run_backtest, standard

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / 'experiments_v2'


def _read(folder: Path):
    rows = evaluate.read_predictions(folder)
    return {(r['series_id'], r['origin_date'], r['horizon']): r for r in rows}


def combine(folders, weights=None, how='mean'):
    """폴더별 예측 → 행 목록(PREDICTION_COLUMNS 순서의 dict). 키 집합이 다르면 멈춘다."""
    tables = [_read(Path(f)) for f in folders]
    keys = list(tables[0])
    if any(set(t) != set(keys) for t in tables[1:]):
        raise SystemExit('실험들의 (계열, 기준일, 시점) 목록이 다름. 같은 기준일 목록·계열로 돌린 결과만 합칠 수 있음')
    w = np.ones(len(tables)) if weights is None else np.asarray(weights, dtype=float)
    if len(w) != len(tables) or (w < 0).any() or w.sum() <= 0:
        raise SystemExit('가중치 개수·값이 잘못됨')
    out = []
    for key in keys:
        rows = [t[key] for t in tables]
        ok = [i for i, r in enumerate(rows) if r['status'] == 'OK' and r['predicted_price'] not in ('', None)]
        row = dict(rows[0])
        if ok:
            values = np.array([float(rows[i]['predicted_price']) for i in ok])
            raw = np.array([float(rows[i]['predicted_price_raw'] or rows[i]['predicted_price']) for i in ok])
            if how == 'median':
                price, price_raw = float(np.median(values)), float(np.median(raw))
            else:
                ww = w[ok] / w[ok].sum()
                price, price_raw = float(values @ ww), float(raw @ ww)
            row.update(predicted_price=price, predicted_price_raw=price_raw, status='OK', error_code='')
        out.append(row)
    return out


def run(args):
    folders = [Path(f) for f in args.folders]
    configs = [json.loads((f / 'config.json').read_text(encoding='utf-8')) for f in folders]
    origin_lists = {c.get('origin_list') for c in configs}
    if len(origin_lists) != 1:
        raise SystemExit(f'기준일 목록이 다름: {origin_lists}')
    weights = [float(x) for x in args.weights.split(',')] if args.weights else None
    rows = combine(folders, weights, args.how)
    stamp = date.today().strftime('%Y%m%d')
    base = f'{args.name}-{configs[0]["origin_list"]}{"-" + configs[0]["month"] if configs[0].get("month") else ""}-{stamp}'
    folder = next(Path(args.out) / f'{base}-{n:02d}' for n in range(1, 100) if not (Path(args.out) / f'{base}-{n:02d}').exists())
    folder.mkdir(parents=True)
    record = {'name': args.name, 'model': 'Ensemble', 'phase': 'v2', 'experiment_id': folder.name,
              'data_version': standard.DATA_VERSION, 'origin_list': configs[0]['origin_list'],
              'month': configs[0].get('month'), 'how': args.how, 'weights': weights,
              'members': [c['experiment_id'] for c in configs], 'member_configs': configs,
              'git_sha': run_backtest.git('rev-parse', 'HEAD') or None}
    record['config_id'] = run_backtest.config_id({**record, 'extra_features': [], 'feature_set': 'v2:ensemble'})
    (folder / 'config.json').write_text(json.dumps(record, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    with open(folder / 'predictions.csv', 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f, lineterminator='\n')
        writer.writerow(standard.PREDICTION_COLUMNS)
        for r in rows:
            r = {**r, 'experiment_id': folder.name, 'model': 'Ensemble', 'config_id': record['config_id']}
            writer.writerow([r[c] for c in standard.PREDICTION_COLUMNS])
    snap = loader.Snapshot(args.snapshot)
    metrics, digest = evaluate.write_metrics(folder, snap)
    evaluate.print_metrics(metrics)
    print(f'metrics SHA-256 {digest}')
    return folder


def main(argv=None):
    parser = argparse.ArgumentParser(description='v2 앙상블(끝난 실험 예측 평균)')
    parser.add_argument('folders', nargs='+')
    parser.add_argument('--name', required=True)
    parser.add_argument('--weights')
    parser.add_argument('--how', choices=('mean', 'median'), default='mean')
    parser.add_argument('--snapshot', type=Path, default=evaluate.DEFAULT_SNAPSHOT)
    parser.add_argument('--out', type=Path, default=OUT)
    args = parser.parse_args(argv)
    print(f'결과: {run(args)}')
    return 0


if __name__ == '__main__':
    sys.exit(main())
