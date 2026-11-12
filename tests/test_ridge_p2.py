"""Fast Ridge p2 tests; synthetic snapshots and isolated output only, no full Validation."""
import copy
from datetime import date, timedelta
import json
from pathlib import Path
from types import SimpleNamespace

import numpy as np
import pytest

from model_comparison.ridge.model import RidgeModel
from model_comparison.ridge.model_p2 import AUDIT_SINK, RidgeP2Model
from model_comparison.ridge import p2
from tests.test_snapshot_tools import fake_raw
from tools import evaluate, export_snapshot, loader, run_backtest, standard
from tools.runtime import OriginInputs, TrainingData
from tools.validate_experiment import Report, check_config


def history(X=None, y=None, names=None):
    X = np.array([[1., 2., np.nan], [3., np.nan, np.nan], [9., 8., np.nan]]) if X is None else np.asarray(X)
    return TrainingData(1, date(2025, 1, 6), features=X,
                        targets=np.array([100., 200., 300.]) if y is None else np.asarray(y),
                        feature_names=['current', 'counter_price', 'production_yoy'] if names is None else names)


def inputs(row, names=None):
    return OriginInputs(1, date(2025, 1, 7), features={h: list(row) for h in standard.HORIZONS},
                        feature_names=['current', 'counter_price', 'production_yoy'] if names is None else names)


def test_train_only_medians_and_prediction_reuse_without_mutation():
    h = history()
    original = h.features.copy()
    model = RidgeP2Model()
    model.fit(h, 42)
    np.testing.assert_array_equal(model.fill_values_, [3., 5., 0.])
    assert model.all_missing_.tolist() == [False, False, True]
    np.testing.assert_array_equal(h.features, original)
    scaler = model.model.named_steps['scaler']
    np.testing.assert_array_equal(scaler.mean_, [13 / 3, 5., 0.])
    mean_before, fills_before = scaler.mean_.copy(), model.fill_values_.copy()
    actual = model.predict(inputs([np.nan, np.nan, 1e12]))
    expected = model.predict(inputs([3., 5., np.nan]))
    np.testing.assert_array_equal(actual, expected)
    model.predict(inputs([999999., np.nan, -99999.]))
    np.testing.assert_array_equal(model.fill_values_, fills_before)
    np.testing.assert_array_equal(scaler.mean_, mean_before)
    assert len(actual) == 7 and np.isfinite(actual).all()


def test_all_missing_column_is_retained_frozen_and_relearned_on_refit():
    model = RidgeP2Model()
    model.fit(history(), 42)
    assert model.model.named_steps['ridge'].coef_.shape == (3,)
    assert model.model.named_steps['ridge'].coef_[2] == 0
    assert model.predict(inputs([3., 5., 0.])) == model.predict(inputs([3., 5., 9999.]))
    h = history()
    h.features[:, 2] = [1., 3., 8.]
    model.fit(h, 42)
    assert model.fill_values_[2] == 3 and not model.all_missing_[2]


@pytest.mark.parametrize('bad', [np.nan, np.inf, -np.inf, 0., -1.])
def test_invalid_targets_rejected_and_failed_refit_invalidates_model(bad):
    model = RidgeP2Model()
    model.fit(history(), 42)
    h = history()
    h.targets[1] = bad
    with pytest.raises(ValueError, match='Target prices'):
        model.fit(h, 42)
    with pytest.raises(RuntimeError, match='fitted'):
        model.predict(inputs([3., 5., 0.]))


@pytest.mark.parametrize('bad', [np.inf, -np.inf])
def test_infinite_features_rejected_in_train_and_predict(bad):
    model = RidgeP2Model()
    h = history()
    h.features[1, 1] = bad
    with pytest.raises(ValueError, match='infinity'):
        model.fit(h, 42)
    model.fit(history(), 42)
    with pytest.raises(ValueError, match='infinity'):
        model.predict(inputs([3., bad, 0.]))
    # Even an all-missing training column cannot silently accept infinity.
    with pytest.raises(ValueError, match='infinity'):
        model.predict(inputs([3., 5., bad]))


