"""실행: python -m app.garak_collect [--start 2021-01-01] [--end 2026-11-24]
가락시장 반입물량만 따로 수집해 item_production(ARRIVAL·DAY·GARAK)에 적재한다.

price_pipeline은 KAMIS·기상 등 모든 원천을 함께 받는다. 다른 원천이 막혀 있거나 반입량 과거치를 처음 채울 때 이 명령을 쓴다.
처음 실행하면 2021-01-01부터 받고(일요일 제외, 날짜당 1~2회 요청), 이후에는 마지막 수집일부터 이어 받는다.
.env의 GARAK_API_ID·GARAK_API_PASSWORD가 필요하다.
"""
import argparse
import json
import os
from datetime import date

from dotenv import load_dotenv

from app.core.db import make_engine
from app.collectors import garak
from app.services import collection_service, warehouse_service


def main(argv=None):
    parser = argparse.ArgumentParser(description='가락시장 반입물량 수집·적재')
    parser.add_argument('--start', type=date.fromisoformat, help='수집 시작일. 생략하면 이어 받기(처음이면 2021-01-01)')
    parser.add_argument('--end', type=date.fromisoformat, help='수집 종료일. 생략하면 오늘')
    args = parser.parse_args(argv)
    load_dotenv()
    url = os.getenv('DATABASE_URL')
    if not url:
        parser.error('DATABASE_URL 설정이 필요합니다')
    engine = make_engine(url)
    end = min(args.end or collection_service.today(), collection_service.today())
    items = collection_service.prediction_items(engine)
    run = collection_service.collect_garak(engine, items, args.start, end, collection_service.fetch_text,
                                           collection_service.Credentials.from_env())
    linked = sorted({item.name for item in items if garak.item_code(item.name)})
    stored = 0
    if run.get('startDate'):
        stored = warehouse_service.refresh_item_arrival(engine, [item.id for item in items],
                                                        since=date.fromisoformat(run['startDate']))
    print(json.dumps({'collection': run, 'linkedItems': linked, 'itemProductionRows': stored},
                     ensure_ascii=False, default=str))


if __name__ == '__main__':
    main()
