"""구조적 가격 전달 모델 자체 실행기(독립 트랙, PRD §11). 기준서의 p1/p2 단계·제출 형식과는 무관하다.

    # 점검(검증 구간 한 달)
    uv run --extra prices python -m model_comparison.structural.run --config model_comparison/structural/config.json \\
        --name smoke-v0 --origins validation --month 2025-01 --series 1,2,9001

    # 튜닝 시도 1회(튜닝 기준일 53개 × 10계열). 반드시 --record-trial로 기록하고, 시도는 최대 40회
    uv run --extra prices python -m model_comparison.structural.run --config model_comparison/structural/configs/<변형>.json \\
        --name t01-v0 --origins tune --record-trial

    # 검증 전체 1회(마지막에 한 번만. runs/struct 안에 검증 기록이 있으면 거부)
    uv run --extra prices python -m model_comparison.structural.run --config model_comparison/structural/config.json \\
        --name final-validation --origins validation

규칙은 tools/run_backtest.py와 같다(읽기만 하고 고치지 않음). 계열별·기준일 순서로, 각 ISO 주의 첫 기준일에 새 모델을 만들어
fit(그 기준일까지의 학습 표본)하고 매 기준일 predict한다. 공통 로더(tools.loader.Snapshot)의 training_data·origin_inputs로만
입력을 받는다. NO_INPUT(학습 관측 400개 미만·최신 관측 7일 초과·특징 창 결측), FIT_FAILED, PREDICT_FAILED, INVALID_VALUE,
TIMEOUT(재학습 기준일 600초, 예측만 60초)을 기록하고 후처리는 round(0.5 올림, 최소 1)이다.

이 트랙의 자체 규칙(깨지지 않게 코드로 막는다)
- 2025-10-31 이후 기준일(간격·최종 시험 구간)은 거부한다.
- 튜닝 시도는 최대 40회. 튜닝 기준일 전체 실행은 --record-trial이 필수이고, 모든 시도(실패 포함)가 runs/struct/tuning_log.csv에 남는다.
- 검증 전체(--month·--series 없는 validation) 실행은 한 번뿐이다. 시작할 때 기록이 남으므로 중간에 죽어도 다시 못 돌린다.
- 결과 폴더가 이미 있으면 거부한다.
- 줄인 실행(--month·--series)은 predictions.csv·run.log·status_summary.json(상태별 개수·시간)만 남기고 MAPE·rMAE·naive 비교는
  계산하지도 출력하지도 않는다(검증을 반복해서 엿보는 우회 방지). score.py도 그런 폴더의 채점을 거부한다.
"""
from tools.runtime import apply_environment

_CHANGED_ENV = apply_environment()  # 라이브러리를 불러오기 전에 스레드 수를 고정한다

import argparse
import csv
import hashlib
import importlib
import json
import math
import subprocess
import sys
import time
import traceback
from datetime import date, timedelta
from pathlib import Path

from model_comparison.structural import score
from tools import loader, origins, standard
from tools.validate_experiment import round_half_up

ROOT = Path(__file__).resolve().parents[2]
DEFAULT_SNAPSHOT = ROOT / 'data' / 'snapshots' / standard.DATA_VERSION
DEFAULT_OUT = ROOT / 'runs' / 'struct'
TUNING_LOG = 'tuning_log.csv'
STATUS_SUMMARY = 'status_summary.json'
TUNING_COLUMNS = ('trial', 'name', 'params', 'macro_mape', 'seconds', 'status')
MAX_TRIALS = 40
LAST_ALLOWED_ORIGIN = standard.VALIDATION[1]  # 2025-10-31. 이후 기준일은 간격·최종 시험 구간
USER_REQUIRED = ('model', 'class', 'params', 'feature_set', 'extra_features', 'target_transform', 'strategy', 'seed')
CONFIG_ID_KEYS = USER_REQUIRED
PREDICTION_COLUMNS = ('run', 'series_id', 'item', 'market', 'origin_date', 'target_date', 'horizon',
                      'predicted_price_raw', 'predicted_price', 'status', 'error_code')


class RunError(Exception):
    pass


# ---- 실행 전 검사(스냅샷 없이 시험 가능) -----------------------------------------------------------------------

