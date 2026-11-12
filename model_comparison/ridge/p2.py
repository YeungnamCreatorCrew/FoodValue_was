"""Audited Ridge p2 orchestration. Default is a read-only plan; --execute trains.

No tuning and no Test entry point. See experiments/p2/README.md for protocol.
"""
from tools.runtime import apply_environment

apply_environment()

import argparse
from collections import Counter
from contextlib import contextmanager
from datetime import datetime, timezone
import hashlib
from importlib import metadata
import json
from pathlib import Path
import platform
import os
import subprocess
import sys
import time
import traceback
import tomllib
from uuid import uuid4

from tools import check_snapshot, evaluate, loader, run_backtest, standard
from tools.validate_experiment import validate
from model_comparison.ridge.model_p2 import AUDIT_SINK, PREPROCESSING_VERSION

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
RECORDS = HERE / 'experiments' / 'p2'
P1_ID = 'ridge-p1-20261111-07'
VERSION = 'ridge-p2-v1'
CLASS = 'model_comparison.ridge.model_p2:RidgeP2Model'
SOURCE_PATHS = [
    'model_comparison/ridge/model.py', 'model_comparison/ridge/model_p2.py',
    'model_comparison/ridge/config_alpha_10.json', 'model_comparison/ridge/p2.py',
    'model_comparison/MODEL_TRAINING_STANDARD.md', 'model_comparison/MODEL_TRAINING_TEAM_CONVENTIONS.md',
    'pyproject.toml', 'uv.lock',
    *[f'tools/{name}.py' for name in ('standard', 'runtime', 'loader', 'run_backtest',
                                    'evaluate', 'validate_experiment', 'origins', 'snapshot', 'check_snapshot')],
]


def now():
    return datetime.now(timezone.utc).isoformat()


def git(*args):
    # Git output (including Korean diffs) is UTF-8 even on a CP949 Windows host.
    result = subprocess.run(['git', *args], cwd=ROOT, capture_output=True, check=True)
    return result.stdout.decode('utf-8').strip()


def read(path):
    return json.loads(Path(path).read_text(encoding='utf-8'))


def digest(path):
    with Path(path).open('rb') as handle:
        return hashlib.file_digest(handle, 'sha256').hexdigest()


def canonical(value):
    return json.dumps(value, ensure_ascii=False, sort_keys=True, allow_nan=False, separators=(',', ':'))


def object_hash(value):
    return hashlib.sha256(canonical(value).encode('utf-8')).hexdigest()


def exclusive_json(path, value):
    with Path(path).open('x', encoding='utf-8', newline='\n') as handle:
        handle.write(json.dumps(value, ensure_ascii=False, sort_keys=True, indent=2, allow_nan=False) + '\n')


def append_event(path, value):
    with Path(path).open('a', encoding='utf-8', newline='\n') as handle:
        handle.write(canonical({'at': now(), **value}) + '\n')
        handle.flush()


