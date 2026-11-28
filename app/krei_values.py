"""실행: uv run python -m app.krei_values data/krei_values/OVR0000000036/8780.json [더 많은 파일 …]

KREI 관측월보 추출 결과 JSON을 krei_report_value에 upsert한다. 형식·규칙은 data/krei_values/README.md.
파일마다 결과를 한 줄 JSON으로 출력하고, 하나라도 실패하면 종료 코드 2.
"""
import argparse
import json
import os
from pathlib import Path

from dotenv import load_dotenv

from app.core.db import make_engine
from app.services import krei_value_service


def main():
    parser = argparse.ArgumentParser(description='KREI 관측월보 추출값 적재')
    parser.add_argument('files', nargs='+', type=Path)
    args = parser.parse_args()
    load_dotenv()
    url = os.getenv('DATABASE_URL')
    if not url:
        parser.error('DATABASE_URL 설정이 필요합니다')
    engine = make_engine(url)
    failed = False
    try:
        for path in args.files:
            try:
                result = {'file': str(path), 'status': 'SUCCESS', **krei_value_service.load_file(engine, path)}
            except (krei_value_service.ExtractionError, json.JSONDecodeError, OSError) as error:
                failed = True
                result = {'file': str(path), 'status': 'FAILED', 'error': str(error)}
            print(json.dumps(result, ensure_ascii=False))
        return 2 if failed else 0
    finally:
        engine.dispose()


if __name__ == '__main__':
    raise SystemExit(main())
