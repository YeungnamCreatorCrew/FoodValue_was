"""공통 평가기(기준서 §8). 정답·naive·mean7은 여기서만 결합한다(모델 제출 파일에는 넣지 않음).

    # 실험 하나: metrics.json 생성(run_backtest가 끝에 자동 실행)
    uv run --extra prices python -m tools.evaluate experiments/xgb-p1-20261116-01

    # 여러 모델 비교: 세 결과(policy·model_only·common_success)와 순위·채택 조건 표
    uv run --extra prices python -m tools.evaluate --compare experiments/xgb-p1-... experiments/lgbm-p1-... --out comparison.json

metrics.json에는 장비마다 다른 값(시간·메모리·실행일)을 넣지 않는다. 그래서 같은 설정이면 4명의 파일이 바이트 단위로 같고
(단계 0 점검), 마지막 줄의 metrics SHA-256으로 대조할 수 있다. 자원(학습 시간·메모리)은 run.log에 있다.
"""
import argparse
import csv
import hashlib
import json
import math
import sys
from collections import defaultdict
from datetime import date
from itertools import pairwise
from pathlib import Path

from tools import loader, standard
from tools.validate_experiment import round_half_up

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_SNAPSHOT = ROOT / 'data' / 'snapshots' / standard.DATA_VERSION
METRICS = 'metrics.json'


def r6(value):
    return None if value is None or (isinstance(value, float) and math.isnan(value)) else round(float(value), 6)


def read_predictions(folder: Path):
    with open(folder / 'predictions.csv', encoding='utf-8', newline='') as f:
        return list(csv.DictReader(f))


def points_for(rows, snap: loader.Snapshot):
    """공통 평가 대상(§8.1): 목표일 실제 가격이 있고 naive가 계산되는 (계열, 기준일, 시점)."""
    points = []
    for r in rows:
        sid, d, h = int(r['series_id']), date.fromisoformat(r['origin_date']), int(r['horizon'])
        target = date.fromisoformat(r['target_date'])
        y, naive = snap.actual_price(sid, target), snap.naive(sid, d)
        if y is None or naive is None:
            continue
        mean7 = snap.mean7(sid, d)
        kind_origin, kind_target = snap.kind_at(sid, d), snap.kind_at(sid, target)
        points.append({
            'key': (sid, d, h), 'series_id': sid, 'market': snap.series[sid].market, 'origin': d, 'horizon': h,
            'season': standard.SEASONS[target.month], 'y': y, 'naive': float(round_half_up(naive)),
            'mean7': None if mean7 is None else float(round_half_up(mean7)),
            'ok': r['status'] == 'OK', 'pred': float(r['predicted_price']) if r['status'] == 'OK' else None,
            'kind_cross': None if kind_origin is None else int(kind_origin != kind_target),
        })
    return points


def _ape(y, yhat):
    return abs(y - yhat) / y * 100


