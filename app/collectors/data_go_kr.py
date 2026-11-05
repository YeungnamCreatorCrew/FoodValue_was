"""공공데이터포털(data.go.kr) 표준 JSON 응답 처리와 두 개의 수집 API.

- 기상청 지상(종관, ASOS) 일자료: 주산지 관측소의 일별 기온·강수·습도·일조
- 한국천문연구원 특일 정보(공휴일): 명절·공휴일 달력 특징
- 기상청 단기예보(동네예보): 17개 시·도 대표 격자의 일별 예보 → weather_daily(FORECAST)
"""
import re
from datetime import date, datetime, timedelta

from app.collectors.http import AuthError, CollectorError, as_list, number, service_key, text_value
from app.collectors.records import Record, gather

ASOS_URL = 'https://apis.data.go.kr/1360000/AsosDalyInfoService/getWthrDataList'
VILAGE_URL = 'https://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getVilageFcst'
HOLIDAY_URL = 'https://apis.data.go.kr/B090041/openapi/service/SpcdeInfoService/getRestDeInfo'
KMA, ASOS = 'KMA', 'ASOS_DAILY'
KASI, HOLIDAY = 'KASI', 'HOLIDAY'
VILAGE = 'VILAGE_FCST_DAILY'
# 17개 시·도 대표 격자(기상청 단기예보 격자 좌표). 관측소 평균(ACTUAL)과 지점 구성이 다르다.
FORECAST_POINTS = {
    '서울': (60, 127), '부산': (98, 76), '대구': (89, 90), '인천': (55, 124), '광주': (58, 74), '대전': (67, 100),
    '울산': (102, 84), '세종': (66, 103), '경기': (60, 120), '강원': (73, 134), '충북': (69, 107), '충남': (68, 100),
    '전북': (63, 89), '전남': (51, 67), '경북': (89, 91), '경남': (91, 77), '제주': (52, 38)}
# 단기예보 발표시각(KST). API 제공은 발표 약 10분 뒤부터다.
VILAGE_BASE_TIMES = (2, 5, 8, 11, 14, 17, 20, 23)
VILAGE_DELAY_MINUTES = 15
ASOS_FIELDS = ('avgTa', 'minTa', 'maxTa', 'sumRn', 'avgRhm', 'sumSsHr')
ASOS_UNITS = {'avgTa': 'C', 'minTa': 'C', 'maxTa': 'C', 'sumRn': 'mm', 'avgRhm': '%', 'sumSsHr': 'hr'}
PAGE_SIZE = 999
AUTH_CODES = {'20', '30', '31', '32', '33'}  # 서비스 접근 거부·미등록 키·기한 만료·미등록 IP·미서명 호출
NO_DATA = '03'
# weather_daily(전국)를 만들 ASOS 지점번호 97곳. 2026-11-03 자료로 1~339번을 전수 조회해 응답이 있는 지점만 남겼다.
# 신설 지점(181 서청주, 296 북부산 등)은 설치 이전 기간이 무자료이며 집계에서 자연히 빠진다.
NATIONAL_STATIONS = (
    '90', '93', '95', '98', '99', '100', '101', '102', '104', '105', '106', '108', '112', '114', '115', '119',
    '121', '127', '129', '130', '131', '133', '135', '136', '137', '138', '140', '143', '146', '152', '155',
    '156', '159', '162', '165', '168', '169', '170', '172', '174', '177', '181', '184', '185', '188', '189', '192',
    '201', '202', '203', '211', '212', '216', '217', '221', '226', '232', '235', '236', '238', '239', '243',
    '244', '245', '247', '248', '251', '252', '253', '254', '255', '257', '258', '259', '260', '261', '262',
    '263', '264', '266', '268', '271', '272', '273', '276', '277', '278', '279', '281', '283', '284', '285',
    '288', '289', '294', '295', '296')


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


