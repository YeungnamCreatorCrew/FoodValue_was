"""v2(모든 자료 연동·통합 학습) 테스트: 시점 규칙, 창 통계, 반입량 결측 처리, 통합 실행기."""
import argparse
import csv
import json
import math
import shutil
from datetime import date, timedelta

import numpy as np
import pytest

from model_comparison.v2 import features as F
from model_comparison.v2 import run_pooled
from model_comparison.v2 import snapshot as v2_snapshot
from tests.test_snapshot_tools import fake_raw
from tools import export_snapshot, loader, standard
from tools import snapshot as tools_snapshot


@pytest.fixture(scope='module')
def snap_dir(tmp_path_factory):
    out = tmp_path_factory.mktemp('snap') / standard.DATA_VERSION
    export_snapshot.build(fake_raw(), out, cutoff=standard.DATA_CUTOFF)
    return out


def write_extra(folder, cut=None):
    """가짜 v2 추가 자료: 관측소 2곳 날씨(2015~), 반입량(2021~, 일요일 행 없음). cut 이후 날짜 행은 지운다."""
    folder.mkdir(parents=True, exist_ok=True)
    day, weather, garak = date(2015, 1, 1), [], []
    while day <= standard.DATA_CUTOFF:
        if cut is None or day < cut:
            for stn in (100, 200):
                rain = '' if day.toordinal() % 3 else f'{day.toordinal() % 11}'
                weather.append([stn, day.isoformat(), 10 + day.toordinal() % 13 + stn / 100, 0, 20, rain, 60, 5])
            if day >= date(2021, 1, 1) and day.weekday() != 6:
                for item in standard.ITEMS:
                    garak.append([day.isoformat(), item, 100 + day.toordinal() % 17])
        day += timedelta(days=1)
    tables = {
        'asos_station_daily.csv': (('stn_id', 'obs_date', 'avg_ta', 'min_ta', 'max_ta', 'sum_rn', 'avg_rhm', 'sum_ss_hr'),
                                   weather),
        'garak_arrivals_daily.csv': (('arrival_date', 'item', 'ton'), garak),
        'item_station.csv': (('item', 'stn_id', 'stn_name', 'role'),
                             [[item, s, 'x', 'x'] for item in standard.ITEMS for s in (100, 200)]),
    }
    for name, (header, rows) in tables.items():
        with open(folder / name, 'w', encoding='utf-8', newline='') as f:
            writer = csv.writer(f, lineterminator='\n')
            writer.writerow(header)
            writer.writerows(rows)
    (folder / 'manifest.json').write_text(json.dumps({'extra_id': 'test'}), encoding='utf-8')
    return folder


def test_window_stat_matches_manual_sum():
    values = np.arange(30, dtype=float)
    values[5] = np.nan
    out = F._window_stat(values, end_lag=1, length=7, how='sum')
    # 행 20 = values[13..19] 합
    assert out[20] == pytest.approx(values[13:20].sum())
    # 행 10 = values[3..9], 5번 결측(6/7 ≥ 70%) → 평균 × 7
    assert out[10] == pytest.approx(np.nanmean(values[3:10]) * 7)
    assert math.isnan(out[3])


def test_v2_features_use_only_data_before_d(tmp_path, snap_dir):
    """d일과 그 뒤 날씨·반입량을 지워도 기준일 d의 v2 특징은 같아야 한다."""
    d = date(2025, 3, 5)
    snap = loader.Snapshot(snap_dir)
    full = F.V2Features(snap, write_extra(tmp_path / 'full'))
    part = F.V2Features(snap, write_extra(tmp_path / 'part', cut=d))
    bundles, blocks = [], [b for b in F.V2_BLOCKS if b != 'KREI']  # KREI는 별도 스냅샷(아래 KREI 테스트)
    i = snap.series[1].index(d)
    a = F.rows(snap, full, 1, [i], [3], bundles, blocks)[0]
    b = F.rows(snap, part, 1, [i], [3], bundles, blocks)[0]
    assert ((a == b) | (np.isnan(a) & np.isnan(b))).all()
    names = F.feature_names(bundles, blocks)
    assert not np.isnan(a[names.index('ow_temp_w52')]) and not np.isnan(a[names.index('garak_w8')])


