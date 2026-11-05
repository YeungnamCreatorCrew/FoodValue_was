"""Open API 응답 해석. 실제 네트워크·인증키를 사용하지 않는다."""
from datetime import date, timedelta

import pytest

from app.collectors import data_go_kr, http, kamis
from app.collectors.records import windows

CODE = '246-00-04'


def kamis_payload(rows, code='000'):
    return {'condition': [], 'data': {'error_code': code, 'item': rows}}


def kamis_row(county, regday, price, year='2026'):
    return {'itemname': '대파', 'kindname': '대파(1kg)', 'countyname': county, 'marketname': '',
            'yyyy': year, 'regday': regday, 'price': price}


def asos_payload(rows, code='00'):
    return {'response': {'header': {'resultCode': code, 'resultMsg': 'OK'},
                         'body': {'items': {'item': rows}, 'totalCount': len(rows)}}}


def test_kamis_code_and_params():
    assert kamis.parse_code(CODE) == {'category': '200', 'item': '246', 'kind': '00', 'rank': '04'}
    with pytest.raises(ValueError):
        kamis.parse_code('대파')
    params = kamis.params(CODE, kamis.WHOLESALE, date(2026, 1, 1), date(2026, 3, 31), 'k', 'id')
    assert params['p_productclscode'] == '02' and params['p_itemcategorycode'] == '200'
    assert params['p_startday'] == '2026-01-01' and params['p_returntype'] == 'json'


def test_kamis_keeps_only_national_average_with_prices():
    payload = kamis_payload([kamis_row('평균', '10/07', '3,120'), kamis_row('서울', '10/07', '3,500'),
                             kamis_row('평균', '10/08', '-'), kamis_row('평년', '10/07', '2,900'),
                             kamis_row('평균', '10/09', '3,000')])
    records = kamis.parse(payload, CODE, kamis.RETAIL, 7, '1kg')
    assert [(r.observed_on, r.payload['price']) for r in records] == [(date(2026, 10, 7), '3,120'),
                                                                     (date(2026, 10, 9), '3,000')]
    assert records[0].key == f'{CODE}:2026-10-07' and records[0].item_id == 7
    assert records[0].units == {'price': 'KRW', 'unitLabel': '1kg'}
    # 실제 KAMIS 응답은 빈 이름 필드를 []로 보낸다.
    empty = kamis.parse(kamis_payload([{**kamis_row('평균', '10/07', '3,120'), 'itemname': [], 'kindname': []}]),
                        CODE, kamis.RETAIL, 7, None)
    assert empty[0].entity_name is None


def test_kamis_status_codes():
    assert kamis.parse({'data': ['001']}, CODE, kamis.RETAIL, 1, None) == []
    with pytest.raises(http.AuthError):
        kamis.parse({'data': ['900']}, CODE, kamis.RETAIL, 1, None)
    with pytest.raises(http.CollectorError):
        kamis.parse({'data': {'error_code': '200'}}, CODE, kamis.RETAIL, 1, None)
    with pytest.raises(http.CollectorError):
        kamis.parse('nope', CODE, kamis.RETAIL, 1, None)


def test_kamis_collect_splits_windows_and_reports_partial():
    calls = []

    def fetch(url, params):
        calls.append(params['p_startday'])
        if len(calls) == 2:
            raise http.NetworkError('URLError')
        return kamis_payload([kamis_row('평균', params['p_startday'][5:].replace('-', '/'), '1,000')])
    batch = kamis.collect(fetch, code=CODE, dataset=kamis.RETAIL, item_id=1, unit_label=None,
                          start=date(2026, 1, 1), end=date(2026, 6, 30), cert_key='k', cert_id='i')
    assert calls == ['2026-01-01', '2026-04-01', '2026-06-30']
    assert batch.requests == 3 and len(batch.records) == 2 and batch.partial_error == 'URLError'


def test_collect_raises_when_everything_failed_or_auth_fails():
    def broken(url, params):
        raise http.NetworkError('TimeoutError')
    with pytest.raises(http.NetworkError):
        kamis.collect(broken, code=CODE, dataset=kamis.RETAIL, item_id=1, unit_label=None,
                      start=date(2026, 1, 1), end=date(2026, 6, 30), cert_key='k', cert_id='i')
    calls = []

    def denied(url, params):
        calls.append(1)
        raise http.AuthError('KAMIS_900')
    with pytest.raises(http.AuthError):
        kamis.collect(denied, code=CODE, dataset=kamis.RETAIL, item_id=1, unit_label=None,
                      start=date(2026, 1, 1), end=date(2026, 6, 30), cert_key='k', cert_id='i')
    assert calls == [1]


