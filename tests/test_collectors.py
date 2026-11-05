"""Open API 응답 해석. 실제 네트워크·인증키를 사용하지 않는다."""
from datetime import date

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
    batch = data_go_kr.collect_asos(fetch, key='a%2Bb', stations=['133', '108', '108'],
                                    start=date(2025, 1, 1), end=date(2026, 6, 1))
    assert batch.requests == 4 and batch.records == [] and batch.partial_error is None
    assert seen[0]['stnIds'] == '108' and seen[0]['serviceKey'] == 'a+b'
    assert (seen[0]['startDt'], seen[0]['endDt']) == ('20250101', '20260101')
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
