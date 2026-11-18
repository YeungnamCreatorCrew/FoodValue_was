"""Review regressions: synthetic inputs and temporary audit registries only."""
import json
from collections import Counter
from pathlib import Path
import subprocess
import sys

import numpy as np
import pytest

from model_comparison.ridge.v2 import audit as A, comparison as C, run as R
from model_comparison.ridge.v2.model import PooledRidgeV2
from model_comparison.ridge.v2.tests.test_integration import synthetic, setup_run
from model_comparison.ridge.v2.tests.test_model import data
from model_comparison.ridge.v2.tests.test_audit_comparison import fixture_result
from tools import evaluate, standard


@pytest.mark.parametrize('mode,category,status,terminal', [
    ('no_training', 'expected_missing', 'FIT_FAILED', 'COMPLETED_WITH_MISSING'),
    ('empty_training', 'expected_missing', 'FIT_FAILED', 'COMPLETED_WITH_MISSING'),
    ('missing_horizon', 'expected_missing', 'FIT_FAILED', 'COMPLETED_WITH_MISSING'),
    ('no_input', 'expected_missing', 'NO_INPUT', 'COMPLETED_WITH_MISSING'),
    ('fit_error', 'fit_failure', 'FIT_FAILED', 'FAILED'),
    ('predict_error', 'predict_failure', 'PREDICT_FAILED', 'FAILED'),
    ('nan_prediction', 'abnormal_prediction', 'PREDICT_FAILED', 'FAILED'),
    ('negative_prediction', 'abnormal_prediction', 'INVALID_VALUE', 'FAILED'),
    ('fit_timeout', 'timeout', 'FIT_FAILED', 'FAILED'),
    ('predict_timeout', 'timeout', 'TIMEOUT', 'FAILED'),
    ('ok', 'success', 'OK', 'COMPLETED'),
])
def test_health_separates_expected_missing_errors_and_original_statuses(
        tmp_path, synthetic, monkeypatch, mode, category, status, terminal):
    config, args, snap, days, attempt = setup_run(tmp_path, synthetic)
    x, y, h, names = data()

    class Matrices:
        def __init__(self, *args):
            self.names = names

        def training(self, *args):
            if mode == 'no_training':
                return None
            if mode == 'empty_training':
                return x[:0], y[:0], h[:0]
            if mode == 'missing_horizon':
                return x[h != 7], y[h != 7], h[h != 7]
            return x, y, h

        def inputs(self, *args):
            if mode == 'no_input':
                return None
            return np.stack([x[np.where(h == g)[0][0]] for g in standard.HORIZONS])

    class Model(PooledRidgeV2):
        def fit(self, *args):
            if mode == 'fit_error':
                raise RuntimeError('synthetic fit failure')
            return super().fit(*args)

        def predict(self, *args):
            if mode == 'predict_error':
                raise RuntimeError('synthetic predict failure')
            if mode == 'nan_prediction':
                return np.full(7, np.nan)
            if mode == 'negative_prediction':
                return np.full(7, -1.)
            return super().predict(*args)

    monkeypatch.setattr('tools.run_backtest.load_class', lambda _: Model)
    if mode in ('fit_timeout', 'predict_timeout'):
        limits = dict(standard.TIMEOUT_SECONDS)
        limits['refit' if mode == 'fit_timeout' else 'predict'] = -1
        monkeypatch.setattr(standard, 'TIMEOUT_SECONDS', limits)
    result = R.train(config, snap, days[:1], [1], args, attempt, matrix_factory=Matrices)
    assert result == terminal
    rows = evaluate.read_predictions(attempt.folder)
    assert len(rows) == 7 and {r['status'] for r in rows} == {status}
    health = A.read(attempt.folder/'prediction_health.json')
    assert health['categories'][category] == 7
    assert health['prediction_rows'] == 7
    assert health['missing_rate'] == (1. if category == 'expected_missing' else 0.)
    assert health['prediction_success_rate'] == (1. if category == 'success' else 0.)
    assert health['error_row_count'] == (0 if category in ('expected_missing', 'success') else 7)
    assert health['has_model_errors'] == (terminal == 'FAILED')
    assert health['error_event_count'] == (1 if mode in (
        'fit_error', 'predict_error', 'fit_timeout', 'predict_timeout') else 0)
    assert R.exit_code(result) == (1 if terminal == 'FAILED' else 0)
    assert A.read(attempt.folder/'metrics_full_precision.json')['policy']


