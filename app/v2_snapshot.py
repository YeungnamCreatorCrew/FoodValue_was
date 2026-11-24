"""실행: python -m app.v2_snapshot --as-of 2026-10-31 --out data/live/check-20261031 --compare data/snapshots/fv-snap-20261031-v1
DB에서 기준일까지 자료로 v2 입력 스냅샷 폴더를 만든다(app.services.v2_snapshot 참고).

--compare: 실험 스냅샷과 파일별로 비교한다. 같은 마감일로 만들어 모두 '같음'이면, 서비스가 DB에서 만드는 입력이
실험 때 입력과 같다는 뜻이다(생산량 파일은 만드는 방법이 달라 비교에서 뺀다).
"""
import argparse
import json
import os
from datetime import date
from pathlib import Path

from dotenv import load_dotenv
from sqlalchemy import create_engine

from app.services import v2_snapshot


def main(argv=None):
    parser = argparse.ArgumentParser(description='DB → v2 입력 스냅샷')
    parser.add_argument('--as-of', type=date.fromisoformat, required=True, help='기준일(이날까지 자료)')
    parser.add_argument('--out', type=Path, required=True)
    parser.add_argument('--replace', action='store_true', help='out이 있으면 지우고 다시 만든다')
    parser.add_argument('--compare', type=Path, help='비교할 실험 스냅샷 폴더')
    args = parser.parse_args(argv)
    load_dotenv()
    url = os.getenv('DATABASE_URL')
    if not url:
        parser.error('DATABASE_URL 설정이 필요합니다')
    engine = create_engine(url, pool_pre_ping=True, hide_parameters=True)
    manifest = v2_snapshot.build(engine, args.as_of, args.out, replace=args.replace)
    result = {'out': str(args.out), 'cutoff': manifest['cutoff'],
              'series': [f"{s['series_id']} {s['item']} {s['market']}" for s in manifest['series']]}
    if args.compare:
        diff = v2_snapshot.compare(args.out, args.compare)
        result['compare'] = {name: ('같음' if same else f'다름 ({rows_a}행 vs {rows_b}행)')
                             for name, (same, rows_a, rows_b) in diff.items()}
        result['allSame'] = all(same for same, _, _ in diff.values())
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
