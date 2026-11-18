"""네트워크/실제 DB 없이 판권 범위·날짜 정책·원본 근거를 회귀 검증한다."""
from datetime import date, datetime

import pytest

from app.collectors import krei


@pytest.mark.parametrize('content, expected', [
    ('통권 제 319호 2025년 7월 4일 발행(월간·비매품)', date(2025, 7, 4)),
    ('통권발행·편집인/원장제1319호 2025년한두봉7월발행처4일 발행(월간·비매품)', date(2025, 7, 4)),
    ('통권 제319호\n2025년 7월 4일 발행', date(2025, 7, 4)),
    ('본문 2023년 4월 3일 발행한 자료 참고\n통권 제319호 2025년 7월 4일 발행 등록번호 2024.9.10', date(2025, 7, 4)),
    ('본문 2025년 7월 4일 발행', None),
    ('통권 제319호\n본문 2025년 7월 4일 발행한 자료를 참고', None),
    ('표지 날짜 없음\f통권 제319호 2025년 7월 4일 발행', None),
    ('통권 제319호 등록번호 2025년 7월 4일 발행', None),
    ('통권 제319호 2025년 2월 30일 발행', None),
    ('통권 제319호 2025년 2월 30일 발행 / 2025년 3월 1일 발행', None),
    # 7654에는 이전 호 판권과 새 판권의 텍스트 레이어가 겹친다. 이전 날짜를 채택하지 않는다.
    ('통권통권 제제 991호1010호2020년2021년11월3월 23일31일 발행(월간·비매품)발행(월간·비매품)', None),
    ('통권 제319호 2025년 7월 일 발행', None),
    ('통권 제319호 2025년 7월 4일', None),
    ('통권 제319호 2025년 7월 4일 발행 / 2025년 7월 5일 발행', None),
    ('통권 제319호 2025년 ' + '한' * 25 + '7월 4일 발행', None),
])
def test_colophon_scoped_extraction(content, expected):
    printed, raw, _ = krei.imprint(content)
    assert printed == expected
    if expected:
        assert raw in content.replace('\n', ' ') and '발행' in raw


@pytest.mark.parametrize('printed, api, expected, basis', [
    (date(2025, 7, 4), '20250702160559', '2025-07-04T00:00:00+09:00', 'IMPRINT'),
    (date(2025, 7, 2), '20250704160559', '2025-07-04T16:05:59+09:00', 'REG_DATE'),
    (date(2025, 7, 4), '20250704160559', '2025-07-04T16:05:59+09:00', 'REG_DATE'),
    (date(2025, 7, 4), '20250704000000', '2025-07-04T00:00:00+09:00', 'REG_DATE'),
    (None, '20250702160559', '2025-07-02T16:05:59+09:00', 'REG_DATE'),
    (date(2021, 3, 31), '20230510120000', '2023-05-10T12:00:00+09:00', 'REG_DATE'),
    (None, None, None, None),
])
def test_maximum_date_policy(printed, api, expected, basis):
    moment, actual_basis, _ = krei.availability(date(2025, 7, 1), printed, krei.parse_reg_date(api))
    assert (moment.isoformat() if moment else None) == expected
    assert actual_basis == basis


@pytest.mark.parametrize('raw', [None, '', 20250704000000, '20250230000000', '20250704', '20250704129999'])
def test_invalid_api_timestamp(raw):
    assert krei.parse_reg_date(raw) is None


def test_payload_keeps_api_and_discloses_unknown_imprint():
    entry = {'yyyy': '2025', 'mm': '07', 'reg_date': '20250702160559'}
    meta = krei.date_metadata(entry, None, None, None)
    assert entry['reg_date'] == '20250702160559'
    assert meta['api_registered_at'] == meta['available_from'] == '2025-07-02T16:05:59+09:00'
    assert meta['imprint_status'] == 'UNCONFIRMED'
    assert meta['available_from_status'] == 'PROVISIONAL_API_ONLY'
    assert meta['automatic_training_approval'] is False
    assert meta['historical_pdf_version_verified'] is False


def test_pdf8583_record_consistency_and_repeatability():
    entry = {'yyyy': '2025', 'mm': '07', 'reg_date': '20250702160559',
             'pdf_link': 'https://aglook.krei.re.kr/main/uObserveMonth/OVR0000000008/download/8583/ORGTEXT_FILE',
             'item_name': '엽근채소'}
    cover = '통권발행·편집인/원장제1319호 2025년한두봉7월발행처4일 발행(월간·비매품)'
    first = krei.report_record(entry, 'OVR0000000008', b'%PDF', cover)
    second = krei.report_record(entry, 'OVR0000000008', b'%PDF', cover)
    assert first == second
    assert first.published_at.isoformat() == first.payload['available_from'] == '2025-07-04T00:00:00+09:00'
    assert first.payload['reg_date'] == '20250702160559'
    assert first.payload['imprint_date'] == '2025-07-04'
    assert '한두봉' in first.payload['imprint_raw']
