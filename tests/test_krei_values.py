"""KREI 관측월보 추출 JSON 검증. DB를 쓰지 않는다."""
import json
from pathlib import Path

import pytest

from app.services.krei_value_service import ExtractionError, parse_document, validate_value

BASE = {'item_name': '대파', 'metric': 'SHIPMENT', 'kind': 'OUTLOOK', 'target_start': '2026-11-01',
        'target_end': '2026-11-30', 'basis': 'PREV_YEAR', 'value': 1.5, 'unit': '%', 'direction': 'UP', 'evidence': '전년 대비 1.5% 증가'}


def doc(*values):
    return {'source_record_key': 'OVR0000000036:8780', 'pdf_sha256': 'a' * 64, 'extractor': 'claude', 'extractor_version': 'v1',
            'values': list(values) or [BASE]}


def test_relative_value_needs_explicit_direction_and_range_midpoint():
    with pytest.raises(ExtractionError, match='direction'):
        validate_value({**BASE, 'value': -0.1, 'direction': None}, 0)  # "평년과 비슷"을 부호로 DOWN 처리하지 않는다.
    assert validate_value({**BASE, 'value': -0.1, 'direction': 'FLAT'}, 0)['direction'] == 'FLAT'
    row = validate_value({**BASE, 'basis': 'LEVEL', 'value': None, 'value_low': 1330, 'value_high': 1390,
                          'unit': '원/kg', 'direction': None}, 0)
    assert row['value'] == 1360 and row['direction'] is None


@pytest.mark.parametrize('change, message', [
    ({'metric': 'PRICE'}, 'metric'),
    ({'value': None, 'direction': None}, 'value와 direction'),
    ({'unit': None}, 'unit'),
    ({'unit': '원/kg'}, '% 또는 %p'),
    ({'basis': 'LEVEL'}, 'LEVEL 값에 %'),
    ({'target_end': '2026-10-31'}, 'target_end'),
    ({'value_low': 1}, '같이 채움'),
    ({'published_at': '2026-11-03'}, '알 수 없는 필드'),  # 발표 시점은 원본 호에서만 온다.
    ({'evidence': ' '}, 'evidence'),
])
def test_rejects_invalid_values(change, message):
    with pytest.raises(ExtractionError, match=message):
        validate_value({**BASE, **change}, 0)


def test_rejects_duplicate_fact_in_one_document():
    with pytest.raises(ExtractionError, match='두 번'):
        parse_document(doc(BASE, {**BASE, 'value': 2.0}))
    # 같은 항목이라도 작형이 다르면 다른 사실이다.
    assert len(parse_document(doc(BASE, {**BASE, 'crop_type': '신선'}))[4]) == 2


def test_committed_extraction_files_are_valid():
    files = sorted(Path('data/krei_values').glob('*/*.json'))
    assert files
    for path in files:
        key, _, _, _, rows = parse_document(json.loads(path.read_text(encoding='utf-8')))
        assert key == f'{path.parent.name}:{path.stem}' and rows


def test_unmapped_is_checked_but_not_loaded():
    document = {**doc(), 'unmapped': [{'item_name': '양파', 'what': '수급 단계', 'evidence': "'안정' 단계"}]}
    assert len(parse_document(document)[4]) == 1
    with pytest.raises(ExtractionError, match='unmapped'):
        parse_document({**doc(), 'unmapped': [{'evidence': 'what 없음'}]})
    with pytest.raises(ExtractionError, match='최상위'):
        parse_document({**doc(), 'published_at': '2026-11-03'})