@pytest.mark.parametrize('names', [[], ['a', 'a', 'b'], ['a', '', 'b'], ['a', 1, 'b']])
def test_invalid_training_names(names):
    with pytest.raises(ValueError, match='names'):
        RidgeP2Model().fit(history(names=names), 42)


def test_feature_order_shape_horizons_and_fixed_parameters():
    model = RidgeP2Model()
    with pytest.raises(RuntimeError):
        model.predict(inputs([1, 2, 3]))
    model.fit(history(), 42)
    for names in [['counter_price', 'current', 'production_yoy'], ['current', 'other', 'production_yoy']]:
        with pytest.raises(ValueError, match='order'):
            model.predict(inputs([1, 2, 3], names))
    with pytest.raises(ValueError, match='shape'):
        model.predict(inputs([1, 2]))
    wrong = inputs([1, 2, 3])
    del wrong.features[7]
    with pytest.raises(ValueError, match='horizons'):
        model.predict(wrong)
    for kwargs in [{'alpha': 1}, {'alpha': float('nan')}, {'solver': 'auto'}]:
        with pytest.raises(ValueError):
            RidgeP2Model(**kwargs)
    with pytest.raises(ValueError, match='seed'):
        model.fit(history(), 43)
    with pytest.raises(ValueError, match='shape'):
        model.fit(history(X=np.empty((0, 3)), y=[]), 42)
    with pytest.raises(ValueError, match='shape'):
        model.fit(history(X=[[1, 2]], y=[100]), 42)


def test_finite_base_features_predict_exactly_like_p1():
    rng = np.random.default_rng(42)
    X = rng.normal(size=(120, len(standard.BASE_FEATURES)))
    y = 1000 + X[:, 0] * 10
    h = history(X, y, list(standard.BASE_FEATURES))
    inp = inputs(X[0], list(standard.BASE_FEATURES))
    old, new = RidgeModel(alpha=10, solver='lsqr'), RidgeP2Model()
    old.fit(h, 42)
    new.fit(h, 42)
    np.testing.assert_array_equal(old.predict(inp), new.predict(inp))
    np.testing.assert_array_equal(old.model.named_steps['scaler'].scale_, new.model.named_steps['scaler'].scale_)


def test_diagnostics_capture_scaling_coefficients_and_missingness():
    events = []
    token = AUDIT_SINK.set(events.append)
    try:
        model = RidgeP2Model()
        model.fit(history(), 42)
        model.predict(inputs([np.nan, 5., 123.]))
    finally:
        AUDIT_SINK.reset(token)
    fit, pred = events
    assert fit['feature_count'] == 3
    assert fit['features']['production_yoy']['all_missing'] is True
    assert fit['features']['counter_price']['missing_rate'] == 1 / 3
    assert 'coefficient_raw' in fit['features']['current']
    assert 'high_correlation_pairs' in fit
    assert pred['missing_counts']['current'] == 7
    assert pred['all_missing_training_columns_frozen_counts']['production_yoy'] == 7
    json.dumps(events, allow_nan=False)


@pytest.fixture(scope='module')
def synthetic_snapshot(tmp_path_factory):
    folder = tmp_path_factory.mktemp('ridge-p2-snapshot') / standard.DATA_VERSION
    export_snapshot.build(fake_raw(), folder, cutoff=standard.DATA_CUTOFF)
    return folder


@pytest.mark.parametrize('bundle', list(standard.EXTRA_BUNDLES))
def test_five_configs_match_loader_and_common_validator(bundle, synthetic_snapshot):
    config = p2.config_for([bundle])
    assert p2.read(p2.HERE / 'configs/p2' / (bundle.lower() + '.json')) == config
    assert config['params'] == {'alpha': 10, 'solver': 'lsqr'}
    report = Report('p2-config')
    folder = Path('ridge-p2-20261111-01')
    complete = {**config, 'experiment_id': folder.name, 'standard_version': standard.STANDARD_VERSION,
                'git_sha': 'test', 'data_version': standard.DATA_VERSION, 'phase': 'p2', 'origins': 'validation',
                'refit': standard.REFIT, 'runtime': {'threads': standard.THREADS}, 'tuning': {}}
    check_config(complete, folder, report)
    assert report.errors == []
    snap = loader.Snapshot(synthetic_snapshot)
    h, inp = snap.load_as_of(1, date(2025, 1, 6), config['extra_features'])
    assert h.feature_names == inp.feature_names == loader.feature_names([bundle])
    assert h.features.shape[1] == len(standard.BASE_FEATURES) + len(standard.EXTRA_BUNDLES[bundle])
    model = RidgeP2Model()
    model.fit(h, 42)
    assert np.isfinite(model.predict(inp)).all()


