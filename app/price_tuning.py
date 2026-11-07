"""XGBoost 하이퍼파라미터 후보를 과거 기준일 재현 백테스트로 비교한다(DB 읽기 전용).

실행 예:
    python -m app.price_tuning --item-id 1 --tune-start 2026-02-01 --tune-end 2026-07-31 \
        --check-start 2026-08-01 --check-end 2026-10-27 --workers 4 --out tuning.json

- 후보마다 FOODVALUE_XGB_PARAMS 환경변수로 파라미터를 바꿔 price_backtest.run을 그대로 실행한다.
  운영 배치와 같은 입력·모델 선택·공개지연 규칙이 적용된다.
- 튜닝 구간(tune)에서 소매·도매 평균 MAPE가 가장 낮은 후보를 고르고, 겹치지 않는 확인 구간(check)에서
  현재 기본값과 다시 비교한다. 같은 구간으로 고르고 확인하면 성능이 실제보다 좋게 보이기 때문이다.
- 결과는 표로 출력하고 --out에 JSON으로 저장한다. 기본값(XGB_PARAMS)은 자동으로 바꾸지 않는다.
"""
import argparse
import json
import os
import time
from datetime import date

from dotenv import load_dotenv
from sqlalchemy import create_engine

from app.price_backtest import base_dates, run
from app.services.price_prediction import XGB_PARAMS, XGB_PARAMS_ENV

CANDIDATES = {
    'current': {},
    'more_trees': {'n_estimators': 200, 'subsample': .8, 'colsample_bytree': .8},
    'deeper_slow': {'n_estimators': 300, 'max_depth': 4, 'learning_rate': .03, 'subsample': .8,
                    'colsample_bytree': .8, 'min_child_weight': 5},
    'deep_regularized': {'n_estimators': 150, 'max_depth': 5, 'subsample': .8, 'colsample_bytree': .8,
                         'reg_lambda': 5},
    'shallow_fast': {'n_estimators': 120, 'max_depth': 2, 'learning_rate': .1},
}
MARKETS = ('RETAIL', 'WHOLESALE')


def evaluate(engine, item_id, dates, workers, params):
    os.environ[XGB_PARAMS_ENV] = json.dumps(params)
    try:
        result, started = {}, time.monotonic()
        for market in MARKETS:
            output, _ = run(engine, item_id, dates, workers, market)
            overall = output['summary']['overall']
            failed = sum(r['status'] != 'SUCCESS' for r in output['runs'])
            result[market] = {**{k: overall.get(k) for k in ('points', 'mape', 'naiveMape', 'mae', 'mapeImprovementPct',
                                                            'directionAccuracy')},
                              'failedOrigins': failed,
                              'models': {m: s['points'] for m, s in output['summary'].get('byModel', {}).items()}}
        scores = [result[m]['mape'] for m in MARKETS if result[m].get('mape') is not None]
        result['meanMape'] = round(sum(scores) / len(scores), 3) if len(scores) == len(MARKETS) else None
        result['seconds'] = round(time.monotonic() - started)
        return result
    finally:
        os.environ.pop(XGB_PARAMS_ENV, None)


def table(title, rows):
    lines = [f'## {title}', '| 후보 | 평균 MAPE | 소매 MAPE | 도매 MAPE | 소매 직전가 대비 | 도매 직전가 대비 | 시간(초) |',
             '|---|---|---|---|---|---|---|']
    for name, r in rows.items():
        lines.append(f"| {name} | {r['meanMape']} | {r['RETAIL']['mape']} | {r['WHOLESALE']['mape']} | "
                     f"{r['RETAIL']['mapeImprovementPct']}% | {r['WHOLESALE']['mapeImprovementPct']}% | {r['seconds']} |")
    return '\n'.join(lines)


def main(argv=None):
    parser = argparse.ArgumentParser(description='XGBoost 하이퍼파라미터 후보 비교(DB 읽기 전용)')
    parser.add_argument('--item-id', type=int, required=True)
    for name in ('tune-start', 'tune-end', 'check-start', 'check-end'):
        parser.add_argument(f'--{name}', type=date.fromisoformat, required=True)
    parser.add_argument('--every', type=int, default=7)
    parser.add_argument('--workers', type=int, default=4)
    parser.add_argument('--only', nargs='*', choices=list(CANDIDATES), help='일부 후보만 실행')
    parser.add_argument('--out', default='tuning.json')
    args = parser.parse_args(argv)
    if args.tune_end >= args.check_start:
        parser.error('확인 구간은 튜닝 구간 이후여야 합니다')
    load_dotenv()
    url = os.getenv('DATABASE_URL')
    if not url:
        parser.error('DATABASE_URL 설정이 필요합니다')
    engine = create_engine(url, pool_pre_ping=True, hide_parameters=True)
    names = args.only or list(CANDIDATES)
    report = {'defaults': XGB_PARAMS, 'candidates': {n: CANDIDATES[n] for n in names}, 'tune': {}, 'check': {}}
    try:
        tune_dates = base_dates(args.tune_start, args.tune_end, args.every)
        for name in names:
            report['tune'][name] = evaluate(engine, args.item_id, tune_dates, args.workers, CANDIDATES[name])
            print(f'[tune] {name}: {json.dumps(report["tune"][name], ensure_ascii=False)}', flush=True)
        ranked = sorted((r['meanMape'], n) for n, r in report['tune'].items() if r['meanMape'] is not None)
        best = ranked[0][1] if ranked else 'current'
        report['best'] = best
        check_dates = base_dates(args.check_start, args.check_end, args.every)
        for name in dict.fromkeys(['current', best]):
            report['check'][name] = evaluate(engine, args.item_id, check_dates, args.workers, CANDIDATES[name])
            print(f'[check] {name}: {json.dumps(report["check"][name], ensure_ascii=False)}', flush=True)
        with open(args.out, 'w', encoding='utf-8') as handle:
            json.dump(report, handle, ensure_ascii=False, indent=2)
        print(table('튜닝 구간', report['tune']))
        print(table('확인 구간', report['check']))
        print(f'최고 후보: {best} {json.dumps({**XGB_PARAMS, **CANDIDATES[best]})}')
        return 0
    finally:
        engine.dispose()


if __name__ == '__main__':
    raise SystemExit(main())
