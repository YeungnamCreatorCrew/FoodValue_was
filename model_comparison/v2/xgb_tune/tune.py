"""v2 XGBoost(Huber + inv_scale) 구성원 튜닝 — LightGBM 기본값과의 앙상블 MAPE로 판단(튜닝 기준일).

    uv run --extra prices python -m model_comparison.v2.xgb_tune.tune

실제 실행(2026-11-18~19, Windows PC)은 1단계 20개 + combo = 21회에서 멈췄다(2단계는 시작 직후 중단, 결과 없음).
2단계 목록은 기록용으로 남겨 둔다. 시도별 결과는 같은 폴더의 tuning_log.csv.

1. 기준: v1feat_xgb_robust, v1feat_lgbm 을 튜닝 기준일(tune)로 실행 → 앙상블(기준 앙상블)
2. XGBoost 후보 20개를 하나씩 바꿔 tune 실행 → 각각 같은 LightGBM과 앙상블 → 앙상블 MAPE 기록
3. 기준보다 좋아진 변경이 2개 이상이면 합친 설정 1개 더
4. 2단계: combo 주변 19개 → 모두 합쳐 기준서 예산 40회
5. 앙상블 MAPE가 가장 낮은 XGBoost 설정을 검증 전체(validation)로 한 번 확인:
   기준 3종(XGB 기준 + LightGBM + AutoARIMA p2)과 새 3종(XGB 최고 + LightGBM + AutoARIMA p2)을 비교
결과: runs/v2_xgb_tune.csv(시도별), runs/v2_xgb_tune_summary.json(최종 요약). 끊겨도 다시 실행하면 이어 감.
"""
import csv
import json
import os
import subprocess
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
RUNS = ROOT / 'runs'
CONFIGS = RUNS / 'v2_xgb_tune_configs'
LOG = RUNS / 'v2_xgb_tune.csv'
SUMMARY = RUNS / 'v2_xgb_tune_summary.json'
ARIMA = ROOT / 'experiments' / 'arima-p2-20261112-01'
BASE = json.loads((ROOT / 'model_comparison/v2/configs/v1feat_xgb_robust.json').read_text(encoding='utf-8'))
LGBM = ROOT / 'model_comparison/v2/configs/v1feat_lgbm.json'

# 기본값(models.PooledXGB.DEFAULTS + robust): n_estimators 300, max_depth 4, learning_rate .05, subsample .8,
# colsample_bytree .6, min_child_weight 20, reg_lambda 10, huber_slope .02, series_weight inv_scale
CANDIDATES = {
    'base': {},
    'depth3': {'max_depth': 3}, 'depth5': {'max_depth': 5}, 'depth6': {'max_depth': 6},
    'trees150': {'n_estimators': 150}, 'trees600': {'n_estimators': 600},
    'lr03_t500': {'learning_rate': .03, 'n_estimators': 500}, 'lr10_t150': {'learning_rate': .1, 'n_estimators': 150},
    'huber01': {'huber_slope': .01}, 'huber03': {'huber_slope': .03}, 'huber05': {'huber_slope': .05},
    'mcw5': {'min_child_weight': 5}, 'mcw50': {'min_child_weight': 50},
    'lambda1': {'reg_lambda': 1.0}, 'lambda30': {'reg_lambda': 30.0},
    'col04': {'colsample_bytree': .4}, 'col08': {'colsample_bytree': .8},
    'sub06': {'subsample': .6}, 'sub10': {'subsample': 1.0},
    'depth5_lr03_t500': {'max_depth': 5, 'learning_rate': .03, 'n_estimators': 500},
}
# 2단계: combo(트리 600·깊이 6·mcw 5·Huber 0.03) 주변을 더 본다. 1단계 21회 + 19회 = 기준서 예산 40회
STAGE2 = {
    'c_depth7': {'max_depth': 7}, 'c_depth8': {'max_depth': 8}, 'c_depth5': {'max_depth': 5},
    'c_trees900': {'n_estimators': 900}, 'c_trees450': {'n_estimators': 450},
    'c_lr03_t1000': {'learning_rate': .03, 'n_estimators': 1000}, 'c_lr07_t450': {'learning_rate': .07, 'n_estimators': 450},
    'c_mcw2': {'min_child_weight': 2}, 'c_mcw10': {'min_child_weight': 10},
    'c_huber02': {'huber_slope': .02}, 'c_huber04': {'huber_slope': .04},
    'c_lambda3': {'reg_lambda': 3.0}, 'c_lambda20': {'reg_lambda': 20.0},
    'c_col05': {'colsample_bytree': .5}, 'c_col07': {'colsample_bytree': .7},
    'c_sub07': {'subsample': .7}, 'c_sub09': {'subsample': .9},
    'c_sub10': {'subsample': 1.0}, 'c_depth7_mcw10': {'max_depth': 7, 'min_child_weight': 10},
}
BUDGET = 40
FIELDS = ('trial', 'changes', 'xgb_folder', 'xgb_mape', 'ens_folder', 'ens_mape', 'seconds')