def test_mixed_health_and_exit_codes():
    h = R.health_summary(Counter(success=5, expected_missing=3, predict_failure=2),
                         Counter(predict_failure=1))
    assert h['prediction_success_rate'] == .5 and h['missing_rate'] == .3
    assert h['error_row_count'] == 2 and h['has_model_errors']
    assert R.health_summary(Counter(), Counter())['missing_rate'] is None
    for status in ('FAILED', 'FAILED_PREFLIGHT', 'PARTIAL', 'INTERRUPTED', 'ABANDONED', 'INCOMPLETE'):
        assert R.exit_code(status) == 1
    for status in ('COMPLETED_WITH_MISSING', 'COMPLETED', 'PLANNED', 'HELP', 'REPORTED'):
        assert R.exit_code(status) == 0


@pytest.mark.parametrize('midway', [False, True])
def test_failed_refit_clears_previous_diagnostics_and_coefficients(monkeypatch, midway):
    model = PooledRidgeV2().fit(*data())
    assert model.diagnostics_ and model.importance()
    if midway:
        from sklearn.linear_model import Ridge
        old = Ridge.fit
        calls = 0

        def fail(self, *args, **kwargs):
            nonlocal calls
            calls += 1
            if calls == 3:
                raise MemoryError('synthetic refit OOM')
            return old(self, *args, **kwargs)

        monkeypatch.setattr(Ridge, 'fit', fail)
        with pytest.raises(MemoryError):
            model.fit(*data())
    else:
        x, y, h, names = data()
        y[0] = np.nan
        with pytest.raises(ValueError):
            model.fit(x, y, h, names)
    assert model.diagnostics_ == [] and model.models == {} and model.importance() == {}
    assert model.names == [] and model.keep == [] and not model.fitted_


def test_finish_seal_failure_recovery_effective_status_and_idempotence(tmp_path, monkeypatch):
    root = tmp_path/'runs'
    attempt = A.Attempt(root)
    original_write = A.exclusive_json

    def fail(path, value):
        if Path(path).name == 'artifacts_sha256.json':
            raise OSError('synthetic disk failure')
        return original_write(path, value)

    with monkeypatch.context() as m:
        m.setattr(A, 'exclusive_json', fail)
        with pytest.raises(OSError):
            attempt.finish('COMPLETED')
    original_outcome = (attempt.folder/'outcome.json').read_bytes()
    assert A.effective_outcome(attempt.folder)['status'] == 'INCOMPLETE'
    with pytest.raises(ValueError, match='Incomplete'):
        C.load_result(attempt.folder)
    A.recover_incomplete(root)
    assert (attempt.folder/'outcome.json').read_bytes() == original_outcome
    effective = A.effective_outcome(attempt.folder)
    assert effective['status'] == 'ABANDONED'
    assert effective['recorded_outcome']['status'] == 'COMPLETED'
    assert effective['recovery']['recorded_status'] == 'COMPLETED'
    before = {p.name: p.read_bytes() for p in attempt.folder.iterdir()}
    A.recover_incomplete(root)
    with pytest.raises(FileExistsError):
        attempt.finish('COMPLETED')
    assert {p.name: p.read_bytes() for p in attempt.folder.iterdir()} == before
    with pytest.raises(ValueError, match='Incomplete'):
        C.load_result(attempt.folder)
    assert A.verify_seal(attempt.folder)


def test_recovery_resumes_after_recovery_record_before_seal(tmp_path, monkeypatch):
    attempt = A.Attempt(tmp_path/'runs')
    old = A.exclusive_json

    def fail(path, value):
        if Path(path).name == 'artifacts_sha256.json':
            raise OSError('second interruption')
        return old(path, value)

    with monkeypatch.context() as m:
        m.setattr(A, 'exclusive_json', fail)
        with pytest.raises(OSError):
            A.recover_incomplete(tmp_path/'runs')
    A.recover_incomplete(tmp_path/'runs')
    assert A.effective_outcome(attempt.folder)['status'] == 'ABANDONED'
    assert A.verify_seal(attempt.folder)


def test_main_sealing_failure_is_code_two_and_preserves_terminal_record(tmp_path, monkeypatch):
    monkeypatch.setattr(A.Attempt, 'capture', lambda self: None)
    old = A.exclusive_json

    def fail(path, value):
        if Path(path).name == 'artifacts_sha256.json':
            raise OSError('synthetic seal failure')
        return old(path, value)

    monkeypatch.setattr(A, 'exclusive_json', fail)
    assert R.main(['--help'], root=tmp_path/'runs') == 2
    folder = next((tmp_path/'runs').glob('ridge-v2-*'))
    assert A.read(folder/'outcome.json')['status'] == 'HELP'
    assert A.effective_outcome(folder)['status'] == 'INCOMPLETE'
    assert [json.loads(line)['event'] for line in (folder/'events.jsonl').read_text().splitlines()].count('HELP') == 1


