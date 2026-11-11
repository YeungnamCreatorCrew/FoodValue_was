"""공통 로더·실행기·평가기(기준서 §3, §5, §8, §9) 테스트. 가짜 스냅샷으로 처음부터 끝까지 돌린다."""
import argparse
import csv
import json
import math
from datetime import date, timedelta
from pathlib import Path

import numpy as np
import pytest

from tests.test_snapshot_tools import fake_raw
from tools import evaluate, export_snapshot, loader, run_backtest, standard
from tools.validate_experiment import validate


@pytest.fixture(scope='module')
def snap_dir(tmp_path_factory):
    out = tmp_path_factory.mktemp('snap') / standard.DATA_VERSION
    export_snapshot.build(fake_raw(), out, cutoff=standard.DATA_CUTOFF)
    return out


@pytest.fixture(scope='module')
def snap(snap_dir):
    return loader.Snapshot(snap_dir)


# ---- 로더 ---------------------------------------------------------------------------------

def test_training_data_has_no_future_targets_and_respects_window(snap):
    as_of = date(2025, 1, 6)
    data = snap.training_data(1, as_of)
    targets = [o + timedelta(days=int(h)) for o, h in zip(data.origins, data.horizons)]
    assert max(targets) <= as_of
    assert min(data.origins) >= as_of - timedelta(days=standard.TRAIN_WINDOW_DAYS - 1 - standard.FEATURE_LOOKBACK_DAYS)
    assert data.features.shape == (len(data.targets), len(standard.BASE_FEATURES))
    assert max(day for day, _ in data.prices) <= as_of
    assert set(data.horizons) == set(standard.HORIZONS)


def test_features_match_repository_definition(snap):
    from app.services.price_prediction import features
    s = snap.series[1]
    d = date(2025, 3, 5)
    i = s.index(d)
    days = [s.day(j) for j in range(len(s.actual))]
    values = [None if math.isnan(v) else float(v) for v in s.filled]
    expected = features(days, values, [int(a) for a in s.age], i, 3)
    row = snap.origin_inputs(1, d).features[3]
    names = list(standard.BASE_FEATURES)
    order = ['current', 'lag1', 'lag7', 'lag14', 'lag28', 'mean7', 'mean28', 'change7', 'volatility7',
             'target_weekday', 'target_season_sin', 'target_season_cos', 'price_age']
    assert [round(float(row[names.index(n)]), 9) for n in order] == [round(x, 9) for x in expected]
    assert row[names.index('horizon')] == 3


def test_kind_switch_feature_and_no_input(snap):
    s = snap.series[9001]
    switch = next(s.day(i) for i in range(len(s.actual)) if s.base[i, -1] == 0)
    row = snap.origin_inputs(9001, switch + timedelta(days=2)).features[1]
    assert row[standard.BASE_FEATURES.index('days_since_kind_switch')] == 2
    assert snap.origin_inputs(1, date(2025, 3, 5)).features[1][-1] == standard.KIND_SWITCH_CAP_DAYS
    with pytest.raises(loader.NoInput):
        snap.origin_inputs(1, standard.DATA_CUTOFF + timedelta(days=8))


# ---- 실행기 ---------------------------------------------------------------------------------

class Broken:
    """FIT_FAILED·PREDICT_FAILED·INVALID_VALUE를 만드는 모델."""

    def __init__(self, mode='ok'):
        self.mode = mode

    def fit(self, history, seed):
        if self.mode == 'fit':
            raise RuntimeError('boom')
        self.current = history.feature_names.index('current')

    def predict(self, inputs):
        if self.mode == 'none':
            return [None] * 7
        if self.mode == 'negative':
            return [-1.0] + [float(inputs.features[h][self.current]) for h in range(2, 8)]
        return [float(inputs.features[h][self.current]) * 1.0000004 for h in range(1, 8)]


def run(tmp_path, snap_dir, config, monkeypatch=None, cls=None, **kw):
    path = tmp_path / f'config-{len(list(tmp_path.glob("config-*")))}.json'
    path.write_text(json.dumps(config, ensure_ascii=False), encoding='utf-8')
    if cls is not None:
        monkeypatch.setattr(run_backtest, 'load_class', lambda spec: cls)
    args = argparse.Namespace(config=path, phase=kw.get('phase', 'smoke'), origins=kw.get('origins'),
                              month=kw.get('month', '2025-01'), series=kw.get('series'), snapshot=snap_dir,
                              out=tmp_path / 'experiments', experiment_id=None, where=kw.get('where', 'local'),
                              tuning_log=kw.get('tuning_log'), record_trial=kw.get('record_trial'))
    return run_backtest.run(args)


def read_csv(path):
    with open(path, encoding='utf-8', newline='') as f:
        return list(csv.DictReader(f))


