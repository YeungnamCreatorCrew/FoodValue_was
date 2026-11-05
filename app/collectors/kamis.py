"""KAMIS 품목 가격. 소매가는 예측 대상, 도매가는 선행 지표로만 쓴다.

item.price_code 형식: 품목코드-품종코드-등급코드 (예: 246-00-04). 부류코드는 품목코드 첫 자리로 정해진다.

- 최근 PERIOD_LIMIT_DAYS일: 기간별 품목 가격(periodProductList). 응답의 countyname '평균' 행을 전국 평균으로 쓴다.
  로컬 실측에서 이 API는 최근 1년치만 돌려주고 더 오래된 기간은 시간 초과가 났다.
- 그보다 오래된 날짜: 일별 부류별 가격(dailyPriceByCategoryList)을 날짜마다 1회 호출해 해당 품목·품종·등급 행의
  당일 가격(dpr1)을 쓴다. 토·일은 KAMIS 미조사일이라 요청하지 않는다. 당일 열 이름(day1)의 (월/일)이 요청일과
  다르면 직전 조사일 값을 이어 보여준 것으로 보고 저장하지 않는다.
  응답에 품목·품종·등급 코드 열이 없으면 형식이 예상과 다른 것이므로 추측해서 저장하지 않고 오류로 남긴다.
"""
import re
from datetime import date, timedelta

from app.collectors.http import AuthError, CollectorError, as_list, number, text_value
from app.collectors.records import Record, gather, windows

URL = 'https://www.kamis.or.kr/service/price/xml.do'
SOURCE = 'KAMIS'
RETAIL = 'RETAIL_DAILY'
WHOLESALE = 'WHOLESALE_DAILY'
CLASS_CODES = {RETAIL: '01', WHOLESALE: '02'}
NATIONAL_COUNTY = '평균'
WINDOW_DAYS = 90
PERIOD_LIMIT_DAYS = 364  # periodProductList로 받는 최근 기간
DAILY_ACTION = 'dailyPriceByCategoryList'
DAILY_WORKERS = 4
DAY_LABEL = re.compile(r'\((\d{1,2})/(\d{1,2})\)')
CODE_PATTERN = re.compile(r'^(\d{3})-(\d{2})-(\d{2})$')


def parse_code(code: str):
    match = CODE_PATTERN.match(code or '')
    if not match:
        raise ValueError('KAMIS price_code는 품목-품종-등급(예: 246-00-04) 형식이어야 합니다')
    item, kind, rank = match.groups()
    return {'category': item[0] + '00', 'item': item, 'kind': kind, 'rank': rank}


def params(code: str, dataset: str, start: date, end: date, cert_key: str, cert_id: str):
    parsed = parse_code(code)
    return {'action': 'periodProductList', 'p_productclscode': CLASS_CODES[dataset],
            'p_startday': start.isoformat(), 'p_endday': end.isoformat(),
            'p_itemcategorycode': parsed['category'], 'p_itemcode': parsed['item'],
            'p_kindcode': parsed['kind'], 'p_productrankcode': parsed['rank'],
            'p_convert_kg_yn': 'N', 'p_cert_key': cert_key, 'p_cert_id': cert_id, 'p_returntype': 'json'}


def _rows(payload):
    data = payload.get('data') if isinstance(payload, dict) else None
    if isinstance(data, list):  # 오류·무자료는 ["001"] 형태로 온다.
        status = str(data[0]) if data else '001'
        rows = []
    elif isinstance(data, dict):
        status = str(data.get('error_code') or '000')
        rows = as_list(data.get('item'))
    else:
        raise CollectorError('KAMIS_UNEXPECTED_RESPONSE')
    if status == '900':
        raise AuthError('KAMIS_900')
    if status not in ('000', '001'):
        raise CollectorError(f'KAMIS_{status}')
    return rows