def collect_asos(fetch, *, key, stations, end, workers=4):
    """stations: {지점번호: 시작일}. 지점마다 기간 전체를 한 번에 요청하고 999행 단위로 페이지를 넘긴다.

    공공데이터포털은 지점을 하나씩만 받으므로 지점별 요청을 소수 병렬로 실행한다. 5년 = 지점당 2페이지.
    """
    def call(station, first):
        def run():
            records, total = asos_page(fetch, key, station, first, end, 1)
            pages = max(1, -(-total // PAGE_SIZE))
            for page in range(2, pages + 1):
                records += asos_page(fetch, key, station, first, end, page)[0]
            return records, pages
        return run
    return gather((call(station, first) for station, first in sorted(stations.items()) if first <= end), workers)


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


def vilage_base(now: datetime):
    """now(KST) 기준 가장 최근에 제공된 단기예보 발표시각."""
    ready = now - timedelta(minutes=VILAGE_DELAY_MINUTES)
    hours = [h for h in VILAGE_BASE_TIMES if h <= ready.hour]
    if hours:
        return ready.replace(hour=hours[-1], minute=0, second=0, microsecond=0)
    return (ready - timedelta(days=1)).replace(hour=23, minute=0, second=0, microsecond=0)


RANGE_MM = re.compile(r'^([\d.]+)\s*~\s*([\d.]+)\s*mm$')
OVER_MM = re.compile(r'^([\d.]+)\s*mm\s*이상$')
UNDER_MM = re.compile(r'^([\d.]+)\s*mm\s*미만$')
PLAIN_MM = re.compile(r'^([\d.]+)\s*(mm)?$')


def precipitation_mm(value):
    """단기예보 강수량 범주 → mm. 범위는 중간값, '1mm 미만'은 0.5, 'Nmm 이상'은 N(하한)."""
    value = (text_value(value) or '').replace(' ', '')
    if value in ('', '강수없음'):
        return 0.0
    for pattern, convert in ((RANGE_MM, lambda m: (float(m[1]) + float(m[2])) / 2),
                             (UNDER_MM, lambda m: float(m[1]) / 2), (OVER_MM, lambda m: float(m[1])),
                             (PLAIN_MM, lambda m: float(m[1]))):
        match = pattern.match(value)
        if match:
            return convert(match)
    return None


def vilage_records(rows, name, base: datetime):
    """격자 1곳의 시간별 예보를 날짜별 1레코드로 요약한다. 24시간이 모두 있어야 평균·합계를 만든다."""
    days = {}
    for row in rows:
        day = parse_compact(row.get('fcstDate'))
        if day is None:
            continue
        entry = days.setdefault(day, {'TMP': {}, 'REH': {}, 'PCP': {}, 'POP': {}})
        category, hour, value = row.get('category'), text_value(row.get('fcstTime')), row.get('fcstValue')
        if category in ('TMN', 'TMX'):
            entry[category] = number(value)
        elif category in entry and hour:
            entry[category][hour] = precipitation_mm(value) if category == 'PCP' else number(value)
    records = []
    for day, entry in sorted(days.items()):
        def full(category):
            values = [v for v in entry[category].values() if v is not None]
            return values if len(values) == 24 else None
        tmp, reh, pcp, pop = full('TMP'), full('REH'), full('PCP'), list(entry['POP'].values())
        payload = {'fcstDate': day.isoformat(), 'point': name, 'baseDateTime': base.isoformat(),
                   'hours': len(entry['TMP']), 'tmpMean': round(sum(tmp) / 24, 2) if tmp else None,
                   'tmn': entry.get('TMN'), 'tmx': entry.get('TMX'),
                   'pcpSum': round(sum(pcp), 1) if pcp else None, 'rehMean': round(sum(reh) / 24, 2) if reh else None,
                   'popMax': max((v for v in pop if v is not None), default=None)}
        record = Record(KMA, VILAGE, f'{name}:{base.strftime("%Y%m%d%H%M")}:{day.isoformat()}', payload,
                        observed_on=day, entity_code=name, entity_name=name,
                        units={'tmpMean': 'C', 'tmn': 'C', 'tmx': 'C', 'pcpSum': 'mm', 'rehMean': '%', 'popMax': '%'})
        record.issued_at = base
        records.append(record)
    return records


def collect_vilage(fetch, *, key, base: datetime, workers=4):
    def call(name, nx, ny):
        def run():
            params = {'serviceKey': service_key(key), 'pageNo': 1, 'numOfRows': 1000, 'dataType': 'JSON',
                      'base_date': base.strftime('%Y%m%d'), 'base_time': base.strftime('%H%M'), 'nx': nx, 'ny': ny}
            rows, total = body(fetch(VILAGE_URL, params))
            pages = max(1, -(-total // 1000))
            for page in range(2, pages + 1):
                rows += body(fetch(VILAGE_URL, {**params, 'pageNo': page}))[0]
            return vilage_records(rows, name, base), pages
        return run
    return gather((call(name, nx, ny) for name, (nx, ny) in FORECAST_POINTS.items()), workers)