NAIVE = json.loads((Path(__file__).resolve().parents[1] / 'tools' / 'configs' / 'naive.json').read_text(encoding='utf-8'))


def test_naive_smoke_is_valid_and_deterministic(tmp_path, snap_dir):
    first = run(tmp_path, snap_dir, NAIVE, series='1,2')
    second = run(tmp_path, snap_dir, NAIVE, series='1,2')
    assert first.name.startswith('base-smoke-') and first != second
    assert validate(first).errors == []
    assert (first / 'metrics.json').read_bytes() == (second / 'metrics.json').read_bytes()
    metrics = json.loads((first / 'metrics.json').read_text(encoding='utf-8'))
    policy = metrics['results']['policy']
    assert policy['macro_mape'] == policy['naive_macro_mape'] and metrics['success_rate'] == 1.0
    config = json.loads((first / 'config.json').read_text(encoding='utf-8'))
    assert config['data_version'] == standard.DATA_VERSION and config['refit'] == standard.REFIT
    rows = read_csv(first / 'predictions.csv')
    assert len({r['origin_date'] for r in rows}) == len([d for d in loader.Snapshot(snap_dir).origins['validation']
                                                         if d.strftime('%Y-%m') == '2025-01'])


@pytest.mark.parametrize('mode,status', [('fit', 'FIT_FAILED'), ('none', 'PREDICT_FAILED'), ('negative', 'INVALID_VALUE')])
def test_failures_are_recorded_and_policy_falls_back_to_naive(tmp_path, snap_dir, monkeypatch, mode, status):
    config = {**NAIVE, 'model': 'Ridge', 'class': 'x:Broken', 'params': {'mode': mode, 'solver': 'cholesky'}}
    folder = run(tmp_path, snap_dir, config, monkeypatch, cls=lambda mode, solver: Broken(mode))
    rows = read_csv(folder / 'predictions.csv')
    assert any(r['status'] == status and r['predicted_price'] == '' for r in rows)
    assert validate(folder).errors == []
    metrics = json.loads((folder / 'metrics.json').read_text(encoding='utf-8'))
    assert metrics['success_rate'] < 1
    if mode != 'negative':
        assert metrics['results']['policy']['macro_mape'] == metrics['results']['policy']['naive_macro_mape']


def test_raw_is_rounded_half_up_and_recorded_with_six_decimals(tmp_path, snap_dir, monkeypatch):
    config = {**NAIVE, 'model': 'Ridge', 'class': 'x:Broken', 'params': {'mode': 'ok', 'solver': 'cholesky'}}
    folder = run(tmp_path, snap_dir, config, monkeypatch, cls=lambda mode, solver: Broken(mode))
    row = read_csv(folder / 'predictions.csv')[0]
    assert len(row['predicted_price_raw'].split('.')[1]) == 6


def test_guards(tmp_path, snap_dir):
    with pytest.raises(Exception, match='p1 단계'):
        run(tmp_path, snap_dir, NAIVE, phase='p1', origins='test', month=None)
    with pytest.raises(run_backtest.RunError, match='docker'):
        run(tmp_path, snap_dir, NAIVE, phase='test', month=None)
    with pytest.raises(run_backtest.RunError, match='model'):
        run(tmp_path, snap_dir, {**NAIVE, 'model': 'GPT'})


def test_record_trial_and_tuning_log(tmp_path, snap_dir):
    trials = tmp_path / 'runs' / 'tuning.csv'
    run(tmp_path, snap_dir, NAIVE, phase='p1', origins='tune', month='2025-01', record_trial=trials)
    run(tmp_path, snap_dir, NAIVE, phase='p1', origins='tune', month='2025-02', record_trial=trials)
    logged = read_csv(trials)
    assert [t['trial'] for t in logged] == ['1', '2']
    folder = run(tmp_path, snap_dir, NAIVE, phase='p1', month='2025-03', tuning_log=trials)
    config = json.loads((folder / 'config.json').read_text(encoding='utf-8'))
    assert config['tuning']['trials_used'] == 2
    assert len(read_csv(folder / 'tuning_log.csv')) == 2


# ---- 평가기 ---------------------------------------------------------------------------------

def test_compare_common_success_and_ranking(tmp_path, snap_dir, monkeypatch):
    naive = run(tmp_path, snap_dir, NAIVE)
    broken = run(tmp_path, snap_dir, {**NAIVE, 'model': 'Ridge', 'class': 'x:Broken',
                                      'params': {'mode': 'negative', 'solver': 'cholesky'}},
                 monkeypatch, cls=lambda mode, solver: Broken(mode))
    result = evaluate.compare([naive, broken], loader.Snapshot(snap_dir))
    a, b = (result['experiments'][f.name] for f in (naive, broken))
    assert a['common_success']['points'] == b['common_success']['points'] < a['policy']['points']
    assert set(result['ranking_policy_macro_mape']) == {naive.name, broken.name}