def test_base_control_allowed_as_p2():
    config = p2.config_for()
    assert config['extra_features'] == [] and config['feature_set'] == 'base_v1'
    assert config == p2.read(p2.HERE / 'configs/p2/control.json')
    assert loader.check_bundles(['PRODUCTION', 'MARKET']) == ('MARKET', 'PRODUCTION')
    assert p2.config_for(['PRODUCTION', 'MARKET'])['feature_set'] == 'base_v1+MARKET+PRODUCTION'


def test_real_p1_snapshot_single_origin_prediction_parity():
    # Read-only, two individual fits; this is not a backtest or a Validation run.
    snapshot = p2.ROOT / 'data/snapshots' / standard.DATA_VERSION
    if not snapshot.exists():
        pytest.skip('Official local snapshot unavailable')
    snap = loader.Snapshot(snapshot)
    for sid in (1, 9001):
        h, inp = snap.load_as_of(sid, date(2025, 1, 6))
        old, new = RidgeModel(alpha=10, solver='lsqr'), RidgeP2Model()
        old.fit(h, 42)
        new.fit(h, 42)
        np.testing.assert_array_equal(old.predict(inp), new.predict(inp))
        assert run_backtest.prediction_rows(old.predict(inp), 'OK', '') == run_backtest.prediction_rows(new.predict(inp), 'OK', '')


def test_loader_future_targets_do_not_enter_fit(synthetic_snapshot):
    snap = loader.Snapshot(synthetic_snapshot)
    d = date(2025, 1, 6)
    before = snap.training_data(1, d, list(standard.EXTRA_BUNDLES))
    assert all(o + timedelta(days=int(h)) <= d for o, h in zip(before.origins, before.horizons))
    s = snap.series[1]
    s.actual[s.index(d) + 1:] = 99999999.
    after = snap.training_data(1, d, list(standard.EXTRA_BUNDLES))
    np.testing.assert_array_equal(before.features, after.features)
    np.testing.assert_array_equal(before.targets, after.targets)
    a, b = RidgeP2Model(), RidgeP2Model()
    a.fit(before, 42)
    b.fit(after, 42)
    np.testing.assert_array_equal(a.fill_values_, b.fill_values_)


def test_production_respects_publication_and_event_is_known_calendar(synthetic_snapshot):
    snap = loader.Snapshot(synthetic_snapshot)
    extras = loader.ExtraFeatures(snap)
    extras.production['대파'] = {2022: (100., date(2023, 6, 30)),
                                2023: (200., date(2024, 6, 30)),
                                2024: (800., date(2025, 6, 30))}
    matrix = extras.origin_matrix(1, ['PRODUCTION'])
    s = snap.series[1]
    assert matrix[s.index(date(2025, 6, 29)), 0] == 1.
    assert matrix[s.index(date(2025, 6, 30)), 0] == 3.
    assert extras.event_row(date(2025, 10, 6)) == (0., 0., 1., 0.)


@pytest.fixture
def execution(tmp_path, synthetic_snapshot, monkeypatch):
    snap = loader.Snapshot(synthetic_snapshot)
    args = SimpleNamespace(records=tmp_path / 'audit', out=tmp_path / 'output', snapshot=synthetic_snapshot,
                           month='2025-01', series='1')
    args.records.mkdir()
    provenance = {'snapshot_id': standard.DATA_VERSION, 'git_sha': run_backtest.git('rev-parse', 'HEAD'),
                  'source_sha256': {'model': 'synthetic'}}
    monkeypatch.setattr(p2, 'lineage', lambda path: provenance)
    scope = p2.scope_for(snap, args.month, args.series)
    return snap, args, provenance, scope