def test_garak_missing_sunday_is_zero_but_before_coverage_is_nan(tmp_path, snap_dir):
    snap = loader.Snapshot(snap_dir)
    v2 = F.V2Features(snap, write_extra(tmp_path / 'e'))
    names = F.feature_names([], ['GARAK'])
    s = snap.series[1]
    d = date(2025, 3, 5)
    row = F.rows(snap, v2, 1, [s.index(d)], [1], [], ['GARAK'])[0]
    week = [d - timedelta(days=k) for k in range(1, 8)]
    expected = sum(0 if day.weekday() == 6 else 100 + day.toordinal() % 17 for day in week)
    assert row[names.index('garak_w1')] == pytest.approx(expected)
    early = F.rows(snap, v2, 1, [s.index(date(2020, 6, 1))], [1], [], ['GARAK'])[0]
    assert math.isnan(early[names.index('garak_w1')])


def test_garak_spike_rule_uses_only_past_values():
    start = date(2021, 1, 4)
    tons = {('무', start + timedelta(days=i)): 300.0 + i for i in range(30)}
    tons['무', start + timedelta(days=1)] = 0.0  # 0톤은 기준에서 빠질 뿐 의심값이 아님
    early, spike, normal = start + timedelta(days=5), start + timedelta(days=20), start + timedelta(days=25)
    tons['무', early] = 99999.0  # 직전 값이 10개 미만 → 판정 안 함
    tons['무', spike] = 300.0 * 9  # 직전 중앙값(~310)의 8배 초과
    tons['무', normal] = 300.0 * 7  # 7배 → 유지
    assert set(v2_snapshot.drop_garak_spikes(tons)) == {('무', spike)}


def test_clean_blanks_only_spikes_and_is_deterministic(tmp_path):
    raw = write_extra(tmp_path / 'raw')
    path = raw / 'garak_arrivals_daily.csv'
    lines = path.read_text(encoding='utf-8').splitlines()
    target = next(i for i, line in enumerate(lines) if line.startswith('2025-03-04,'))
    day, item, _ = lines[target].split(',')
    lines[target] = f'{day},{item},99999'
    path.write_text('\n'.join(lines) + '\n', encoding='utf-8')
    files = {name: {'sha256': tools_snapshot.sha256(raw / name), 'rows': 0}
             for name in ('asos_station_daily.csv', 'garak_arrivals_daily.csv', 'item_station.csv')}
    (raw / 'manifest.json').write_text(json.dumps({'extra_id': 'raw', 'base_snapshot_id': standard.DATA_VERSION,
                                                   'base_manifest_sha256': 'x', 'cutoff': '2026-10-31',
                                                   'files': files}), encoding='utf-8')
    a = v2_snapshot.clean(raw, tmp_path / 'a')
    b = v2_snapshot.clean(raw, tmp_path / 'b')
    assert a['files'] == b['files'] and a['cleaning']['garak_spike']['dropped'] == 1
    out = (tmp_path / 'a' / 'garak_arrivals_daily.csv').read_text(encoding='utf-8').splitlines()
    assert out[target] == f'{day},{item},' and sum(x != y for x, y in zip(out, lines)) == 1
    assert (tmp_path / 'a' / 'asos_station_daily.csv').read_bytes() == (raw / 'asos_station_daily.csv').read_bytes()