def test_bootstrap_is_reproducible(snap):
    rows = []
    for d in snap.origins['validation'][:40]:
        for h in standard.HORIZONS:
            rows.append({'series_id': '1', 'origin_date': d.isoformat(), 'horizon': str(h),
                         'target_date': (d + timedelta(days=h)).isoformat(), 'status': 'OK',
                         'predicted_price': str(int(snap.naive(1, d)) + 3)})
    points = evaluate.points_for(rows, snap)
    first = evaluate.bootstrap(points, lambda p: p['pred'])
    assert first == evaluate.bootstrap(points, lambda p: p['pred'])
    assert first['ci_low'] <= first['delta'] <= first['ci_high']


# ---- 2차 외부변수 묶음(§5.2) ----------------------------------------------------------------------

ALL_BUNDLES = list(standard.EXTRA_BUNDLES)


def test_bundle_names_are_ordered_and_validated():
    names = loader.feature_names(['MACRO', 'MARKET'])
    assert names[len(standard.BASE_FEATURES):] == [*standard.EXTRA_BUNDLES['MARKET'], *standard.EXTRA_BUNDLES['MACRO']]
    with pytest.raises(ValueError, match='모르는'):
        loader.check_bundles(['WEATHER'])  # 주산지 기상은 쓰지 않음


def _drop_from(folder, name, column, first_day):
    path = folder / name
    rows = read_csv(path)
    with open(path, 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0]), lineterminator='\n')
        writer.writeheader()
        writer.writerows(r for r in rows if r[column] < first_day.isoformat())


def test_bundles_use_only_data_up_to_d_minus_1(tmp_path, snap_dir):
    """d일과 그 뒤의 상대 시장·기상·환율을 지워도 기준일 d의 외부변수는 같아야 한다(§3.1)."""
    import shutil
    d = date(2016, 1, 29)  # 가짜 스냅샷의 기상·환율이 있는 기간
    cut = tmp_path / 'cut'
    shutil.copytree(snap_dir, cut)
    _drop_from(cut, 'weather_daily.csv', 'weather_date', d)
    _drop_from(cut, 'exchange_rate_daily.csv', 'rate_date', d)
    rows = read_csv(cut / 'price_daily.csv')
    with open(cut / 'price_daily.csv', 'w', encoding='utf-8', newline='') as f:  # 상대 계열(2)만 d부터 삭제
        writer = csv.DictWriter(f, fieldnames=list(rows[0]), lineterminator='\n')
        writer.writeheader()
        writer.writerows(r for r in rows if not (r['series_id'] == '2' and r['price_date'] >= d.isoformat()))
    full = loader.Snapshot(snap_dir).origin_inputs(1, d, ALL_BUNDLES).features
    part = loader.Snapshot(cut).origin_inputs(1, d, ALL_BUNDLES).features
    for h in standard.HORIZONS:
        a, b = full[h], part[h]
        assert ((a == b) | (np.isnan(a) & np.isnan(b))).all(), h


def test_market_and_event_values(snap):
    d = date(2025, 9, 26)
    names = loader.feature_names(ALL_BUNDLES)
    row = dict(zip(names, snap.origin_inputs(1, d, ALL_BUNDLES).features[1]))
    counter = snap.series[2].filled[snap.series[2].index(d - timedelta(days=1))]
    assert row['counter_price'] == counter
    assert row['target_counter_ratio'] == pytest.approx(snap.series[1].filled[snap.series[1].index(d)] / counter)
    # 가짜 명절: 2025-10-05~07, 영향 2025-09-25~10-07 → 목표일 9/27까지 8일, 영향 기간 안
    assert (row['days_to_major_holiday'], row['days_from_major_holiday'], row['target_in_event_window']) == (8, 45, 1)
    inside = dict(zip(names, snap.origin_inputs(1, date(2025, 10, 3), ALL_BUNDLES).features[3]))
    assert inside['days_to_major_holiday'] == inside['days_from_major_holiday'] == 0
    data = snap.training_data(1, date(2025, 3, 3), ['MARKET'])
    assert data.features.shape[1] == len(standard.BASE_FEATURES) + 4 and data.feature_names[-1] == 'counter_change28'


def test_p2_config_must_name_feature_set(tmp_path, snap_dir):
    config = {**NAIVE, 'extra_features': ['MARKET']}
    with pytest.raises(run_backtest.RunError, match='base_v1\\+MARKET'):
        run(tmp_path, snap_dir, config, phase='p2')
    folder = run(tmp_path, snap_dir, {**config, 'feature_set': 'base_v1+MARKET'}, phase='p2', series='1,2')
    assert validate(folder).errors == []
