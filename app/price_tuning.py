"""XGBoost 하이퍼파라미터 후보를 실데이터로 비교한다(DB 읽기 전용).

실행 예:
    python -m app.price_tuning --item-id 1 --anchor 2026-11-06 --anchor 2025-11-06 --anchor 2024-11-06 \
        --only default v4 huber --workers 4 --out tuning.json

- predict()는 기준일마다 최근 최대 240개 예측 시작일로 시간순 백테스트를 한다(선택 구간 → 보정 → 최종 평가 구간).
  이 스크립트는 후보 파라미터마다 그 내부 백테스트를 실행하고, 후보 모델별 선택·평가 구간 MAPE를 모은다.
  기준일을 하나씩 따로 재현하는 app.price_backtest보다 수십 배 빠르다(기준일당 예측 1회).
- 운영과 같은 입력 로딩(price_batch_service.load_inputs)·공개지연 규칙·모델 선택 규칙을 쓴다.
- 후보 순위는 선택 구간 MAPE로 정하고, 평가 구간은 확인용으로만 본다(같은 구간으로 고르고 확인하지 않기 위해).
- --anchor를 여러 개 주면 서로 다른 기간(예: 올해·작년)에서 같은 후보가 일관되게 좋은지 볼 수 있다.
- 결과는 표로 출력하고 --out에 JSON으로 저장한다. 기본값(XGB_PARAMS)은 자동으로 바꾸지 않는다.
"""
import argparse
import json
import multiprocessing
import os
import time
from concurrent.futures import ProcessPoolExecutor
from datetime import date

from dotenv import load_dotenv
from sqlalchemy.orm import Session

from app.core.db import make_engine
from app.repositories import series_repository
from app.services.price_batch_service import load_inputs
from app.services.price_prediction import DAMPING_ENV, XGB_PARAMS, XGB_PARAMS_ENV, check_dependencies, predict

# 후보 값은 v3 기본값(V3_PARAMS) 대비 바뀌는 부분만 적는다. 이름은 v4 튜닝 기록(model_comparison/xgboost/README_MODEL.md)과 같다.
# 'current'는 v4 튜닝 당시의 기본값, 즉 v3 설정이다. 지금 코드의 기본값(XGB_PARAMS)과 비교하려면 'default'를 쓴다.
V3_PARAMS = {'n_estimators': 80, 'max_depth': 3, 'learning_rate': .05, 'subsample': 1, 'colsample_bytree': 1,
             'min_child_weight': 1, 'reg_lambda': 1, 'objective': 'reg:squarederror'}
CANDIDATES = {
    'default': None,
    'current': {},
    'conservative': {'n_estimators': 60, 'max_depth': 2, 'learning_rate': .05, 'min_child_weight': 10,
                     'reg_lambda': 10},
    'regularized': {'n_estimators': 150, 'max_depth': 3, 'learning_rate': .03, 'subsample': .8,
                    'colsample_bytree': .8, 'min_child_weight': 10, 'reg_lambda': 10},
    'more_trees': {'n_estimators': 200, 'subsample': .8, 'colsample_bytree': .8},
    'deeper_slow': {'n_estimators': 300, 'max_depth': 4, 'learning_rate': .03, 'subsample': .8,
                    'colsample_bytree': .8, 'min_child_weight': 5},
    'shallow_fast': {'n_estimators': 120, 'max_depth': 2, 'learning_rate': .1},
    # 2차: 1차에서 규제가 강할수록 평가 구간 성능이 좋아서 conservative 주변을 더 본다.
    'conservative_strong': {'n_estimators': 40, 'max_depth': 2, 'learning_rate': .05, 'min_child_weight': 20,
                            'reg_lambda': 20},
    'conservative_d3': {'n_estimators': 60, 'max_depth': 3, 'learning_rate': .05, 'min_child_weight': 10,
                        'reg_lambda': 10},
    'conservative_sub': {'n_estimators': 60, 'max_depth': 2, 'learning_rate': .05, 'min_child_weight': 10,
                         'reg_lambda': 10, 'subsample': .8, 'colsample_bytree': .8},
}
# v5 실험(model_comparison/xgboost/README_MODEL.md): v4 설정 위에서 손실 함수·변화폭 축소(damping)를 바꾼다. 값: (파라미터 덮어쓰기, damping)
V4_PARAMS = {**V3_PARAMS, 'n_estimators': 60, 'max_depth': 2, 'min_child_weight': 10, 'reg_lambda': 10,
             'objective': 'reg:squarederror'}
HUBER = {'objective': 'reg:pseudohubererror'}
VARIANTS = {
    'v4': ({}, 1),
    'damp_0.7': ({}, .7),
    'damp_0.5': ({}, .5),
    'huber': ({**HUBER, 'huber_slope': .02}, 1),
    'huber_damp_0.7': ({**HUBER, 'huber_slope': .02}, .7),
    'huber_0.01': ({**HUBER, 'huber_slope': .01}, 1),
    'huber_0.05': ({**HUBER, 'huber_slope': .05}, 1),
}
MARKETS = ('RETAIL', 'WHOLESALE')
LEARNERS = ('XGBOOST', 'XGBOOST_EXT', 'XGBOOST_WEIGHTED')


def full_params(name):
    if name in VARIANTS:
        return {**V4_PARAMS, **VARIANTS[name][0], 'damping': VARIANTS[name][1]}
    return dict(XGB_PARAMS) if CANDIDATES[name] is None else {**V3_PARAMS, **CANDIDATES[name]}