def check_origins(days):
    """검증 구간(2024-11-01 ~ 2025-10-31) 밖 기준일이 하나라도 있으면 거부. 최종 시험 기준일은 어떤 경우에도 쓰지 않는다."""
    late = [d for d in days if d > LAST_ALLOWED_ORIGIN]
    if late:
        raise RunError(f'{LAST_ALLOWED_ORIGIN} 이후 기준일은 쓸 수 없음(최종 시험 구간 보호): {len(late)}개, 예 {late[0]}')
    try:
        origins.guard('p1', days)
    except origins.ForbiddenOriginError as error:
        raise RunError(str(error)) from error
    return list(days)


def read_trials(out: Path):
    path = Path(out) / TUNING_LOG
    if not path.exists():
        return []
    with open(path, encoding='utf-8', newline='') as f:
        return list(csv.DictReader(f))


def check_trial_budget(out: Path):
    used = len(read_trials(out))
    if used >= MAX_TRIALS:
        raise RunError(f'튜닝 시도가 이미 {used}회 — 상한 {MAX_TRIALS}회라 더 실행할 수 없음')
    return used


def run_kind(origin_list: str, month, series) -> str:
    """tune_trial: 튜닝 기준일 전체 / validation_full: 검증 전체(1회) / smoke: --month나 --series로 줄인 점검."""
    if month or series:
        return 'smoke'
    return 'validation_full' if origin_list == 'validation' else 'tune_trial'


def check_validation_once(out: Path):
    out = Path(out)
    if not out.exists():
        return
    for config in sorted(out.glob('*/config.json')):
        try:
            kind = json.loads(config.read_text(encoding='utf-8')).get('kind')
        except (OSError, ValueError):
            continue
        if kind == 'validation_full':
            raise RunError(f'검증 전체 실행은 1회뿐인데 이미 기록이 있음: {config.parent.name}')


def pre_checks(args, out: Path):
    """스냅샷을 읽기 전에 막을 수 있는 것들."""
    kind = run_kind(args.origins, args.month, args.series)
    if args.origins == 'validation' and args.series and not args.month:
        raise RunError('검증 구간 일부 계열만 보는 실행은 --month와 함께만 가능(점검 용도)')
    if args.record_trial and kind != 'tune_trial':
        raise RunError('--record-trial은 튜닝 기준일 전체 실행(--origins tune, --month·--series 없음)에만 쓸 수 있음')
    if kind == 'tune_trial':
        if not args.record_trial:
            raise RunError('튜닝 기준일 전체 실행은 --record-trial이 필수(모든 시도를 기록해야 함)')
        check_trial_budget(out)
    if kind == 'validation_full':
        check_validation_once(out)
    return kind


# ---- 실행 ---------------------------------------------------------------------------------------------------

def load_class(spec: str):
    module, _, name = spec.partition(':')
    if not name:
        raise RunError(f'class는 "모듈:클래스" 형식이어야 함: {spec!r}')
    return getattr(importlib.import_module(module), name)


def config_id(config: dict) -> str:
    content = json.dumps({k: config.get(k) for k in CONFIG_ID_KEYS}, sort_keys=True, ensure_ascii=False)
    return hashlib.sha256(content.encode('utf-8')).hexdigest()[:8]


def git(*args):
    try:
        return subprocess.run(['git', *args], cwd=ROOT, capture_output=True, text=True, check=False).stdout.strip()
    except OSError:
        return ''


def prediction_rows(values, status, error):
    """모델 출력 7개 -> (raw, 최종 가격, 상태, 오류) 7개. run_backtest와 같은 후처리."""
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


