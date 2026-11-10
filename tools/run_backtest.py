"""공통 실행기(기준서 §3.4, §7, §9, §10). 모델 담당자는 설정 파일 하나와 Model 클래스만 준비한다.

    # 단계 0 점검(naive, 2025-01)
    uv run --extra prices python -m tools.run_backtest --config tools/configs/naive.json --phase smoke --month 2025-01

    # 튜닝 시도 1회(튜닝 목록). 결과 폴더는 runs/(Git 제외), 시도 기록은 --record-trial 파일에 한 줄 추가
    uv run --extra prices python -m tools.run_backtest --config my.json --phase p1 --origins tune --out runs \\
        --record-trial runs/xgb-p1-tuning.csv

    # 1차 제출(검증 전체). 튜닝 기록을 결과 폴더의 tuning_log.csv로 넣는다
    uv run --extra prices python -m tools.run_backtest --config my.json --phase p1 --tuning-log runs/xgb-p1-tuning.csv

설정 파일(JSON):
    {"model": "XGBoost", "owner": "A", "class": "model_comparison.xgboost.model:XGBModel",
     "params": {...}, "feature_set": "base_v1", "extra_features": [], "target_transform": "change_ratio",
     "strategy": "direct_per_horizon", "seed": 42}
실행기가 experiment_id·config_id·git_sha·data_version·phase·origins·refit·runtime·tuning을 채워 config.json으로 저장한다.

동작
- 시작할 때 apply_environment()(스레드 4·PYTHONHASHSEED 등), origins.guard()(test가 아니면 시험 기준일 거부)
- 계열별·기준일 순서로, 각 ISO 주의 첫 기준일에 새 모델 인스턴스를 만들어 fit(그 기준일까지의 학습 표본), 매 기준일 predict
- NO_INPUT(학습 관측 400개 미만·최신 관측 7일 초과·특징 창 결측), FIT_FAILED, PREDICT_FAILED, INVALID_VALUE, TIMEOUT 기록
- 시간 제한(재학습 기준일 600초, 예측만 60초)은 끝난 뒤 잰 시간으로 판정한다(넘으면 그 기준일 예측을 버리고 TIMEOUT)
- 후처리: raw는 소수 6자리로 기록, predicted_price = round(raw)(0.5 올림, 최소 1)
- 끝나면 evaluate로 metrics.json을 만들고 validate_experiment로 형식을 검사한다
"""
from tools.runtime import apply_environment

_CHANGED_ENV = apply_environment()  # 라이브러리를 불러오기 전에 스레드 수를 고정한다

import argparse
import csv
import hashlib
import importlib
import json
import math
import os
import platform
import subprocess
import sys
import time
import traceback
from datetime import date, timedelta
from pathlib import Path

from tools import evaluate, loader, origins, standard
from tools.validate_experiment import round_half_up, validate

ROOT = Path(__file__).resolve().parents[1]
PREFIX = {name: prefix for prefix, (name, _) in standard.MODELS.items()}
BASELINE_MODELS = {'naive', 'mean7'}
CONFIG_ID_KEYS = ('model', 'class', 'params', 'feature_set', 'extra_features', 'target_transform', 'strategy', 'seed')
USER_REQUIRED = ('model', 'class', 'params', 'feature_set', 'extra_features', 'target_transform', 'strategy', 'seed')


class RunError(Exception):
    pass


def config_id(config: dict) -> str:
    content = json.dumps({k: config.get(k) for k in CONFIG_ID_KEYS}, sort_keys=True, ensure_ascii=False)
    return hashlib.sha256(content.encode('utf-8')).hexdigest()[:8]


def load_class(spec: str):
    module, _, name = spec.partition(':')
    if not name:
        raise RunError(f'class는 "모듈:클래스" 형식이어야 함: {spec!r}')
    return getattr(importlib.import_module(module), name)


def git(*args):
    try:
        return subprocess.run(['git', *args], cwd=ROOT, capture_output=True, text=True, check=False).stdout.strip()
    except OSError:
        return ''


