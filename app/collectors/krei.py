"""한국농촌경제연구원(KREI) 농업관측본부 관측월보 → external_observation(KREI, MONTHLY_REPORT).

연동 명세: 농업관측본부 「관측월보, 속보 XML 연동 v1.0」(2021-09-24). 인증키 없이 공개된 GET API다.
- 목록 XML(montlyReport)은 품목 묶음 단위로 온다. 대파·양파·마늘은 양념채소(OVR0000000036),
  배추·무는 엽근채소(OVR0000000008)로 조회해야 한다. 개별 품목 코드(대파 OVR0000000004)로는 결과가 없다.
- XML에는 수치가 없고 PDF 링크만 있다. PDF를 받아 텍스트(pdftotext)와 판권의 발행일을 함께 저장한다.
  수치 추출은 별도 단계에서 이 텍스트(또는 원본 PDF)로 한다.

발표 시점(published_at)
- published_at은 기존과 같이 보수적인 발표 후보다. 실제 최초 공개 시각을 증명하지 않는다.
- API 등록시각과 PDF 인쇄일(서울 자정 표현)의 최댓값을 쓰며 늦은 재등록일도 버리지 않는다.
- reg_date 원문, imprint_date/원문, available_from/정책/미확인 상태는 payload에 별도 보존한다.
- 인쇄일 미확인 시 API 임시 후보를 쓰며 과거 학습을 자동 승인하지 않는다.
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

# 열 혼입 복구는 표지 판권(통권 호수 뒤, 등록번호 앞)에서만 허용한다.
INTERLEAVED_IMPRINT = re.compile(r'(?<![0-9])([0-9]{4})\s*년[^0-9\n]{0,24}([0-9]{1,2})\s*월[^0-9\n]{0,24}([0-9]{1,2})\s*일\s*발행')
DATE_POLICY = 'MAX_API_REGISTERED_PDF_IMPRINT_V1'

IMPRINT = re.compile(r'(\d{4})\s*년\s*(\d{1,2})\s*월\s*(\d{1,2})\s*일\s*발행')
ISSUE_NO = re.compile(r'통권[^0-9\n]{0,30}([0-9]+)\s*호')
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
    if not isinstance(value, str) or not re.fullmatch(r'[0-9]{14}', value):
        return None
    try:
        return datetime.strptime(value, '%Y%m%d%H%M%S').replace(tzinfo=SEOUL)
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
    """첫 페이지 판권만 해석한다. 본문/등록번호 날짜는 후보로 쓰지 않는다.

    통권 뒤 최대 240자, 최대 4줄 안에서만 열 혼입 문자를 허용한다.
    여러 유효 날짜가 충돌하면 추정하지 않는다. raw에는 혼입 원문도 보존한다.
    """
    cover = content.split('\f', 1)[0]
    issues = list(ISSUE_NO.finditer(cover))
    issue = issues[0][1] if issues else None
    found = []
    for marker in issues:
        region = cover[marker.end():marker.end() + 240]
        region = '\n'.join(region.splitlines()[:4])
        region = re.split(r'등록\s*번호|등록일|디자인|인쇄_', region, maxsplit=1)[0]
        # 줄바꿈만 합쳐 열 사이의 인명/발행처를 그대로 근거에 남긴다.
        compact_lines = region.replace('\n', ' ')
        if not re.match(r'\s*[0-9]{4}\s*년', compact_lines):
            continue
        for match in INTERLEAVED_IMPRINT.finditer(compact_lines):
            try:
                day = date(*map(int, match.groups()))
            except ValueError:
                return None, None, issue
            found.append((day, match[0], marker[1]))
    if len({day for day, _, _ in found}) == 1:
        return found[0]
    return None, None, issue


def imprint_with_evidence(content, *, pdf_sha256, source_record_key, evidence=None):
    """동일 PDF 표지의 검토된 OCR만 명시적으로 재사용한다. OCR 엔진을 실행하지 않는다.

    숫자를 보정하거나 API로 인쇄일을 추정하지 않는다. 원문·SHA·페이지·검토상태가
    맞지 않거나 유효한 native 판권과 충돌하면 수집을 거부한다.
    """
    native = imprint(content)
    if evidence is None:
        return native
    if not isinstance(evidence, dict):
        raise CollectorError('KREI_INVALID_IMPRINT_EVIDENCE')
    text = evidence.get('text')
    if (evidence.get('source_record_key') != source_record_key
            or not pdf_sha256 or evidence.get('pdf_sha256') != pdf_sha256
            or type(evidence.get('page')) is not int or evidence['page'] != 1
            or evidence.get('method') not in ('NATIVE_COVER_TEXT', 'CACHED_COVER_OCR', 'FOCUSED_COVER_OCR')
            or evidence.get('review_status') not in ('PRIOR_VERIFIED_MANIFEST_MATCH', 'SOURCE_IMAGE_REVIEWED')
            or not isinstance(text, str) or not 1 <= len(text) <= 2000
            or '\f' in text
            or hashlib.sha256(text.encode('utf-8')).hexdigest() != evidence.get('text_sha256')):
        raise CollectorError('KREI_INVALID_IMPRINT_EVIDENCE')
    parsed = imprint(text)
    if parsed[0] is None or parsed[0].isoformat() != evidence.get('expected_imprint_date'):
        raise CollectorError('KREI_UNCONFIRMED_IMPRINT_EVIDENCE')
    if native[0] is not None and native[0] != parsed[0]:
        raise CollectorError('KREI_CONFLICTING_IMPRINT_EVIDENCE')
    # 충돌하는 숨은 텍스트를 대신하려면 실제 렌더링한 표지 OCR의 이미지 검토가 필요하다.
    if native[0] is None and content.strip() and len(list(ISSUE_NO.finditer(content.split('\f', 1)[0]))) > 1:
        if evidence['method'] != 'FOCUSED_COVER_OCR' or evidence['review_status'] != 'SOURCE_IMAGE_REVIEWED':
            raise CollectorError('KREI_AMBIGUOUS_NATIVE_IMPRINT')
    return parsed


def availability(first: date, printed: date | None, registered: datetime | None):
    """기존 published_at 후보 계약: API 시각과 인쇄일의 늦은 값.

    날짜만 있는 인쇄일은 프로젝트 규칙에 따라 서울 자정으로 표현한다.
    호 월 밖의 등록시각도 버리지 않는다(재등록을 과거로 소급하지 않음).
    """
    candidates = []
    if printed is not None:
        candidates.append((datetime(printed.year, printed.month, printed.day, tzinfo=SEOUL), 'IMPRINT'))
    if registered is not None:
        candidates.append((registered, 'REG_DATE'))
    if not candidates:
        return None, None, []
    moment, basis = max(candidates)
    return moment, basis, [name for _, name in candidates]


def date_metadata(entry, printed, raw, issue_no):
    """추출 JSON 계약을 바꾸지 않고 원본 payload에 세 날짜와 한계를 구분한다."""
    first = issue_month(entry)
    registered = parse_reg_date(entry.get('reg_date'))
    moment, basis, accepted = availability(first, printed, registered)
    return {
        'imprint_date': printed.isoformat() if printed else None, 'imprint_raw': raw,
        'issue_no': issue_no, 'published_basis': basis, 'published_candidates': accepted,
        'api_registered_at': registered.isoformat() if registered else None,
        'available_from': moment.isoformat() if moment else None,
        'available_from_policy': DATE_POLICY,
        'imprint_status': 'EXTRACTED' if printed else 'UNCONFIRMED',
        'available_from_status': ('METADATA_CANDIDATE' if printed else
                                  'PROVISIONAL_API_ONLY' if registered else 'UNKNOWN'),
        'pdf_date_time_assumption': 'ASIA_SEOUL_START_OF_DAY' if printed else None,
        'date_outside_issue_window': [name for value, name in ((printed, 'IMPRINT'), (registered, 'REG_DATE'))
                                      if value is not None and first is not None and not plausible(value, first)],
        'historical_publication_verified': False, 'historical_pdf_version_verified': False,
        'automatic_training_approval': False,
    }


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


def report_record(entry, group, body, content, *, cover_evidence=None):
    first = issue_month(entry)
    pdf_sha256 = hashlib.sha256(body).hexdigest() if body else None
    printed, imprint_raw, issue_no = imprint_with_evidence(
        content or '', pdf_sha256=pdf_sha256, source_record_key=f'{group}:{pdf_id(entry["pdf_link"])}',
        evidence=cover_evidence)
    registered = parse_reg_date(entry['reg_date'])
    published_at, _, _ = availability(first, printed, registered)
    chars = len((content or '').strip())
    payload = {**entry, 'pdf_id': pdf_id(entry['pdf_link']),
               'pdf_sha256': pdf_sha256,
               'pdf_bytes': len(body) if body else None,
               'pdf_status': 'OK' if body else 'NOT_PDF',
               'text_status': 'OK' if chars >= MIN_TEXT_CHARS else 'NO_TEXT' if body else None,
               'text': content if chars >= MIN_TEXT_CHARS else None,
               **date_metadata(entry, printed, imprint_raw, issue_no)}
    if cover_evidence is not None:
        payload['imprint_evidence'] = {key: cover_evidence[key] for key in
                                       ('page', 'method', 'review_status', 'text_sha256')}
    record = Record(SOURCE, DATASET, f'{group}:{payload["pdf_id"]}', payload, observed_on=first,
                    entity_code=group, entity_name=GROUPS.get(group, entry['item_name']))
    record.period_start, record.period_end = first, month_end(first)
    record.published_at = published_at
    return record


def collect(fetch_bytes, *, groups, years, cache_dir: Path, workers=3, cover_evidence=None):
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
            evidence = (cover_evidence or {}).get(f'{group}:{pdf_id(entry["pdf_link"])}')
            return [report_record(entry, group, body, content, cover_evidence=evidence)]
        return run

    batch = gather((report(group, entry) for group, entry in found), workers)
    batch.requests += requests
    return batch