def run_series(cls, params, seed, snap, series_id, days, log, bundles=()):
    """한 계열의 모든 기준일. 반환: [(기준일, [(raw, price, status, error) x 7])], 통계. run_backtest.run_series와 같은 규칙."""
    results, stats = [], {'refits': 0, 'fit_seconds': 0.0, 'predict_seconds': 0.0, 'timeouts': 0}
    model, fit_state, week = None, ('FIT_FAILED', 'NOT_FITTED'), None
    for d in days:
        refit_seconds = 0.0
        if d.isocalendar()[:2] != week:
            week = d.isocalendar()[:2]
            stats['refits'] += 1
            started = time.perf_counter()
            try:
                history = snap.training_data(series_id, d, bundles)
                model = cls(**params)
                model.fit(history, seed)
                fit_state = ('OK', '')
            except loader.NoInput as error:
                fit_state = ('NO_INPUT', 'TRAIN_' + str(error).split(' ')[0][:20])
                log(f'  {series_id} {d} 재학습 NO_INPUT: {error}')
            except Exception as error:  # noqa: BLE001 — 모델 오류는 기록하고 계속한다
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
            inputs = snap.origin_inputs(series_id, d, bundles)
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


def record_trial(out: Path, name, params, macro_mape, seconds, status):
    path = Path(out) / TUNING_LOG
    new = not path.exists()
    trial = len(read_trials(out)) + 1
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, 'a', encoding='utf-8', newline='') as f:
        writer = csv.writer(f, lineterminator='\n')
        if new:
            writer.writerow(TUNING_COLUMNS)
        writer.writerow([trial, name, json.dumps(params, sort_keys=True, ensure_ascii=False),
                         '' if macro_mape is None else macro_mape, round(seconds, 1), status])
    print(f'튜닝 기록 {path}에 시도 {trial} 추가({status})')
    return trial