def test_empty_garak_ton_is_nan_not_zero(tmp_path, snap_dir):
    """정제본에서 빈 ton(뺀 값)은 NaN: 그 주 합은 남은 값 평균 × 7, 일요일(행 없음)은 0톤."""
    extra = write_extra(tmp_path / 'e')
    path = extra / 'garak_arrivals_daily.csv'
    d = date(2025, 3, 5)
    blank = (d - timedelta(days=1)).isoformat()
    item = loader.Snapshot(snap_dir).series[1].item
    text = '\n'.join(f'{blank},{item},' if line.startswith(f'{blank},{item},') else line
                     for line in path.read_text(encoding='utf-8').splitlines()) + '\n'
    path.write_text(text, encoding='utf-8')
    snap = loader.Snapshot(snap_dir)
    v2 = F.V2Features(snap, extra)
    names = F.feature_names([], ['GARAK'])
    row = F.rows(snap, v2, 1, [snap.series[1].index(d)], [1], [], ['GARAK'])[0]
    week = [d - timedelta(days=k) for k in range(2, 8)]
    kept = [0 if day.weekday() == 6 else 100 + day.toordinal() % 17 for day in week]
    assert row[names.index('garak_w1')] == pytest.approx(sum(kept) / len(kept) * 7)


def test_pooled_runner_end_to_end(tmp_path, snap_dir):
    extra = write_extra(tmp_path / 'extra')
    config = {'name': 't', 'class': 'model_comparison.v2.models:PooledXGB',
              'params': {'n_estimators': 20, 'max_depth': 2}, 'bundles': ['MARKET'],
              'blocks': ['ORIGIN_WEATHER', 'GARAK', 'SERIES_ID'], 'window_days': 1825, 'seed': 42}
    path = tmp_path / 'c.json'
    path.write_text(json.dumps(config), encoding='utf-8')
    args = argparse.Namespace(config=path, origins='validation', month='2025-02', series=None, snapshot=snap_dir,
                              extra=extra, out=tmp_path / 'out')
    folder = run_pooled.run(args)
    metrics = json.loads((folder / 'metrics.json').read_text(encoding='utf-8'))
    assert metrics['series_count'] == 3 and metrics['results']['policy']['points'] > 0
    assert (folder / 'importance.json').exists()
    second = run_pooled.run(args)
    assert (folder / 'metrics.json').read_bytes() == (second / 'metrics.json').read_bytes()
    shutil.rmtree(tmp_path / 'out')


def test_pooled_runner_refuses_test_origins(tmp_path, snap_dir):
    path = tmp_path / 'c.json'
    path.write_text(json.dumps({'name': 't', 'class': 'x:y'}), encoding='utf-8')
    args = argparse.Namespace(config=path, origins='test', month=None, series=None, snapshot=snap_dir,
                              extra=tmp_path, out=tmp_path)
    with pytest.raises(SystemExit, match='최종 시험'):
        run_pooled.run(args)


def test_price_dynamics_use_only_prices_up_to_d():
    """PRICE_DYN: d 뒤 가격을 바꿔도 기준일 d의 값(작년 같은 시기 h일 변화 포함)은 같아야 한다."""
    rng = np.random.default_rng(0)
    v = 1000 * np.exp(np.cumsum(rng.normal(0, .02, 1500)))
    v[rng.random(1500) < .3] = np.nan
    d = 1200
    other = v.copy()
    other[d + 1:] = 1.0
    a, b = F.price_dynamics(v), F.price_dynamics(other)
    assert ((a[d] == b[d]) | (np.isnan(a[d]) & np.isnan(b[d]))).all()
    for h in standard.HORIZONS:
        assert F._analog(v, h)[0][d] == pytest.approx(F._analog(other, h)[0][d], nan_ok=True)
    assert a.shape[1] == len(F.PRICE_DYN_NAMES) - 1  # pd_analog_chg_h는 시점별로 rows()가 붙인다


def test_price_dynamics_flat_share_and_days_since_change():
    v = np.array([100.0] * 40 + [110.0] + [110.0] * 5)
    out = F.price_dynamics(v)
    names = F.PRICE_DYN_NAMES
    assert out[39, names.index('pd_flat_share28')] == pytest.approx(1.0)
    assert out[40, names.index('pd_days_since_change')] == 0
    assert out[45, names.index('pd_days_since_change')] == 5