def test_execution_seals_reuses_and_records_official_metrics(execution):
    snap, args, provenance, scope = execution
    config = p2.config_for(['PRODUCTION'])
    first = p2.run_one(config, provenance, scope, snap, args)
    assert first['state'] == 'COMPLETED', first
    second = p2.run_one(config, provenance, scope, snap, args)
    assert second['reused'] and first['folder'] == second['folder']
    attempt = Path(first['attempt'])
    result = p2.read(attempt / 'result.json')
    assert result['comparison_eligible'] is False and result['delta_vs_p1_pp'] is None
    assert result['decision'] == 'PENDING_REVIEW'
    assert result['macro_mape'] == first['metrics']['results']['policy']['macro_mape']
    assert result['adoption'] == first['metrics']['adoption']
    assert set(result['by_item']) == {'대파'} and set(result['by_market']) == {'RETAIL'}
    assert result['validation']['errors'] == []
    start = p2.read(attempt / 'start.json')
    assert start['feature_names'] == loader.feature_names(['PRODUCTION'])
    assert start['requested_config_file_sha256'] == p2.digest(attempt / 'requested_config.json')
    assert 'python' in (Path(first['folder']) / 'environment.txt').read_text(encoding='utf-8')
    assert (attempt / 'diagnostics.jsonl').exists()
    assert len(list(args.out.iterdir())) == 1


def test_corrupted_result_is_not_reused_and_old_artifacts_retained(execution):
    snap, args, provenance, scope = execution
    config = p2.config_for(['EVENT'])
    first = p2.run_one(config, provenance, scope, snap, args)
    path = Path(first['folder']) / 'metrics.json'
    path.write_text('{}\n', encoding='utf-8')
    second = p2.run_one(config, provenance, scope, snap, args)
    assert second['state'] == 'COMPLETED' and not second['reused']
    assert first['folder'] != second['folder'] and path.read_text(encoding='utf-8') == '{}\n'
    assert 'REUSE_REJECTED' in (args.records / 'events.jsonl').read_text(encoding='utf-8')


def test_changed_data_source_or_scope_invalidates_identity(execution):
    snap, args, provenance, scope = execution
    config = p2.config_for(['EVENT'])
    p2.run_one(config, provenance, scope, snap, args)
    changed = copy.deepcopy(provenance)
    changed['source_sha256']['model'] = 'changed'
    assert p2.find_completed(args.records, p2.identity(config, changed, scope), snap) is None
    different = {**scope, 'month': '2025-02'}
    assert p2.find_completed(args.records, p2.identity(config, provenance, different), snap) is None
    assert p2.find_completed(args.records, p2.identity(p2.config_for(['MARKET']), provenance, scope), snap) is None


def test_incomplete_and_failed_runs_are_retained_and_resumed(execution, monkeypatch):
    snap, args, provenance, scope = execution
    config = p2.config_for(['EVENT'])
    original_main = run_backtest.main
    monkeypatch.setattr(run_backtest, 'main', lambda argv: 1)
    failed = p2.run_one(config, provenance, scope, snap, args)
    assert failed['state'] == 'FAILED'
    assert (Path(failed['attempt']) / 'failure.json').exists()
    assert not (Path(failed['attempt']) / 'completion.json').exists()
    incomplete = args.records / 'attempts' / 'abandoned'
    incomplete.mkdir()
    p2.exclusive_json(incomplete / 'start.json', {'identity': p2.identity(config, provenance, scope)})
    monkeypatch.setattr(run_backtest, 'main', original_main)
    resumed = p2.run_one(config, provenance, scope, snap, args)
    assert resumed['state'] == 'COMPLETED' and not resumed['reused']
    assert p2.read(incomplete / 'interrupted.json')['state'] == 'INTERRUPTED'
    assert (Path(failed['attempt']) / 'failure.json').exists()