def write_status_summary(folder: Path, seconds: float) -> dict:
    """줄인 실행(--month·--series)용: 상태별 개수와 실행 시간만 쓴다. MAPE·rMAE·naive 비교는 계산하지 않는다."""
    counts = {}
    with open(Path(folder) / 'predictions.csv', encoding='utf-8', newline='') as f:
        for row in csv.DictReader(f):
            counts[row['status']] = counts.get(row['status'], 0) + 1
    summary = {'status_counts': dict(sorted(counts.items())), 'prediction_rows': sum(counts.values()),
               'seconds': round(seconds, 1)}
    (Path(folder) / STATUS_SUMMARY).write_text(json.dumps(summary, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    return summary


def run(args) -> Path:
    user = json.loads(Path(args.config).read_text(encoding='utf-8'))
    missing = [k for k in USER_REQUIRED if k not in user]
    if missing:
        raise RunError(f'설정 파일에 필요한 항목이 없음: {missing}')
    out = Path(args.out)
    kind = pre_checks(args, out)
    folder = out / args.name
    if folder.exists():
        raise RunError(f'이미 있는 결과 폴더: {folder}')
    snap = loader.Snapshot(args.snapshot)
    days = snap.origins[args.origins]
    if args.month:
        days = [d for d in days if d.strftime('%Y-%m') == args.month]
    if not days:
        raise RunError(f'기준일이 없음: origins={args.origins}, month={args.month}')
    check_origins(days)
    series_ids = snap.series_ids
    if args.series:
        series_ids = [int(s) for s in args.series.split(',')]
        unknown = set(series_ids) - set(snap.series_ids)
        if unknown:
            raise RunError(f'스냅샷에 없는 계열: {sorted(unknown)}')
    try:
        bundles = loader.check_bundles(user['extra_features'])
    except ValueError as error:
        raise RunError(str(error)) from error
    expected_set = '+'.join((standard.BASE_FEATURE_SET, *bundles))
    if user['feature_set'] != expected_set:
        raise RunError(f'feature_set은 extra_features와 맞게 {expected_set!r}이어야 함')
    cls = load_class(user['class'])

    folder.mkdir(parents=True)  # 이 시점부터 기록이 남는다(검증 1회 규칙은 이 config.json으로 센다)
    config = {**user, 'name': args.name, 'kind': kind, 'origins': args.origins, 'month': args.month,
              'series': series_ids, 'origin_count': len(days), 'git_sha': git('rev-parse', 'HEAD') or None,
              'data_version': standard.DATA_VERSION, 'refit': standard.REFIT, 'threads': standard.THREADS}
    config['config_id'] = config_id(config)
    (folder / 'config.json').write_text(json.dumps(config, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    log_file = open(folder / 'run.log', 'w', encoding='utf-8')  # noqa: SIM115 — 끝에서 닫음

    def log(message):
        print(message)
        log_file.write(message + '\n')
        log_file.flush()

    started = time.perf_counter()
    macro, status = None, 'ERROR'
    try:
        if _CHANGED_ENV:
            log(f'환경변수를 기준서 값으로 바꿈: {sorted(_CHANGED_ENV)}')
        log(f'{args.name} kind={kind} config_id={config["config_id"]} origins={args.origins}'
            f'{" month=" + args.month if args.month else ""} 기준일 {len(days)}개 x 계열 {len(series_ids)}개')
        with open(folder / 'predictions.csv', 'w', encoding='utf-8', newline='') as f:
            writer = csv.writer(f, lineterminator='\n')
            writer.writerow(PREDICTION_COLUMNS)
            for sid in series_ids:
                s = snap.series[sid]
                t0 = time.perf_counter()
                results, stats = run_series(cls, config['params'], config['seed'], snap, sid, days, log, bundles)
                ok = 0
                for d, rows in results:
                    for h, (raw, price, st, error) in zip(standard.HORIZONS, rows):
                        ok += st == 'OK'
                        writer.writerow([args.name, sid, s.item, s.market, d.isoformat(),
                                         (d + timedelta(days=h)).isoformat(), h, raw, price, st, error])
                log(f'계열 {sid:>5} {s.item} {s.market:9} 재학습 {stats["refits"]}회 {stats["fit_seconds"]:.1f}s '
                    f'예측 {stats["predict_seconds"]:.1f}s OK {ok}/{len(results) * len(standard.HORIZONS)} '
                    f'({time.perf_counter() - t0:.1f}s)')
        if kind == 'smoke':  # 줄인 실행은 정확도 지표를 만들지도 보이지도 않는다(예산 우회 방지)
            summary = write_status_summary(folder, time.perf_counter() - started)
            log(f'상태 집계 {json.dumps(summary["status_counts"], sort_keys=True)} (정확도 지표는 계산하지 않음)')
            status = 'SMOKE'
        else:
            metrics, digest = score.write_metrics(folder, snap)
            score.print_metrics(metrics)
            log(f'metrics SHA-256 {digest}')
            policy = metrics['results']['policy']
            macro = policy.get('macro_mape')
            status = 'OK' if metrics['success_rate'] >= standard.ADOPTION['min_success_rate'] else 'LOW_SUCCESS'
    except Exception as error:  # noqa: BLE001 — 실패한 시도도 기록해야 한다
        log(f'실행 실패: {type(error).__name__}: {error}')
        log(traceback.format_exc(limit=5))
        raise
    finally:
        seconds = time.perf_counter() - started
        log(f'총 {seconds:.1f}s')
        log_file.close()
        if kind == 'tune_trial':
            record_trial(out, args.name, config['params'], macro, seconds, status)
    return folder


def main(argv=None):
    parser = argparse.ArgumentParser(description='구조적 가격 전달 모델 자체 실행기(PRD §11)')
    parser.add_argument('--config', required=True, type=Path, help='모델 설정 JSON')
    parser.add_argument('--name', required=True, help='실행 이름(결과 폴더 이름). runs/struct/<name>')
    parser.add_argument('--origins', required=True, choices=('tune', 'validation'), help='기준일 목록(시험 목록은 없음)')
    parser.add_argument('--month', help='YYYY-MM. 그 달 기준일만(점검)')
    parser.add_argument('--series', help='계열 id 쉼표 목록(점검)')
    parser.add_argument('--snapshot', type=Path, default=DEFAULT_SNAPSHOT)
    parser.add_argument('--out', type=Path, default=DEFAULT_OUT)
    parser.add_argument('--record-trial', action='store_true', help='튜닝 시도로 runs/struct/tuning_log.csv에 기록')
    args = parser.parse_args(argv)
    try:
        folder = run(args)
    except (RunError, FileNotFoundError, ValueError) as error:
        print(f'실패: {error}', file=sys.stderr)
        return 1
    except Exception as error:  # noqa: BLE001 — 실행 중 오류(시도는 이미 기록됨)
        print(f'실패: {type(error).__name__}: {error}', file=sys.stderr)
        return 1
    print(f'결과: {folder}')
    return 0


if __name__ == '__main__':
    sys.exit(main())