def summarize(points, predict):
    """predict(point) → 예측값(None이면 그 점 제외). 계열별 지표와 macro·micro."""
    per = defaultdict(lambda: {'n': 0, 'ape': 0.0, 'ae': 0.0, 'naive_ape': 0.0, 'naive_ae': 0.0})
    micro, micro_naive, count = 0.0, 0.0, 0
    for p in points:
        yhat = predict(p)
        if yhat is None:
            continue
        s = per[p['series_id']]
        s['n'] += 1
        s['ape'] += _ape(p['y'], yhat)
        s['ae'] += abs(p['y'] - yhat)
        s['naive_ape'] += _ape(p['y'], p['naive'])
        s['naive_ae'] += abs(p['y'] - p['naive'])
        micro += _ape(p['y'], yhat)
        micro_naive += _ape(p['y'], p['naive'])
        count += 1
    series = {}
    for sid in sorted(per):
        s = per[sid]
        mape, naive_mape = s['ape'] / s['n'], s['naive_ape'] / s['n']
        mae, naive_mae = s['ae'] / s['n'], s['naive_ae'] / s['n']
        series[str(sid)] = {
            'points': s['n'], 'mape': r6(mape), 'mae': r6(mae), 'naive_mape': r6(naive_mape), 'naive_mae': r6(naive_mae),
            'rmae': r6(mae / naive_mae) if naive_mae > 0 else None,
            'relative_improvement_pct': r6((naive_mape - mape) / naive_mape * 100) if naive_mape > 0 else None,
            'win': mape < naive_mape,
        }
    if not series:
        return {'series_count': 0, 'points': 0}
    mapes = [v['mape'] for v in series.values()]
    naive_mapes = [v['naive_mape'] for v in series.values()]
    rmaes = [v['rmae'] for v in series.values() if v['rmae'] is not None]
    macro, naive_macro = sum(mapes) / len(mapes), sum(naive_mapes) / len(naive_mapes)
    return {
        'series_count': len(series), 'points': count,
        'macro_mape': r6(macro), 'naive_macro_mape': r6(naive_macro),
        'micro_mape': r6(micro / count), 'naive_micro_mape': r6(micro_naive / count),
        'relative_improvement_pct': r6((naive_macro - macro) / naive_macro * 100) if naive_macro > 0 else None,
        'macro_rmae': r6(sum(rmaes) / len(rmaes)) if rmaes else None,
        'rmae_null_series': [sid for sid, v in series.items() if v['rmae'] is None],
        'series_wins': sum(v['win'] for v in series.values()),
        'series': series,
    }


def breakdown(points, predict, key):
    groups = defaultdict(list)
    for p in points:
        if p[key] is not None:
            groups[p[key]].append(p)
    out = {}
    for name in sorted(groups, key=str):
        s = summarize(groups[name], predict)
        out[str(name)] = {k: s.get(k) for k in ('series_count', 'points', 'macro_mape', 'naive_macro_mape',
                                                 'relative_improvement_pct')}
    return out


def bootstrap(points, predict):
    """기준일 월 블록 부트스트랩(§8.3). Δ = naive macro MAPE − 모델 macro MAPE(양수면 모델이 좋음)."""
    import numpy as np
    usable = [p for p in points if predict(p) is not None]
    months = sorted({p['origin'].strftime('%Y-%m') for p in usable})
    series = sorted({p['series_id'] for p in usable})
    if not months:
        return None
    m_index, s_index = {m: i for i, m in enumerate(months)}, {s: i for i, s in enumerate(series)}
    shape = (len(months), len(series))
    model, naive, count = np.zeros(shape), np.zeros(shape), np.zeros(shape)
    for p in usable:
        i, j = m_index[p['origin'].strftime('%Y-%m')], s_index[p['series_id']]
        model[i, j] += _ape(p['y'], predict(p))
        naive[i, j] += _ape(p['y'], p['naive'])
        count[i, j] += 1
    rng = np.random.default_rng(standard.BOOTSTRAP['seed'])
    deltas = []
    for _ in range(standard.BOOTSTRAP['iterations']):
        weight = np.bincount(rng.integers(0, len(months), len(months)), minlength=len(months)).astype(float)
        n = weight @ count
        has = n > 0
        if not has.any():
            continue
        delta = ((weight @ naive)[has] / n[has]).mean() - ((weight @ model)[has] / n[has]).mean()
        deltas.append(delta)
    low, high = np.percentile(deltas, [2.5, 97.5])
    point = summarize(usable, predict)
    return {'iterations': standard.BOOTSTRAP['iterations'], 'seed': standard.BOOTSTRAP['seed'], 'blocks': len(months),
            'delta': r6(point['naive_macro_mape'] - point['macro_mape']), 'ci_low': r6(low), 'ci_high': r6(high)}


def result(points, predict, with_bootstrap=True):
    out = summarize(points, predict)
    if not out.get('points'):
        return out
    out['by_market'] = breakdown(points, predict, 'market')
    out['by_season'] = breakdown(points, predict, 'season')
    out['by_horizon'] = breakdown(points, predict, 'horizon')
    out['by_kind_cross'] = breakdown(points, predict, 'kind_cross')
    if with_bootstrap:
        out['bootstrap'] = bootstrap(points, predict)
    return out