def test_data_go_kr_result_codes():
    assert data_go_kr.body(asos_payload([], code='03')) == ([], 0)
    with pytest.raises(http.AuthError):
        data_go_kr.body(asos_payload([], code='30'))
    with pytest.raises(http.CollectorError):
        data_go_kr.body(asos_payload([], code='22'))
    single = {'response': {'header': {'resultCode': '00'}, 'body': {'items': {'item': {'tm': '2026-10-01'}}}}}
    assert data_go_kr.body(single) == ([{'tm': '2026-10-01'}], 1)
    empty = {'response': {'header': {'resultCode': '00'}, 'body': {'items': '', 'totalCount': 0}}}
    assert data_go_kr.body(empty) == ([], 0)


def test_asos_and_holiday_records():
    rows = [{'tm': '2026-10-01', 'stnId': '108', 'stnNm': '서울', 'avgTa': '18.2', 'minTa': '14.0',
             'maxTa': '23.1', 'sumRn': '', 'avgRhm': '70.5', 'sumSsHr': '6.1', 'extra': 'x'}]
    record = data_go_kr.asos_records(rows)[0]
    assert record.key == '108:2026-10-01' and record.entity_code == '108'
    assert record.payload['sumRn'] is None and 'extra' not in record.payload
    holiday = data_go_kr.holiday_records([{'locdate': 20261005, 'dateName': '추석', 'isHoliday': 'Y',
                                           'dateKind': '01', 'seq': 1}])[0]
    assert holiday.observed_on == date(2026, 10, 5) and holiday.key == '2026-10-05:추석'


def test_asos_requests_station_years_and_holiday_months():
    seen = []

    def fetch(url, params):
        seen.append(params)
        return asos_payload([])
    # 관측소마다 시작일이 다르다(새 관측소만 백필). 기간 전체를 한 번에 요청한다.
    batch = data_go_kr.collect_asos(fetch, key='a%2Bb', end=date(2026, 6, 1), workers=1,
                                    stations={'133': date(2026, 5, 20), '108': date(2025, 1, 1), '90': date(2026, 7, 1)})
    assert batch.requests == 2 and batch.records == [] and batch.partial_error is None
    assert [p['stnIds'] for p in seen] == ['108', '133'] and seen[0]['serviceKey'] == 'a+b'
    assert (seen[0]['startDt'], seen[0]['endDt']) == ('20250101', '20260601')
    assert len(set(data_go_kr.NATIONAL_STATIONS)) == len(data_go_kr.NATIONAL_STATIONS) == 97
    seen.clear()
    data_go_kr.collect_holidays(fetch, key='k', years=[2026])
    assert [p['solMonth'] for p in seen] == [f'{m:02d}' for m in range(1, 13)]


def test_http_decode_and_helpers():
    assert http.decode(b'{"a": 1}') == {'a': 1}
    with pytest.raises(http.AuthError):
        http.decode(b'<OpenAPI_ServiceResponse><returnAuthMsg>SERVICE_KEY_IS_NOT_REGISTERED_ERROR</returnAuthMsg>')
    with pytest.raises(http.CollectorError):
        http.decode(b'<html>maintenance</html>')
    assert http.number('1,234') == 1234.0 and http.number('-') is None and http.number('') is None
    assert http.service_key('abc%3D%3D') == 'abc==' and http.service_key('abc==') == 'abc=='
    assert list(windows(date(2026, 1, 1), date(2026, 1, 5), 2)) == [
        (date(2026, 1, 1), date(2026, 1, 2)), (date(2026, 1, 3), date(2026, 1, 4)), (date(2026, 1, 5), date(2026, 1, 5))]


def test_fetch_json_retries_network_errors_without_leaking_url(monkeypatch):
    import urllib.error
    attempts = []

    def failing(request, timeout):
        attempts.append(request.full_url)
        raise urllib.error.URLError('down')
    monkeypatch.setattr(http.urllib.request, 'urlopen', failing)
    with pytest.raises(http.NetworkError) as error:
        http.fetch_json('https://example.invalid/api', {'serviceKey': 'secret'}, sleep=lambda s: None)
    assert len(attempts) == 3 and 'secret' not in str(error.value)


