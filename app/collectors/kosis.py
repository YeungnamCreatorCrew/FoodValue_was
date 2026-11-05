"""KOSIS(국가통계포털) 농작물생산조사 연간 전국 생산량 → item_production(PRODUCTION, YEAR).

통계표·항목 코드는 KOSIS 메타 API(getMeta type=ITM)로 확인한 값이다. item.name이 키와 같을 때만 연결한다.
LST_CHN_DE(최종 수정일)를 공표 시점으로 저장한다. 최초 공표일 이후의 날짜이므로 보수적인 값이다.
"""
from datetime import date

from app.collectors.http import AuthError, CollectorError, number, text_value
from app.collectors.records import Record, gather

URL = 'https://kosis.kr/openapi/Param/statisticsParameterData.do'
SOURCE, DATASET = 'KOSIS', 'CROP_PRODUCTION'
ORG_ID = '101'  # 국가데이터처(통계청)
NATIONAL = '00'
AUTH_CODES = {'10', '11'}  # 인증키 누락·유효하지 않은 인증키
NO_DATA = '30'
# item.name → (통계표, 항목). 단위는 모두 톤.
PRODUCTION_SERIES = {
    '대파': ('DT_1ET0291', 'T44'), '쪽파': ('DT_1ET0291', 'T62'), '양파': ('DT_1ET0291', 'T80'),
    '마늘': ('DT_1ET0291', 'T92'), '생강': ('DT_1ET0291', 'T86'), '건고추': ('DT_1ET0291', 'T14'),
    '풋고추': ('DT_1ET0291', 'T20'),
    '배추': ('DT_1ET0028', 'T10'), '시금치': ('DT_1ET0028', 'T52'), '상추': ('DT_1ET0028', 'T70'),
    '양배추': ('DT_1ET0028', 'T88'),
    '무': ('DT_1ET0029', 'T10'), '당근': ('DT_1ET0029', 'T64'),
    '고구마': ('DT_1ET0026', 'T15'), '감자': ('DT_1ET0026', 'T25'),
    '사과': ('DT_1ET0292', 'T10'), '배': ('DT_1ET0292', 'T16'), '복숭아': ('DT_1ET0292', 'T22'),
    '포도': ('DT_1ET0292', 'T28'), '감귤': ('DT_1ET0292', 'T34'), '단감': ('DT_1ET0292', 'T46'),
}


def params(key, table, item, start_year, end_year):
    return {'method': 'getList', 'apiKey': key, 'orgId': ORG_ID, 'tblId': table, 'itmId': item, 'objL1': NATIONAL,
            'prdSe': 'Y', 'startPrdDe': str(start_year), 'endPrdDe': str(end_year), 'format': 'json', 'jsonVD': 'Y'}


def parse(payload, table, item, item_id):
    if isinstance(payload, dict):  # 오류는 {"err": "..", "errMsg": ".."} 객체로 온다.
        code = str(payload.get('err', ''))
        if code == NO_DATA:
            return []
        if code in AUTH_CODES:
            raise AuthError(f'KOSIS_{code}')
        raise CollectorError(f'KOSIS_{code or "UNEXPECTED_RESPONSE"}')
    if not isinstance(payload, list):
        raise CollectorError('KOSIS_UNEXPECTED_RESPONSE')
    records = []
    for row in payload:
        year, volume = text_value(row.get('PRD_DE')), number(row.get('DT'))
        if not year or not year.isdigit() or volume is None:
            continue  # 미공표 연도는 '-'로 온다.
        changed = text_value(row.get('LST_CHN_DE'))
        record = Record(SOURCE, DATASET, f'{ORG_ID}:{table}:{item}:{NATIONAL}:{year}',
                        {key: text_value(row.get(key)) for key in ('PRD_DE', 'DT', 'ITM_ID', 'ITM_NM', 'C1', 'C1_NM',
                                                                   'UNIT_NM', 'LST_CHN_DE', 'TBL_ID')},
                        observed_on=date(int(year), 12, 31), entity_code=f'{table}:{item}',
                        entity_name=text_value(row.get('ITM_NM')), units={'volume': text_value(row.get('UNIT_NM'))},
                        item_id=item_id)
        record.period_start, record.period_end = date(int(year), 1, 1), date(int(year), 12, 31)
        record.published_at = date.fromisoformat(changed) if changed else None
        records.append(record)
    return records


def collect(fetch, *, key, items, start_year, end_year):
    """items: [(item_id, 품목명)]. 매핑이 없는 품목은 요청하지 않는다."""
    calls = []
    for item_id, name in items:
        table, item = PRODUCTION_SERIES[name]
        calls.append(lambda item_id=item_id, table=table, item=item:
                     parse(fetch(URL, params(key, table, item, start_year, end_year)), table, item, item_id))
    return gather(calls)