def parse(payload, code: str, dataset: str, item_id: int, unit_label: str | None):
    rows = _rows(payload)
    records = []
    for row in rows:
        if text_value(row.get('countyname')) != NATIONAL_COUNTY:
            continue
        price = number(row.get('price'))
        day = observed_date(row.get('yyyy'), row.get('regday'))
        if day is None or price is None or price <= 0:
            continue
        records.append(Record(SOURCE, dataset, f'{code}:{day.isoformat()}', dict(row), observed_on=day,
                              entity_code=code, entity_name=text_value(row.get('kindname')) or text_value(row.get('itemname')),
                              units={'price': 'KRW', 'unitLabel': unit_label}, item_id=item_id))
    return records


def observed_date(year, regday):
    year, regday = text_value(year), text_value(regday)
    if not year or not regday or '/' not in regday:
        return None
    try:
        month, day = (int(x) for x in regday.split('/')[:2])
        return date(int(year), month, day)
    except ValueError:
        return None


def daily_params(code: str, dataset: str, day: date, cert_key: str, cert_id: str):
    parsed = parse_code(code)
    return {'action': DAILY_ACTION, 'p_product_cls_code': CLASS_CODES[dataset], 'p_item_category_code': parsed['category'],
            'p_regday': day.isoformat(), 'p_convert_kg_yn': 'N', 'p_cert_key': cert_key, 'p_cert_id': cert_id,
            'p_returntype': 'json'}


def parse_daily(payload, code: str, dataset: str, item_id: int, unit_label: str | None, day: date):
    rows = [row for row in _rows(payload) if isinstance(row, dict)]
    if rows and not any('item_code' in row and 'kind_code' in row and 'rank_code' in row for row in rows):
        raise CollectorError('KAMIS_UNEXPECTED_DAILY_RESPONSE')
    parsed = parse_code(code)
    match = next((row for row in rows if (text_value(row.get('item_code')), text_value(row.get('kind_code')),
                                          text_value(row.get('rank_code'))) == (parsed['item'], parsed['kind'], parsed['rank'])), None)
    if match is None:
        return []  # 그날 조사하지 않은 품목
    label = DAY_LABEL.search(text_value(match.get('day1')) or '')
    if label and (int(label.group(1)), int(label.group(2))) != (day.month, day.day):
        return []  # 미조사일에 직전 조사일 값을 보여준 경우
    price = number(match.get('dpr1'))
    if price is None or price <= 0:
        return []
    payload = {'price': text_value(match.get('dpr1')), 'regday': day.isoformat(), 'api': DAILY_ACTION,
               **{key: text_value(match.get(key)) for key in ('item_name', 'kind_name', 'rank', 'unit', 'day1')}}
    return [Record(SOURCE, dataset, f'{code}:{day.isoformat()}', payload, observed_on=day, entity_code=code,
                   entity_name=payload['kind_name'] or payload['item_name'],
                   units={'price': 'KRW', 'unitLabel': unit_label}, item_id=item_id)]


def survey_days(start: date, end: date):
    day = start
    while day <= end:
        if day.weekday() < 5:
            yield day
        day += timedelta(days=1)


def collect(fetch, *, code, dataset, item_id, unit_label, start, end, cert_key, cert_id):
    parse_code(code)
    recent = max(start, end - timedelta(days=PERIOD_LIMIT_DAYS))
    calls = [lambda first=first, last=last: parse(fetch(URL, params(code, dataset, first, last, cert_key, cert_id)),
                                                  code, dataset, item_id, unit_label)
             for first, last in windows(recent, end, WINDOW_DAYS)]
    calls += [lambda day=day: parse_daily(fetch(URL, daily_params(code, dataset, day, cert_key, cert_id)),
                                          code, dataset, item_id, unit_label, day)
              for day in survey_days(start, recent - timedelta(days=1))]
    return gather(calls, workers=DAILY_WORKERS if len(calls) > 20 else 1)