def peak_memory_mb():
    """최대 RSS(MB). Linux·macOS는 resource, Windows는 PeakWorkingSetSize."""
    try:
        import resource
        peak = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        return round(peak / (1024 * 1024 if sys.platform == 'darwin' else 1024), 1)
    except ImportError:
        pass
    try:
        import ctypes
        from ctypes import wintypes

        class Counters(ctypes.Structure):
            _fields_ = [('cb', wintypes.DWORD), ('PageFaultCount', wintypes.DWORD),
                        ('PeakWorkingSetSize', ctypes.c_size_t), ('WorkingSetSize', ctypes.c_size_t),
                        ('QuotaPeakPagedPoolUsage', ctypes.c_size_t), ('QuotaPagedPoolUsage', ctypes.c_size_t),
                        ('QuotaPeakNonPagedPoolUsage', ctypes.c_size_t), ('QuotaNonPagedPoolUsage', ctypes.c_size_t),
                        ('PagefileUsage', ctypes.c_size_t), ('PeakPagefileUsage', ctypes.c_size_t)]
        counters = Counters()
        counters.cb = ctypes.sizeof(Counters)
        process = ctypes.windll.kernel32.GetCurrentProcess()
        ctypes.windll.psapi.GetProcessMemoryInfo(process, ctypes.byref(counters), counters.cb)
        return round(counters.PeakWorkingSetSize / 1024 / 1024, 1)
    except (OSError, AttributeError):
        return None


def environment_text(where: str) -> str:
    try:
        freeze = subprocess.run(['uv', 'pip', 'freeze'], cwd=ROOT, capture_output=True, text=True, check=False).stdout
    except OSError:
        freeze = ''
    if not freeze.strip():
        from importlib import metadata
        freeze = '\n'.join(sorted(f'{d.metadata["Name"]}=={d.version}' for d in metadata.distributions()))
    cpu = platform.processor()
    try:
        cpu = next(line.split(':', 1)[1].strip() for line in Path('/proc/cpuinfo').read_text().splitlines()
                   if line.startswith('model name'))
    except (OSError, StopIteration):
        pass
    lines = [
        f'git_sha: {git("rev-parse", "HEAD")}',
        f'git_dirty: {bool(git("status", "--porcelain", "--untracked-files=no"))}',
        f'where: {where}',
        f'image_digest: {os.getenv("FOODVALUE_IMAGE_DIGEST", "")}',
        f'python: {sys.version.split()[0]}',
        f'os: {platform.platform()}',
        f'cpu: {cpu}',
        f'cpu_count: {os.cpu_count()}',
        f'thread_env: {json.dumps({k: os.environ.get(k) for k in standard.THREAD_ENV}, ensure_ascii=False)}',
        '',
        '# uv pip freeze',
        freeze.strip(),
    ]
    return '\n'.join(lines) + '\n'


def next_experiment_id(out: Path, prefix: str, phase: str) -> str:
    day = date.today().strftime('%Y%m%d')
    for seq in range(1, 100):
        candidate = f'{prefix}-{phase}-{day}-{seq:02d}'
        if not (out / candidate).exists():
            return candidate
    raise RunError('같은 날 실험 번호가 99를 넘음')


def select_origins(snap: loader.Snapshot, phase: str, origin_list: str | None, month: str | None):
    origin_list = origin_list or ('test' if phase == 'test' else 'validation')
    days = snap.origins[origin_list]
    if month:
        days = [d for d in days if d.strftime('%Y-%m') == month]
    if not days:
        raise RunError(f'기준일이 없음: origins={origin_list}, month={month}')
    origins.guard(phase, days)
    return origin_list, days


def tuning_summary(path: Path | None):
    if not path:
        return [], {'trials_used': 0, 'seconds_used': 0}
    with open(path, encoding='utf-8', newline='') as f:
        reader = csv.DictReader(f)
        if tuple(reader.fieldnames or ()) != standard.TUNING_COLUMNS:
            raise RunError(f'튜닝 기록 열은 {standard.TUNING_COLUMNS}이어야 함')
        trials = list(reader)
    seconds = sum(float(t['seconds'] or 0) for t in trials)
    return trials, {'trials_used': len(trials), 'seconds_used': round(seconds)}


