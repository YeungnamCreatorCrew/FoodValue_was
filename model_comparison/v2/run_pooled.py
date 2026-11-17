"""v2 통합 학습 실행기. v1 실행기(run_backtest)와 같은 기준일·주 1회 재학습·후처리·평가기를 쓰고,
계열마다 따로가 아니라 **10개 계열 표본을 한 모델이** 학습한다.

    uv run --extra prices python -m model_comparison.v2.run_pooled --config model_comparison/v2/configs/all.json
    uv run --extra prices python -m model_comparison.v2.run_pooled --config ... --origins tune      # 빠른 비교
    uv run --extra prices python -m model_comparison.v2.run_pooled --config ... --month 2025-01     # 점검

설정(JSON): {"name": "all", "class": "model_comparison.v2.models:PooledXGB", "params": {...},
             "bundles": ["MARKET", ...], "blocks": ["ORIGIN_WEATHER", ...], "window_days": 1825, "seed": 42}
결과: experiments_v2/<name>-<origins>-YYYYMMDD-NN/ (config.json, predictions.csv, metrics.json, run.log,
      environment.txt, importance.json). metrics.json은 v1과 같은 평가기라 v1 결과와 바로 비교된다.
최종 시험 기준일(test)은 쓰지 않는다(v2는 검증 구간까지만, 최종 시험은 팀 합의 후).
"""
from tools.runtime import apply_environment

_CHANGED_ENV = apply_environment()

import argparse
import inspect
import csv
import json
import sys
import time
from datetime import date, timedelta
from pathlib import Path

import numpy as np

from model_comparison.v2 import features as F
from model_comparison.v2.snapshot import EXTRA_DIR
from tools import evaluate, loader, origins, run_backtest, standard

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / 'experiments_v2'


class Matrices:
    """계열 × 시점별 전체 특징 행렬(행 i = 기준일 start+i)을 한 번만 만든다."""

    def __init__(self, snap, v2, bundles, blocks):
        self.snap, self.names = snap, F.feature_names(bundles, blocks)
        self.by = {}
        for sid, s in snap.series.items():
            idx = np.arange(len(s.actual) - max(standard.HORIZONS))
            for h in standard.HORIZONS:
                self.by[sid, h] = F.rows(snap, v2, sid, idx, np.full(idx.size, h), bundles, blocks).astype(np.float32)

    def training(self, sid, as_of_idx, window_days):
        """loader.training_data와 같은 규칙(창·목표일 ≤ as_of·실제 관측·v[o-28..o] 결측 없음), 창 길이만 설정값."""
        s = self.snap.series[sid]
        start = max(0, as_of_idx - window_days + 1)
        observed = int((~np.isnan(s.actual[start:as_of_idx + 1])).sum())
        if observed < standard.MIN_TRAIN_OBSERVATIONS:
            return None
        first = start + standard.FEATURE_LOOKBACK_DAYS
        xs, ys, hs, ages = [], [], [], []
        for h in standard.HORIZONS:
            o = np.arange(first, as_of_idx - h + 1)
            o = o[s.valid[o] & ~np.isnan(s.actual[o + h])]
            xs.append(self.by[sid, h][o])
            ys.append(s.actual[o + h])
            hs.append(np.full(o.size, h))
            ages.append(as_of_idx - (o + h))  # 목표일이 학습 시점보다 며칠 앞인지(최근 가중용)
        n = sum(len(y) for y in ys)
        return (np.concatenate(xs), np.concatenate(ys), np.concatenate(hs), np.full(n, sid),
                np.concatenate(ages).astype(float))

    def inputs(self, sid, i):
        s = self.snap.series[sid]
        if i < 0 or i >= len(s.age) or s.age[i] > standard.MAX_STALE_DAYS or not s.valid[i]:
            return None
        return np.stack([self.by[sid, h][i] for h in standard.HORIZONS])