def run(module, *args):
    """모듈 실행 → '결과: <폴더>' 줄의 폴더, 출력의 policy macro MAPE."""
    cmd = [sys.executable, '-m', module, *map(str, args)]
    print('>>', ' '.join(cmd[2:]), flush=True)
    env = {**os.environ, 'PYTHONIOENCODING': 'utf-8', 'PYTHONUTF8': '1'}  # Windows 파이프에서도 한글 출력이 UTF-8
    out = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True, encoding='utf-8', errors='replace', env=env,
                         check=False)
    if out.returncode != 0:
        print(out.stdout[-2000:], out.stderr[-3000:])
        raise RuntimeError(f'실패: {module} {args}')
    folder = next(line.split('결과:', 1)[1].strip() for line in out.stdout.splitlines() if line.startswith('결과:'))
    metrics = json.loads((Path(folder) / 'metrics.json').read_text(encoding='utf-8'))
    mape = metrics['results']['policy']['macro_mape']
    print(f'   → {Path(folder).name}  policy macro MAPE {mape:.4f}%', flush=True)
    return folder, mape


def config_for(name, changes, origins='tune'):
    params = {**BASE['params'], **changes}
    config = {**BASE, 'name': f'xgbtune-{name}', 'params': params}
    CONFIGS.mkdir(parents=True, exist_ok=True)
    path = CONFIGS / f'{name}.json'
    path.write_text(json.dumps(config, ensure_ascii=False, indent=2), encoding='utf-8')
    return path


def done():
    if not LOG.exists():
        return {}
    with open(LOG, encoding='utf-8', newline='') as f:
        return {r['trial']: r for r in csv.DictReader(f)}


def record(row):
    new = not LOG.exists()
    with open(LOG, 'a', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=FIELDS, lineterminator='\n')
        if new:
            writer.writeheader()
        writer.writerow(row)


