"""스냅샷 내보내기·검사와 작형 이어 붙이기(기준서 §2.2, §2.3) 테스트."""
import json
from datetime import date, timedelta
from decimal import Decimal

import pytest

from tools import check_snapshot, export_snapshot, loader, snapshot, standard


def weekdays(start, end):
    day, out = start, []
    while day <= end:
        if day.weekday() < 5:
            out.append(day)
        day += timedelta(days=1)
    return out


def obs(kind, days, price=1000, source=1):
    return [(d, kind, price, source) for d in days]


# ---- 이어 붙이기 규칙 -------------------------------------------------------------

def test_merge_switches_after_three_consecutive_days_and_ignores_early_days():
    days = weekdays(date(2024, 4, 1), date(2024, 5, 31))
    winter = obs('06', [d for d in days if d <= date(2024, 5, 20)], 1000, 11)
    # 봄 작형이 5/6에 하루, 5/13부터 연속 관측
    spring = obs('01', [date(2024, 5, 6)] + [d for d in days if d >= date(2024, 5, 13)], 2000, 13)
    rows = loader.merge_kinds(winter + spring, days)
    switch = [r for r in rows if r.kind_switch]
    assert [(r.price_date, r.kind_code) for r in switch] == [(date(2024, 5, 15), '01')]
    assert rows[0].kind_switch == 0  # 처음 시작은 전환이 아님
    assert {r.kind_code for r in rows if r.price_date < date(2024, 5, 15)} == {'06'}
    assert next(r for r in rows if r.price_date == date(2024, 5, 6)).price == 1000  # 전환 전 새 작형 값 안 씀


def test_merge_never_returns_to_previous_kind():
    days = weekdays(date(2024, 5, 1), date(2024, 6, 28))
    winter = obs('06', days, 1000)  # 떠난 작형이 계속 관측돼도
    spring = obs('01', [d for d in days if d >= date(2024, 5, 6)], 2000)
    rows = loader.merge_kinds(winter + spring, days)
    assert sum(r.kind_switch for r in rows) == 1
    assert rows[-1].kind_code == '01'


def test_merge_restarts_after_ten_missing_survey_days():
    days = weekdays(date(2021, 5, 3), date(2021, 11, 30))
    spring = obs('01', [d for d in days if d <= date(2021, 7, 30)])
    autumn = obs('03', [d for d in days if d >= date(2021, 10, 4)], 3000)  # 고랭지 없음 → 봄에서 가을로
    rows = loader.merge_kinds(spring + autumn, days)
    restart = next(r for r in rows if r.price_date == date(2021, 10, 4))
    assert (restart.kind_code, restart.kind_switch) == ('03', 1)
    assert not [r for r in rows if date(2021, 7, 30) < r.price_date < date(2021, 10, 4)]


def test_merge_prefers_month_priority_when_two_candidates_ready():
    days = weekdays(date(2021, 9, 20), date(2021, 10, 29))
    spring = obs('01', days, 1000)  # 고랭지 없던 해: 봄이 10월까지 이어짐
    # 10월: next(봄)=고랭지 02, 그 달 우선 작형=가을 03. 같은 날 둘 다 3일째 → 우선 작형 03
    highland = obs('02', [d for d in days if d >= date(2021, 10, 4)], 2000)
    autumn = obs('03', [d for d in days if d >= date(2021, 10, 4)], 3000)
    rows = loader.merge_kinds(spring + highland + autumn, days)
    assert [(r.price_date, r.kind_code) for r in rows if r.kind_switch] == [(date(2021, 10, 6), '03')]


def test_merge_start_picks_priority_or_next_in_cycle():
    days = weekdays(date(2024, 8, 1), date(2024, 8, 9))
    rows = loader.merge_kinds(obs('06', days) + obs('03', days, 3000), days)
    assert rows[0].kind_code == '03'  # 8월 우선 02 없음 → 순환상 02 다음 03


# ---- 내보내기 → 검사 ----------------------------------------------------------------

CUTOFF = standard.DATA_CUTOFF


def fake_raw():
    calendar, day = [], date(2016, 1, 1)
    while day <= date(2027, 12, 31):
        closed = day.weekday() >= 5
        calendar.append((day, day.isoweekday(), False, None, 1, 1, False, closed))
        day += timedelta(days=1)
    survey = [d for d, *_, closed in calendar if not closed and d <= CUTOFF]
    series = [(1, '대파', 'RETAIL', '246', '00', '04', Decimal('1.000'), 'kg'),
              (2, '대파', 'WHOLESALE', '246', '00', '04', Decimal('1.000'), 'kg'),
              (11, '배추(월동)', 'RETAIL', '211', '06', '04', Decimal('1.000'), '포기'),
              (13, '배추(봄)', 'RETAIL', '211', '01', '04', Decimal('1.000'), '포기')]
    daily = [(sid, d, 1000 + d.toordinal() % 50) for sid in (1, 2) for d in survey]
    daily += [(11, d, 3000) for d in survey if d.month in (12, 1, 2, 3, 4, 5)]
    daily += [(13, d, 4000) for d in survey if d.month in (5, 6, 7, 8, 9, 10, 11)]
    daily.append((1, CUTOFF + timedelta(days=3), 9999))  # 마감일 뒤 행은 쿼리가 거르는 것을 흉내
    return {
        'series': series,
        'price_daily': [r for r in daily if r[1] <= CUTOFF],
        'calendar_day': calendar,
        'calendar_event': [('CHUSEOK', '추석', date(2025, 10, 5), date(2025, 10, 7), date(2025, 9, 25),
                            date(2025, 10, 7))],
        'weather_daily': [(d, Decimal('12.50'), 20, 5, Decimal('0.0'), 60, 5, 0, 0, 0, 93) for d in survey[:30]],
        'exchange_rate_daily': [(d, 'USD', Decimal('1380.1200'), '1달러') for d in survey[:30]],
        'production': export_snapshot.production_rows(lambda key: {2024: 1.0, 2025: 2.0, 2026: 3.0}, CUTOFF,
                                                      ['대파', '배추']),
        'flyway': [('1', 'init', True)],
    }


