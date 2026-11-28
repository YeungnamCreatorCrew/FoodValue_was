"""실행: python -m app.merged_series
배추·무 작형별 가격(price_daily)을 이어 붙여 품목 '배추'·'무'의 MERGED 계열을 만들고 다시 계산한다
(app.services.merged_series_service 참고). price_pipeline도 수집·정제 뒤 같은 일을 한다.
처음 한 번 실행한 뒤 배치를 돌린다: python -m app.price_batch --item-id <배추·무 품목 id>
"""
import json
import os

from dotenv import load_dotenv

from app.core.db import make_engine
from app.services import merged_series_service


def main():
    load_dotenv()
    url = os.getenv('DATABASE_URL')
    if not url:
        raise SystemExit('DATABASE_URL 설정이 필요합니다')
    engine = make_engine(url)
    print(json.dumps(merged_series_service.refresh(engine), ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
