"""실행: python -m app.indicator_batch --item-id 60 [--as-of 2026-10-30] [--validate]
소매 계열 기준 판단 보조 지표 카드를 만든다. 가격(price_daily)이 적재된 뒤에 실행한다."""
import argparse
import json
import os
from datetime import date

from dotenv import load_dotenv
from sqlalchemy import create_engine

from app.core.constants import ID_MAX
from app.services import indicator_batch_service


def main():
    parser = argparse.ArgumentParser(description='판단 보조 지표 카드 생성')
    parser.add_argument('--item-id', type=int, required=True)
    parser.add_argument('--as-of', type=date.fromisoformat, default=None, help='이 날짜 이하 가격만 사용(기본: 마지막 관측일)')
    parser.add_argument('--validate', action='store_true', help='저장된 검증을 쓰지 않고 새로 검증')
    args = parser.parse_args()
    if not 1 <= args.item_id <= ID_MAX:
        parser.error('item-id는 양의 BIGINT 범위여야 합니다')
    load_dotenv()
    url = os.getenv('DATABASE_URL')
    if not url:
        parser.error('DATABASE_URL 설정이 필요합니다')
    engine = create_engine(url, pool_pre_ping=True, hide_parameters=True)
    try:
        result = indicator_batch_service.run(engine, args.item_id, args.as_of, args.validate)
        print(json.dumps(result, ensure_ascii=False))
        return 0 if result['status'] == 'SUCCESS' else 2
    except Exception as error:
        # DB URL이 들어갈 수 있어 예외 원문은 출력하지 않는다.
        print(json.dumps({'status': 'FAILED', 'errorCode': type(error).__name__}))
        return 1
    finally:
        engine.dispose()


if __name__ == '__main__':
    raise SystemExit(main())