def prediction_rows(values, status, error):
    """모델 출력 7개 → (raw 문자열, 최종 가격 문자열, 상태, 오류 코드) 7개. §8.3 후처리."""
    if status != 'OK':
        return [('', '', status, error)] * len(standard.HORIZONS)
    if values is None or len(values) != len(standard.HORIZONS):
        return [('', '', 'PREDICT_FAILED', 'BAD_LENGTH')] * len(standard.HORIZONS)
    rows = []
    for value in values:
        if value is None:
            rows.append(('', '', 'PREDICT_FAILED', 'NONE'))
            continue
        try:
            raw = float(value)
        except (TypeError, ValueError):
            rows.append(('', '', 'PREDICT_FAILED', 'NOT_NUMBER'))
            continue
        if not math.isfinite(raw) or raw <= 0:
            rows.append(('', '', 'INVALID_VALUE', 'NON_POSITIVE' if math.isfinite(raw) else 'NOT_FINITE'))
            continue
        text = f'{raw:.6f}'
        rows.append((text, str(round_half_up(float(text))), 'OK', ''))
    return rows


def run_series(cls, params, seed, snap, series_id, days, log):
    """한 계열의 모든 기준일. 반환: [(기준일, [(raw, price, status, error) × 7])], 통계."""
    results, stats = [], {'refits': 0, 'fit_seconds': 0.0, 'predict_seconds': 0.0, 'timeouts': 0}
    model, fit_state, week = None, ('FIT_FAILED', 'NOT_FITTED'), None
    for d in days:
        refit_seconds = 0.0
        if d.isocalendar()[:2] != week:
            week = d.isocalendar()[:2]
            stats['refits'] += 1
            started = time.perf_counter()
            try:
                history = snap.training_data(series_id, d)
                model = cls(**params)
                model.fit(history, seed)
                fit_state = ('OK', '')
            except loader.NoInput as error:
                fit_state = ('NO_INPUT', 'TRAIN_' + str(error).split(' ')[0][:20])
                log(f'  {series_id} {d} 재학습 NO_INPUT: {error}')
            except Exception as error:  # noqa: BLE001 — 모델 오류는 기록하고 계속한다(§9)
                fit_state = ('FIT_FAILED', type(error).__name__)
                log(f'  {series_id} {d} 재학습 실패: {type(error).__name__}: {error}')
                log(traceback.format_exc(limit=3))
            refit_seconds = time.perf_counter() - started
            stats['fit_seconds'] += refit_seconds
        if fit_state[0] != 'OK':
            results.append((d, prediction_rows(None, *fit_state)))
            continue
        started = time.perf_counter()
        try:
            inputs = snap.origin_inputs(series_id, d)
            values, status, error = model.predict(inputs), 'OK', ''
        except loader.NoInput as reason:
            values, status, error = None, 'NO_INPUT', 'STALE_OR_GAP'
            log(f'  {series_id} {d} NO_INPUT: {reason}')
        except Exception as reason:  # noqa: BLE001
            values, status, error = None, 'PREDICT_FAILED', type(reason).__name__
            log(f'  {series_id} {d} 예측 실패: {type(reason).__name__}: {reason}')
        predict_seconds = time.perf_counter() - started
        stats['predict_seconds'] += predict_seconds
        limit = standard.TIMEOUT_SECONDS['refit'] if refit_seconds else standard.TIMEOUT_SECONDS['predict']
        if refit_seconds + predict_seconds > limit:
            stats['timeouts'] += 1
            values, status, error = None, 'TIMEOUT', f'{refit_seconds + predict_seconds:.0f}s>{limit}s'
            log(f'  {series_id} {d} TIMEOUT {error}')
        results.append((d, prediction_rows(values, status, error)))
    return results, stats


