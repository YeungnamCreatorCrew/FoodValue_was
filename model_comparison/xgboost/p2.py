"""XGBoost 2차 비교(p2, 기준서 §5.2). 1차 설정(config_p1.json)의 params를 고정하고 외부변수 묶음을 하나씩 더한다.

    uv run --extra prices python -m model_comparison.xgboost.p2

1. 묶음 5개(MARKET, NATIONAL_WEATHER, EVENT, MACRO, PRODUCTION)를 하나씩 붙여 검증 전체를 실행
2. 1차 결과보다 policy macro MAPE가 낮아진 묶음이 2개 이상이면 그 묶음 전체로 1번 더 실행
각 실행 결과는 experiments/xgb-p2-…/ (제출 대상), 요약은 runs/xgb-p2-summary.json.
이미 같은 설정으로 끝난 실행이 experiments/에 있으면 건너뛴다(중단 후 다시 실행해도 됨).
"""
import argparse
import json
import sys
from pathlib import Path

from tools import run_backtest, standard

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
EXPERIMENTS = ROOT / 'experiments'
RUNS = ROOT / 'runs'


def p1_result():
    folders = sorted(EXPERIMENTS.glob('xgb-p1-*'))
    if not folders:
        raise SystemExit('experiments/xgb-p1-…가 없음. 1차 결과를 먼저 받아 오세요(git pull)')
    metrics = json.loads((folders[-1] / 'metrics.json').read_text(encoding='utf-8'))
    return folders[-1].name, metrics['results']['policy']['macro_mape']


def done_runs():
    """(config_id, month) → (폴더, policy macro MAPE). 점검 실행(--month)과 검증 전체 실행을 구분한다."""
    out = {}
    for folder in EXPERIMENTS.glob('xgb-p2-*'):
        try:
            config = json.loads((folder / 'config.json').read_text(encoding='utf-8'))
            metrics = json.loads((folder / 'metrics.json').read_text(encoding='utf-8'))
        except (OSError, ValueError):
            continue
        out[config['config_id'], config.get('month')] = (folder.name, metrics['results']['policy']['macro_mape'])
    return out


def run_bundles(base, bundles, args):
    ordered = [b for b in standard.EXTRA_BUNDLES if b in bundles]
    config = {**base, 'extra_features': ordered, 'feature_set': '+'.join([standard.BASE_FEATURE_SET, *ordered])}
    key = (run_backtest.config_id(config), args.month)
    done = done_runs()
    if key in done:
        print(f'건너뜀(이미 있음): {"+".join(ordered)} → {done[key][0]}')
        return done[key]
    path = RUNS / 'xgb-p2-configs' / f'{"+".join(ordered)}.json'
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(config, ensure_ascii=False, indent=2), encoding='utf-8')
    argv = ['--config', str(path), '--phase', 'p2']
    if args.snapshot:
        argv += ['--snapshot', str(args.snapshot)]
    if args.month:
        argv += ['--month', args.month]
    if run_backtest.main(argv) != 0:
        return None, None
    return done_runs().get(key, (None, None))


def main(argv=None):
    parser = argparse.ArgumentParser(description='XGBoost 2차 비교')
    parser.add_argument('--snapshot', type=Path)
    parser.add_argument('--month', help='점검용: 그 달 기준일만(제출에는 쓰지 않음)')
    args = parser.parse_args(argv)
    base = json.loads((HERE / 'config_p1.json').read_text(encoding='utf-8'))
    p1_name, p1_mape = p1_result()
    print(f'1차 결과 {p1_name}: policy macro MAPE {p1_mape}')
    results = {}
    for bundle in standard.EXTRA_BUNDLES:
        results[bundle] = run_bundles(base, [bundle], args)
    if args.month:  # 점검 실행은 기준일이 달라 1차와 비교할 수 없다
        print('점검 실행(--month): 1차와 비교하지 않음')
        return 0
    helpful = [b for b, (_, mape) in results.items() if mape is not None and mape < p1_mape]
    combined = None
    if len(helpful) >= 2:
        combined = ('+'.join(helpful), *run_bundles(base, helpful, args))
    summary = {'p1': {'experiment': p1_name, 'macro_mape': p1_mape},
               'single': {b: {'experiment': e, 'macro_mape': m, 'delta_vs_p1': None if m is None else round(p1_mape - m, 6)}
                          for b, (e, m) in results.items()},
               'helpful': helpful,
               'combined': None if combined is None else {'bundles': combined[0], 'experiment': combined[1],
                                                          'macro_mape': combined[2]}}
    RUNS.mkdir(exist_ok=True)
    (RUNS / 'xgb-p2-summary.json').write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding='utf-8')
    print(f'\n1차 {p1_mape:.4f}%')
    for bundle, (exp, mape) in results.items():
        mark = ' ← 효과 있음' if bundle in helpful else ''
        print(f'  + {bundle:17} {mape if mape is None else f"{mape:.4f}%"}  {exp}{mark}')
    if combined:
        print(f'  + {combined[0]} {combined[2]:.4f}%  {combined[1]}')
    elif len(helpful) < 2:
        print('  효과 있던 묶음이 2개 미만이라 묶음 전체 실행은 생략')
    return 0


if __name__ == '__main__':
    sys.exit(main())
