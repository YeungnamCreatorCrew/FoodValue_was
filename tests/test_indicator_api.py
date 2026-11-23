import json
from datetime import timedelta

import pytest
from sqlalchemy import text

from app.services import indicator_service
from tests.test_fridge import api  # noqa: F401  (픽스처)
from tests.test_prices import DAY, ROOT, prices  # noqa: F401  (픽스처)

from app.core.constants import INDICATOR_SPEC_VERSION as SPEC  # noqa: E402
SUMMARY = {'headline': '대파는 지금 평년보다 싼 편입니다.',
           'signals': [{'key': 'SEASONAL', 'label': '같은 시기 대비', 'state': 'DOWN', 'stateLabel': '싼 편'}]}


@pytest.fixture
def indicators(prices, monkeypatch):
    client, engine, _ = prices
    monkeypatch.setattr(indicator_service, 'today', lambda: DAY)
    yield client, engine


def add_run(engine, series_id, as_of, status='SUCCESS', spec=SPEC, cards=True, notices=()):
    with engine.begin() as conn:
        run_id = conn.execute(text('SELECT COALESCE(MAX(id),0)+1 FROM price_indicator_run')).scalar()
        conn.execute(text('INSERT INTO price_indicator_run(id,series_id,as_of_date,data_date,spec_version,status,summary,notices) '
                          'VALUES(:i,:s,:d,:d,:v,:st,:sm,:n)'),
                     {'i': run_id, 's': series_id, 'd': as_of, 'v': spec, 'st': status, 'sm': json.dumps(SUMMARY),
                      'n': json.dumps(list(notices))})
        if cards:
            conn.execute(text('INSERT INTO price_indicator_card(run_id,indicator_key,verdict,state,fact,evidence,chart) '
                              'VALUES(:r,:k,:v,:s,:f,:e,:c)'),
                         {'r': run_id, 'k': 'SEASONAL', 'v': 'FACT', 's': 'DOWN', 'f': json.dumps({'diffRate': -0.149}),
                          'e': json.dumps({'r2Adj': 0.111}), 'c': json.dumps({'type': 'SEASONAL_OVERLAY', 'years': []})})
    return run_id


def test_ready_run_returns_cards_with_camel_case(indicators):
    client, engine = indicators
    add_run(engine, 1, DAY)
    result = client.get(ROOT + '/items/2/indicators').json()
    assert result['status'] == 'READY' and result['asOfDate'] == DAY.isoformat() and result['specVersion'] == SPEC
    assert result['summary']['headline'] == SUMMARY['headline'] and result['summary']['signals'][0]['stateLabel'] == '싼 편'
    card = result['cards'][0]
    assert (card['key'], card['verdict'], card['state']) == ('SEASONAL', 'FACT', 'DOWN')
    assert card['fact'] == {'diffRate': -0.149} and card['chart']['type'] == 'SEASONAL_OVERLAY'


def test_notices_explain_missing_cards(indicators):
    client, engine = indicators
    notice = {'key': 'WHOLESALE_LEAD', 'reason': 'KIND_SWITCH', 'text': '작형이 막 바뀌어서 잠시 쉬어요.'}
    add_run(engine, 1, DAY, notices=[notice])
    assert client.get(ROOT + '/items/2/indicators').json()['notices'] == [notice]
    add_run(engine, 1, DAY - timedelta(days=1))
    assert client.get(ROOT + '/items/2/indicators').json()['notices'] == [notice]  # 가장 최근 기준일의 실행만 쓴다


def test_old_run_is_stale_but_still_shown(indicators):
    client, engine = indicators
    add_run(engine, 1, DAY - timedelta(days=8))
    result = client.get(ROOT + '/items/2/indicators').json()
    assert result['status'] == 'STALE' and len(result['cards']) == 1
    add_run(engine, 1, DAY - timedelta(days=7))  # 정확히 7일 전은 아직 STALE이 아니다(더 최근 기준일이 우선)
    assert client.get(ROOT + '/items/2/indicators').json()['status'] == 'READY'


def test_latest_run_wins_and_future_or_other_spec_ignored(indicators):
    client, engine = indicators
    add_run(engine, 1, DAY - timedelta(days=3))
    add_run(engine, 1, DAY + timedelta(days=2))  # 오늘 이후 기준일은 쓰지 않는다
    add_run(engine, 1, DAY, spec='ind-v0')  # 다른 규칙 버전도 쓰지 않는다
    assert client.get(ROOT + '/items/2/indicators').json()['asOfDate'] == (DAY - timedelta(days=3)).isoformat()


def test_no_run_insufficient_history_and_unsupported_market(indicators):
    client, engine = indicators
    none = client.get(ROOT + '/items/2/indicators').json()
    assert none['status'] == 'NO_DATA' and none['cards'] == [] and none['unavailableReason']
    add_run(engine, 1, DAY, status='INSUFFICIENT_DATA', cards=False)
    short = client.get(ROOT + '/items/2/indicators').json()
    assert short['status'] == 'INSUFFICIENT_HISTORY' and short['cards'] == [] and short['unavailableReason']
    wholesale = client.get(ROOT + '/items/2/indicators?market=WHOLESALE').json()
    assert wholesale['status'] == 'NO_DATA' and wholesale['market'] == 'WHOLESALE' and 'summary' in wholesale


def test_unknown_item_is_404_and_bad_market_is_rejected(indicators):
    client, _ = indicators
    assert client.get(ROOT + '/items/999/indicators').status_code == 404
    assert client.get(ROOT + '/items/2/indicators?market=BAD').status_code == 400


def test_list_items_carry_indicator_signals_and_year_range(indicators):
    client, engine = indicators
    run_id = add_run(engine, 1, DAY)
    with engine.begin() as conn:
        conn.execute(text('INSERT INTO price_indicator_card(run_id,indicator_key,verdict,state,fact,evidence) VALUES(:r,:k,:v,:s,:f,:e)'),
                     {'r': run_id, 'k': 'PRICE_POSITION', 'v': 'FACT', 's': 'DOWN',
                      'f': json.dumps({'low': 1000, 'high': 3000, 'percentile': 0.2}), 'e': '{}'})
    rows = {r['seriesId']: r for r in client.get(ROOT + '/items').json()['items']}
    hit = rows[1]['indicators']
    assert hit['asOfDate'] == DAY.isoformat() and hit['stale'] is False
    assert hit['signals'][0]['stateLabel'] == '싼 편'
    assert hit['yearRange'] == {'low': 1000, 'high': 3000, 'percentile': 0.2}
    assert all(r['indicators'] is None for sid, r in rows.items() if sid != 1)
    assert client.get(ROOT + '/items/2').json()['item']['indicators'] is None