def run(args):
    config = json.loads(Path(args.config).read_text(encoding='utf-8'))
    bundles = loader.check_bundles(config.get('bundles', []))
    blocks = [b for b in F.V2_BLOCKS if b in config.get('blocks', [])]
    unknown = set(config.get('blocks', [])) - set(F.V2_BLOCKS)
    if unknown:
        raise SystemExit(f'모르는 v2 묶음: {sorted(unknown)}')
    window = int(config.get('window_days', standard.TRAIN_WINDOW_DAYS))
    snap = loader.Snapshot(args.snapshot)
    if args.origins == 'test':
        raise SystemExit('v2는 최종 시험 기준일을 쓰지 않음(팀 합의 후 별도 진행)')
    days = snap.origins[args.origins]
    if args.month:
        days = [d for d in days if d.strftime('%Y-%m') == args.month]
    origins.guard('p2', days)
    series_ids = [int(x) for x in args.series.split(',')] if args.series else snap.series_ids
    v2 = F.V2Features(snap, args.extra)
    cls = run_backtest.load_class(config['class'])
    params = config.get('params', {})
    fit_takes_groups = 'groups' in inspect.signature(cls.fit).parameters  # 계열·최근 가중을 받는 모델만

    stamp = date.today().strftime('%Y%m%d')
    base = f'{config["name"]}-{args.origins}{"-" + args.month if args.month else ""}-{stamp}'
    folder = next(Path(args.out) / f'{base}-{n:02d}' for n in range(1, 100) if not (Path(args.out) / f'{base}-{n:02d}').exists())
    folder.mkdir(parents=True)
    record = {**config, 'experiment_id': folder.name, 'data_version': standard.DATA_VERSION,
              'v2_extra': (json.loads((Path(args.extra) / 'manifest.json').read_text(encoding='utf-8'))
                           if any(b in F.NEEDS_EXTRA for b in blocks) else None),
              'origin_list': args.origins, 'month': args.month, 'series': series_ids, 'phase': 'v2',
              'git_sha': run_backtest.git('rev-parse', 'HEAD') or None, 'refit': standard.REFIT,
              'model': config.get('model', 'XGBoost'), 'feature_count': len(F.feature_names(bundles, blocks))}
    record['config_id'] = run_backtest.config_id({**record, 'extra_features': [*bundles, *blocks],
                                                  'feature_set': f'v2:{window}'})
    (folder / 'config.json').write_text(json.dumps(record, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    (folder / 'environment.txt').write_text(run_backtest.environment_text('local'), encoding='utf-8')
    log_file = open(folder / 'run.log', 'w', encoding='utf-8')  # noqa: SIM115

    def log(message):
        print(message)
        log_file.write(message + '\n')
        log_file.flush()

    started = time.perf_counter()
    mats = Matrices(snap, v2, bundles, blocks)
    log(f'{folder.name} 특징 {len(mats.names)}개, 창 {window}일, 기준일 {len(days)}개 × 계열 {len(series_ids)}개 '
        f'(특징 준비 {time.perf_counter() - started:.0f}s)')
    results = {sid: [] for sid in series_ids}
    model, week, fit_seconds, importance = None, None, 0.0, None
    for d in days:
        if d.isocalendar()[:2] != week:
            week = d.isocalendar()[:2]
            t0 = time.perf_counter()
            parts = [mats.training(sid, snap.series[sid].index(d), window) for sid in snap.series_ids]
            parts = [p for p in parts if p is not None]
            model = None
            if parts:
                X, y, h, g, age = (np.concatenate([p[k] for p in parts]) for k in range(5))
                model = cls(**params)
                try:
                    if fit_takes_groups:
                        model.fit(X, y, h, mats.names, config.get('seed', 42), groups=g, ages=age)
                    else:
                        model.fit(X, y, h, mats.names, config.get('seed', 42))
                except Exception as error:  # noqa: BLE001
                    log(f'  {d} 재학습 실패: {type(error).__name__}: {error}')
                    model = None
            fit_seconds += time.perf_counter() - t0
            log(f'  {d} 재학습 표본 {sum(len(p[1]) for p in parts)}개 {time.perf_counter() - t0:.1f}s')
        for sid in series_ids:
            x = mats.inputs(sid, snap.series[sid].index(d))
            if model is None:
                rows = run_backtest.prediction_rows(None, 'FIT_FAILED', 'NOT_FITTED')
            elif x is None:
                rows = run_backtest.prediction_rows(None, 'NO_INPUT', 'STALE_OR_GAP')
            else:
                values = model.predict(x, np.array(standard.HORIZONS))
                rows = run_backtest.prediction_rows([None if np.isnan(v) else float(v) for v in values], 'OK', '')
            results[sid].append((d, rows))
    if model is not None and hasattr(model, 'importance'):
        importance = model.importance()
    with open(folder / 'predictions.csv', 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f, lineterminator='\n')
        writer.writerow(standard.PREDICTION_COLUMNS)
        for sid in series_ids:
            s = snap.series[sid]
            for d, rows in results[sid]:
                for h, (raw, price, status, error) in zip(standard.HORIZONS, rows):
                    writer.writerow([folder.name, record['model'], record['config_id'], standard.DATA_VERSION, sid,
                                     s.item, s.market, d.isoformat(), (d + timedelta(days=h)).isoformat(), h, raw,
                                     price, status, error])
    if importance:
        (folder / 'importance.json').write_text(json.dumps(importance, ensure_ascii=False, indent=1), encoding='utf-8')
    log(f'RESOURCES {json.dumps({"total_seconds": round(time.perf_counter() - started, 1), "fit_seconds": round(fit_seconds, 1), "peak_memory_mb": run_backtest.peak_memory_mb()})}')
    metrics, digest = evaluate.write_metrics(folder, snap)
    evaluate.print_metrics(metrics)
    log(f'metrics SHA-256 {digest}')
    if importance:
        groups = {}
        for name, value in importance.items():
            key = name.split('_')[0] if name.startswith(('ow_', 'wa_', 'garak', 'cross', 'is_')) else 'v1'
            groups[key] = groups.get(key, 0) + value
        total = sum(groups.values()) or 1
        log('특징 묶음별 중요도(마지막 재학습): ' + ', '.join(f'{k} {v / total:.0%}' for k, v in
                                                     sorted(groups.items(), key=lambda kv: -kv[1])))
    log_file.close()
    return folder


def main(argv=None):
    parser = argparse.ArgumentParser(description='v2 통합 학습 실행기')
    parser.add_argument('--config', required=True, type=Path)
    parser.add_argument('--origins', choices=('tune', 'validation'), default='validation')
    parser.add_argument('--month')
    parser.add_argument('--series', help='예측할 계열(학습은 항상 10개 계열 전체)')
    parser.add_argument('--snapshot', type=Path, default=evaluate.DEFAULT_SNAPSHOT)
    parser.add_argument('--extra', type=Path, default=EXTRA_DIR)
    parser.add_argument('--out', type=Path, default=OUT)
    args = parser.parse_args(argv)
    folder = run(args)
    print(f'결과: {folder}')
    return 0


if __name__ == '__main__':
    sys.exit(main())
