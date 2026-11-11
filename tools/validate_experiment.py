"""실험 결과 폴더가 기준서 §10 제출 형식과 고정값을 지키는지 검사한다.

    python -m tools.validate_experiment experiments/xgb-p1-20261116-01
    python -m tools.validate_experiment --all          # experiments/ 아래 전부 + 기준서 파일 확인

오류가 하나라도 있으면 종료 코드 1. CI(.github/workflows/standard.yml)가 PR마다 --all로 실행한다.
경고는 실패로 치지 않지만 결과 보고서에 적어야 하는 것들이다.
"""
import argparse
import csv
import json
import math
import sys
from collections import Counter
from datetime import date, timedelta
from pathlib import Path

from tools import standard

ROOT = Path(__file__).resolve().parent.parent
EXPERIMENTS = ROOT / 'experiments'

PARAM_RULES = {
    'XGBoost': {'tree_method': 'hist', 'n_jobs': standard.THREADS},
    'LightGBM': {'deterministic': True, 'force_row_wise': True, 'num_threads': standard.THREADS},
    'AutoARIMA': {'n_jobs': 1},
}


def round_half_up(value: float) -> int:
    return max(1, math.floor(value + 0.5))


class Report:
    def __init__(self, name):
        self.name, self.errors, self.warnings = name, [], []

    def error(self, message):
        self.errors.append(message)

    def warn(self, message):
        self.warnings.append(message)

    def print(self):
        mark = 'OK' if not self.errors else 'FAIL'
        print(f'[{mark}] {self.name}')
        for message in self.errors:
            print(f'   오류: {message}')
        for message in self.warnings:
            print(f'   경고: {message}')


def check_config(config, folder, report):
    missing = [key for key in standard.CONFIG_REQUIRED if key not in config]
    if missing:
        report.error(f'config.json 필수 항목 없음: {missing}')
    match = standard.EXPERIMENT_ID.match(str(config.get('experiment_id', '')))
    if not match:
        report.error(f'experiment_id 형식 오류: {config.get("experiment_id")!r} (예: xgb-p1-20261116-01)')
        return None
    if config['experiment_id'] != folder.name:
        report.error(f'폴더 이름({folder.name})과 experiment_id({config["experiment_id"]})가 다름')
    prefix, phase = match['model'], match['phase']
    if config.get('standard_version') != standard.STANDARD_VERSION:
        report.error(f'standard_version은 {standard.STANDARD_VERSION!r}이어야 함: {config.get("standard_version")!r}')
    if config.get('data_version') != standard.DATA_VERSION:
        report.error(f'data_version은 {standard.DATA_VERSION!r}이어야 함: {config.get("data_version")!r}')
    if config.get('phase') != phase:
        report.error(f'phase({config.get("phase")})가 experiment_id의 단계({phase})와 다름')
    if config.get('origins') != standard.ORIGIN_SETS[phase]:
        report.error(f'{phase} 단계의 origins는 {standard.ORIGIN_SETS[phase]!r}이어야 함: {config.get("origins")!r}')
    if prefix in standard.MODELS:
        model, owner = standard.MODELS[prefix]
        if config.get('model') != model:
            report.error(f'접두어 {prefix}의 model은 {model!r}이어야 함: {config.get("model")!r}')
        if config.get('owner') != owner:
            report.warn(f'담당 표기가 기준서({owner})와 다름: {config.get("owner")!r}')
    if config.get('refit') != standard.REFIT:
        report.error(f'refit은 {standard.REFIT!r}이어야 함(주 1회 재학습): {config.get("refit")!r}')
    runtime = config.get('runtime') or {}
    if runtime.get('threads') != standard.THREADS:
        report.error(f'runtime.threads는 {standard.THREADS}이어야 함: {runtime.get("threads")!r}')
    if phase == 'test' and runtime.get('where') != 'docker':
        report.error('최종 시험(test)은 Docker에서 실행해야 함(runtime.where = "docker", 기준서 §1.3)')
    if not isinstance(config.get('seed'), int):
        report.error('seed는 정수여야 함')
    params = config.get('params') or {}
    for key, expected in PARAM_RULES.get(config.get('model'), {}).items():
        if params.get(key) != expected:
            report.error(f'{config.get("model")} 결정적 실행 옵션 {key}={expected!r} 필요: {params.get(key)!r}')
    if config.get('model') == 'Ridge' and params.get('solver') in (None, 'auto'):
        report.error("Ridge는 solver를 명시해야 함('auto' 금지)")
    extra = config.get('extra_features') or []
    if extra:
        unknown = [b for b in extra if b not in standard.EXTRA_BUNDLES]
        if unknown:
            report.error(f'모르는 외부변수 묶음 {unknown}. 가능: {list(standard.EXTRA_BUNDLES)}(§5.2)')
        expected_set = '+'.join([standard.BASE_FEATURE_SET] + [b for b in standard.EXTRA_BUNDLES if b in extra])
        if config.get('feature_set') != expected_set:
            report.error(f'feature_set은 extra_features와 맞게 {expected_set!r}이어야 함')
        if phase == 'p1':
            report.warn('기본 특징 세트 밖의 특징 사용: 1차 순위에는 기본 세트 결과만 쓴다(§5.1)')
        if config.get('model') == 'AutoARIMA' and set(extra) - {'EVENT'}:
            report.error('AutoARIMA 2차는 EVENT 묶음만 쓸 수 있음(§5.2)')
    elif config.get('feature_set') != standard.BASE_FEATURE_SET:
        report.error(f'extra_features가 없으면 feature_set은 {standard.BASE_FEATURE_SET!r}이어야 함')
    if '-pooled-' in config['experiment_id']:
        report.warn('통합(pooled) 모델: 1차 순위에 넣지 않는다(§3.5)')
    return phase


