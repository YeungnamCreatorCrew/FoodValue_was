"""KAMIS 기간별 품목 가격(periodProductList). 소매가는 예측 대상, 도매가는 선행 지표로만 쓴다.

item.price_code 형식: 품목코드-품종코드-등급코드 (예: 246-00-04). 부류코드는 품목코드 첫 자리로 정해진다.
응답의 countyname '평균' 행을 전국 평균으로 사용한다. 지역별 행은 적재하지 않는다.
"""
import re
from datetime import date

from app.collectors.http import AuthError, CollectorError, as_list, number, text_value
from app.collectors.records import Record, gather, windows

URL = 'https://www.kamis.or.kr/service/price/xml.do'
SOURCE = 'KAMIS'
RETAIL = 'RETAIL_DAILY'
WHOLESALE = 'WHOLESALE_DAILY'
CLASS_CODES = {RETAIL: '01', WHOLESALE: '02'}
NATIONAL_COUNTY = '평균'
WINDOW_DAYS = 90
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


def parse(payload, code: str, dataset: str, item_id: int, unit_label: str | None):
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


def collect(fetch, *, code, dataset, item_id, unit_label, start, end, cert_key, cert_id):
    parse_code(code)
    return gather(lambda first=first, last=last: parse(fetch(URL, params(code, dataset, first, last, cert_key, cert_id)),
                                                       code, dataset, item_id, unit_label)
                  for first, last in windows(start, end, WINDOW_DAYS))
