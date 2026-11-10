"""XGBoost 1차 튜닝(기준서 §6). 튜닝 목록(origins_tune)만 쓰고, 시도마다 tuning_log에 한 줄 남긴다.

    uv run --extra prices python -m model_comparison.xgboost.tune                 # 최대 40회 / 누적 3시간
    uv run --extra prices python -m model_comparison.xgboost.tune --trials 5     # 시험 삼아 몇 번만(기록은 이어짐)
    uv run --extra prices python -m model_comparison.xgboost.tune --seeds         # 상위 3개 설정 시드 42·43·44 재현

- 1회째는 v5 기본값(config.json). 이후 Optuna TPE(시드 42)로 고른다. 중단 후 다시 실행하면 기록을 읽어 이어 간다.
- 결과 폴더는 runs/(Git 제외), 기록은 runs/xgb-p1-tuning.csv, 최고 설정은 model_comparison/xgboost/config_p1.json
- 선택 지표: 튜닝 목록의 policy macro MAPE
"""
import argparse
import json
import sys
from pathlib import Path

from tools import run_backtest, standard

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
RUNS = ROOT / 'runs'
LOG = RUNS / 'xgb-p1-tuning.csv'
BEST = HERE / 'config_p1.json'
BUDGET = standard.TUNING_BUDGET['p1']


def base_config():
    return json.loads((HERE / 'config.json').read_text(encoding='utf-8'))


def space(trial):
    objective = trial.suggest_categorical('objective', ['reg:pseudohubererror', 'reg:squarederror'])
    params = {
        'n_estimators': trial.suggest_int('n_estimators', 30, 300, log=True),
        'max_depth': trial.suggest_int('max_depth', 2, 6),
        'learning_rate': trial.suggest_float('learning_rate', 0.01, 0.2, log=True),
        'min_child_weight': trial.suggest_float('min_child_weight', 1, 100, log=True),
        'reg_lambda': trial.suggest_float('reg_lambda', 0.1, 100, log=True),
        'subsample': trial.suggest_float('subsample', 0.6, 1.0),
        'colsample_bytree': trial.suggest_float('colsample_bytree', 0.5, 1.0),
        'objective': objective,
    }
    if objective == 'reg:pseudohubererror':
        params['huber_slope'] = trial.suggest_float('huber_slope', 0.005, 0.1, log=True)
    return params


def run_once(config, args, record=True, seed=None):
    """설정 하나로 튜닝 목록 전체 백테스트 → (policy macro MAPE, 결과 폴더)."""
    config = {**config, 'seed': seed if seed is not None else config['seed']}
    path = RUNS / 'xgb-tune-configs' / f'{run_backtest.config_id(config)}-s{config["seed"]}.json'
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(config, ensure_ascii=False, indent=2), encoding='utf-8')
    argv = ['--config', str(path), '--phase', 'p1', '--origins', 'tune', '--out', str(RUNS)]
    if args.snapshot:
        argv += ['--snapshot', str(args.snapshot)]
    if record:
        argv += ['--record-trial', str(LOG)]
    before = {p for p in RUNS.glob('xgb-p1-*') if p.is_dir()}
    if run_backtest.main(argv) != 0:
        return None, None
    folder = max({p for p in RUNS.glob('xgb-p1-*') if p.is_dir()} - before, key=lambda p: p.stat().st_mtime)
    metrics = json.loads((folder / 'metrics.json').read_text(encoding='utf-8'))
    return metrics['results']['policy']['macro_mape'], folder


def logged():
    if not LOG.exists():
        return []
    trials, _ = run_backtest.tuning_summary(LOG)
    return trials


def tune(args):
    import optuna

    optuna.logging.set_verbosity(optuna.logging.WARNING)
    base = base_config()
    sampler = optuna.samplers.TPESampler(seed=42, n_startup_trials=8)
    study = optuna.create_study(direction='minimize', sampler=sampler)
    done = logged()
    seconds = sum(float(t['seconds'] or 0) for t in done)
    # 이미 한 시도를 학습기에 다시 알려 준다(이어 하기)
    for t in done:
        params = json.loads(t['params'])
        dist = {k: v for k, v in params.items() if k not in ('tree_method', 'n_jobs')}
        if t['macro_mape'] and t['status'] == 'OK':
            try:
                study.enqueue_trial(dist, skip_if_exists=True)
                trial = study.ask()
                space(trial)
                study.tell(trial, float(t['macro_mape']))
            except (ValueError, KeyError):
                pass
    limit = min(BUDGET['trials'], len(done) + args.trials) if args.trials else BUDGET['trials']
    print(f'기록된 시도 {len(done)}회, 누적 {seconds / 60:.1f}분. 이번 목표 {limit}회까지(상한 {BUDGET["trials"]}회·{BUDGET["seconds"] // 3600}시간)')
    while len(logged()) < limit:
        if seconds >= BUDGET['seconds']:
            print('누적 시간 상한 도달 — 멈춤')
            break
        if not logged():
            params = base['params']
            trial = None
        else:
            trial = study.ask()
            params = {**space(trial), 'tree_method': 'hist', 'n_jobs': standard.THREADS}
        config = {**base, 'params': params}
        mape, _ = run_once(config, args)
        if trial is not None:
            study.tell(trial, mape if mape is not None else float('inf'))
        seconds = sum(float(t['seconds'] or 0) for t in logged())
        best = min((t for t in logged() if t['macro_mape']), key=lambda t: float(t['macro_mape']))
        print(f'== 시도 {len(logged())}: {mape} / 최고 {best["macro_mape"]} (시도 {best["trial"]})')
    write_best()


def write_best():
    trials = [t for t in logged() if t['macro_mape'] and t['status'] == 'OK']
    if not trials:
        return
    best = min(trials, key=lambda t: float(t['macro_mape']))
    config = {**base_config(), 'params': json.loads(best['params'])}
    BEST.write_text(json.dumps(config, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(f'최고 설정(시도 {best["trial"]}, policy macro MAPE {best["macro_mape"]}) → {BEST}')


def seeds(args):
    """상위 3개 설정을 시드 42·43·44로 다시 돌려 평균·편차(§6). 튜닝 시도로 세지 않고 기록도 따로 둔다."""
    import statistics

    trials = sorted((t for t in logged() if t['macro_mape'] and t['status'] == 'OK'),
                    key=lambda t: float(t['macro_mape']))[:3]
    report = []
    for t in trials:
        config = {**base_config(), 'params': json.loads(t['params'])}
        values = [float(t['macro_mape']) if s == 42 else run_once(config, args, record=False, seed=s)[0]
                  for s in standard.REPEAT_SEEDS]
        report.append({'trial': t['trial'], 'config_id': t['config_id'], 'macro_mape_by_seed': values,
                       'mean': statistics.mean(values), 'stdev': statistics.pstdev(values)})
        print(f'시도 {t["trial"]}: {values} → 평균 {report[-1]["mean"]:.4f}, 편차 {report[-1]["stdev"]:.4f}')
    (RUNS / 'xgb-p1-seeds.json').write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding='utf-8')


def main(argv=None):
    parser = argparse.ArgumentParser(description='XGBoost 1차 튜닝')
    parser.add_argument('--trials', type=int, help='이번에 더 할 시도 수(기본: 상한까지)')
    parser.add_argument('--seeds', action='store_true', help='상위 3개 설정 시드 재현')
    parser.add_argument('--snapshot', type=Path)
    args = parser.parse_args(argv)
    RUNS.mkdir(exist_ok=True)
    seeds(args) if args.seeds else tune(args)
    return 0


if __name__ == '__main__':
    sys.exit(main())
