import csv
import json
import os
from datetime import date, timedelta

import pytest

from tools import origins, runtime, standard
from tools import validate_experiment
from tools.validate_experiment import round_half_up, validate


def calendar(start, end):
    day, rows = start, []
    while day <= end:
        rows.append((day, day.weekday() >= 5))
        day += timedelta(days=1)
    return rows


def make_experiment(tmp_path, *, experiment_id='xgb-p1-20261116-01', origin_days=None, **overrides):
    folder = tmp_path / experiment_id
    folder.mkdir()
    phase = experiment_id.split('-')[-3]
    config = {'experiment_id': experiment_id, 'model': 'XGBoost', 'owner': 'A', 'standard_version': 'v1',
              'git_sha': 'abc', 'data_version': standard.DATA_VERSION, 'phase': phase,
              'origins': standard.ORIGIN_SETS[phase], 'feature_set': 'base_v1', 'extra_features': [],
              'target_transform': 'ratio', 'strategy': 'direct_per_horizon', 'refit': standard.REFIT,
              'params': {'tree_method': 'hist', 'n_jobs': 4, 'random_state': 42}, 'seed': 42,
              'runtime': {'where': 'docker' if phase == 'test' else 'local', 'threads': 4},
              'tuning': {'trials_used': 3, 'seconds_used': 100}}
    config.update(overrides)
    (folder / 'config.json').write_text(json.dumps(config), encoding='utf-8')
    origin_days = origin_days or [date(2024, 11, 4), date(2024, 11, 5)]
    with (folder / 'predictions.csv').open('w', encoding='utf-8', newline='') as handle:
        writer = csv.writer(handle)
        writer.writerow(standard.PREDICTION_COLUMNS)
        for series in range(1, 11):
            for origin in origin_days:
                for h in standard.HORIZONS:
                    raw = 1000.5 + h
                    writer.writerow([experiment_id, 'XGBoost', 'cfg1', standard.DATA_VERSION, series, series, 'RETAIL',
                                     origin, origin + timedelta(days=h), h, raw, round_half_up(raw), 'OK', ''])
    (folder / 'metrics.json').write_text('{}', encoding='utf-8')
    (folder / 'environment.txt').write_text('git abc', encoding='utf-8')
    (folder / 'run.log').write_text('', encoding='utf-8')
    with (folder / 'tuning_log.csv').open('w', encoding='utf-8', newline='') as handle:
        csv.writer(handle).writerow(standard.TUNING_COLUMNS)
    return folder


def test_valid_experiment_passes(tmp_path):
    report = validate(make_experiment(tmp_path))
    assert report.errors == []


def test_test_origins_are_rejected_outside_test_phase(tmp_path):
    report = validate(make_experiment(tmp_path, origin_days=[date(2025, 11, 10)]))
    assert any('허용되지 않은 기준일' in e for e in report.errors)


def test_test_phase_requires_docker_and_no_tuning(tmp_path):
    folder = make_experiment(tmp_path, experiment_id='xgb-test-20261201-01', origin_days=[date(2025, 11, 10)],
                             runtime={'where': 'local', 'threads': 4})
    with (folder / 'tuning_log.csv').open('a', encoding='utf-8', newline='') as handle:
        csv.writer(handle).writerow([1, 'cfg', '{}', 5.0, 10, 'OK'])
    errors = validate(folder).errors
    assert any('Docker' in e for e in errors) and any('튜닝할 수 없음' in e for e in errors)


@pytest.mark.parametrize('override, fragment', [
    ({'runtime': {'where': 'local', 'threads': 8}}, 'runtime.threads'),
    ({'refit': 'daily'}, 'refit'),
    ({'standard_version': 'v0'}, 'standard_version'),
    ({'params': {'tree_method': 'exact', 'n_jobs': 4}}, 'tree_method'),
    ({'tuning': {'trials_used': 41, 'seconds_used': 1}}, '상한'),
    ({'model': 'LightGBM'}, 'model은'),
])
def test_rule_violations_fail(tmp_path, override, fragment):
    assert any(fragment in e for e in validate(make_experiment(tmp_path, **override)).errors)


def test_rounding_and_missing_rows_fail(tmp_path):
    folder = make_experiment(tmp_path)
    path = folder / 'predictions.csv'
    lines = path.read_text(encoding='utf-8').splitlines()
    header, first = lines[0], lines[1].split(',')
    first[11] = str(int(first[11]) + 1)  # 반올림 규칙 위반
    path.write_text('\n'.join([header, ','.join(first)] + lines[3:]) + '\n', encoding='utf-8')  # 한 행 누락
    errors = validate(folder).errors
    assert any('round' in e for e in errors) or any('7행' in e for e in errors)


def test_origin_lists_and_guard():
    lists = origins.build(calendar(date(2024, 10, 1), date(2026, 11, 30)))
    assert lists['validation'][0] == date(2024, 11, 1) and lists['validation'][-1] == date(2025, 10, 31)
    assert all(d.weekday() < 5 for d in lists['validation'])
    assert len(lists['tune']) in (52, 53) and lists['tune'][0] == date(2024, 11, 1)
    assert lists['test'][0] == date(2025, 11, 10) and lists['test'][-1] == date(2026, 10, 23)
    origins.guard('p1', lists['tune'])
    with pytest.raises(origins.ForbiddenOriginError):
        origins.guard('p1', [date(2025, 11, 10)])
    with pytest.raises(origins.ForbiddenOriginError):
        origins.guard('focus', [date(2025, 11, 3)])  # 간격 구간
    with pytest.raises(origins.ForbiddenOriginError):
        origins.guard('test', [date(2025, 1, 6)])


def test_constants_and_environment(monkeypatch):
    assert standard.majority(10) == 6 and standard.majority(8) == 5 and standard.majority(6) == 4
    assert round_half_up(1000.5) == 1001 and round_half_up(0.2) == 1
    monkeypatch.setenv('OMP_NUM_THREADS', '16')
    changed = runtime.apply_environment()
    assert os.environ['OMP_NUM_THREADS'] == '4' and 'OMP_NUM_THREADS' in changed


def test_committed_standard_matches_constants():
    report = validate_experiment.check_standard_file()
    assert not report.errors and not report.warnings, report.errors + report.warnings
