"""과거 시점 재현 백테스트: 과거 기준일마다 그때까지의 자료로만 7일 예측을 만들고 이후 실제 가격과 비교한다.

실행 예:
    python -m app.price_backtest --item-id 1 --start 2026-05-01 --end 2026-10-27 --every 7 --workers 4
    python -m app.price_backtest --item-id 1 --start 2026-05-01 --end 2026-10-27 --csv backtest.csv

- 운영 배치와 같은 입력 로딩(price_batch_service.load_inputs)과 모델(price_prediction.predict)을 쓴다.
  기준일 이후 가격·외부 원천은 읽지 않고, 공개지연 규칙도 그대로 적용된다.
- DB를 읽기만 한다. price_forecast·price_model_run에 아무것도 쓰지 않는다.
- 비교 기준은 '직전 가격 유지'(기준일의 최신 관측가)다. 실제 가격이 없는 날(주말·공휴일)은 비교에서 빠진다.
- 원천 수정 이력이 있으면 최신 수정본으로 재현한다(수정 전 값 복원은 하지 않음).
"""
import argparse
import csv
import json
import multiprocessing
import os
from concurrent.futures import ProcessPoolExecutor
from datetime import date, timedelta
from statistics import mean

from dotenv import load_dotenv
from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session

from app.core.constants import ID_MAX
from app.models.price import PriceDaily
from app.services.price_batch_service import guidance, load_inputs
from app.services.price_prediction import HORIZON, InsufficientDataError, ModelDependencyError, check_dependencies, predict


def base_dates(start: date, end: date, every: int):
    day, result = start, []
    while day <= end:
        result.append(day)
        day += timedelta(days=every)
    return result


def _forecast(task):
    base_date, rows, covariates = task
    try:
        return base_date, predict(rows, base_date, covariates), None
    except InsufficientDataError:
        return base_date, None, {'status': 'INSUFFICIENT_DATA'}
    except Exception as error:
        # 자식 프로세스의 예외는 부모로 넘어오며 형식이 바뀔 수 있어(PicklingError) 여기서 문자열로 바꾼다.
        # 예측 단계에는 DB 주소·인증키가 없어 메시지를 남겨도 된다.
        return base_date, None, {'status': 'FAILED', 'errorCode': type(error).__name__, 'message': str(error)[:300]}


def records_for(base_date, result, rows, actual: dict[date, int]):
    """기준일 하나의 시점별 비교 행. 실제 가격이 있는 목표일만 만든다."""
    current_day, current = rows[-1]
    recommendation, after, _ = guidance(result.prices, current, result.quality)
    records = []
    for horizon in range(1, HORIZON + 1):
        target = base_date + timedelta(days=horizon)
        if target not in actual:
            continue
        records.append({'baseDate': base_date.isoformat(), 'targetDate': target.isoformat(), 'horizon': horizon,
                        'model': result.model, 'quality': result.quality, 'recommendation': recommendation,
                        'currentPrice': current, 'currentDate': current_day.isoformat(),
                        'predicted': result.prices[horizon - 1], 'lower': result.lower[horizon - 1],
                        'upper': result.upper[horizon - 1], 'actual': actual[target]})
    return records


def _ape(predicted, actual):
    return abs(predicted - actual) / actual * 100


def summarize(records):
    """전체·시점별 오차. naive는 직전 가격 유지(기준일 최신 관측가)."""
    if not records:
        return {'points': 0}

    def block(rows):
        # 방향 적중률은 모델이 움직임을 예측했고 실제로도 움직인 점만 센다. 직전 가격 유지(평평한 예측)는 방향을 말하지
        # 않으므로 오답으로 세지 않고, 그 비율은 flatPredictionShare로 따로 보여 준다.
        directional = [r for r in rows if r['actual'] != r['currentPrice'] and r['predicted'] != r['currentPrice']]
        hits = [(r['predicted'] > r['currentPrice']) == (r['actual'] > r['currentPrice']) for r in directional]
        flat = sum(r['predicted'] == r['currentPrice'] for r in rows)
        bounded = [r for r in rows if r['lower'] is not None and r['upper'] is not None]
        model_mape = mean(_ape(r['predicted'], r['actual']) for r in rows)
        naive_mape = mean(_ape(r['currentPrice'], r['actual']) for r in rows)
        return {'points': len(rows), 'mape': round(model_mape, 3), 'naiveMape': round(naive_mape, 3),
                'mae': round(mean(abs(r['predicted'] - r['actual']) for r in rows), 1),
                'naiveMae': round(mean(abs(r['currentPrice'] - r['actual']) for r in rows), 1),
                'mapeImprovementPct': round((naive_mape - model_mape) / naive_mape * 100, 1) if naive_mape else None,
                'directionAccuracy': round(mean(hits), 3) if hits else None, 'directionSamples': len(hits),
                'flatPredictionShare': round(flat / len(rows), 3),
                'intervalCoverage': round(mean(r['lower'] <= r['actual'] <= r['upper'] for r in bounded), 3) if bounded else None,
                'intervalSamples': len(bounded)}

    summary = {'overall': block(records),
               'byHorizon': {h: block([r for r in records if r['horizon'] == h])
                             for h in range(1, HORIZON + 1) if any(r['horizon'] == h for r in records)},
               'byModel': {}}
    for model in sorted({r['model'] for r in records}):
        summary['byModel'][model] = block([r for r in records if r['model'] == model])
    return summary


