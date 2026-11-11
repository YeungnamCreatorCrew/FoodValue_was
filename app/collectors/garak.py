"""서울시농수산식품공사 가락시장 반입물량(경매후) → item_production(ARRIVAL, DAY).

요청: dataOpen.do?id=발급ID&passwd=신청 비밀번호&dataid=data21&date=YYYYMMDD&pagesize=100&pageidx=N
- 응답은 XML(<lists><list_total_count>N</list_total_count><list>...</list></lists>)이고 값은 CDATA로 온다.
- 한 번 호출로 그날 모든 품목(약 120행)을 돌려준다. 한 페이지는 100행까지라 날짜마다 1~2회 요청한다.
  여러 품목을 받아도 날짜당 요청 수는 같다.
- 행: BURYU(부류), SORT_CD, ITM_CD(품목코드, 대파 24500), ITM_NM, CORP_CD_1~6(도매법인별), SUM_TOT(합계).
  단위는 톤이다(2026-11 실측: 전체 합계가 하루 약 8천 톤, 대파 약 400톤).
  부류 합계 행(ITM_CD '합계'·'계'·'…계')은 품목이 아니므로 저장하지 않는다.
- 2021년 이전 날짜는 HTTP 400("검색가능 년도는 2021년 부터 입니다")이라 FIRST_DAY부터만 요청한다.
- 일요일·휴장일은 합계 행만 빈 값으로 온다. 그날은 레코드를 만들지 않는다.
- 인증 정보가 틀리면 HTTP 500 HTML 페이지가 온다(2026-11 실측). 날짜마다 같은 실패를 반복하지 않도록
  가장 최근 날짜를 먼저 한 번 요청하고, 실패하면 나머지를 요청하지 않는다.
"""
import re
import xml.etree.ElementTree as ElementTree
from datetime import date, timedelta

from app.collectors.http import AuthError, CollectorError, number, text_value
from app.collectors.records import Batch, Record, gather

URL = 'https://www.garak.co.kr/homepage/publicdata/dataOpen.do'
SOURCE, DATASET = 'GARAK', 'ARRIVAL_DAILY'
DATA_ID = 'data21'
PAGE_SIZE = 100  # 서버 최대값. 더 크게 요청해도 100행만 온다.
FIRST_DAY = date(2021, 1, 1)
WORKERS = 4
VOLUME_UNIT = 'TON'
FIELDS = ('BURYU', 'SORT_CD', 'ITM_CD', 'ITM_NM', 'CORP_CD_1', 'CORP_CD_2', 'CORP_CD_3', 'CORP_CD_4',
          'CORP_CD_5', 'CORP_CD_6', 'SUM_TOT')
ITEM_CODE = re.compile(r'^\d{5}$')
# item.name → 가락시장 품목코드(ITM_CD). 2026-11-10 응답에서 이름이 같은 품목만 넣었다.
# 이름이 달라 대응이 애매한 품목(예: 풋고추 ↔ 생고추, 애호박 ↔ 호박)은 추측해서 넣지 않는다.
ITEM_CODES = {
    '대파': '24500', '쪽파': '24503', '양파': '24400', '마늘': '24300', '생강': '24600', '건고추': '24100',
    '배추': '21100', '양배추': '21200', '시금치': '21300', '상추': '21400', '깻잎': '21500', '부추': '21600',
    '미나리': '21900', '무': '23100', '당근': '23200', '감자': '15200', '고구마': '15100',
    '오이': '22300', '토마토': '22500', '딸기': '22600', '수박': '22100', '파프리카': '25121', '브로콜리': '25800',
    '양상추': '25200',
    '사과': '41100', '배': '41200', '복숭아': '41300', '포도': '41400', '감귤': '41500', '단감': '41600',
}


def params(user_id: str, password: str, day: date, page: int):
    return {'id': user_id, 'passwd': password, 'dataid': DATA_ID, 'pagesize': str(PAGE_SIZE), 'pageidx': str(page),
            'portal.templet': 'false', 'date': day.strftime('%Y%m%d')}


def parse_page(text: str):
    """XML 한 페이지 → (전체 행 수, 행 목록). 형식이 다르면 추측하지 않고 오류로 남긴다."""
    try:
        root = ElementTree.fromstring(text.strip())
    except ElementTree.ParseError:
        raise CollectorError('GARAK_NON_XML_RESPONSE') from None
    total = root.findtext('list_total_count') if root.tag == 'lists' else None
    if total is None or not total.strip().isdigit():
        raise CollectorError('GARAK_UNEXPECTED_RESPONSE')
    rows = [{field: (node.findtext(field) or '').strip() for field in FIELDS} for node in root.findall('list')]
    return int(total), rows


def records(rows, day: date, targets: dict[str, int]):
    """targets: 가락 품목코드 → item_id. 반입량이 없거나 음수인 행은 만들지 않는다."""
    result = []
    for row in rows:
        code = text_value(row.get('ITM_CD'))
        if not code or not ITEM_CODE.match(code) or code not in targets:
            continue
        volume = number(row.get('SUM_TOT'))
        if volume is None or volume < 0:
            continue
        result.append(Record(SOURCE, DATASET, f'{code}:{day.isoformat()}', dict(row), observed_on=day,
                             entity_code=code, entity_name=text_value(row.get('ITM_NM')),
                             units={'volume': VOLUME_UNIT}, item_id=targets[code]))
    return result


def fetch_day(fetch, user_id: str, password: str, day: date, targets: dict[str, int]):
    """한 날짜의 모든 페이지를 받는다. (레코드, 요청 수)를 반환한다."""
    rows, page, requests = [], 1, 0
    while True:
        total, found = parse_page(fetch(URL, params(user_id, password, day, page)))
        requests += 1
        rows += found
        if not found or len(rows) >= total:
            break
        page += 1
    return records(rows, day, targets), requests


def days(start: date, end: date):
    """최근 날짜부터. 일요일은 경매가 없어 요청하지 않는다."""
    day = end
    while day >= start:
        if day.weekday() != 6:
            yield day
        day -= timedelta(days=1)


def collect(fetch, *, user_id, password, targets: dict[str, int], start: date, end: date):
    """fetch(url, params) → 응답 문자열. targets: 가락 품목코드 → item_id."""
    order = list(days(max(start, FIRST_DAY), end))
    if not order:
        return Batch([], 0)
    first, requests = fetch_day(fetch, user_id, password, order[0], targets)  # 실패하면 그대로 올려 중단한다.
    try:
        rest = gather([lambda day=day: fetch_day(fetch, user_id, password, day, targets) for day in order[1:]],
                      workers=WORKERS)
    except AuthError:
        raise
    except CollectorError as error:  # 나머지 날짜가 모두 실패해도 첫 날짜 결과는 보존한다(PARTIAL).
        if not first:
            raise
        rest = Batch([], len(order) - 1, error.code)
    merged = {record.key: record for record in first + rest.records}
    return Batch(list(merged.values()), requests + rest.requests, rest.partial_error)