def test_price_only_blocks_run_without_extra_folder(tmp_path, snap_dir):
    """SERIES_ID·CROSS_ITEM·PRICE_DYN만 쓰면 추가 자료 폴더가 없어도 돈다. 가중·LightGBM 경로도 함께 확인."""
    for cls, params in (('PooledXGB', {'n_estimators': 20, 'max_depth': 2, 'series_weight': 'inv_scale',
                                       'halflife_days': 365}),
                        ('PooledLGBM', {'n_estimators': 20, 'num_leaves': 4, 'series_weight': 'balanced'})):
        config = {'name': cls, 'class': f'model_comparison.v2.models:{cls}', 'params': params,
                  'bundles': ['MARKET'], 'blocks': ['SERIES_ID', 'CROSS_ITEM', 'PRICE_DYN'], 'seed': 42}
        path = tmp_path / f'{cls}.json'
        path.write_text(json.dumps(config), encoding='utf-8')
        args = argparse.Namespace(config=path, origins='validation', month='2025-02', series=None,
                                  snapshot=snap_dir, extra=tmp_path / 'missing', out=tmp_path / 'out')
        folder = run_pooled.run(args)
        metrics = json.loads((folder / 'metrics.json').read_text(encoding='utf-8'))
        assert metrics['results']['policy']['points'] > 0
    shutil.rmtree(tmp_path / 'out')


def test_sample_weights_balance_series_and_decay():
    from model_comparison.v2.models import sample_weights

    y = np.array([.1, .1, .1, .01])
    groups = np.array([1, 1, 1, 2])
    w = sample_weights(y, groups, None, 'balanced')
    assert w[:3].sum() == pytest.approx(w[3]) and w.mean() == pytest.approx(1)
    w = sample_weights(y, groups, None, 'inv_scale')
    assert w[3] / w[0] == pytest.approx(10)
    w = sample_weights(y, None, np.array([0, 365, 730, 0]), None, 365)
    assert w[0] / w[1] == pytest.approx(2) and w[1] / w[2] == pytest.approx(2)
    assert sample_weights(y, groups, None) is None


def test_ensemble_averages_ok_rows_and_falls_back_to_members(tmp_path, snap_dir):
    from model_comparison.v2 import ensemble

    folders = []
    for name, depth in (('a', 2), ('b', 3)):
        config = {'name': name, 'class': 'model_comparison.v2.models:PooledXGB',
                  'params': {'n_estimators': 20, 'max_depth': depth}, 'bundles': [], 'blocks': ['SERIES_ID'],
                  'seed': 42}
        path = tmp_path / f'{name}.json'
        path.write_text(json.dumps(config), encoding='utf-8')
        folders.append(run_pooled.run(argparse.Namespace(
            config=path, origins='validation', month='2025-02', series=None, snapshot=snap_dir,
            extra=tmp_path / 'missing', out=tmp_path / 'out')))
    rows = ensemble.combine(folders, [3, 1])
    a, b = (ensemble._read(f) for f in folders)
    for r in rows:
        key = (r['series_id'], r['origin_date'], r['horizon'])
        if a[key]['status'] == 'OK' and b[key]['status'] == 'OK':
            expected = .75 * float(a[key]['predicted_price']) + .25 * float(b[key]['predicted_price'])
            assert r['predicted_price'] == pytest.approx(expected)
        elif a[key]['status'] != 'OK' and b[key]['status'] != 'OK':
            assert r['status'] == a[key]['status']
    folder = ensemble.run(argparse.Namespace(folders=[str(f) for f in folders], name='e', weights=None, how='mean',
                                             snapshot=snap_dir, out=tmp_path / 'ens'))
    assert json.loads((folder / 'metrics.json').read_text(encoding='utf-8'))['results']['policy']['points'] > 0