@contextmanager
def execution_lock(records):
    """OS lock auto-releases on process death; the audit lock file is retained."""
    records.mkdir(parents=True, exist_ok=True)
    with (records / 'execution.lock').open('a+b') as handle:
        handle.seek(0, 2)
        if not handle.tell():
            handle.write(b'0')
            handle.flush()
        handle.seek(0)
        try:
            if sys.platform == 'win32':
                import msvcrt
                msvcrt.locking(handle.fileno(), msvcrt.LK_NBLCK, 1)
            else:
                import fcntl
                fcntl.flock(handle, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except OSError as error:
            raise RuntimeError('Another Ridge p2 runner holds this record directory') from error
        try:
            yield
        finally:
            handle.seek(0)
            if sys.platform == 'win32':
                msvcrt.locking(handle.fileno(), msvcrt.LK_UNLCK, 1)
            else:
                fcntl.flock(handle, fcntl.LOCK_UN)


def config_for(bundles=()):
    base = read(HERE / 'config_alpha_10.json')
    ordered = list(loader.check_bundles(bundles))
    return {**base, 'class': CLASS, 'extra_features': ordered,
            'feature_set': '+'.join([standard.BASE_FEATURE_SET, *ordered])}


def p1_result(folder=None):
    folder = Path(folder or ROOT / 'experiments' / P1_ID)
    reference = read(RECORDS / 'p1_reference.json')
    if folder.name != P1_ID:
        raise ValueError('Only the pinned official p1 result is a baseline')
    for name, expected in reference['artifacts_sha256'].items():
        if digest(folder / name) != expected:
            raise ValueError(f'Official p1 artifact changed: {name}')
    report = validate(folder)
    if report.errors:
        raise ValueError(f'Invalid official p1: {report.errors}')
    return read(folder / 'config.json'), read(folder / 'metrics.json')


def lineage(snapshot):
    errors, _ = check_snapshot.check(snapshot)
    if errors:
        raise ValueError(f'Snapshot check failed: {errors}')
    manifest = read(Path(snapshot) / 'manifest.json')
    reference = read(RECORDS / 'p1_reference.json')
    if digest(Path(snapshot) / 'manifest.json') != reference['snapshot_manifest_sha256']:
        raise ValueError('Snapshot manifest differs from official p1')
    versions = {name: metadata.version(name) for name in ('numpy', 'scipy', 'scikit-learn')}
    locked = tomllib.loads((ROOT / 'uv.lock').read_text(encoding='utf-8'))
    for name, version in versions.items():
        allowed = {p['version'] for p in locked['package'] if p['name'] == name}
        if version not in allowed:
            raise ValueError(f'Installed {name}=={version} differs from uv.lock: {sorted(allowed)}')
    if sys.version_info[:2] != (3, 12):
        raise ValueError('The common standard requires Python 3.12')
    return {'version': VERSION, 'preprocessing_version': PREPROCESSING_VERSION,
            'git_sha': git('rev-parse', 'HEAD'),
            'branch': git('branch', '--show-current'),
            'tracked_diff_sha256': object_hash(git('diff', 'HEAD', '--', *SOURCE_PATHS)),
            'source_sha256': {p: digest(ROOT / p) for p in SOURCE_PATHS},
            'python': platform.python_version(), 'libraries': versions,
            'standard_version': standard.STANDARD_VERSION,
            'snapshot_id': manifest['snapshot_id'],
            'snapshot_manifest_sha256': digest(Path(snapshot) / 'manifest.json'),
            'snapshot_files_sha256': {n: info['sha256'] for n, info in manifest['files'].items()}}


def scope_for(snap, month=None, series=None):
    _, days = run_backtest.select_origins(snap, 'p2', 'validation', month)
    ids = snap.series_ids if not series else sorted(set(int(s) for s in series.split(',')))
    if not ids or set(ids) - set(snap.series_ids):
        raise ValueError('Unknown or empty series selection')
    return {'phase': 'p2', 'origin_list': 'validation', 'month': month,
            'series': ids, 'days': [d.isoformat() for d in days],
            'comparison_eligible': month is None and ids == snap.series_ids}


def identity(config, provenance, scope):
    # Full SHA-256 identity; the common eight-character config_id alone is insufficient.
    return {'config': config, 'config_sha256': object_hash(config), 'lineage': provenance, 'scope': scope}


def verify_result(folder, expected, snap):
    """Read only: validate contract, exact grid, configuration and official metrics."""
    report = validate(folder)
    if report.errors:
        raise ValueError(f'Common validator errors: {report.errors}')
    config = read(folder / 'config.json')
    requested, scope = expected['config'], expected['scope']
    if any(config.get(k) != v for k, v in requested.items()):
        raise ValueError('Saved config differs from requested config')
    if (config['config_id'] != run_backtest.config_id(requested)
            or config['phase'] != 'p2' or config['origin_list'] != 'validation'
            or config['month'] != scope['month'] or sorted(config['series']) != scope['series']
            or config['data_version'] != expected['lineage']['snapshot_id']
            or config['git_sha'] != expected['lineage']['git_sha']):
        raise ValueError('Saved config scope or lineage differs')
    rows = evaluate.read_predictions(folder)
    keys = [(int(r['series_id']), r['origin_date'], int(r['horizon'])) for r in rows]
    wanted = {(s, d, h) for s in scope['series'] for d in scope['days'] for h in standard.HORIZONS}
    if len(keys) != len(wanted) or set(keys) != wanted:
        raise ValueError('Incomplete prediction grid')
    if any(r['model'] != 'Ridge' or r['config_id'] != config['config_id'] for r in rows):
        raise ValueError('Prediction row model/config_id mismatch')
    if any(r['item_id'] != snap.series[int(r['series_id'])].item
           or r['market'] != snap.series[int(r['series_id'])].market for r in rows):
        raise ValueError('Prediction row item/market mismatch')
    # Do not call write_metrics: existing official output must remain byte-identical.
    metrics = evaluate.evaluate(folder, snap)
    if read(folder / 'metrics.json') != metrics:
        raise ValueError('Metrics do not match official recomputation')
    bad = set(metrics['status_counts']) - {'OK', 'NO_INPUT'}
    if bad or not metrics['evaluated_points'] or not metrics['results']['model_only'].get('points'):
        raise ValueError(f'Execution contains model failures or no successful evaluated points: {sorted(bad)}')
    return metrics, {'errors': report.errors, 'warnings': report.warnings}


def completed_attempt(attempt, expected, snap):
    if (attempt / 'failure.json').exists() or (attempt / 'interrupted.json').exists():
        return None
    completion = read(attempt / 'completion.json')
    if completion['state'] != 'COMPLETED' or completion['identity'] != expected:
        return None
    required = set(standard.EXPERIMENT_FILES) | {
        'audit/start.json', 'audit/requested_config.json', 'audit/diagnostics.jsonl', 'audit/result.json'}
    if expected['scope']['comparison_eligible']:
        required.add('audit/official_comparison.json')
    if not required.issubset(completion['artifacts_sha256']):
        raise ValueError('Completion seal lacks required artifacts')
    folder = Path(completion['folder'])
    for name, sha in completion['artifacts_sha256'].items():
        base = attempt if name.startswith('audit/') else folder
        relative = name.removeprefix('audit/')
        if digest(base / relative) != sha:
            raise ValueError(f'Completed artifact changed: {name}')
    metrics, report = verify_result(folder, expected, snap)
    return {'attempt': str(attempt), 'folder': str(folder), 'metrics': metrics,
            'validation': report, 'state': 'COMPLETED', 'reused': True}


def find_completed(records, expected, snap):
    """Unsealed, failed, corrupted or older-lineage attempts are never reusable."""
    for attempt in sorted((records / 'attempts').glob('*')):
        try:
            start = read(attempt / 'start.json')
            if not (attempt / 'completion.json').exists():
                if not (attempt / 'failure.json').exists() and not (attempt / 'interrupted.json').exists():
                    exclusive_json(attempt / 'interrupted.json', {'at': now(), 'state': 'INTERRUPTED',
                                   'reason': 'Previous process ended before terminal record; artifacts retained'})
                continue
            if start['identity'] != expected:
                continue
            result = completed_attempt(attempt, expected, snap)
            if result:
                return result
        except (OSError, ValueError, KeyError, TypeError) as error:
            append_event(records / 'events.jsonl', {'event': 'REUSE_REJECTED', 'attempt': str(attempt),
                                                   'reason': str(error)})
    return None


def summary_result(metrics, baseline, snap, eligible=True):
    policy = metrics['results']['policy']
    old = baseline['results']['policy']
    delta = lambda a, b: round(a - b, 6)
    series, items = {}, {}
    for sid, values in policy['series'].items():
        meta = snap.series[int(sid)]
        change = delta(values['mape'], old['series'][sid]['mape']) if eligible else None
        series[sid] = {**values, 'item': meta.item, 'market': meta.market, 'delta_vs_p1_pp': change}
        items.setdefault(meta.item, []).append(sid)
    by_item = {}
    for item, ids in items.items():
        mape = sum(series[s]['mape'] for s in ids) / len(ids)
        p1 = sum(old['series'][s]['mape'] for s in ids) / len(ids) if eligible else None
        by_item[item] = {'macro_mape': round(mape, 6), 'series_count': len(ids),
                         'delta_vs_p1_pp': delta(mape, p1) if eligible else None}
    markets = {m: {**v, 'delta_vs_p1_pp': delta(v['macro_mape'], old['by_market'][m]['macro_mape'])
                    if eligible else None} for m, v in policy['by_market'].items()}
    changes = [s['delta_vs_p1_pp'] for s in series.values()] if eligible else []
    return {'comparison_eligible': eligible, 'macro_mape': policy['macro_mape'],
            'naive_macro_mape': policy['naive_macro_mape'],
            'naive_relative_improvement_pct': policy['relative_improvement_pct'],
            'delta_vs_p1_pp': delta(policy['macro_mape'], old['macro_mape']) if eligible else None,
            'relative_improvement_vs_p1_pct': round((old['macro_mape'] - policy['macro_mape']) /
                                                      old['macro_mape'] * 100, 6) if eligible else None,
            'macro_rmae': policy['macro_rmae'], 'series_wins_vs_naive': policy['series_wins'],
            'series_improved_vs_p1': sum(c < 0 for c in changes) if eligible else None,
            'series_worsened_vs_p1': sum(c > 0 for c in changes) if eligible else None,
            'series_tied_vs_p1': sum(c == 0 for c in changes) if eligible else None,
            'series': series, 'by_item': by_item, 'by_market': markets,
            'success_rate': metrics['success_rate'], 'evaluated_points': metrics['evaluated_points'],
            'status_counts_all_rows': metrics['status_counts'], 'adoption': metrics['adoption'],
            'model_only': metrics['results']['model_only']}


def run_one(config, provenance, scope, snap, args):
    expected = identity(config, provenance, scope)
    reused = find_completed(args.records, expected, snap)
    if reused:
        append_event(args.records / 'events.jsonl', {'event': 'REUSED', 'attempt': reused['attempt'],
                                                     'identity_sha256': object_hash(expected)})
        return reused
    attempt = args.records / 'attempts' / (datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S') + '-' + uuid4().hex[:12])
    attempt.mkdir(parents=True)
    # The common runner independently refuses any pre-existing output folder.
    exp_id = run_backtest.next_experiment_id(args.out, 'ridge', 'p2')
    folder = args.out / exp_id
    config_path = attempt / 'requested_config.json'
    exclusive_json(config_path, config)
    argv = ['--config', str(config_path), '--phase', 'p2', '--origins', 'validation',
            '--snapshot', str(args.snapshot), '--out', str(args.out), '--experiment-id', exp_id]
    if scope['month']:
        argv += ['--month', scope['month']]
    if args.series:
        argv += ['--series', ','.join(map(str, scope['series']))]
    exclusive_json(attempt / 'start.json', {'at': now(), 'state': 'RUNNING', 'version': VERSION,
                   'experiment_id': exp_id, 'identity': expected, 'identity_sha256': object_hash(expected),
                   'folder': str(folder), 'argv': [sys.executable, '-m', 'tools.run_backtest', *argv],
                   'command': subprocess.list2cmdline([sys.executable, '-m', 'tools.run_backtest', *argv]),
                   'driver_argv': sys.argv, 'requested_config_file_sha256': digest(config_path),
                   'feature_names': loader.feature_names(config['extra_features']),
                   'feature_count': len(loader.feature_names(config['extra_features']))})
    append_event(args.records / 'events.jsonl', {'event': 'STARTED', 'attempt': str(attempt), 'experiment_id': exp_id})
    token = AUDIT_SINK.set(lambda record: append_event(attempt / 'diagnostics.jsonl', record))
    started = time.perf_counter()
    try:
        # Archive exact source bytes, including uncommitted sources. Never copy .env.
        for name in SOURCE_PATHS:
            dest = attempt / 'sources' / name
            dest.parent.mkdir(parents=True, exist_ok=True)
            with dest.open('xb') as handle:
                handle.write((ROOT / name).read_bytes())
        # Public CLI entry point; config and runtime artifacts remain common output.
        status = run_backtest.main(argv)
        if status:
            raise RuntimeError(f'Common runner exit status {status}')
        metrics, report = verify_result(folder, expected, snap)
        # Detect data/source edits during execution before sealing a reusable run.
        if lineage(args.snapshot) != provenance:
            raise ValueError('Data, environment or source changed during execution')
        _, baseline = p1_result()
        result = summary_result(metrics, baseline, snap, scope['comparison_eligible'])
        rows = evaluate.read_predictions(folder)
        result['failure_types_all_rows'] = dict(Counter(f'{r["status"]}:{r["error_code"]}'
                                                       for r in rows if r['status'] != 'OK'))
        result['validation'] = report
        result['seconds'] = round(time.perf_counter() - started, 6)
        result['kind'] = 'control' if not config['extra_features'] else (
            'single' if len(config['extra_features']) == 1 else 'combination')
        result['bundles'] = config['extra_features']
        result['decision'] = 'PENDING_REVIEW'
        if scope['comparison_eligible']:
            comparison = evaluate.compare([ROOT / 'experiments' / P1_ID, folder], snap)
            exclusive_json(attempt / 'official_comparison.json', comparison)
        exclusive_json(attempt / 'result.json', result)
        hashes = {name: digest(folder / name) for name in standard.EXPERIMENT_FILES}
        for path in attempt.rglob('*'):
            if path.is_file():
                hashes['audit/' + path.relative_to(attempt).as_posix()] = digest(path)
        completion = {'at': now(), 'state': 'COMPLETED', 'identity': expected, 'folder': str(folder),
                      'artifacts_sha256': hashes, 'seconds': result['seconds']}
        exclusive_json(attempt / 'completion.json', completion)
        append_event(args.records / 'events.jsonl', {'event': 'COMPLETED', 'attempt': str(attempt)})
        return {'attempt': str(attempt), 'folder': str(folder), 'metrics': metrics,
                'validation': report, 'state': 'COMPLETED', 'reused': False}
    except BaseException as error:
        interrupted = isinstance(error, (KeyboardInterrupt, SystemExit))
        state = 'INTERRUPTED' if interrupted else 'FAILED'
        exclusive_json(attempt / ('interrupted.json' if interrupted else 'failure.json'),
                       {'at': now(), 'state': state, 'error_type': type(error).__name__, 'error': str(error),
                        'seconds': time.perf_counter() - started, 'traceback': traceback.format_exc()})
        append_event(args.records / 'events.jsonl', {'event': state, 'attempt': str(attempt), 'error': str(error)})
        if interrupted:
            raise
        return {'attempt': str(attempt), 'folder': str(folder), 'state': state, 'error': str(error)}
    finally:
        AUDIT_SINK.reset(token)


def combination_candidates(singles, p1_mape):
    if set(singles) != set(standard.EXTRA_BUNDLES) or any(v is None for v in singles.values()):
        raise ValueError('Combination requires all five verified, completed single-bundle runs')
    helpful = [b for b in standard.EXTRA_BUNDLES
               if singles[b]['metrics']['results']['policy']['macro_mape'] < p1_mape]
    return helpful if len(helpful) >= 2 else []


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--execute', action='store_true', help='Explicitly run training; default prints PLANNED only')
    parser.add_argument('--bundle', action='append', choices=tuple(standard.EXTRA_BUNDLES), default=[])
    parser.add_argument('--all', action='store_true', help='Five singles, then eligible combination')
    parser.add_argument('--control', action='store_true', help='Separate p2 base-only control')
    parser.add_argument('--combine', action='store_true', help='Combine helpful bundles from five completed singles')
    parser.add_argument('--snapshot', type=Path, default=evaluate.DEFAULT_SNAPSHOT)
    parser.add_argument('--out', type=Path, default=ROOT / 'experiments')
    parser.add_argument('--records', type=Path, default=RECORDS / 'execution')
    parser.add_argument('--month', help='Diagnostic subset only: never compare with full official p1')
    parser.add_argument('--series', help='Diagnostic subset only: comma-separated IDs')
    args = parser.parse_args(argv)
    args.records, args.out, args.snapshot = args.records.resolve(), args.out.resolve(), args.snapshot.resolve()
    if (args.combine or args.all) and (args.month or args.series):
        parser.error('Combination selection requires full Validation scope')
    if args.execute and not (args.bundle or args.all or args.control or args.combine):
        parser.error('--execute requires --bundle, --control, --combine or --all')
    p1_config, baseline = p1_result()
    selected = list(standard.EXTRA_BUNDLES) if args.all else list(loader.check_bundles(args.bundle))
    planned = [config_for([b]) for b in selected]
    if args.control:
        planned.insert(0, config_for())
    if not args.execute:
        print(json.dumps({'state': 'PLANNED', 'training_executed': False, 'p1': P1_ID,
                          'configs': planned or [config_for([b]) for b in standard.EXTRA_BUNDLES],
                          'combination': 'After five verified singles; all bundles improving policy MAPE vs p1'},
                         ensure_ascii=False, indent=2))
        return 0
    provenance = lineage(args.snapshot)
    snap = loader.Snapshot(args.snapshot)
    scope = scope_for(snap, args.month, args.series)
    if scope['comparison_eligible'] and scope['series'] != sorted(p1_config['series']):
        raise ValueError('Series differ from official p1')
    with execution_lock(args.records):
        results = []
        for config in planned:
            results.append(run_one(config, provenance, scope, snap, args))
        if args.all or args.combine:
            singles = {}
            for b in standard.EXTRA_BUNDLES:
                expected = identity(config_for([b]), provenance, scope)
                singles[b] = find_completed(args.records, expected, snap)
            bundles = combination_candidates(singles, baseline['results']['policy']['macro_mape'])
            if bundles:
                combined = run_one(config_for(bundles), provenance, scope, snap, args)
                if combined['state'] == 'COMPLETED':
                    # Kept outside sealed attempts so reuse never mutates archived records.
                    comparison = {'at': now(), 'kind': 'combination_vs_singles', 'bundles': bundles,
                                  'combination': combined['folder'], 'singles': {b: singles[b]['folder'] for b in bundles},
                                  'delta_combination_minus_single_pp': {
                                      b: round(combined['metrics']['results']['policy']['macro_mape'] -
                                               singles[b]['metrics']['results']['policy']['macro_mape'], 6) for b in bundles}}
                    exclusive_json(args.records / f'combination-{uuid4().hex}.json', comparison)
                results.append(combined)
            else:
                append_event(args.records / 'events.jsonl', {'event': 'COMBINATION_SKIPPED',
                             'reason': 'Fewer than two single bundles improve official p1 policy MAPE'})
        print(json.dumps([{k: v for k, v in r.items() if k != 'metrics'} for r in results], ensure_ascii=False, indent=2))
        return int(any(r['state'] != 'COMPLETED' for r in results))


if __name__ == '__main__':
    if sys.platform == 'win32' and not sys.flags.utf8_mode:
        # Common tools use text-mode subprocesses. Enable Python UTF-8 mode at
        # startup without patching the shared tools or changing their contracts.
        os.execv(sys.executable, [sys.executable, '-X', 'utf8', '-m',
                                 'model_comparison.ridge.p2', *sys.argv[1:]])
    try:
        sys.exit(main())
    except (OSError, ValueError, RuntimeError) as error:
        print(f'Ridge p2 failed: {error}', file=sys.stderr)
        sys.exit(1)
