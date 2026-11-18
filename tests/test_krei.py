"""KREI 관측월보 목록·판권 해석. 실제 네트워크를 사용하지 않는다."""
from datetime import date, datetime
from pathlib import Path

import pytest

from app.collectors import krei
from app.collectors.http import CollectorError

GROUP = 'OVR0000000036'


def entry(mm='04', reg='20200331173806', pdf='7033', year='2020', group=GROUP):
    return {'yyyy': year, 'mm': mm, 'ovr_item_code': group, 'prt_ovr_item_code': 'OVR0000000093',
            'krei_item_code': '36', 'item_name': '양념채소', 'prt_item_name': '원예', 'title': '월보',
            'pdf_link': f'https://aglook.krei.re.kr/main/uObserveMonth/{group}/download/{pdf}/ORGTEXT_FILE',
            'description': None, 'reg_date': reg, 'mod_date': None}


def index_xml(*items):
    rows = ''.join('<item>' + ''.join(f'<{k}>{v or ""}</{k}>' for k, v in item.items()) + '</item>' for item in items)
    return f'<?xml version="1.0" encoding="UTF-8"?><channel><yyyy>2020</yyyy><mm></mm>{rows}</channel>'.encode()


IMPRINT_TEXT = ('본문 2019년 5월 1일 발행한 속보 참고\n' * 30 +
                '통권 제 941호 2020년 3월 31일 발행(월간·비매품) 정기간행물 등록번호\n')


def test_parse_index_and_pdf_id():
    rows = krei.parse_index(index_xml(entry()))
    assert rows[0]['mm'] == '04' and rows[0]['description'] is None
    assert krei.pdf_id(rows[0]['pdf_link']) == '7033'
    with pytest.raises(CollectorError):
        krei.parse_index(b'<html>maintenance</html>')


def test_imprint_prefers_issue_line():
    printed, raw, issue = krei.imprint(IMPRINT_TEXT)
    assert printed == date(2020, 3, 31) and issue == '941' and raw.startswith('2020년 3월 31일')


def test_availability_takes_later_value_including_reuploads():
    first = date(2020, 4, 1)
    moment, basis, accepted = krei.availability(first, date(2020, 3, 31), krei.parse_reg_date('20200331173806'))
    assert basis == 'REG_DATE' and accepted == ['IMPRINT', 'REG_DATE'] and moment.hour == 17
    # 늦은 재등록일도 보존하며 과거 인쇄일로 소급하지 않는다.
    moment, basis, _ = krei.availability(date(2021, 4, 1), date(2021, 3, 31), krei.parse_reg_date('20230510120000'))
    assert basis == 'REG_DATE' and moment == datetime(2023, 5, 10, 12, tzinfo=krei.SEOUL)
    # 이미지 PDF(판권 없음)는 그럴듯한 reg_date만 쓴다. 둘 다 없으면 UNKNOWN.
    assert krei.availability(date(2025, 4, 1), None, krei.parse_reg_date('20250402192725'))[1] == 'REG_DATE'
    assert krei.availability(date(2008, 4, 1), None, krei.parse_reg_date('20110315000000'))[0] == datetime(2011, 3, 15, tzinfo=krei.SEOUL)


def test_collect_downloads_parses_and_caches(tmp_path, monkeypatch):
    calls = []

    def fetch(url, params=None, timeout=None):
        calls.append(url)
        if url == krei.INDEX_URL:
            other = entry(group='OVR0000000008', pdf='1')  # 다른 묶음은 버린다.
            return index_xml(entry(), entry(mm='05', reg='20200501114128', pdf='7115'), other)
        return b'%PDF-1.4 fake' if '/7033/' in url else b''  # 7115는 서버가 빈 응답

    monkeypatch.setattr(krei, 'pdf_text', lambda path: IMPRINT_TEXT)
    monkeypatch.setattr(krei.shutil, 'which', lambda name: '/usr/bin/pdftotext')
    batch = krei.collect(fetch, groups=[GROUP], years=[2020], cache_dir=tmp_path)
    records = {r.key: r for r in batch.records}
    assert set(records) == {f'{GROUP}:7033', f'{GROUP}:7115'} and batch.requests == 3
    ok, empty = records[f'{GROUP}:7033'], records[f'{GROUP}:7115']
    assert ok.period_start == date(2020, 4, 1) and ok.period_end == date(2020, 4, 30)
    assert ok.payload['issue_no'] == '941' and ok.payload['text_status'] == 'OK' and ok.payload['pdf_sha256']
    assert ok.published_at.date() == date(2020, 3, 31)
    assert empty.payload['pdf_status'] == 'NOT_PDF' and empty.payload['text'] is None
    assert empty.published_at is not None and empty.payload['published_basis'] == 'REG_DATE'
    assert (tmp_path / GROUP / '7033.pdf').exists() and not (tmp_path / GROUP / '7115.pdf').exists()
    calls.clear()
    krei.collect(fetch, groups=[GROUP], years=[2020], cache_dir=tmp_path)
    assert not any('/7033/' in url for url in calls)  # 캐시 재사용


def test_download_rejects_foreign_host(tmp_path):
    with pytest.raises(CollectorError):
        krei.download(lambda *a, **k: b'%PDF', 'https://evil.example/x.pdf', tmp_path / 'x.pdf')


def test_missing_pdftotext_fails_fast(tmp_path, monkeypatch):
    monkeypatch.setattr(krei.shutil, 'which', lambda name: None)
    with pytest.raises(CollectorError, match='PDFTOTEXT_NOT_FOUND'):
        krei.collect(lambda *a, **k: b'', groups=[GROUP], years=[2020], cache_dir=Path(tmp_path))
