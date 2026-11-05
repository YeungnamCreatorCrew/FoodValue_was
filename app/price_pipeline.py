"""통합 파이프라인: Open API 수집 → 적재 → 품목별 7일 예측.

실행 예:
    python -m app.price_pipeline                     # 모든 KAMIS 원물 품목, 증분 수집 후 예측
    python -m app.price_pipeline --item-id 1 --item-id 2
    python -m app.price_pipeline --start 2022-01-01 --collect-only   # 과거 자료 백필
    python -m app.price_pipeline --predict-only
OS 스케줄러에서 서울 기준 하루 1회 호출한다. 종료 코드: 0 성공, 1 실패, 2 일부 자료 부족·수집 실패, 3 실행 중.
"""
import argparse
import json
import os
from datetime import date

from dotenv import load_dotenv
from sqlalchemy import create_engine

from app.core.constants import ID_MAX
from app.services import collection_service, price_batch_service

COLLECTION_FAILURES = {'AUTH_ERROR', 'NETWORK_ERROR', 'FAILED', 'PARTIAL'}


def parse_args(argv=None):
    parser = argparse.ArgumentParser(description='Open API 통합 수집과 농산물 7일 가격 예측')
    parser.add_argument('--item-id', type=int, action='append', dest='item_ids', help='반복 지정 가능. 생략하면 모든 KAMIS 원물')
    parser.add_argument('--start', type=date.fromisoformat, help='수집 시작일(YYYY-MM-DD). 생략하면 증분 수집')
    parser.add_argument('--end', type=date.fromisoformat, help='수집 종료일. 생략하면 오늘')
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument('--collect-only', action='store_true')
    mode.add_argument('--predict-only', action='store_true')
    args = parser.parse_args(argv)
    if any(not 1 <= item <= ID_MAX for item in args.item_ids or []):
        parser.error('item-id는 양의 BIGINT 범위여야 합니다')
    if args.start and args.end and args.start > args.end:
        parser.error('start는 end보다 늦을 수 없습니다')
    return parser, args


def run(engine, args):
    output = {'collection': [], 'predictions': []}
    items = collection_service.prediction_items(engine, args.item_ids)
    if args.item_ids and len(items) != len(set(args.item_ids)):
        raise ValueError('대상은 KAMIS 원물 품목만 지정할 수 있습니다')
    if not args.predict_only:
        output['collection'] = collection_service.collect(engine, args.item_ids, start=args.start, end=args.end)
    if not args.collect_only:
        for item in items:
            try:
                result = price_batch_service.run(engine, item.id)
            except price_batch_service.BatchBusyError:
                result = {'status': 'BUSY'}
            except Exception as error:
                # DB 주소·인증키가 포함될 수 있어 예외 원문은 출력하지 않는다.
                result = {'status': 'FAILED', 'errorCode': type(error).__name__}
            output['predictions'].append({'itemId': item.id, **result})
    return output


def exit_code(output):
    statuses = [row['status'] for row in output['predictions']]
    if 'FAILED' in statuses:
        return 1
    if 'BUSY' in statuses:
        return 3
    if 'INSUFFICIENT_DATA' in statuses or any(row['status'] in COLLECTION_FAILURES for row in output['collection']):
        return 2
    return 0


def main(argv=None):
    parser, args = parse_args(argv)
    load_dotenv()
    url = os.getenv('DATABASE_URL')
    if not url:
        parser.error('DATABASE_URL 설정이 필요합니다')
    engine = create_engine(url, pool_pre_ping=True, hide_parameters=True)
    try:
        output = run(engine, args)
        print(json.dumps(output, ensure_ascii=False))
        return exit_code(output)
    except Exception as error:
        print(json.dumps({'status': 'FAILED', 'errorCode': type(error).__name__}))
        return 1
    finally:
        engine.dispose()


if __name__ == '__main__':
    raise SystemExit(main())
