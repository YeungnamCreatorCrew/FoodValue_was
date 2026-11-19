"""v2 XGBoost 튜닝 최고 설정이 시드를 바꿔도 기준보다 좋은지 확인(튜닝 기준일). 약 20~30분.

    uv run --extra prices python -m model_comparison.v2.xgb_tune.seeds

기준(base)과 최고 설정을 시드 43·44로 다시 돌려, 각각 같은 LightGBM(시드 42)과 앙상블한다.
시드 42 값은 v2_xgb_tune.csv에 있는 값을 쓴다. 결과: runs/v2_xgb_seeds.json
"""
import csv
import json

from model_comparison.v2.xgb_tune import tune as T

OUT = T.RUNS / 'v2_xgb_seeds.json'


def main():
    state = json.loads(T.SUMMARY.read_text(encoding='utf-8'))
    with open(T.LOG, encoding='utf-8', newline='') as f:
        rows = {r['trial']: r for r in csv.DictReader(f)}
    lgbm = state['lgbm_tune']
    result = json.loads(OUT.read_text(encoding='utf-8')) if OUT.exists() else {}
    best = state['best']
    for name, changes in (('base', {}), (best, state['best_changes'])):
        entry = result.setdefault(name, {'42': {'xgb': float(rows[name]['xgb_mape']), 'ens': float(rows[name]['ens_mape'])}})
        for seed in (43, 44):
            if str(seed) in entry:
                continue
            path = T.config_for(f'{name}_s{seed}', changes)
            config = json.loads(path.read_text(encoding='utf-8'))
            config['seed'] = seed
            path.write_text(json.dumps(config, ensure_ascii=False, indent=2), encoding='utf-8')
            xgb, xgb_mape = T.run('model_comparison.v2.run_pooled', '--config', path, '--origins', 'tune')
            _, ens_mape = T.run('model_comparison.v2.ensemble', xgb, lgbm, '--name', f'ens-xgbseed-{name}-s{seed}')
            entry[str(seed)] = {'xgb': xgb_mape, 'ens': ens_mape}
            OUT.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding='utf-8')
    print('\n튜닝 기준일 앙상블 MAPE (XGBoost + LightGBM)')
    for name, entry in result.items():
        values = [entry[s]['ens'] for s in ('42', '43', '44')]
        print(f'  {name:6} ' + '  '.join(f'{v:.4f}' for v in values) + f'  평균 {sum(values) / 3:.4f}')
    diffs = [result[best][s]['ens'] - result['base'][s]['ens'] for s in ('42', '43', '44')]
    print(f'  {best} − base: ' + '  '.join(f'{d:+.4f}' for d in diffs))


if __name__ == '__main__':
    main()
