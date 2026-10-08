"""실행: python -m app.price_batch --item-id 1. OS 스케줄러에서 하루 1회 호출한다."""
import argparse
import json
import os

from dotenv import load_dotenv
from sqlalchemy import create_engine

from app.core.constants import ID_MAX
from app.services import price_batch_service


def main():
    parser=argparse.ArgumentParser(description='KAMIS 원물 전국 소매가 7일 예측')
    parser.add_argument('--item-id',type=int,required=True)
    args=parser.parse_args()
    if not 1<=args.item_id<=ID_MAX:
        parser.error('item-id는 양의 BIGINT 범위여야 합니다')
    load_dotenv()
    url=os.getenv('DATABASE_URL')
    if not url:
        parser.error('DATABASE_URL 설정이 필요합니다')
    engine=create_engine(url,pool_pre_ping=True,hide_parameters=True)
    try:
        result=price_batch_service.run(engine,args.item_id)
        print(json.dumps(result,ensure_ascii=False))
        return 0 if result['status']=='SUCCESS' else 2
    except price_batch_service.BatchBusyError:
        print(json.dumps({'status':'BUSY'}))
        return 3
    except Exception as error:
        # DB URL·외부 설정이 포함될 수 있어 예외 원문은 출력하지 않는다.
        print(json.dumps({'status':'FAILED','errorCode':type(error).__name__}))
        return 1
    finally:
        engine.dispose()


if __name__=='__main__':
    raise SystemExit(main())
