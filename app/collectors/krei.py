"""한국농촌경제연구원(KREI) 농업관측본부 관측월보 → external_observation(KREI, MONTHLY_REPORT).

연동 명세: 농업관측본부 「관측월보, 속보 XML 연동 v1.0」(2021-09-24). 인증키 없이 공개된 GET API다.
- 목록 XML(montlyReport)은 품목 묶음 단위로 온다. 대파·양파·마늘은 양념채소(OVR0000000036),
  배추·무는 엽근채소(OVR0000000008)로 조회해야 한다. 개별 품목 코드(대파 OVR0000000004)로는 결과가 없다.
- XML에는 수치가 없고 PDF 링크만 있다. PDF를 받아 텍스트(pdftotext)와 판권의 발행일을 함께 저장한다.
  수치 추출은 별도 단계에서 이 텍스트(또는 원본 PDF)로 한다.

발표 시점(published_at)
- 판권 "YYYY년 M월 D일 발행"과 목록의 reg_date(홈페이지 등록일시) 중 그럴듯한 값의 늦은 쪽을 쓴다(보수적).
- reg_date에는 일괄 재등록일(예: 2006~2009호가 2011-03-15, 2021호 일부가 2023-05-10)이 섞여 있다.
  그래서 두 값 모두 해당 호 월 기준 [월초 − PLAUSIBLE_LEAD_DAYS, 월말] 안에 있을 때만 인정한다.
- 둘 다 인정되지 않으면 published_at을 비워 UNKNOWN으로 남긴다(과거 모델에서 쓰지 않는다).
"""
import calendar
import hashlib
import re
import shutil
import subprocess
import xml.etree.ElementTree as ET
from datetime import date, datetime, timedelta
from pathlib import Path
from urllib.parse import urlparse
from zoneinfo import ZoneInfo

from app.collectors.http import CollectorError
from app.collectors.records import Record, gather

INDEX_URL = 'https://aglook.krei.re.kr/main/api/montlyReport'
PDF_HOST = 'aglook.krei.re.kr'
SOURCE, DATASET = 'KREI', 'MONTHLY_REPORT'
# 예측 대상 품목이 속한 월보 묶음
GROUPS = {'OVR0000000036': '양념채소', 'OVR0000000008': '엽근채소'}
PLAUSIBLE_LEAD_DAYS = 40  # 월보는 전월 말~당월 초에 나온다.
MIN_TEXT_CHARS = 500  # 이보다 짧으면 이미지 PDF로 보고 text_status=NO_TEXT
INDEX_TIMEOUT, PDF_TIMEOUT = 30, 180
PDFTOTEXT_TIMEOUT = 120
SEOUL = ZoneInfo('Asia/Seoul')
INDEX_FIELDS = ('yyyy', 'mm', 'ovr_item_code', 'prt_ovr_item_code', 'krei_item_code', 'item_name', 'prt_item_name',
                'title', 'pdf_link', 'description', 'reg_date', 'mod_date')

IMPRINT = re.compile(r'(\d{4})\s*년\s*(\d{1,2})\s*월\s*(\d{1,2})\s*일\s*발행')
ISSUE_NO = re.compile(r'통권\s*제?\s*(\d+)\s*호')
PDF_ID = re.compile(r'/download/(\d+)/')


def text(node, name):
    value = node.findtext(name)
    value = value.strip() if value else ''
    return value or None


def parse_index(body: bytes):
    """목록 XML → 항목 dict 목록. 구조가 다르면 CollectorError."""
    try:
        root = ET.fromstring(body)
    except ET.ParseError:
        raise CollectorError('KREI_NON_XML_RESPONSE') from None
    if root.tag != 'channel':
        raise CollectorError('KREI_UNEXPECTED_RESPONSE')
    return [{name: text(item, name) for name in INDEX_FIELDS} for item in root.findall('item')]


def pdf_id(link):
    match = PDF_ID.search(link or '')
    return match[1] if match else None


def parse_reg_date(value):
    try:
        return datetime.strptime(value, '%Y%m%d%H%M%S').replace(tzinfo=SEOUL) if value else None
    except ValueError:
        return None


def issue_month(entry):
    try:
        return date(int(entry['yyyy']), int(entry['mm']), 1)
    except (TypeError, ValueError):
        return None


def month_end(first: date):
    return first.replace(day=calendar.monthrange(first.year, first.month)[1])


def plausible(moment, first: date):
    if moment is None:
        return False
    day = moment.date() if isinstance(moment, datetime) else moment
    return first - timedelta(days=PLAUSIBLE_LEAD_DAYS) <= day <= month_end(first)


