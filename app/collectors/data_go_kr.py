"""공공데이터포털(data.go.kr) 표준 JSON 응답 처리와 두 개의 수집 API.

- 기상청 지상(종관, ASOS) 일자료: 주산지 관측소의 일별 기온·강수·습도·일조
- 한국천문연구원 특일 정보(공휴일): 명절·공휴일 달력 특징
"""
from datetime import date

from app.collectors.http import AuthError, CollectorError, as_list, number, service_key, text_value
from app.collectors.records import Record, gather, windows

ASOS_URL = 'https://apis.data.go.kr/1360000/AsosDalyInfoService/getWthrDataList'
HOLIDAY_URL = 'https://apis.data.go.kr/B090041/openapi/service/SpcdeInfoService/getRestDeInfo'
KMA, ASOS = 'KMA', 'ASOS_DAILY'
KASI, HOLIDAY = 'KASI', 'HOLIDAY'
ASOS_FIELDS = ('avgTa', 'minTa', 'maxTa', 'sumRn', 'avgRhm', 'sumSsHr')
ASOS_UNITS = {'avgTa': 'C', 'minTa': 'C', 'maxTa': 'C', 'sumRn': 'mm', 'avgRhm': '%', 'sumSsHr': 'hr'}
PAGE_SIZE = 999
AUTH_CODES = {'20', '30', '31', '32', '33'}  # 서비스 접근 거부·미등록 키·기한 만료·미등록 IP·미서명 호출
NO_DATA = '03'
# weather_daily(전국)를 만들 ASOS 지점번호. 폐지·이전된 지점은 무자료(03)로 응답하며 집계에서 빠진다.
# 기상자료개방포털의 지점 목록과 대조해 갱신한다.
NATIONAL_STATIONS = (
    '90', '93', '95', '98', '99', '100', '101', '102', '104', '105', '106', '108', '112', '114', '115', '119',
    '121', '127', '129', '130', '131', '133', '135', '136', '137', '138', '140', '143', '146', '152', '155',
    '156', '159', '162', '165', '168', '169', '170', '172', '174', '177', '184', '185', '188', '189', '192',
    '201', '202', '203', '211', '212', '216', '217', '221', '226', '232', '235', '236', '238', '239', '243',
    '244', '245', '247', '248', '251', '252', '253', '254', '255', '257', '258', '259', '260', '261', '262',
    '263', '264', '266', '268', '271', '272', '273', '276', '277', '278', '279', '281', '283', '284', '285',
    '288', '289', '294', '295')


def body(payload):
    """resultCode를 검사하고 (items 목록, totalCount)를 반환한다."""
    response = payload.get('response') if isinstance(payload, dict) else None
    if not isinstance(response, dict):
        raise CollectorError('DATA_GO_KR_UNEXPECTED_RESPONSE')
    code = str((response.get('header') or {}).get('resultCode', '')).strip()
    if code == NO_DATA:
        return [], 0
    if code in AUTH_CODES:
        raise AuthError(f'DATA_GO_KR_{code}')
    if code not in ('00', '0', '0000'):
        raise CollectorError(f'DATA_GO_KR_{code or "UNKNOWN"}')
    content = response.get('body') or {}
    items = content.get('items')
    rows = as_list(items.get('item')) if isinstance(items, dict) else []
    return rows, int(content.get('totalCount') or len(rows))


def compact(day: date):
    return day.strftime('%Y%m%d')


def parse_compact(value):
    value = text_value(value)
    if not value:
        return None
    digits = value.replace('-', '')[:8]
    try:
        return date(int(digits[:4]), int(digits[4:6]), int(digits[6:8]))
    except ValueError:
        return None


def asos_records(rows):
    records = []
    for row in rows:
        day, station = parse_compact(row.get('tm')), text_value(row.get('stnId'))
        if day is None or station is None:
            continue
        payload = {name: text_value(row.get(name)) for name in ASOS_FIELDS}
        payload.update({'tm': day.isoformat(), 'stnId': station, 'stnNm': text_value(row.get('stnNm'))})
        records.append(Record(KMA, ASOS, f'{station}:{day.isoformat()}', payload, observed_on=day,
                              entity_code=station, entity_name=payload['stnNm'], units=ASOS_UNITS))
    return records


def asos_page(fetch, key, station, first, last, page):
    rows, total = body(fetch(ASOS_URL, {'serviceKey': service_key(key), 'pageNo': page, 'numOfRows': PAGE_SIZE,
        'dataType': 'JSON', 'dataCd': 'ASOS', 'dateCd': 'DAY', 'startDt': compact(first), 'endDt': compact(last),
        'stnIds': station}))
    return asos_records(rows), total


def collect_asos(fetch, *, key, stations, end):
    """stations: {지점번호: 시작일}. 지점×연도 단위로 요청한다. 1년은 한 페이지(999행)에 들어간다."""
    def call(station, first, last):
        def run():
            records, total = asos_page(fetch, key, station, first, last, 1)
            if total > PAGE_SIZE:
                raise CollectorError('ASOS_PAGE_OVERFLOW')
            return records
        return run
    return gather(call(station, first, last) for station, start in sorted(stations.items())
                  for first, last in windows(start, end, 366))


def holiday_records(rows):
    records = []
    for row in rows:
        day, name = parse_compact(row.get('locdate')), text_value(row.get('dateName'))
        if day is None or name is None:
            continue
        payload = {'locdate': day.isoformat(), 'dateName': name, 'isHoliday': text_value(row.get('isHoliday')),
                   'dateKind': text_value(row.get('dateKind'))}
        records.append(Record(KASI, HOLIDAY, f'{day.isoformat()}:{name}', payload, observed_on=day,
                              entity_name=name))
    return records


def collect_holidays(fetch, *, key, years):
    def call(year, month):
        return lambda: holiday_records(body(fetch(HOLIDAY_URL, {'serviceKey': service_key(key), 'solYear': year,
            'solMonth': f'{month:02d}', 'numOfRows': 100, '_type': 'json'}))[0])
    return gather(call(year, month) for year in sorted(set(years)) for month in range(1, 13))
