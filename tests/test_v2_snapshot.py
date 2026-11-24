from datetime import date

from app.services import v2_snapshot
from tools import snapshot


class FakeConnection:
    def __init__(self, rows):
        self.rows = rows

    def execute(self, query):
        return self.rows


def test_production_from_db_maps_names_and_applies_publication_rule():
    rows = [('대파', 2024, 3100), ('마늘', 2024, 300.5), ('배추', 2025, 2000), ('토마토', 2024, 10)]
    got = v2_snapshot.production_from_db(FakeConnection(rows), date(2026, 6, 30))
    # 깐마늘은 KOSIS 이름 '마늘'로 들어온다. 2025년 자료는 2026-06-30부터 쓸 수 있다. 실험 품목이 아니면 뺀다.
    assert got == [('대파', 2024, 3100, date(2025, 6, 30)), ('깐마늘', 2024, 300.5, date(2025, 6, 30)),
                   ('배추', 2025, 2000, date(2026, 6, 30))]
    assert v2_snapshot.production_from_db(FakeConnection(rows), date(2026, 6, 29))[-1][0] == '깐마늘'


def test_compare_reports_same_and_different_files(tmp_path):
    left, right = tmp_path / 'a', tmp_path / 'b'
    left.mkdir(), right.mkdir()
    for name in snapshot.COLUMNS:
        (left / name).write_text('h\n1\n', encoding='utf-8')
        (right / name).write_text('h\n1\n', encoding='utf-8')
    (right / 'price_daily.csv').write_text('h\n1\n2\n', encoding='utf-8')
    result = v2_snapshot.compare(left, right)
    assert 'item_production.csv' not in result
    assert result['price_daily.csv'] == (False, 1, 2) and result['calendar_day.csv'][0] is True