def _job(task):
    name, params, market, anchor, rows, covariates = task
    params = dict(params)
    os.environ[DAMPING_ENV] = str(params.pop('damping', 1))
    os.environ[XGB_PARAMS_ENV] = json.dumps(params)
    started = time.monotonic()
    try:
        result = predict(rows, anchor, covariates)
    except Exception as error:
        return {'candidate': name, 'market': market, 'anchor': anchor.isoformat(), 'status': type(error).__name__}
    metrics = result.metrics
    mape = {stage: {model: round(score['mape'], 3) for model, score in (metrics.get(stage) or {}).items() if score}
            for stage in ('selection', 'evaluation')}
    return {'candidate': name, 'market': market, 'anchor': anchor.isoformat(), 'status': 'SUCCESS',
            'model': result.model, 'quality': result.quality, 'baseline': metrics.get('baselineModel'),
            'selectedInSelection': metrics.get('selectedInSelection'), 'mape': mape,
            'seconds': round(time.monotonic() - started)}


def best_learner(stage_mape):
    found = [(stage_mape[m], m) for m in LEARNERS if m in stage_mape]
    return min(found) if found else (None, None)


def summarize(results):
    """후보별: 시장·기준일마다 최고 XGBoost 계열 후보의 MAPE와 기준 모델 대비 개선율."""
    table = {}
    for r in results:
        if r['status'] != 'SUCCESS':
            continue
        row = table.setdefault(r['candidate'], {'cases': [], 'validated': 0, 'seconds': 0})
        case = {'market': r['market'], 'anchor': r['anchor'], 'model': r['model'], 'quality': r['quality']}
        for stage in ('selection', 'evaluation'):
            baseline = r['mape'][stage].get(r['baseline'])
            learner_mape, learner = best_learner(r['mape'][stage])
            case[stage] = {'baseline': baseline, 'learner': learner, 'learnerMape': learner_mape,
                           'gainPct': round((baseline - learner_mape) / baseline * 100, 2) if baseline and learner_mape else None}
        row['cases'].append(case)
        row['validated'] += r['quality'] == 'VALIDATED'
        row['seconds'] += r['seconds']
    for row in table.values():
        for stage in ('selection', 'evaluation'):
            gains = [c[stage]['gainPct'] for c in row['cases'] if c[stage]['gainPct'] is not None]
            row[f'{stage}MeanGainPct'] = round(sum(gains) / len(gains), 2) if gains else None
    return table


def render(table):
    lines = ['| 후보 | 선택 구간 평균 개선율 | 평가 구간 평균 개선율 | VALIDATED 수 | 학습 시간(초) |', '|---|---|---|---|---|']
    for name, row in sorted(table.items(), key=lambda kv: -(kv[1]['selectionMeanGainPct'] or -1e9)):
        lines.append(f"| {name} | {row['selectionMeanGainPct']}% | {row['evaluationMeanGainPct']}% | "
                     f"{row['validated']}/{len(row['cases'])} | {row['seconds']} |")
    lines.append('')
    lines.append('개선율 = (기준 모델 MAPE − 최고 XGBoost 계열 MAPE) / 기준 모델 MAPE. 양수면 직전가·7일 평균보다 좋음')
    return '\n'.join(lines)


def main(argv=None):
    parser = argparse.ArgumentParser(description='XGBoost 하이퍼파라미터 후보 비교(DB 읽기 전용)')
    parser.add_argument('--item-id', type=int, required=True)
    parser.add_argument('--anchor', type=date.fromisoformat, action='append', required=True,
                        help='예측 기준일. 여러 번 줄 수 있음')
    parser.add_argument('--workers', type=int, default=2)
    parser.add_argument('--only', nargs='*', choices=list(CANDIDATES) + list(VARIANTS), help='일부 후보만 실행')
    parser.add_argument('--out', default='tuning.json')
    args = parser.parse_args(argv)
    load_dotenv()
    url = os.getenv('DATABASE_URL')
    if not url:
        parser.error('DATABASE_URL 설정이 필요합니다')
    check_dependencies()
    engine = make_engine(url)
    names = args.only or list(CANDIDATES)
    inputs = []
    try:
        with Session(engine, expire_on_commit=False) as db:
            for market in MARKETS:
                series = series_repository.get(db, args.item_id, market)
                if series is None:
                    continue
                for anchor in args.anchor:
                    rows, covariates = load_inputs(db, series, anchor)
                    inputs.append((market, anchor, rows, covariates))
    finally:
        engine.dispose()
    # 오래 걸리는 후보를 먼저 넣어 병렬 작업이 끝에 몰리지 않게 한다.
    tasks = [(n, full_params(n), m, a, rows, cov) for n in names for m, a, rows, cov in inputs]
    tasks.sort(key=lambda t: -(t[1]['n_estimators'] * t[1]['max_depth']))
    results = []
    with ProcessPoolExecutor(max_workers=args.workers, mp_context=multiprocessing.get_context('spawn')) as pool:
        for result in pool.map(_job, tasks):
            results.append(result)
            print(json.dumps(result, ensure_ascii=False), flush=True)
    table = summarize(results)
    with open(args.out, 'w', encoding='utf-8') as handle:
        json.dump({'defaults': XGB_PARAMS, 'candidates': {n: full_params(n) for n in names},
                   'anchors': [a.isoformat() for a in args.anchor], 'summary': table, 'results': results},
                  handle, ensure_ascii=False, indent=2)
    print(render(table))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