def test_model_fit_failures_are_not_sealed_as_completed(execution, monkeypatch):
    snap, args, provenance, scope = execution
    class Broken:
        def __init__(self, **kwargs):
            pass
        def fit(self, h, seed):
            raise ValueError('synthetic malformed data')
    monkeypatch.setattr(run_backtest, 'load_class', lambda spec: Broken)
    result = p2.run_one(p2.config_for(['EVENT']), provenance, scope, snap, args)
    assert result['state'] == 'FAILED'
    assert Path(result['folder'], 'metrics.json').exists()  # Failed outputs are still preserved.
    assert not Path(result['attempt'], 'completion.json').exists()


def test_interrupt_is_recorded_and_audit_sink_is_reset(execution, monkeypatch):
    snap, args, provenance, scope = execution
    def interrupt(argv):
        raise KeyboardInterrupt()
    monkeypatch.setattr(run_backtest, 'main', interrupt)
    with pytest.raises(KeyboardInterrupt):
        p2.run_one(p2.config_for(), provenance, scope, snap, args)
    attempts = list((args.records / 'attempts').iterdir())
    assert p2.read(attempts[0] / 'interrupted.json')['state'] == 'INTERRUPTED'
    assert AUDIT_SINK.get() is None


def test_common_recomputation_rejects_incomplete_grid_and_false_metrics(execution):
    snap, args, provenance, scope = execution
    config = p2.config_for(['EVENT'])
    done = p2.run_one(config, provenance, scope, snap, args)
    folder = Path(done['folder'])
    expected = p2.identity(config, provenance, scope)
    metrics_path = folder / 'metrics.json'
    metrics = p2.read(metrics_path)
    altered = copy.deepcopy(metrics)
    altered['success_rate'] = .123
    metrics_path.write_text(json.dumps(altered), encoding='utf-8')
    with pytest.raises(ValueError, match='recomputation'):
        p2.verify_result(folder, expected, snap)
    metrics_path.write_text(json.dumps(metrics), encoding='utf-8')
    predictions = folder / 'predictions.csv'
    lines = predictions.read_text(encoding='utf-8').splitlines(keepends=True)
    # Remove one complete origin (seven horizons): common format checks alone allow it.
    predictions.write_text(''.join(lines[:1] + lines[8:]), encoding='utf-8')
    with pytest.raises(ValueError, match='grid'):
        p2.verify_result(folder, expected, snap)