def check_tuning(config, phase, folder, report):
    path = folder / 'tuning_log.csv'
    if not path.exists():
        return
    with path.open(encoding='utf-8', newline='') as handle:
        reader = csv.DictReader(handle)
        if tuple(reader.fieldnames or ()) != standard.TUNING_COLUMNS:
            report.error(f'tuning_log.csv 열은 {standard.TUNING_COLUMNS}이어야 함: {reader.fieldnames}')
            return
        trials = list(reader)
    budget = standard.TUNING_BUDGET.get(phase)
    if budget and len(trials) > budget['trials']:
        report.error(f'{phase} 튜닝 시도 {len(trials)}회 > 상한 {budget["trials"]}회(§6)')
    tuning = config.get('tuning') or {}
    if budget and tuning.get('trials_used', 0) > budget['trials']:
        report.error(f'config.tuning.trials_used {tuning.get("trials_used")} > 상한 {budget["trials"]}')
    if phase == 'p1' and tuning.get('seconds_used', 0) > budget['seconds']:
        report.warn(f'튜닝 누적 {tuning["seconds_used"]}초 > 권장 상한 {budget["seconds"]}초(§6, 각자 장비 기준)')
    if phase == 'p2' and tuning.get('seconds_used', 0) > budget['seconds']:
        report.error(f'2차 튜닝 누적 {tuning["seconds_used"]}초 > 상한 {budget["seconds"]}초(§6)')
    if phase == 'test' and trials:
        report.error('최종 시험 중에는 튜닝할 수 없음(§0, §7.2)')


def check_predictions(config, phase, folder, report):
    path = folder / 'predictions.csv'
    start, end = standard.phase_window(phase)
    with path.open(encoding='utf-8', newline='') as handle:
        reader = csv.DictReader(handle)
        if tuple(reader.fieldnames or ()) != standard.PREDICTION_COLUMNS:
            report.error(f'predictions.csv 열은 {standard.PREDICTION_COLUMNS}이어야 함: {reader.fieldnames}')
            return
        rows = list(reader)
    if not rows:
        report.error('predictions.csv가 비어 있음')
        return
    keys, per_origin, statuses, bad_dates = set(), Counter(), Counter(), []
    for number, row in enumerate(rows, start=2):
        where = f'{number}행'
        if row['experiment_id'] != config['experiment_id'] or row['data_version'] != standard.DATA_VERSION:
            report.error(f'{where}: experiment_id·data_version이 config와 다름')
            break
        try:
            origin, target, horizon = date.fromisoformat(row['origin_date']), date.fromisoformat(row['target_date']), int(row['horizon'])
        except ValueError:
            report.error(f'{where}: 날짜·시점 형식 오류')
            break
        if horizon not in standard.HORIZONS or target != origin + timedelta(days=horizon):
            report.error(f'{where}: horizon은 1~7이고 target_date = origin_date + horizon이어야 함')
            break
        if not (start <= origin <= end):
            bad_dates.append(origin)
        key = (row['series_id'], origin, horizon)
        if key in keys:
            report.error(f'{where}: (series_id, origin_date, horizon) 중복 {key}')
            break
        keys.add(key)
        per_origin[(row['series_id'], origin)] += 1
        status = row['status']
        statuses[status] += 1
        if status not in standard.STATUSES:
            report.error(f'{where}: 알 수 없는 status {status!r}')
            break
        if status == 'OK':
            try:
                raw, final = float(row['predicted_price_raw']), int(row['predicted_price'])
            except ValueError:
                report.error(f'{where}: OK 행에는 predicted_price_raw(실수)·predicted_price(정수)가 있어야 함')
                break
            if not math.isfinite(raw) or raw <= 0:
                report.error(f'{where}: 원시 예측이 NaN·무한·0 이하면 INVALID_VALUE로 기록해야 함(§8.3)')
                break
            if final != round_half_up(raw):
                report.error(f'{where}: predicted_price는 round(raw)(0.5 올림, 최소 1)여야 함: {raw} → {final}')
                break
        elif row['predicted_price']:
            report.error(f'{where}: 실패 행({status})의 predicted_price는 비워야 함')
            break
    if bad_dates:
        report.error(f'{phase} 단계에서 허용되지 않은 기준일 {len(bad_dates)}개(예: {min(bad_dates)}). '
                     f'허용 구간 {start} ~ {end}. 최종 시험 기준일은 test 단계에서만 쓸 수 있음(§7.2)')
    incomplete = [k for k, count in per_origin.items() if count != len(standard.HORIZONS)]
    if incomplete:
        report.error(f'(계열, 기준일)마다 7행이 있어야 함. 부족한 묶음 {len(incomplete)}개(예: {incomplete[0]})')
    series = {k[0] for k in per_origin}
    origins_per_series = Counter(k[0] for k in per_origin)
    if len(set(origins_per_series.values())) > 1:
        report.error(f'계열마다 기준일 수가 달라 N × 기준일 × 7 행 수가 맞지 않음: {dict(origins_per_series)}')
    if phase != 'smoke' and len(series) != standard.DEFAULT_SERIES_COUNT:
        report.warn(f'계열 수 {len(series)}개(기본 N={standard.DEFAULT_SERIES_COUNT}). manifest의 N과 같은지 확인')
    # 채택 기준 4번의 성공률은 평가 대상(정답·naive가 있는 점) 기준이라 evaluate가 metrics.json에 낸 값을 본다.
    # 행 기준 비율은 정답이 없는 날(원천 결측 구간)의 NO_INPUT까지 포함해 더 낮게 나온다.
    rate = None
    try:
        rate = json.loads((folder / 'metrics.json').read_text(encoding='utf-8')).get('success_rate')
    except (OSError, ValueError, AttributeError):
        pass
    if rate is None:
        total = sum(statuses.values())
        rate = statuses['OK'] / total if total else None
    if rate is not None and rate < standard.ADOPTION['min_success_rate']:
        report.warn(f'성공률 {rate:.2%} < 99% → 채택 기준 4번 미달(§8.4)')