def adoption(policy, success_rate, n):
    """검증 관문 조건 1~5(§8.4). 6(자원)은 최종 시험 Docker 실행 값으로 따로 본다."""
    boot = policy.get('bootstrap') or {}
    checks = {
        '1_relative_improvement_ge_5pct': (policy.get('relative_improvement_pct') or -1e9)
        >= standard.ADOPTION['min_relative_improvement_pct'],
        '2_macro_rmae_lt_1': policy.get('macro_rmae') is not None and policy['macro_rmae'] < standard.ADOPTION['max_macro_rmae'],
        '3_series_wins_majority': policy.get('series_wins', 0) >= standard.majority(n),
        '4_success_rate_ge_99pct': success_rate >= standard.ADOPTION['min_success_rate'],
        '5_bootstrap_ci_low_gt_0': boot.get('ci_low') is not None and boot['ci_low'] > 0,
    }
    return {'checks': checks, 'validation_gate_passed': all(checks.values()),
            'majority_required': standard.majority(n), 'note': '6(자원)은 최종 시험 Docker 실행 값으로 판단'}


def evaluate(folder: Path, snap: loader.Snapshot) -> dict:
    config = json.loads((folder / 'config.json').read_text(encoding='utf-8'))
    rows = read_predictions(folder)
    points = points_for(rows, snap)
    ok = sum(p['ok'] for p in points)
    success_rate = ok / len(points) if points else 0.0
    n = len({int(r['series_id']) for r in rows})
    policy = result(points, lambda p: p['pred'] if p['ok'] else p['naive'])
    status_counts = defaultdict(int)
    for r in rows:
        status_counts[r['status']] += 1
    return {
        'standard_version': standard.STANDARD_VERSION, 'data_version': config.get('data_version'),
        'model': config.get('model'), 'config_id': config.get('config_id'), 'phase': config.get('phase'),
        'origin_list': config.get('origin_list'), 'month': config.get('month'),
        'series_count': n, 'prediction_rows': len(rows), 'status_counts': dict(sorted(status_counts.items())),
        'evaluated_points': len(points), 'success_rate': r6(success_rate),
        'results': {
            'policy': policy,
            'model_only': result(points, lambda p: p['pred'] if p['ok'] else None, with_bootstrap=False),
            'common_success': None,  # 여러 모델을 함께 봐야 정해짐: evaluate --compare
        },
        'baselines': {
            'naive': summarize(points, lambda p: p['naive']) | {'series': None},
            'mean7': summarize(points, lambda p: p['mean7']) | {'series': None},
        },
        'adoption': adoption(policy, success_rate, n),
    }


def write_metrics(folder: Path, snap: loader.Snapshot) -> tuple[dict, str]:
    metrics = evaluate(folder, snap)
    path = folder / METRICS
    with open(path, 'w', encoding='utf-8', newline='\n') as f:
        json.dump(metrics, f, ensure_ascii=False, indent=2, sort_keys=True)
        f.write('\n')
    return metrics, hashlib.sha256(path.read_bytes()).hexdigest()


def compare(folders, snap: loader.Snapshot) -> dict:
    """여러 실험의 세 결과. common_success = 비교하는 모든 모델이 성공한 점만(§8.2)."""
    loaded = {}
    for folder in folders:
        config = json.loads((folder / 'config.json').read_text(encoding='utf-8'))
        points = {p['key']: p for p in points_for(read_predictions(folder), snap)}
        loaded[config['experiment_id']] = (config, points)
    key_sets = [set(points) for _, points in loaded.values()]
    if any(keys != key_sets[0] for keys in key_sets):
        raise SystemExit('실험들의 평가 대상(계열·기준일·시점)이 다름. 같은 기준일 목록·계열로 실행한 결과만 비교할 수 있음')
    common = {k for k in key_sets[0] if all(points[k]['ok'] for _, points in loaded.values())}
    out = {}
    for exp_id, (config, points) in loaded.items():
        values = list(points.values())
        ok = sum(p['ok'] for p in values)
        n = len({p['series_id'] for p in values})
        policy = result(values, lambda p: p['pred'] if p['ok'] else p['naive'])
        out[exp_id] = {
            'model': config.get('model'), 'config_id': config.get('config_id'),
            'success_rate': r6(ok / len(values)),
            'policy': policy,
            'model_only': result(values, lambda p: p['pred'] if p['ok'] else None, with_bootstrap=False),
            'common_success': result([p for p in values if p['key'] in common], lambda p: p['pred'], with_bootstrap=False),
            'adoption': adoption(policy, ok / len(values), n),
        }
    ranking = sorted(out, key=lambda e: out[e]['policy']['macro_mape'])
    ties = []
    for a, b in pairwise(ranking):
        ma, mb = out[a]['policy']['macro_mape'], out[b]['policy']['macro_mape']
        if abs(ma - mb) / min(ma, mb) < standard.ADOPTION['tie_relative']:
            ties.append([a, b])
    return {'common_points': len(common), 'ranking_policy_macro_mape': ranking, 'ties_within_2pct': ties,
            'simplicity_order': list(standard.SIMPLICITY_ORDER), 'experiments': out}


