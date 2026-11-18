"""명시한 로컬 격리 복원 DB에서만 실행하는 날짜 정정 회귀 검사.

KREI_DATE_TEST_DATABASE_URL의 DB명은 foodvalue_krei_dates_ 접두사여야 한다.
일반 pytest에서는 이 DB 테스트를 건너뛰며 실제 개발 DB에는 접속하지 않는다.
"""
import copy
import os
from pathlib import Path

import pytest
from sqlalchemy import create_engine, text
from sqlalchemy.engine import make_url

from app.collectors import krei
from app.services.krei_date_service import DateCorrectionError, apply_corrections
from app.services.krei_value_service import load_file


@pytest.fixture
def engine():
    url = os.getenv('KREI_DATE_TEST_DATABASE_URL')
    if not url:
        pytest.skip('explicit isolated restore database required')
    target = make_url(url)
    assert target.host in ('localhost', '127.0.0.1', '::1')
    assert target.database.startswith('foodvalue_krei_dates_')
    e = create_engine(target, hide_parameters=True)
    yield e
    e.dispose()


def snapshot(engine):
    with engine.connect() as c:
        return tuple(c.execute(text("select count(*), md5(string_agg(to_jsonb(t)::text, chr(10) order by id)) from " + name + " t")).one()
                     for name in ('external_observation', 'krei_report_value'))


def plan(engine):
    with engine.connect() as c:
        reports = c.execute(text("select id,payload,payload_sha256,published_at from external_observation where source='KREI' and dataset='MONTHLY_REPORT' order by id")).mappings().all()
        out = []
        for r in reports:
            payload = r['payload']
            assert payload['available_from_policy'] == krei.DATE_POLICY
            keys = krei.date_metadata(payload, None, None, None)
            out.append({'id': r['id'], 'before_payload_sha256': r['payload_sha256'],
                        'before_published_at': r['published_at'].isoformat(),
                        'value_count': c.execute(text('select count(*) from krei_report_value where observation_id=:id'), {'id': r['id']}).scalar_one(),
                        'metadata': {key: payload[key] for key in keys}})
        assert len(out) >= 2
        return out


def test_isolated_repeat_has_no_changes_and_dates_agree(engine):
    before = snapshot(engine)
    assert not any(apply_corrections(engine, plan(engine)).values())
    assert snapshot(engine) == before
    with engine.connect() as c:
        assert c.execute(text('select count(*) from krei_report_value v join external_observation o on o.id=v.observation_id where v.published_at is distinct from o.published_at')).scalar_one() == 0


def test_isolated_failed_later_patch_rolls_back_earlier_metadata(engine):
    patches = copy.deepcopy(plan(engine))
    patches[0]['metadata']['imprint_raw'] = (patches[0]['metadata']['imprint_raw'] or '') + ' [rollback probe]'
    patches[1]['value_count'] += 1
    before = snapshot(engine)
    with pytest.raises(DateCorrectionError, match='count/date mismatch'):
        apply_corrections(engine, patches)
    assert snapshot(engine) == before


def test_isolated_rejects_api_overwrite_and_inconsistent_maximum(engine):
    patches = copy.deepcopy(plan(engine))
    patches[0]['metadata']['reg_date'] = '20000101000000'
    before = snapshot(engine)
    with pytest.raises(DateCorrectionError, match='maximum-date policy'):
        apply_corrections(engine, patches)
    patches = copy.deepcopy(plan(engine))
    patches[0]['metadata']['available_from'] = '2000-01-01T00:00:00+09:00'
    with pytest.raises(DateCorrectionError, match='maximum-date policy'):
        apply_corrections(engine, patches)
    assert snapshot(engine) == before


def test_isolated_loader_repeat_copies_dates_without_duplicates_or_stale_delete(engine):
    before = snapshot(engine)
    for _ in range(2):
        result = load_file(engine, Path('data/krei_values/OVR0000000008/8583.json'))
        assert result['values'] == 41 and result['removed'] == 0
        assert result['publishedAt'].startswith('2025-07-04T00:00:00')
    assert snapshot(engine) == before