@pytest.fixture
def built(tmp_path):
    out = tmp_path / standard.DATA_VERSION
    manifest = export_snapshot.build(fake_raw(), out, cutoff=CUTOFF, meta={'git_sha': 'abc', 'git_dirty': False})
    return out, manifest


def test_export_then_check_passes(built):
    out, manifest = built
    errors, _ = check_snapshot.check(out)
    assert errors == []
    assert manifest['series_count'] == 3  # 대파 2 + 배추 소매 이어 붙인 9001
    ids = [s['series_id'] for s in manifest['series']]
    assert ids == [1, 2, 9001]
    merged = next(s for s in manifest['series'] if s['series_id'] == 9001)
    assert merged['source_series'] == [{'source_series_id': 11, 'kind_code': '06'},
                                       {'source_series_id': 13, 'kind_code': '01'}]
    assert merged['merge']['per_year']
    # 생산량: 사용 시작일(Y+1-06-30)이 마감일 뒤인 2026년은 빠짐
    assert loader.read_table(out, 'item_production.csv')[-1] == {'item': '배추', 'year': '2025',
                                                                 'production_ton': '2', 'published_from': '2026-06-30'}
    assert loader.read_table(out, 'weather_daily.csv')[0]['avg_temp'] == '12.5'
    assert (out / 'price_daily.csv').read_bytes().count(b'\r') == 0


def test_check_detects_tampering(built):
    out, _ = built
    path = out / 'price_daily.csv'
    lines = path.read_text(encoding='utf-8').splitlines(keepends=True)
    lines[5] = lines[5].rsplit(',', 1)[0] + ',1\n'
    path.write_text(''.join(lines), encoding='utf-8', newline='')
    errors, _ = check_snapshot.check(out)
    assert any('price_daily.csv SHA-256' in e for e in errors)


def test_check_detects_merge_mismatch_even_with_matching_hash(built):
    out, _ = built
    path = out / 'price_daily_merged.csv'
    text = path.read_text(encoding='utf-8').replace(',01,13,1\n', ',01,13,0\n', 1)
    path.write_text(text, encoding='utf-8', newline='')
    manifest = json.loads((out / 'manifest.json').read_text(encoding='utf-8'))
    manifest['files']['price_daily_merged.csv']['sha256'] = snapshot.sha256(path)
    (out / 'manifest.json').write_text(json.dumps(manifest, ensure_ascii=False), encoding='utf-8')
    errors, _ = check_snapshot.check(out)
    assert any('이어 붙이기 재계산과 다름' in e for e in errors)


def test_check_detects_extra_file_and_wrong_snapshot_id(built):
    out, _ = built
    (out / 'extra.csv').write_text('x\n', encoding='utf-8')
    manifest = json.loads((out / 'manifest.json').read_text(encoding='utf-8'))
    manifest['snapshot_id'] = 'other'
    (out / 'manifest.json').write_text(json.dumps(manifest, ensure_ascii=False), encoding='utf-8')
    errors, _ = check_snapshot.check(out)
    assert any('extra.csv' in e for e in errors) and any('snapshot_id' in e for e in errors)


def test_export_rejects_rows_after_cutoff_and_non_empty_folder(tmp_path, built):
    raw = fake_raw()
    raw['price_daily'].append((1, CUTOFF + timedelta(days=1), 1))
    with pytest.raises(export_snapshot.SnapshotError, match='마감일'):
        export_snapshot.build(raw, tmp_path / 'a', cutoff=CUTOFF)
    with pytest.raises(export_snapshot.SnapshotError, match='비어 있지 않음'):
        export_snapshot.build(fake_raw(), built[0], cutoff=CUTOFF)


def test_export_excludes_item_and_rejects_mixed_units(tmp_path):
    manifest = export_snapshot.build(fake_raw(), tmp_path / 'a', cutoff=CUTOFF, exclude_items=['배추'])
    assert [s['series_id'] for s in manifest['series']] == [1, 2] and manifest['excluded_items'] == ['배추']
    raw = fake_raw()
    raw['series'][3] = (13, '배추(봄)', 'RETAIL', '211', '01', '04', Decimal('3.000'), '포기')
    with pytest.raises(export_snapshot.SnapshotError, match='단위'):
        export_snapshot.build(raw, tmp_path / 'b', cutoff=CUTOFF)


def test_quality_flags_long_gap_for_review():
    survey = weekdays(date(2016, 1, 4), CUTOFF)
    days = {d for d in survey if not (date(2025, 6, 25) <= d <= date(2025, 7, 31))}
    quality = snapshot.series_quality(days, survey, CUTOFF)
    assert quality['status'] == 'REVIEW'
    assert quality['missing_runs_from_2023'] == [('2025-06-25', '2025-07-31', 27)]