def imprint(content: str):
    """판권의 발행일과 통권 호수. 통권이 있는 줄의 발행일을 우선한다."""
    lines = content.splitlines()
    issue = next((ISSUE_NO.search(line) for line in lines if ISSUE_NO.search(line)), None)
    candidates = [line for line in lines if ISSUE_NO.search(line)] + lines
    for line in candidates:
        match = IMPRINT.search(line)
        if match:
            try:
                return date(int(match[1]), int(match[2]), int(match[3])), match[0], issue[1] if issue else None
            except ValueError:
                continue
    return None, None, issue[1] if issue else None


def availability(first: date, printed: date | None, registered: datetime | None):
    """(published_at, 채택 근거, 인정된 후보 목록). 인정된 후보 중 늦은 값."""
    candidates = []
    if plausible(printed, first):
        candidates.append((datetime(printed.year, printed.month, printed.day, tzinfo=SEOUL), 'IMPRINT'))
    if plausible(registered, first):
        candidates.append((registered, 'REG_DATE'))
    if not candidates:
        return None, None, []
    moment, basis = max(candidates)
    return moment, basis, [name for _, name in candidates]


def pdf_text(path: Path):
    binary = shutil.which('pdftotext')
    if binary is None:
        raise CollectorError('PDFTOTEXT_NOT_FOUND')
    try:
        result = subprocess.run([binary, '-enc', 'UTF-8', str(path), '-'], capture_output=True,
                                timeout=PDFTOTEXT_TIMEOUT, check=False)
    except subprocess.TimeoutExpired:
        return None
    if result.returncode != 0:
        return None
    # PostgreSQL JSONB는 \u0000을 받지 않는다.
    return result.stdout.decode('utf-8', errors='replace').replace('\x00', '')


def download(fetch_bytes, link, path: Path):
    """캐시에 있으면 재사용한다. PDF가 아니면 None."""
    if path.exists() and path.stat().st_size:
        return path.read_bytes()
    if urlparse(link).hostname != PDF_HOST:
        raise CollectorError('KREI_UNEXPECTED_PDF_HOST')
    body = fetch_bytes(link, timeout=PDF_TIMEOUT)
    if not body.startswith(b'%PDF'):
        return None
    path.parent.mkdir(parents=True, exist_ok=True)
    partial = path.with_suffix('.part')
    partial.write_bytes(body)
    partial.replace(path)
    return body


def report_record(entry, group, body, content):
    first = issue_month(entry)
    printed, imprint_raw, issue_no = imprint(content or '')
    registered = parse_reg_date(entry['reg_date'])
    published_at, basis, accepted = availability(first, printed, registered)
    chars = len((content or '').strip())
    payload = {**entry, 'pdf_id': pdf_id(entry['pdf_link']),
               'pdf_sha256': hashlib.sha256(body).hexdigest() if body else None,
               'pdf_bytes': len(body) if body else None,
               'pdf_status': 'OK' if body else 'NOT_PDF',
               'text_status': 'OK' if chars >= MIN_TEXT_CHARS else 'NO_TEXT' if body else None,
               'text': content if chars >= MIN_TEXT_CHARS else None,
               'imprint_date': printed.isoformat() if printed else None, 'imprint_raw': imprint_raw,
               'issue_no': issue_no, 'published_basis': basis, 'published_candidates': accepted}
    record = Record(SOURCE, DATASET, f'{group}:{payload["pdf_id"]}', payload, observed_on=first,
                    entity_code=group, entity_name=GROUPS.get(group, entry['item_name']))
    record.period_start, record.period_end = first, month_end(first)
    record.published_at = published_at
    return record


def collect(fetch_bytes, *, groups, years, cache_dir: Path, workers=3):
    """묶음·연도별 목록을 받고 각 호의 PDF를 받아 레코드로 만든다. PDF는 cache_dir/{묶음}/{id}.pdf에 남긴다."""
    if shutil.which('pdftotext') is None:
        raise CollectorError('PDFTOTEXT_NOT_FOUND')

    def index(group, year):
        def run():
            body = fetch_bytes(INDEX_URL, {'yyyy': year, 'ovr_item_code': group}, timeout=INDEX_TIMEOUT)
            # 묶음 코드로 조회해도 다른 묶음이 섞이지 않는지 확인한다.
            return [entry for entry in parse_index(body) if entry['ovr_item_code'] == group
                    and pdf_id(entry['pdf_link']) and issue_month(entry)]
        return run

    found, requests = [], 0
    for group in groups:
        for year in years:
            found += [(group, entry) for entry in index(group, year)()]
            requests += 1

    def report(group, entry):
        def run():
            path = cache_dir / group / f'{pdf_id(entry["pdf_link"])}.pdf'
            body = download(fetch_bytes, entry['pdf_link'], path)
            content = pdf_text(path) if body else None
            return [report_record(entry, group, body, content)]
        return run

    batch = gather((report(group, entry) for group, entry in found), workers)
    batch.requests += requests
    return batch