def print_metrics(metrics, digest=None):
    p = metrics['results']['policy']
    print(f'평가 점 {metrics["evaluated_points"]}개, 성공률 {metrics["success_rate"]:.2%}, 계열 {metrics["series_count"]}개')
    if p.get('points'):
        boot = p.get('bootstrap') or {}
        print(f'policy macro MAPE {p["macro_mape"]:.4f}% (naive {p["naive_macro_mape"]:.4f}%) '
              f'개선 {p["relative_improvement_pct"]:+.2f}%  rMAE {p["macro_rmae"]}  승 {p["series_wins"]}/{p["series_count"]}'
              f'  Δ 95% [{boot.get("ci_low")}, {boot.get("ci_high")}]')
        for sid, s in p['series'].items():
            print(f'  {sid:>5} MAPE {s["mape"]:.3f}% (naive {s["naive_mape"]:.3f}%) 개선 {s["relative_improvement_pct"]}')
    checks = metrics['adoption']['checks']
    print('검증 관문: ' + ' '.join(f'{k.split("_")[0]}{"O" if v else "X"}' for k, v in checks.items()))
    if digest:
        print(f'metrics SHA-256 {digest}')


def main(argv=None):
    parser = argparse.ArgumentParser(description='공통 평가기(기준서 §8)')
    parser.add_argument('folders', nargs='*', type=Path)
    parser.add_argument('--compare', nargs='+', type=Path, help='여러 실험 폴더 비교')
    parser.add_argument('--snapshot', type=Path, default=DEFAULT_SNAPSHOT)
    parser.add_argument('--out', type=Path, help='--compare 결과 JSON 경로')
    args = parser.parse_args(argv)
    snap = loader.Snapshot(args.snapshot)
    if args.compare:
        result_ = compare(args.compare, snap)
        print(f'공통 성공 점 {result_["common_points"]}개')
        for exp_id in result_['ranking_policy_macro_mape']:
            e = result_['experiments'][exp_id]
            print(f'  {exp_id:30} policy {e["policy"]["macro_mape"]:.4f}%  model_only {e["model_only"]["macro_mape"]:.4f}%  '
                  f'common {e["common_success"].get("macro_mape")}  성공률 {e["success_rate"]:.2%}  '
                  f'관문 {"통과" if e["adoption"]["validation_gate_passed"] else "미달"}')
        if result_['ties_within_2pct']:
            print(f'  동률(상대 2% 미만): {result_["ties_within_2pct"]} → 더 단순한 모델 우선 {standard.SIMPLICITY_ORDER}')
        if args.out:
            args.out.write_text(json.dumps(result_, ensure_ascii=False, indent=2, sort_keys=True) + '\n', encoding='utf-8')
        return 0
    if not args.folders:
        parser.error('실험 폴더를 주거나 --compare를 쓰세요')
    for folder in args.folders:
        metrics, digest = write_metrics(folder, snap)
        print(f'[{folder.name}]')
        print_metrics(metrics, digest)
    return 0


if __name__ == '__main__':
    sys.exit(main())
