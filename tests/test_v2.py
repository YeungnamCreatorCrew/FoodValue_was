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
from tests.test_snapshot_tools import fake_raw
from tools import export_snapshot, loader, standard


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
    bundles, blocks = [], list(F.V2_BLOCKS)
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
