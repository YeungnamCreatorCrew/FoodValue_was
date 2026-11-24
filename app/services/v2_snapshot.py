"""서비스용 v2 입력: DB → 실험과 같은 형식의 스냅샷 폴더(기준일까지 자료).

v2 앙상블 구성원(XGBoost·LightGBM·AutoARIMA)은 실험 때 tools.loader.Snapshot이 읽는 스냅샷 폴더로 학습·예측했다.
서비스에서 같은 특징을 만들려고 따로 변환 코드를 쓰지 않고, 실험 스냅샷을 만든 함수(tools.export_snapshot.build)를
마감일 = 기준일로 그대로 다시 쓴다. 그래서 같은 DB·같은 마감일이면 실험 스냅샷과 파일이 바이트 단위로 같아야 한다
(app.v2_snapshot --compare로 확인).

다른 점은 생산량 하나다. 실험 스냅샷은 KOSIS API를 직접 불러 item_production.csv를 만들었지만, 서비스는 네트워크 없이
DB에서 만든다(현재 앙상블 구성원은 PRODUCTION 묶음을 쓰지 않는다: configs/v1feat_*.json, autoarima config_p2_event).
DB item_production(KOSIS)이 품목 이름 차이로 비어 있으면 빈 파일이 된다.
"""
import shutil
from datetime import date
from pathlib import Path

from sqlalchemy import text

from tools import export_snapshot, snapshot, standard

PRODUCTION_QUERY = """
SELECT i.name, EXTRACT(YEAR FROM p.period_start)::int AS year, p.volume
FROM item_production p JOIN item i ON i.id = p.item_id
WHERE p.source = 'KOSIS' AND p.measure_type = 'PRODUCTION' AND p.period_type = 'YEAR' AND NOT p.is_estimate
ORDER BY i.name, year"""


def production_from_db(connection, cutoff: date):
    """[(실험 품목, 연도, 톤, 사용 시작일)]. 실험 스냅샷과 같은 규칙: 사용 시작일 = Y+1년 6월 30일, 마감일 이후 연도는 뺀다."""
    by_key = {key: item for item, key in snapshot.PRODUCTION_KEY.items()}
    rows = {}
    for name, year, volume in connection.execute(text(PRODUCTION_QUERY)):
        item = by_key.get(name) or (name if name in snapshot.PRODUCTION_KEY else None)
        usable = date(year + 1, 6, 30)
        if item and usable <= cutoff:
            rows[item, year] = (item, year, int(volume) if float(volume).is_integer() else float(volume), usable)
    return [rows[key] for key in sorted(rows, key=lambda k: (standard.ITEMS.index(k[0]), k[1]))]


def read_raw(engine, cutoff: date) -> dict:
    """export_snapshot.read_database와 같은 쿼리를 이미 만든 engine으로 실행한다(+ DB 생산량)."""
    raw = {}
    with engine.connect() as connection:
        for name, query in export_snapshot.QUERIES.items():
            raw[name] = [tuple(r) for r in connection.execute(text(query), {'cutoff': cutoff})]
        raw['production'] = production_from_db(connection, cutoff)
    return raw


def build(engine, as_of: date, out: Path, *, replace: bool = False) -> dict:
    """as_of까지의 DB 자료로 out에 스냅샷 폴더를 만든다. 반환: manifest."""
    out = Path(out)
    if replace and out.exists():
        shutil.rmtree(out)
    raw = read_raw(engine, as_of)
    manifest = export_snapshot.build(raw, out, cutoff=as_of,
                                     meta={'notes': ['서비스 입력(app.services.v2_snapshot): DB에서 기준일까지',
                                                     '생산량은 DB item_production(KOSIS)에서 만듦']})
    return manifest


def compare(left: Path, right: Path, *, skip=('item_production.csv',)) -> dict:
    """두 스냅샷 폴더의 자료 파일 SHA-256 비교. 반환: 파일 → (같음 여부, 왼쪽 행 수, 오른쪽 행 수)."""
    result = {}
    for name in snapshot.COLUMNS:
        if name in skip:
            continue
        a, b = Path(left) / name, Path(right) / name
        if not (a.exists() and b.exists()):
            result[name] = (False, None, None)
            continue
        result[name] = (snapshot.sha256(a) == snapshot.sha256(b), snapshot.count_rows(a), snapshot.count_rows(b))
    return result
