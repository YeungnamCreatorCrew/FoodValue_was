"""실행: uv run python -m app.krei_monthly [--start-year 2016] [--end-year 2026]

KREI 관측월보(양념채소·엽근채소) 목록과 PDF를 받아 external_observation(KREI, MONTHLY_REPORT)에 적재한다.
인증키는 필요 없고 pdftotext(poppler)가 있어야 한다. 기본값은 작년~올해(증분)다.
원본 PDF는 data/raw/krei_monthly/에 남는다(커밋하지 않음).
"""
import argparse
import json
import os
from pathlib import Path

from dotenv import load_dotenv

from app.core.db import make_engine
from app.services import collection_service
from app.core.dates import today

CACHE_DIR = Path('data/raw/krei_monthly')


def main():
    this_year = today().year
    parser = argparse.ArgumentParser(description='KREI 관측월보 수집')
    parser.add_argument('--start-year', type=int, default=this_year - 1)
    parser.add_argument('--end-year', type=int, default=this_year)
    parser.add_argument('--cache-dir', type=Path, default=CACHE_DIR)
    args = parser.parse_args()
    if not 2000 <= args.start_year <= args.end_year <= this_year:
        parser.error('연도는 2000 ≤ start ≤ end ≤ 올해여야 합니다')
    load_dotenv()
    url = os.getenv('DATABASE_URL')
    if not url:
        parser.error('DATABASE_URL 설정이 필요합니다')
    engine = make_engine(url)
    try:
        result = collection_service.collect_krei_monthly(engine, start_year=args.start_year, end_year=args.end_year,
                                                         cache_dir=args.cache_dir)
        print(json.dumps(result, ensure_ascii=False))
        return 0 if result['status'] in ('SUCCESS', 'NO_DATA') else 2
    finally:
        engine.dispose()


if __name__ == '__main__':
    raise SystemExit(main())