def test_pipeline_arguments_and_exit_codes():
    from app import price_pipeline
    _, args = price_pipeline.parse_args(['--item-id', '3', '--item-id', '4', '--start', '2025-01-01', '--collect-only'])
    assert args.item_ids == [3, 4] and args.start == date(2025, 1, 1) and args.collect_only
    for bad in (['--item-id', '0'], ['--start', '2026-02-01', '--end', '2026-01-01'], ['--collect-only', '--predict-only']):
        with pytest.raises(SystemExit):
            price_pipeline.parse_args(bad)
    ok = {'collection': [{'status': 'SUCCESS'}, {'status': 'SKIPPED'}], 'predictions': [{'status': 'SUCCESS'}]}
    assert price_pipeline.exit_code(ok) == 0
    assert price_pipeline.exit_code({**ok, 'collection': [{'status': 'NETWORK_ERROR'}]}) == 2
    assert price_pipeline.exit_code({**ok, 'predictions': [{'status': 'INSUFFICIENT_DATA'}]}) == 2
    assert price_pipeline.exit_code({**ok, 'predictions': [{'status': 'BUSY'}]}) == 3
    assert price_pipeline.exit_code({**ok, 'predictions': [{'status': 'FAILED'}, {'status': 'BUSY'}]}) == 1


def test_asos_follows_pages():
    pages = []

    def fetch(url, params):
        pages.append(params['pageNo'])
        size = 999 if params['pageNo'] == 1 else 501
        rows = [{'tm': (date(2020, 1, 1) + timedelta(days=(params['pageNo'] - 1) * 999 + i)).isoformat(),
                 'stnId': '108', 'avgTa': '1'} for i in range(size)]
        return {'response': {'header': {'resultCode': '00'}, 'body': {'items': {'item': rows}, 'totalCount': 1500}}}
    batch = data_go_kr.collect_asos(fetch, key='k', stations={'108': date(2020, 1, 1)}, end=date(2024, 2, 8))
    assert pages == [1, 2] and batch.requests == 2 and len(batch.records) == 1500


def test_gather_runs_in_parallel_and_counts_failures():
    from app.collectors.records import Record, gather

    def ok(n):
        return lambda: [Record('S', 'D', f'k{n}', {})]

    def broken():
        raise http.NetworkError('URLError')
    batch = gather([ok(1), broken, ok(2)], workers=3)
    assert batch.requests == 3 and len(batch.records) == 2 and batch.partial_error == 'URLError'


def test_vilage_base_time_and_precipitation_categories():
    from datetime import datetime
    from zoneinfo import ZoneInfo
    seoul = ZoneInfo('Asia/Seoul')
    assert data_go_kr.vilage_base(datetime(2026, 11, 5, 11, 20, tzinfo=seoul)) == datetime(2026, 11, 5, 11, 0, tzinfo=seoul)
    assert data_go_kr.vilage_base(datetime(2026, 11, 5, 11, 10, tzinfo=seoul)) == datetime(2026, 11, 5, 8, 0, tzinfo=seoul)
    assert data_go_kr.vilage_base(datetime(2026, 11, 5, 2, 5, tzinfo=seoul)) == datetime(2026, 11, 4, 23, 0, tzinfo=seoul)
    cases = {'강수없음': 0.0, '0': 0.0, '1mm 미만': 0.5, '1.0mm 미만': 0.5, '3.0mm': 3.0, '30.0~50.0mm': 40.0,
             '50.0mm 이상': 50.0, '이상한값': None}
    assert {value: data_go_kr.precipitation_mm(value) for value in cases} == cases


def test_vilage_records_summarise_full_days_only():
    from datetime import datetime
    base = datetime(2026, 11, 5, 5, 0)
    rows = [{'category': 'TMP', 'fcstDate': '20261106', 'fcstTime': f'{h:02d}00', 'fcstValue': str(h % 10)} for h in range(24)]
    rows += [{'category': 'PCP', 'fcstDate': '20261106', 'fcstTime': f'{h:02d}00', 'fcstValue': '1mm 미만' if h < 2 else '강수없음'} for h in range(24)]
    rows += [{'category': 'TMN', 'fcstDate': '20261106', 'fcstTime': '0600', 'fcstValue': '-1.0'},
             {'category': 'TMX', 'fcstDate': '20261106', 'fcstTime': '1500', 'fcstValue': '9.0'},
             {'category': 'TMP', 'fcstDate': '20261107', 'fcstTime': '0000', 'fcstValue': '3'}]
    full, partial = data_go_kr.vilage_records(rows, '서울', base)
    assert full.key == '서울:202611050500:2026-11-06' and full.issued_at == base
    assert full.payload['tmpMean'] == round(sum(h % 10 for h in range(24)) / 24, 2)
    assert (full.payload['tmn'], full.payload['tmx'], full.payload['pcpSum']) == (-1.0, 9.0, 1.0)
    assert partial.payload['tmpMean'] is None and partial.payload['hours'] == 1