def run(args) -> Path:
    user = json.loads(Path(args.config).read_text(encoding='utf-8'))
    missing = [k for k in USER_REQUIRED if k not in user]
    if missing:
        raise RunError(f'설정 파일에 필요한 항목이 없음: {missing}')
    model_name = user['model']
    prefix = 'base' if model_name in BASELINE_MODELS else PREFIX.get(model_name)
    if not prefix:
        raise RunError(f'model은 {sorted(PREFIX) + sorted(BASELINE_MODELS)} 중 하나: {model_name!r}')
    if args.phase == 'test' and args.where != 'docker':
        raise RunError('최종 시험(test)은 --where docker로 Docker 안에서 실행해야 함(§1.3)')
    if args.phase == 'test' and (args.tuning_log or args.record_trial):
        raise RunError('최종 시험 중에는 튜닝할 수 없음(§7.2)')
    snap = loader.Snapshot(args.snapshot)
    origin_list, days = select_origins(snap, args.phase, args.origins, args.month)
    series_ids = snap.series_ids
    if args.series:
        series_ids = [int(s) for s in args.series.split(',')]
        unknown = set(series_ids) - set(snap.series_ids)
        if unknown:
            raise RunError(f'스냅샷에 없는 계열: {sorted(unknown)}')
    cls = load_class(user['class'])
    trials, tuning = tuning_summary(args.tuning_log)

    out = Path(args.out)
    exp_id = args.experiment_id or next_experiment_id(out, prefix, args.phase)
    folder = out / exp_id
    if folder.exists():
        raise RunError(f'이미 있는 결과 폴더: {folder}')
    folder.mkdir(parents=True)
    config = {**user, 'experiment_id': exp_id, 'owner': user.get('owner', standard.MODELS.get(prefix, ('', ''))[1]),
              'standard_version': standard.STANDARD_VERSION, 'git_sha': git('rev-parse', 'HEAD') or None,
              'data_version': standard.DATA_VERSION, 'phase': args.phase, 'origins': standard.ORIGIN_SETS[args.phase],
              'origin_list': origin_list, 'month': args.month, 'series': series_ids, 'refit': standard.REFIT,
              'runtime': {'where': args.where, 'threads': standard.THREADS}, 'tuning': tuning}
    config['config_id'] = config_id(config)
    (folder / 'config.json').write_text(json.dumps(config, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    (folder / 'environment.txt').write_text(environment_text(args.where), encoding='utf-8')
    with open(folder / 'tuning_log.csv', 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f, lineterminator='\n')
        writer.writerow(standard.TUNING_COLUMNS)
        for t in trials:
            writer.writerow([t[c] for c in standard.TUNING_COLUMNS])

    log_file = open(folder / 'run.log', 'w', encoding='utf-8')  # noqa: SIM115 — 끝에서 닫음

    def log(message):
        print(message)
        log_file.write(message + '\n')
        log_file.flush()

    if _CHANGED_ENV:
        log(f'환경변수를 기준서 값으로 바꿈: {sorted(_CHANGED_ENV)}')
    log(f'{exp_id} config_id={config["config_id"]} model={model_name} phase={args.phase} origins={origin_list}'
        f'{" month=" + args.month if args.month else ""} 기준일 {len(days)}개 × 계열 {len(series_ids)}개')
    started = time.perf_counter()
    per_series = {}
    with open(folder / 'predictions.csv', 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f, lineterminator='\n')
        writer.writerow(standard.PREDICTION_COLUMNS)
        for sid in series_ids:
            s = snap.series[sid]
            t0 = time.perf_counter()
            results, stats = run_series(cls, config['params'], config['seed'], snap, sid, days, log)
            stats['seconds'] = round(time.perf_counter() - t0, 3)
            per_series[sid] = stats
            ok = 0
            for d, rows in results:
                for h, (raw, price, status, error) in zip(standard.HORIZONS, rows):
                    ok += status == 'OK'
                    writer.writerow([exp_id, model_name, config['config_id'], standard.DATA_VERSION, sid, s.item, s.market,
                                     d.isoformat(), (d + timedelta(days=h)).isoformat(),
                                     h, raw, price, status, error])
            log(f'계열 {sid:>5} {s.item} {s.market:9} 재학습 {stats["refits"]}회 {stats["fit_seconds"]:.1f}s '
                f'예측 {stats["predict_seconds"]:.1f}s OK {ok}/{len(results) * len(standard.HORIZONS)}')
    resources = {'total_seconds': round(time.perf_counter() - started, 3), 'peak_memory_mb': peak_memory_mb(),
                 'per_series': {str(k): {kk: round(vv, 3) if isinstance(vv, float) else vv for kk, vv in v.items()}
                                for k, v in per_series.items()},
                 'tuning': tuning}
    log('RESOURCES ' + json.dumps(resources, ensure_ascii=False))

    metrics, digest = evaluate.write_metrics(folder, snap)
    evaluate.print_metrics(metrics)
    log(f'metrics SHA-256 {digest}')
    log_file.close()

    if args.record_trial:
        record_trial(args.record_trial, config, metrics, resources['total_seconds'])
    report = validate(folder)
    report.print()
    if report.errors:
        raise RunError('결과 폴더가 기준서 형식 검사를 통과하지 못함')
    return folder


def record_trial(path: Path, config, metrics, seconds):
    path = Path(path)
    new = not path.exists()
    if not new:
        trials, _ = tuning_summary(path)
        budget = standard.TUNING_BUDGET.get(config['phase'])
        if budget and len(trials) >= budget['trials']:
            print(f'경고: 시도 {len(trials) + 1}회째 — {config["phase"]} 상한 {budget["trials"]}회를 넘음(§6)')
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, 'a', encoding='utf-8', newline='') as f:
        writer = csv.writer(f, lineterminator='\n')
        if new:
            writer.writerow(standard.TUNING_COLUMNS)
            trial = 1
        else:
            trial = len(tuning_summary(path)[0]) + 1
        policy = metrics['results']['policy']
        writer.writerow([trial, config['config_id'], json.dumps(config['params'], sort_keys=True, ensure_ascii=False),
                         policy.get('macro_mape', ''), round(seconds, 1),
                         'OK' if metrics['success_rate'] >= standard.ADOPTION['min_success_rate'] else 'LOW_SUCCESS'])
    print(f'튜닝 기록 {path}에 시도 {trial} 추가')


def main(argv=None):
    parser = argparse.ArgumentParser(description='공통 실행기(기준서 §9)')
    parser.add_argument('--config', required=True, type=Path, help='모델 설정 JSON')
    parser.add_argument('--phase', required=True, choices=standard.PHASES)
    parser.add_argument('--origins', choices=('tune', 'validation', 'test'),
                        help='기준일 목록. 기본: test 단계는 test, 나머지는 validation')
    parser.add_argument('--month', help='YYYY-MM. 그 달 기준일만(단계 0: 2025-01)')
    parser.add_argument('--series', help='계열 id 쉼표 목록(점검용). 제출은 전체 계열')
    parser.add_argument('--snapshot', type=Path, default=evaluate.DEFAULT_SNAPSHOT)
    parser.add_argument('--out', type=Path, default=ROOT / 'experiments', help='결과 상위 폴더. 튜닝 시도는 runs 권장')
    parser.add_argument('--experiment-id')
    parser.add_argument('--where', choices=('local', 'docker'), default='local')
    parser.add_argument('--tuning-log', type=Path, help='이 실험의 tuning_log.csv로 넣을 튜닝 기록')
    parser.add_argument('--record-trial', type=Path, help='이 실행을 튜닝 시도로 기록할 CSV(없으면 만듦)')
    args = parser.parse_args(argv)
    try:
        folder = run(args)
    except (RunError, origins.ForbiddenOriginError, FileNotFoundError, ValueError) as error:
        print(f'실패: {error}', file=sys.stderr)
        return 1
    print(f'결과: {folder}')
    return 0


if __name__ == '__main__':
    sys.exit(main())