def write_krei(folder, reports):
    """가짜 KREI 스냅샷. reports: [(key, available_from, [(item, crop, metric, kind, start, end, basis, value, dir)])]"""
    from model_comparison.v2 import krei

    folder.mkdir(parents=True, exist_ok=True)
    rows = []
    for key, available, facts in reports:
        for item, crop, metric, kind, start, end, basis, value, direction in facts:
            rows.append({'source_record_key': key, 'available_from': available, 'item_name': item, 'crop_type': crop,
                         'metric': metric, 'kind': kind, 'target_start': start, 'target_end': end, 'basis': basis,
                         'value': value, 'value_low': '', 'value_high': '', 'direction': direction})
    with open(folder / 'krei_values.csv', 'w', encoding='utf-8-sig', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=krei.COLUMNS)
        writer.writeheader()
        writer.writerows(rows)
    (folder / 'manifest.json').write_text(json.dumps({'snapshot_id': 'test', 'values_rows': len(rows)}),
                                          encoding='utf-8')
    return folder


def cabbage_report(key, available, month_start, month_end, prev_start, prev_end, outlook, actual, ship):
    return (key, available, [
        ('배추', '', 'WHOLESALE_PRICE', 'OUTLOOK', month_start, month_end, 'LEVEL', outlook, ''),
        ('배추', '', 'WHOLESALE_PRICE', 'OUTLOOK', month_start, month_end, 'PREV_YEAR', '', 'UP'),
        ('배추', '', 'WHOLESALE_PRICE', 'ACTUAL', prev_start, prev_end, 'LEVEL', actual, ''),
        ('배추', '', 'SHIPMENT', 'OUTLOOK', month_start, month_end, 'PREV_YEAR', ship, 'DOWN'),
        ('배추', '가을', 'SHIPMENT', 'OUTLOOK', month_start, month_end, 'PREV_YEAR', '-99', 'DOWN'),
    ])


def test_krei_features_use_only_reports_published_before_d(tmp_path):
    from model_comparison.v2 import krei

    folder = write_krei(tmp_path / 'k', [
        cabbage_report('A:1', '2025-03-06T10:00:00+09:00', '2025-03-01', '2025-03-31', '2025-02-01', '2025-02-28',
                       '12000', '10000', '-15.1'),
        cabbage_report('A:2', '2025-04-02T09:00:00+09:00', '2025-04-01', '2025-04-30', '2025-03-01', '2025-03-31',
                       '9000', '10000', '3'),
        cabbage_report('A:3', '2026-11-03T09:00:00+09:00', '2026-11-01', '2026-11-30', '2026-10-01', '2026-10-31',
                       '1', '1', '1'),  # 마감일 뒤 공개 → 읽지 않음
    ])
    k = krei.KreiSnapshot(folder)
    assert len(k.reports) == 2 and k.dropped_after_cutoff == 1
    start = date(2025, 1, 1)
    filled = np.full(200, 100.0)
    f = k.features('배추', start, filled)
    at = lambda d: dict(zip(krei.NAMES, f[(d - start).days]))  # noqa: E731
    assert np.isnan(at(date(2025, 3, 6))['krei_price_outlook_chg'])  # 공개 당일은 아직 쓰지 않음(d−1 규칙)
    day = at(date(2025, 3, 7))
    assert day['krei_price_outlook_chg'] == pytest.approx(.2)
    assert day['krei_implied_vs_current'] == pytest.approx(.2)  # 지난달 평균 100 × 1.2 / 현재 100 − 1
    assert day['krei_price_dir_py'] == 1 and 'krei_price_dir_nm' not in day  # 평년 대비는 쓰지 않음
    assert day['krei_shipment_py'] == pytest.approx(-15.1)  # 작형 행(-99)이 아니라 전체 행
    assert day['krei_days_since'] == 1
    assert at(date(2025, 4, 3))['krei_price_outlook_chg'] == pytest.approx(-.1)
    # 4월 전망은 4월이 지나면 쓰지 않는다(경과일만 남음)
    late = at(date(2025, 5, 10))
    assert np.isnan(late['krei_price_outlook_chg']) and np.isnan(late['krei_shipment_py'])
    assert late['krei_days_since'] == (date(2025, 5, 10) - date(2025, 4, 2)).days
    # 미래 호를 지워도 과거 기준일 값은 같다
    part = krei.KreiSnapshot(write_krei(tmp_path / 'p', [cabbage_report(
        'A:1', '2025-03-06T10:00:00+09:00', '2025-03-01', '2025-03-31', '2025-02-01', '2025-02-28', '12000', '10000',
        '-15.1')]))
    g = part.features('배추', start, filled)
    i = (date(2025, 3, 20) - start).days
    assert np.allclose(f[i], g[i], equal_nan=True)
    assert np.isnan(k.features('대파', start, filled)).all()