def validate(folder: Path) -> Report:
    report = Report(folder.name)
    missing = [name for name in standard.EXPERIMENT_FILES if not (folder / name).exists()]
    if missing:
        report.error(f'필수 파일 없음: {missing}')
    try:
        config = json.loads((folder / 'config.json').read_text(encoding='utf-8'))
    except (OSError, ValueError) as error:
        report.error(f'config.json을 읽을 수 없음: {type(error).__name__}')
        return report
    phase = check_config(config, folder, report)
    if phase is None:
        return report
    check_tuning(config, phase, folder, report)
    if (folder / 'predictions.csv').exists():
        check_predictions(config, phase, folder, report)
    if (folder / 'metrics.json').exists():
        try:
            json.loads((folder / 'metrics.json').read_text(encoding='utf-8'))
        except ValueError:
            report.error('metrics.json이 JSON이 아님')
    if (folder / 'environment.txt').exists() and not (folder / 'environment.txt').read_text(encoding='utf-8').strip():
        report.error('environment.txt가 비어 있음(git SHA·uv pip freeze 등 §10.4)')
    for secret in ('.env', 'model/.env'):
        if (folder / secret).exists():
            report.error(f'{secret}를 결과 폴더에 넣으면 안 됨(§1.3)')
    return report


def check_standard_file() -> Report:
    report = Report(standard.STANDARD_FILE)
    path = ROOT / standard.STANDARD_FILE
    if not path.exists():
        report.error(f'{standard.STANDARD_FILE}이 없음. 기준서를 옮기거나 지웠다면 tools/standard.py의 STANDARD_FILE도 함께 바꿔야 함')
        return report
    head = path.read_text(encoding='utf-8')[:300]
    if f'기준서 {standard.STANDARD_VERSION}' not in head:
        report.error(f'기준서 제목의 판({head.splitlines()[0]!r})이 tools/standard.py의 '
                     f'STANDARD_VERSION={standard.STANDARD_VERSION!r}와 다름. 둘을 같은 PR에서 함께 바꿔야 함')
    return report


def main(argv=None):
    parser = argparse.ArgumentParser(description='실험 결과 폴더의 기준서 준수 검사')
    parser.add_argument('folders', nargs='*', type=Path)
    parser.add_argument('--all', action='store_true', help='experiments/ 아래 모든 실험 + 기준서 파일')
    args = parser.parse_args(argv)
    reports = []
    if args.all:
        reports.append(check_standard_file())
        folders = sorted(p for p in EXPERIMENTS.iterdir() if p.is_dir()) if EXPERIMENTS.exists() else []
    else:
        folders = args.folders
    if not args.all and not folders:
        parser.error('검사할 실험 폴더를 주거나 --all을 쓰세요')
    reports += [validate(folder) for folder in folders]
    for report in reports:
        report.print()
    failed = [r for r in reports if r.errors]
    print(f'검사 {len(reports)}개, 실패 {len(failed)}개')
    return 1 if failed else 0


if __name__ == '__main__':
    sys.exit(main())
