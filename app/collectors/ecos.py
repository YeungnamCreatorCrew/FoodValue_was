"""한국은행 ECOS 통계검색(StatisticSearch) 일별 환율 → exchange_rate_daily.

통계표 731Y001(주요국 통화의 대원화환율), 주기 D. 인증키는 URL 경로에 들어가므로 오류에 URL을 남기지 않는다.
"""
from datetime import date

from app.collectors.http import AuthError, CollectorError, number, text_value
from app.collectors.records import Record, gather
from app.collectors.data_go_kr import compact, parse_compact

BASE_URL = 'https://ecos.bok.or.kr/api/StatisticSearch'
SOURCE, DATASET = 'ECOS', 'EXCHANGE_RATE_DAILY'
STAT_CODE = '731Y001'
CURRENCIES = {'USD': '0000001'}  # 원/미국달러(매매기준율)
PAGE_SIZE = 1000
NO_DATA = 'INFO-200'
AUTH_CODES = {'INFO-100'}  # 인증키가 유효하지 않음


def url(key, start: date, end: date, item, first_row=1, last_row=PAGE_SIZE):
    return f'{BASE_URL}/{key}/json/kr/{first_row}/{last_row}/{STAT_CODE}/D/{compact(start)}/{compact(end)}/{item}'


def parse(payload, currency):
    if not isinstance(payload, dict):
        raise CollectorError('ECOS_UNEXPECTED_RESPONSE')
    if 'RESULT' in payload:  # 오류·무자료는 {"RESULT": {"CODE": "INFO-200", ...}}
        code = str((payload['RESULT'] or {}).get('CODE', ''))
        if code == NO_DATA:
            return [], 0
        if code in AUTH_CODES:
            raise AuthError(f'ECOS_{code}')
        raise CollectorError(f'ECOS_{code or "UNEXPECTED_RESPONSE"}')
    body = payload.get('StatisticSearch') or {}
    records = []
    for row in body.get('row') or []:
        day, rate = parse_compact(row.get('TIME')), number(row.get('DATA_VALUE'))
        if day is None or rate is None or rate <= 0:
            continue
        records.append(Record(SOURCE, DATASET, f'{STAT_CODE}:{currency}:{day.isoformat()}',
                              {key: text_value(row.get(key)) for key in ('TIME', 'DATA_VALUE', 'ITEM_CODE1', 'ITEM_NAME1',
                                                                         'UNIT_NAME', 'STAT_CODE')},
                              observed_on=day, entity_code=currency, entity_name=text_value(row.get('ITEM_NAME1')),
                              units={'rate': text_value(row.get('UNIT_NAME'))}))
    return records, int(body.get('list_total_count') or len(records))


def collect(fetch, *, key, start: date, end: date):
    def call(currency, item):
        def run():
            records, total = parse(fetch(url(key, start, end, item), {}), currency)
            pages = max(1, -(-total // PAGE_SIZE))
            for page in range(1, pages):
                records += parse(fetch(url(key, start, end, item, page * PAGE_SIZE + 1, (page + 1) * PAGE_SIZE), {}), currency)[0]
            return records, pages
        return run
    return gather(call(currency, item) for currency, item in CURRENCIES.items())