def test_forced_id_collision_does_not_overwrite(tmp_path, monkeypatch):
    from datetime import datetime, timezone
    fixed = datetime(2026, 11, 17, tzinfo=timezone.utc)

    class Clock:
        @staticmethod
        def now(*args):
            return fixed

    monkeypatch.setattr(A, 'datetime', Clock)
    monkeypatch.setattr(A, 'uuid4', lambda: type('ID', (), {'hex': 'fixed'})())
    first = A.Attempt(tmp_path)
    before = {p.name: p.read_bytes() for p in first.folder.iterdir()}
    with pytest.raises(FileExistsError):
        A.Attempt(tmp_path)
    assert {p.name: p.read_bytes() for p in first.folder.iterdir()} == before


def test_windows_process_lock_contention_and_release_after_kill(tmp_path):
    if sys.platform != 'win32':
        pytest.skip('Native Windows locking regression')
    code = ('from pathlib import Path; import sys; '
            'from model_comparison.ridge.v2.audit import lock; '
            'scope=lock(Path(sys.argv[1])); scope.__enter__(); '
            'print("LOCKED",flush=True); sys.stdin.read()')
    child = subprocess.Popen([sys.executable, '-B', '-c', code, str(tmp_path)],
                             stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                             text=True, encoding='utf-8', cwd=A.ROOT)
    try:
        assert child.stdout.readline().strip() == 'LOCKED'
        with pytest.raises(RuntimeError, match='holds the audit lock'):
            with A.lock(tmp_path):
                pytest.fail('Second writer acquired the lock')
    finally:
        child.kill()
        child.communicate(timeout=10)
    with A.lock(tmp_path):
        pass


def test_reference_numbers_are_descriptive_in_json_and_report():
    base, new = fixture_result(10), fixture_result(5)
    new['conditions']['v2_sha'] = 'different'
    c = C.compare(base, new)
    assert c['policy']['overall']['mape']['relative_improvement_pct'] == 50
    assert c['effect_attribution'] == 'not_established'
    report = C.markdown(new, {'CONTROL': c})
    assert '50 (reference; descriptive only; improvement effect NOT established)' in report
    assert 'direct improvement effect is NOT established' in report
    assert 'policy includes Naive fallback' in report
    assert c['series_counts']['unavailable'] == 10


def test_actual_grid_mismatch_cannot_be_direct_even_with_equal_provenance():
    base, new = fixture_result(10), fixture_result(5)
    new['grid'] = set(list(new['grid'])[1:])
    assert 'different:actual_grid' in C.compare(base, new)['comparability']['reasons']


@pytest.mark.parametrize('value', [None, float('nan'), float('inf'), -float('inf')])
def test_missing_or_nonfinite_comparison_is_unavailable(value):
    for base, new in ((value, 5.), (5., value)):
        c = C.change(base, new, 'mape')
        assert c['absolute_difference'] is None and c['relative_improvement_pct'] is None
        assert c['direction'] == 'unavailable'


def test_model_only_vs_policy_and_common_success_metrics_all_ten_series():
    base, new = fixture_result(10), fixture_result(5)
    new['points'][0]['ok'] = False
    for result in (base, new):
        result['policy'] = C.statistics(result['points'], 'policy', range(1, 11))
        result['model_only'] = C.statistics(result['points'], 'model_only', range(1, 11))
    c = C.compare(base, new)
    assert len(c['model_only']['series']) == 10
    assert c['policy']['series']['1']['mape']['new'] == 20
    assert c['model_only']['series']['1']['mape']['new'] is None
    assert c['paired_analysis']['common_success']['new']['overall']['error_points'] == 9
    assert c['policy']['overall']['mape']['absolute_difference'] == -3.5
    assert c['policy']['overall']['mape']['unit'] == '%p'
    assert c['policy']['overall']['mape']['relative_improvement_pct'] == 35
    for m in C.ERRORS:
        assert c['paired_analysis']['common_success']['changes']['overall'][m]['relative_improvement_pct'] == 50
    assert C.naive_comparison(new)['model_only'] is None


def test_zero_baseline_and_zero_naive_error():
    assert C.change(0., 0., 'mape')['relative_improvement_pct'] is None
    assert C.change(0., 1., 'mape')['direction'] == 'worsened'
    result = fixture_result(0.)
    for p in result['points']:
        p['naive'] = p['y']
    metrics = C.statistics(result['points'], 'policy', range(1, 11))
    assert metrics['overall']['rmae'] is None
    assert metrics['overall']['metric_series_counts']['rmae'] == 0