def run(engine, item_id, dates, workers=1):
    check_dependencies()  # 병렬 실행 전에 부모에서 확인해 원인 메시지를 그대로 보여 준다.
    tasks = []
    with Session(engine) as db:
        actual = dict(db.execute(select(PriceDaily.price_date, PriceDaily.price).where(
            PriceDaily.item_id == item_id, PriceDaily.region == 'NATIONAL',
            PriceDaily.price_date.between(dates[0], dates[-1] + timedelta(days=HORIZON)))).all())
        for base_date in dates:
            rows, covariates = load_inputs(db, item_id, base_date)
            if rows:
                tasks.append((base_date, rows, covariates))
    runs, records = [], []
    # fork는 부모가 이미 XGBoost(OpenMP)를 썼으면 자식이 멈출 수 있어 spawn으로 새 프로세스를 띄운다.
    with ProcessPoolExecutor(max_workers=workers, mp_context=multiprocessing.get_context('spawn')) as pool:
        for base_date, result, failure in pool.map(_forecast, tasks):
            rows = next(task[1] for task in tasks if task[0] == base_date)
            if result is None:
                runs.append({'baseDate': base_date.isoformat(), **failure})
                continue
            found = records_for(base_date, result, rows, actual)
            records += found
            weighting = (result.metrics.get('weighting') or {}).get('weights')
            metrics = result.metrics
            runs.append({'baseDate': base_date.isoformat(), 'status': 'SUCCESS', 'model': result.model,
                         'quality': result.quality, 'comparedPoints': len(found), 'weights': weighting,
                         # 모델 내부 검증: 어떤 후보가 선택 구간에서 뽑혔고 최종 평가 구간에서 기준 모델을 얼마나 이겼는지
                         'selectedInSelection': metrics.get('selectedInSelection'), 'baselineModel': metrics.get('baselineModel'),
                         'evaluationWindow': [metrics.get('evaluationStart'), metrics.get('evaluationEnd')],
                         'internalMape': {stage: {name: round(score['mape'], 3) for name, score in (metrics.get(stage) or {}).items() if score}
                                          for stage in ('selection', 'evaluation')}})
    return {'itemId': item_id, 'baseDates': len(dates), 'runs': runs, 'summary': summarize(records)}, records


def main(argv=None):
    parser = argparse.ArgumentParser(description='과거 기준일 재현 백테스트(DB 읽기 전용)')
    parser.add_argument('--item-id', type=int, required=True)
    parser.add_argument('--start', type=date.fromisoformat, required=True, help='첫 기준일')
    parser.add_argument('--end', type=date.fromisoformat, required=True, help='마지막 기준일')
    parser.add_argument('--every', type=int, default=7, help='기준일 간격(일)')
    parser.add_argument('--workers', type=int, default=1)
    parser.add_argument('--csv', help='시점별 비교 행을 저장할 CSV 경로')
    args = parser.parse_args(argv)
    if not 1 <= args.item_id <= ID_MAX or args.every < 1 or args.workers < 1 or args.start > args.end:
        parser.error('item-id·every·workers·기간을 확인하세요')
    load_dotenv()
    url = os.getenv('DATABASE_URL')
    if not url:
        parser.error('DATABASE_URL 설정이 필요합니다')
    engine = create_engine(url, pool_pre_ping=True, hide_parameters=True)
    try:
        output, records = run(engine, args.item_id, base_dates(args.start, args.end, args.every), args.workers)
        if args.csv and records:
            with open(args.csv, 'w', newline='', encoding='utf-8') as handle:
                writer = csv.DictWriter(handle, fieldnames=list(records[0]))
                writer.writeheader()
                writer.writerows(records)
        print(json.dumps(output, ensure_ascii=False))
        return 0
    except ModelDependencyError as error:
        print(json.dumps({'status': 'FAILED', 'errorCode': 'ModelDependencyError', 'message': str(error)}, ensure_ascii=False))
        return 1
    except Exception as error:
        # DB 주소가 포함될 수 있어 예외 원문은 출력하지 않는다.
        print(json.dumps({'status': 'FAILED', 'errorCode': type(error).__name__}))
        return 1
    finally:
        engine.dispose()


if __name__ == '__main__':
    raise SystemExit(main())
