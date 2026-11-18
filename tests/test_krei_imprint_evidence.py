"""원본 PDF를 제외한 검토된 판권 근거로 119호와 SHA-bound OCR fallback을 회귀 검증한다."""
import copy
import hashlib
import json
from datetime import date
from pathlib import Path

import pytest

from app.collectors import krei
from app.collectors.http import CollectorError
from tests.test_krei import entry, index_xml

EVIDENCE_PATH = Path('data/krei_values/handoff_20261118/date_handling_20261118/imprint_evidence119.json')
PACKETS = json.loads(EVIDENCE_PATH.read_text(encoding='utf-8'))['reports']


@pytest.mark.parametrize('packet', PACKETS, ids=[p['source_record_key'] for p in PACKETS])
def test_reviewed_monthly_colophon_corpus(packet):
    group, pdf_id = packet['source_record_key'].split(':')
    document = json.loads(Path(f'data/krei_values/{group}/{pdf_id}.json').read_text(encoding='utf-8'))
    assert packet['pdf_sha256'] == document['pdf_sha256']
    printed, raw, _ = krei.imprint_with_evidence('', pdf_sha256=document['pdf_sha256'],
        source_record_key=document['source_record_key'], evidence=packet)
    assert printed == date.fromisoformat(packet['expected_imprint_date'])
    assert raw in packet['text'].replace('\n', ' ')


def packet_for(body=b'%PDF-local-test'):
    text = '통권 제1420호 2026년 11월 3일 발행(월간·비매품) 등록번호 2024.9.10'
    return {'source_record_key': 'OVR0000000036:8780', 'pdf_sha256': hashlib.sha256(body).hexdigest(),
            'page': 1, 'method': 'FOCUSED_COVER_OCR', 'review_status': 'SOURCE_IMAGE_REVIEWED',
            'text': text, 'text_sha256': hashlib.sha256(text.encode()).hexdigest(),
            'expected_imprint_date': '2026-11-03'}


@pytest.mark.parametrize('change', [
    {'pdf_sha256': '0' * 64}, {'source_record_key': 'OVR0000000008:8786'},
    {'page': 2}, {'page': True}, {'method': 'GUESS'}, {'review_status': 'UNREVIEWED'},
    {'text_sha256': '0' * 64}, {'text': '임의로 날짜 보충'}, {'text': None},
    {'expected_imprint_date': '2026-11-04'},
])
def test_rejects_mismatched_or_unreviewed_evidence(change):
    packet = packet_for()
    with pytest.raises(CollectorError):
        krei.imprint_with_evidence('', pdf_sha256=packet['pdf_sha256'],
            source_record_key=packet['source_record_key'], evidence={**packet, **change})


def test_rejects_later_page_and_missing_colophon_even_with_matching_text_hash():
    packet = packet_for()
    for content in ('\f' + packet['text'], '본문 2026년 11월 3일 발행'):
        bad = {**packet, 'text': content, 'text_sha256': hashlib.sha256(content.encode()).hexdigest()}
        with pytest.raises(CollectorError):
            krei.imprint_with_evidence('', pdf_sha256=packet['pdf_sha256'], source_record_key=packet['source_record_key'], evidence=bad)


def test_valid_native_date_cannot_be_overwritten_by_ocr():
    packet = packet_for()
    with pytest.raises(CollectorError, match='CONFLICTING'):
        krei.imprint_with_evidence('통권 제1419호 2026년 11월 4일 발행',
            pdf_sha256=packet['pdf_sha256'], source_record_key=packet['source_record_key'], evidence=packet)


def test_hidden_conflicting_layers_require_reviewed_raster_colophon():
    packet = next(p for p in PACKETS if p['source_record_key'].endswith(':7654'))
    native = '통권 제991호 2020년 11월 23일 발행\n통권 제1010호 2021년 3월 31일 발행'
    assert krei.imprint(native)[0] is None
    for bad in ({**packet, 'method': 'CACHED_COVER_OCR'},
                {**packet, 'review_status': 'PRIOR_VERIFIED_MANIFEST_MATCH'}):
        with pytest.raises(CollectorError, match='AMBIGUOUS'):
            krei.imprint_with_evidence(native, pdf_sha256=packet['pdf_sha256'], source_record_key=packet['source_record_key'], evidence=bad)
    assert krei.imprint_with_evidence(native, pdf_sha256=packet['pdf_sha256'],
        source_record_key=packet['source_record_key'], evidence=packet)[0] == date(2021, 3, 31)


def test_report_record_keeps_api_maximum_and_evidence_without_numeric_json_change():
    body = b'%PDF-local-test'
    packet = packet_for(body)
    e = entry(mm='11', reg='20261104160559', pdf='8780', year='2026')
    record = krei.report_record(e, 'OVR0000000036', body, '', cover_evidence=packet)
    assert record.payload['imprint_date'] == '2026-11-03'
    assert record.payload['reg_date'] == e['reg_date']
    assert record.published_at.isoformat() == record.payload['available_from'] == '2026-11-04T16:05:59+09:00'
    assert record.payload['imprint_evidence']['text_sha256'] == packet['text_sha256']
    assert record.payload['text_status'] == 'NO_TEXT'
    assert record.payload['automatic_training_approval'] is False
    with pytest.raises(CollectorError):
        krei.report_record(e, 'OVR0000000036', None, '', cover_evidence=packet)


def test_collect_uses_explicit_same_sha_evidence_and_rejects_wrong_cached_pdf(tmp_path, monkeypatch):
    body = b'%PDF-local-test'
    packet = packet_for(body)
    e = entry(mm='11', reg='20261102000000', pdf='8780', year='2026')
    def fetch(url, params=None, timeout=None):
        return index_xml(e) if url == krei.INDEX_URL else body
    monkeypatch.setattr(krei, 'pdf_text', lambda path: '')
    monkeypatch.setattr(krei.shutil, 'which', lambda name: 'pdftotext')
    evidence = {packet['source_record_key']: packet}
    batch = krei.collect(fetch, groups=['OVR0000000036'], years=[2026], cache_dir=tmp_path, cover_evidence=evidence)
    assert len(batch.records) == 1 and batch.records[0].published_at.date() == date(2026, 11, 3)
    bad = copy.deepcopy(evidence);bad[packet['source_record_key']]['pdf_sha256'] = '0' * 64
    with pytest.raises(CollectorError):
        krei.collect(fetch, groups=['OVR0000000036'], years=[2026], cache_dir=tmp_path, cover_evidence=bad)