def kosis_row(year, value, changed='2026-10-28'):
    return {'PRD_DE': year, 'DT': value, 'ITM_ID': 'T44', 'ITM_NM': '대파:생산량', 'C1': '00', 'C1_NM': '전국',
            'UNIT_NM': '톤', 'LST_CHN_DE': changed, 'TBL_ID': 'DT_1ET0291', 'ORG_ID': '101'}


def test_kosis_parse_years_units_and_errors():
    from app.collectors import kosis
    records = kosis.parse([kosis_row('2024', '405823', '2025-10-29'), kosis_row('2025', '440715'),
                           kosis_row('2026', '-', '2026-08-12')], 'DT_1ET0291', 'T44', 7)
    assert [r.key for r in records] == ['101:DT_1ET0291:T44:00:2024', '101:DT_1ET0291:T44:00:2025']
    first = records[0]
    assert (first.period_start, first.period_end, first.published_at) == (date(2024, 1, 1), date(2024, 12, 31), date(2025, 10, 29))
    assert first.item_id == 7 and first.units == {'volume': '톤'} and first.payload['DT'] == '405823'
    assert kosis.parse({'err': '30', 'errMsg': '데이터가 존재하지 않습니다.'}, 'T', 'I', 1) == []
    with pytest.raises(http.AuthError):
        kosis.parse({'err': '11', 'errMsg': '유효하지 않은 인증KEY입니다.'}, 'T', 'I', 1)
    with pytest.raises(http.CollectorError):
        kosis.parse({'err': '21'}, 'T', 'I', 1)


def test_kosis_requests_national_series_per_item():
    from app.collectors import kosis
    seen = []

    def fetch(url, params):
        seen.append(params)
        return [kosis_row('2025', '1000')]
    batch = kosis.collect(fetch, key='k', items=[(1, '대파'), (2, '배추')], start_year=2020, end_year=2026)
    assert batch.requests == 2 and len(batch.records) == 2
    assert [(p['tblId'], p['itmId'], p['objL1'], p['prdSe']) for p in seen] == [
        ('DT_1ET0291', 'T44', '00', 'Y'), ('DT_1ET0028', 'T10', '00', 'Y')]
    assert (seen[0]['startPrdDe'], seen[0]['endPrdDe']) == ('2020', '2026')


def test_ecos_url_parse_and_errors():
    from app.collectors import ecos
    assert ecos.url('KEY', date(2026, 10, 1), date(2026, 11, 4), '0000001') == (
        'https://ecos.bok.or.kr/api/StatisticSearch/KEY/json/kr/1/1000/731Y001/D/20261001/20261104/0000001')
    payload = {'StatisticSearch': {'list_total_count': 2, 'row': [
        {'STAT_CODE': '731Y001', 'ITEM_CODE1': '0000001', 'ITEM_NAME1': '원/미국달러(매매기준율)', 'UNIT_NAME': '원',
         'TIME': '20261103', 'DATA_VALUE': '1385.2'},
        {'TIME': '20261104', 'DATA_VALUE': '1,390.50', 'UNIT_NAME': '원'}]}}
    records, total = ecos.parse(payload, 'USD')
    assert total == 2 and [(r.observed_on, r.payload['DATA_VALUE']) for r in records] == [
        (date(2026, 11, 3), '1385.2'), (date(2026, 11, 4), '1,390.50')]
    assert records[0].key == '731Y001:USD:2026-11-03' and records[0].entity_code == 'USD'
    assert ecos.parse({'RESULT': {'CODE': 'INFO-200', 'MESSAGE': '해당하는 데이터가 없습니다.'}}, 'USD') == ([], 0)
    with pytest.raises(http.AuthError):
        ecos.parse({'RESULT': {'CODE': 'INFO-100'}}, 'USD')
    with pytest.raises(http.CollectorError):
        ecos.parse({'RESULT': {'CODE': 'ERROR-500'}}, 'USD')


def test_ecos_pages_by_row_range():
    from app.collectors import ecos
    urls = []

    def fetch(url, params):
        urls.append(url)
        rows = [{'TIME': '20261104', 'DATA_VALUE': '1'}]
        return {'StatisticSearch': {'list_total_count': 1500, 'row': rows}}
    batch = ecos.collect(fetch, key='K', start=date(2021, 1, 1), end=date(2026, 11, 4))
    assert batch.requests == 2 and '/1/1000/' in urls[0] and '/1001/2000/' in urls[1]