def test_krei_shipment_direction_only_flat_is_zero(tmp_path):
    from model_comparison.v2 import krei

    facts = [('배추', '', 'WHOLESALE_PRICE', 'OUTLOOK', '2025-03-01', '2025-03-31', 'LEVEL', '12000', ''),
             ('배추', '', 'WHOLESALE_PRICE', 'ACTUAL', '2025-02-01', '2025-02-28', 'LEVEL', '10000', ''),
             ('배추', '', 'SHIPMENT', 'OUTLOOK', '2025-03-01', '2025-03-31', 'PREV_YEAR', '', 'FLAT'),
             ('무', '', 'WHOLESALE_PRICE', 'OUTLOOK', '2025-03-01', '2025-03-31', 'LEVEL', '12000', ''),
             ('무', '', 'SHIPMENT', 'OUTLOOK', '2025-03-01', '2025-03-31', 'PREV_YEAR', '', 'DOWN')]
    k = krei.KreiSnapshot(write_krei(tmp_path / 'k', [('A:1', '2025-03-06T10:00:00+09:00', facts)]))
    start = date(2025, 3, 1)
    i, j = (date(2025, 3, 10) - start).days, krei.NAMES.index('krei_shipment_py')
    assert k.features('배추', start, np.full(20, 100.0))[i, j] == 0
    assert np.isnan(k.features('무', start, np.full(20, 100.0))[i, j])


def test_krei_rejects_missing_columns_and_row_count_mismatch(tmp_path):
    from model_comparison.v2 import krei

    folder = write_krei(tmp_path / 'k', [cabbage_report(
        'A:1', '2025-03-06T10:00:00+09:00', '2025-03-01', '2025-03-31', '2025-02-01', '2025-02-28', '1', '1', '1')])
    (folder / 'manifest.json').write_text(json.dumps({'values_rows': 999}), encoding='utf-8')
    with pytest.raises(ValueError, match='행 수'):
        krei.KreiSnapshot(folder)
    with open(folder / 'krei_values.csv', 'w', encoding='utf-8-sig', newline='') as f:
        f.write('source_record_key,available_from\nA:1,2025-03-06T10:00:00+09:00\n')
    with pytest.raises(ValueError, match='열'):
        krei.KreiSnapshot(folder)


def test_pooled_runner_with_krei_block(tmp_path, snap_dir):
    folder = write_krei(tmp_path / 'k', [cabbage_report(
        'A:1', '2025-01-03T10:00:00+09:00', '2025-01-01', '2025-01-31', '2024-12-01', '2024-12-31', '1', '1', '1')])
    config = {'name': 'k', 'class': 'model_comparison.v2.models:PooledXGB',
              'params': {'n_estimators': 20, 'max_depth': 2}, 'bundles': [], 'blocks': ['SERIES_ID', 'KREI'],
              'seed': 42}
    path = tmp_path / 'k.json'
    path.write_text(json.dumps(config), encoding='utf-8')
    out = run_pooled.run(argparse.Namespace(config=path, origins='validation', month='2025-02', series=None,
                                            snapshot=snap_dir, extra=tmp_path / 'missing', krei=folder,
                                            out=tmp_path / 'out'))
    record = json.loads((out / 'config.json').read_text(encoding='utf-8'))
    assert record['v2_krei']['snapshot_id'] == 'test' and record['feature_count'] == 15 + 6 + 5