def main():
    RUNS.mkdir(exist_ok=True)
    state = json.loads(SUMMARY.read_text(encoding='utf-8')) if SUMMARY.exists() else {}
    if 'lgbm_tune' not in state:
        state['lgbm_tune'] = run('model_comparison.v2.run_pooled', '--config', LGBM, '--origins', 'tune')[0]
        SUMMARY.write_text(json.dumps(state, ensure_ascii=False, indent=2), encoding='utf-8')
    lgbm = state['lgbm_tune']

    trials = dict(CANDIDATES)
    for name, changes in trials.items():
        if name in done():
            continue
        t0 = time.time()
        xgb, xgb_mape = run('model_comparison.v2.run_pooled', '--config', config_for(name, changes), '--origins', 'tune')
        ens, ens_mape = run('model_comparison.v2.ensemble', xgb, lgbm, '--name', f'ens-xgbtune-{name}')
        record({'trial': name, 'changes': json.dumps(changes), 'xgb_folder': xgb, 'xgb_mape': xgb_mape,
                'ens_folder': ens, 'ens_mape': ens_mape, 'seconds': round(time.time() - t0)})

    rows = done()
    base = float(rows['base']['ens_mape'])
    better = [n for n, r in rows.items() if n in CANDIDATES and n != 'base' and float(r['ens_mape']) < base]
    if len(better) >= 2 and 'combo' not in rows:
        combo = {}
        for name in sorted(better, key=lambda n: float(rows[n]['ens_mape'])):
            for key, value in CANDIDATES[name].items():
                combo.setdefault(key, value)  # 같은 파라미터면 더 좋았던 후보 값
        t0 = time.time()
        xgb, xgb_mape = run('model_comparison.v2.run_pooled', '--config', config_for('combo', combo), '--origins', 'tune')
        ens, ens_mape = run('model_comparison.v2.ensemble', xgb, lgbm, '--name', 'ens-xgbtune-combo')
        record({'trial': 'combo', 'changes': json.dumps(combo), 'xgb_folder': xgb, 'xgb_mape': xgb_mape,
                'ens_folder': ens, 'ens_mape': ens_mape, 'seconds': round(time.time() - t0)})
        rows = done()

    if 'combo' in rows:
        combo_changes = json.loads(rows['combo']['changes'])
        for name, changes in STAGE2.items():
            if len(rows) >= BUDGET:
                break
            if name in rows:
                continue
            merged = {**combo_changes, **changes}
            t0 = time.time()
            xgb, xgb_mape = run('model_comparison.v2.run_pooled', '--config', config_for(name, merged), '--origins', 'tune')
            ens, ens_mape = run('model_comparison.v2.ensemble', xgb, lgbm, '--name', f'ens-xgbtune-{name}')
            record({'trial': name, 'changes': json.dumps(merged), 'xgb_folder': xgb, 'xgb_mape': xgb_mape,
                    'ens_folder': ens, 'ens_mape': ens_mape, 'seconds': round(time.time() - t0)})
            rows = done()

    best = min(rows, key=lambda n: float(rows[n]['ens_mape']))
    state.update(trials=len(rows), tune_seconds=sum(int(r['seconds']) for r in rows.values()),
                 base_tune_ens=base, best=best, best_changes=json.loads(rows[best]['changes']),
                 best_tune_ens=float(rows[best]['ens_mape']), improved_on_tune=[n for n in better])
    print(f'\n튜닝 기준일: 기준 앙상블 {base:.4f}% → 최고 {best} {float(rows[best]["ens_mape"]):.4f}%', flush=True)
    SUMMARY.write_text(json.dumps(state, ensure_ascii=False, indent=2), encoding='utf-8')

    # 검증 전체로 한 번만 확인
    if 'val_lgbm' not in state:
        state['val_lgbm'] = run('model_comparison.v2.run_pooled', '--config', LGBM)[0]
    if 'val_xgb_base' not in state:
        state['val_xgb_base'] = run('model_comparison.v2.run_pooled', '--config', config_for('base_val', {}))[0]
    best_key = f'val_xgb_{best}'
    if best == 'combo' and 'val_xgb_best' in state:  # 1단계 때 이미 돌린 combo 검증
        state.setdefault(best_key, state['val_xgb_best'])
    if best != 'base' and best_key not in state:
        state[best_key] = run('model_comparison.v2.run_pooled', '--config', config_for(f'{best}_val', state['best_changes']))[0]
    SUMMARY.write_text(json.dumps(state, ensure_ascii=False, indent=2), encoding='utf-8')
    finals = {'base': state['val_xgb_base'], best: state.get(best_key, state['val_xgb_base'])}
    for label, xgb in finals.items():
        for extra, name in (([], 'xgb+lgbm'), ([ARIMA], 'xgb+lgbm+arima')):
            key = f'val_ens_{label}_{name}'
            if key not in state:
                state[key] = run('model_comparison.v2.ensemble', xgb, state['val_lgbm'], *extra,
                                 '--name', f'ens-xgbtune-{label}-{name.replace("+", "-")}')[1]
                SUMMARY.write_text(json.dumps(state, ensure_ascii=False, indent=2), encoding='utf-8')
    print('\n검증 전체(244개) 앙상블 MAPE')
    for key, value in state.items():
        if key.startswith('val_ens_'):
            print(f'  {key[8:]:40} {value:.4f}%')
    print(f'\n요약: {SUMMARY}')


if __name__ == '__main__':
    main()