def test_summary_formulas_and_combination_selection():
    _, baseline = p2.p1_result()
    metrics = copy.deepcopy(baseline)
    snap = SimpleNamespace(series={int(s): SimpleNamespace(item='item'+str(int(s)//2), market='RETAIL')
                                   for s in baseline['results']['policy']['series']})
    metrics['results']['policy']['macro_mape'] = 4.
    metrics['results']['policy']['series']['1']['mape'] -= 1
    result = p2.summary_result(metrics, baseline, snap)
    assert result['delta_vs_p1_pp'] == round(4 - 5.060471, 6)
    assert result['series_improved_vs_p1'] == 1 and result['series_worsened_vs_p1'] == 0
    singles = {b: {'metrics': copy.deepcopy(metrics)} for b in standard.EXTRA_BUNDLES}
    assert p2.combination_candidates(singles, 5.060471) == list(standard.EXTRA_BUNDLES)
    for value in singles.values():
        value['metrics']['results']['policy']['macro_mape'] = 6.
    assert p2.combination_candidates(singles, 5.060471) == []
    singles['MARKET']['metrics']['results']['policy']['macro_mape'] = 4.
    assert p2.combination_candidates(singles, 5.060471) == []
    singles['MARKET'] = None
    with pytest.raises(ValueError, match='all five'):
        p2.combination_candidates(singles, 5.060471)


def test_default_cli_never_calls_training(monkeypatch, capsys):
    def forbidden(*a, **k):
        pytest.fail('Default planning must not train')
    monkeypatch.setattr(p2, 'run_one', forbidden)
    monkeypatch.setattr(p2, 'lineage', forbidden)
    assert p2.main([]) == 0
    assert json.loads(capsys.readouterr().out)['state'] == 'PLANNED'
    with pytest.raises(SystemExit):
        p2.main(['--execute'])
    with pytest.raises(SystemExit):
        p2.main(['--combine', '--month', '2025-01'])


def test_p1_original_files_unchanged():
    before = p2.read(p2.RECORDS / 'preservation_before.json')
    protected = ('model_comparison/ridge/model.py', 'model_comparison/ridge/config_alpha_10.json',
                 'model_comparison/ridge/experiments/v1/', 'experiments/' + p2.P1_ID + '/')
    files = {n: sha for n, sha in before['files'].items() if any(n.startswith(p) for p in protected)}
    assert files
    for name, sha in files.items():
        assert p2.digest(p2.ROOT / name) == sha, name


def test_exclusive_output_and_os_lock(tmp_path):
    path = tmp_path / 'existing.json'
    p2.exclusive_json(path, {'original': True})
    with pytest.raises(FileExistsError):
        p2.exclusive_json(path, {'original': False})
    assert p2.read(path) == {'original': True}
    with p2.execution_lock(tmp_path / 'records'):
        with pytest.raises(RuntimeError, match='Another'):
            with p2.execution_lock(tmp_path / 'records'):
                pass
    with p2.execution_lock(tmp_path / 'records'):
        pass


def test_all_orchestration_and_combination_delta_without_training(synthetic_snapshot, tmp_path, monkeypatch):
    snap = loader.Snapshot(synthetic_snapshot)
    p1_config, baseline = p2.p1_result()
    p1_config = {**p1_config, 'series': snap.series_ids}
    monkeypatch.setattr(p2, 'p1_result', lambda: (p1_config, baseline))
    monkeypatch.setattr(p2, 'lineage', lambda path: {})
    calls = []
    def fake_run(config, provenance, scope, snapshot, args):
        calls.append(config['extra_features'])
        return {'state': 'COMPLETED', 'folder': 'combination', 'metrics': {'results': {'policy': {'macro_mape': 3.5}}}}
    def fake_completed(records, expected, snapshot):
        bundle = expected['config']['extra_features'][0]
        mape = 4. if bundle in ('MARKET', 'EVENT') else 6.
        return {'state': 'COMPLETED', 'folder': bundle, 'metrics': {'results': {'policy': {'macro_mape': mape}}}}
    monkeypatch.setattr(p2, 'run_one', fake_run)
    monkeypatch.setattr(p2, 'find_completed', fake_completed)
    monkeypatch.setattr(run_backtest, 'main', lambda *a: pytest.fail('No training in orchestration unit test'))
    records = tmp_path / 'records'
    assert p2.main(['--execute', '--all', '--snapshot', str(synthetic_snapshot),
                    '--records', str(records), '--out', str(tmp_path / 'output')]) == 0
    assert calls == [[b] for b in standard.EXTRA_BUNDLES] + [['MARKET', 'EVENT']]
    comparison = p2.read(next(records.glob('combination-*.json')))
    assert comparison['delta_combination_minus_single_pp'] == {'MARKET': -.5, 'EVENT': -.5}


def test_seal_requires_every_common_and_audit_artifact(execution):
    snap, args, provenance, scope = execution
    config = p2.config_for(['EVENT'])
    done = p2.run_one(config, provenance, scope, snap, args)
    attempt = Path(done['attempt'])
    completion = p2.read(attempt / 'completion.json')
    completion['artifacts_sha256'].pop('metrics.json')
    (attempt / 'completion.json').write_text(json.dumps(completion), encoding='utf-8')
    with pytest.raises(ValueError, match='required artifacts'):
        p2.completed_attempt(attempt, p2.identity(config, provenance, scope), snap)


def test_git_diff_decodes_korean_as_utf8(monkeypatch):
    monkeypatch.setattr(p2.subprocess, 'run', lambda *a, **k: SimpleNamespace(stdout='한글 변경\n'.encode('utf-8')))
    assert p2.git('diff') == '한글 변경'