def fake_kind_observations(seed=0, years=(2019, 2020, 2021, 2022)):
    """가짜 배추 작형별 관측: 작형마다 출하 기간 + 시작 전 띄엄띄엄 관측 + 겹치는 기간(떠나는 작형도 계속 관측)."""
    rng = np.random.default_rng(seed)
    seasons = [('06', (1, 1), (5, 15)), ('01', (5, 1), (7, 31)), ('02', (7, 15), (10, 31)), ('03', (10, 20), (12, 31))]
    obs = {}
    for year in years:
        for kind, (m1, d1), (m2, d2) in seasons:
            begin, end = date(year, m1, d1), date(year, m2, d2)
            level = int(rng.integers(800, 3000))
            day = begin - timedelta(days=12)
            while day <= end + timedelta(days=10):
                early = day < begin
                if (not early or rng.random() < .3) and day.weekday() < 5:
                    obs[day, kind] = level + int(rng.integers(-100, 100))
                day += timedelta(days=1)
    survey = []
    day = date(years[0], 1, 1)
    while day <= date(years[-1], 12, 31):
        if day.weekday() < 5:
            survey.append(day)
        day += timedelta(days=1)
    return [(d, k, p) for (d, k), p in sorted(obs.items())], survey


def test_kind_state_replays_merge_rule_switches():
    """KIND 묶음이 따라가는 작형 상태가 이어 붙이기(loader.merge_kinds)의 전환일과 같아야 한다."""
    obs, survey = fake_kind_observations()
    merged = loader.merge_kinds([(d, k, p, 1) for d, k, p in obs], survey)
    expected = [(r.price_date, r.kind_code) for r in merged if r.kind_switch]
    start = merged[0].price_date
    n = (merged[-1].price_date - start).days + 1
    filled = np.full(n, 1000.0)
    _, switches = F.kind_state(obs, survey, start, n, filled)
    assert switches == expected and len(expected) >= 8


def test_kind_state_uses_only_observations_up_to_d():
    """d 뒤 작형별 관측을 지워도 d까지의 KIND 특징은 같아야 한다(여러 d에서)."""
    obs, survey = fake_kind_observations(seed=1)
    start = obs[0][0]
    n = (survey[-1] - start).days + 1
    filled = np.linspace(900, 1500, n)
    full, _ = F.kind_state(obs, survey, start, n, filled)
    assert np.isfinite(full[:, 1]).sum() > 50 and np.isfinite(full[:, 4]).sum() > 100
    for d in (date(2020, 4, 28), date(2021, 7, 12), date(2022, 10, 18), date(2022, 12, 30)):
        part, _ = F.kind_state([o for o in obs if o[0] <= d], [s for s in survey if s <= d], start, n, filled)
        i = (d - start).days
        a, b = full[:i + 1], part[:i + 1]
        assert ((a == b) | (np.isnan(a) & np.isnan(b))).all(), d


def test_kind_state_real_snapshot_matches_merged_file():
    """실제 스냅샷이 있으면: 다시 따라간 전환일이 price_daily_merged.csv의 kind_switch와 같아야 한다."""
    folder = loader.Path(__file__).resolve().parents[1] / 'data' / 'snapshots' / standard.DATA_VERSION
    if not (folder / 'price_daily_kind.csv').exists():
        pytest.skip('실제 스냅샷 없음')
    survey = [d for d, closed in loader.read_calendar(folder) if not closed]
    kinds, merged = {}, {}
    for r in loader.read_table(folder, 'price_daily_kind.csv'):
        kinds.setdefault(int(r['merged_series_id']), []).append(
            (date.fromisoformat(r['price_date']), r['kind_code'], int(r['price'])))
    for r in loader.read_table(folder, 'price_daily_merged.csv'):
        merged.setdefault(int(r['series_id']), []).append(r)
    for sid, obs in kinds.items():
        rows = merged[sid]
        expected = [(date.fromisoformat(r['price_date']), r['kind_code']) for r in rows if r['kind_switch'] == '1']
        start = date.fromisoformat(rows[0]['price_date'])
        n = (date.fromisoformat(rows[-1]['price_date']) - start).days + 1
        _, switches = F.kind_state(obs, survey, start, n, np.full(n, 1000.0))
        assert switches == expected, sid
