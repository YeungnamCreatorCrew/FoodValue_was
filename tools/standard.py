"""「가격 예측 모델 비교 실험 기준서 v1」(model_comparison/MODEL_TRAINING_STANDARD.md)의 고정값.

이 파일의 값은 기준서와 같아야 한다. 기준서를 바꾸면(v2) 이 파일도 같은 PR에서 바꾸고 STANDARD_VERSION을 올린다.
모든 공통 도구(loader·run_backtest·evaluate·check_snapshot)와 실험 검사기(validate_experiment)는
여기서 값을 가져다 쓴다. 숫자를 코드 곳곳에 직접 쓰지 않는다.
"""
import re
from datetime import date

STANDARD_VERSION = 'v1'
STANDARD_FILE = 'model_comparison/MODEL_TRAINING_STANDARD.md'

# §0, §2 데이터
DATA_VERSION = 'fv-snap-20261031-v1'
COLLECT_START = date(2016, 1, 1)
DATA_CUTOFF = date(2026, 10, 31)
TIMEZONE = 'Asia/Seoul'

# §2.1, §2.2 계열. 배추·무는 작형별 원본을 이어 붙인 가상 계열(§2.3)
ITEMS = ('대파', '양파', '깐마늘', '배추', '무')
MERGED_SERIES = {9001: ('배추', 'RETAIL'), 9002: ('배추', 'WHOLESALE'),
                 9011: ('무', 'RETAIL'), 9012: ('무', 'WHOLESALE')}
KIND_CYCLE = ('06', '01', '02', '03')  # 월동 → 봄 → 고랭지 → 가을 → 월동
KIND_PRIORITY_BY_MONTH = {12: '06', 1: '06', 2: '06', 3: '06', 4: '06', 5: '01', 6: '01',
                          7: '02', 8: '02', 9: '02', 10: '03', 11: '03'}
KIND_SWITCH_RUN = 3  # 다음 작형이 3 조사일 연속이면 전환
KIND_RESTART_GAP = 10  # 현재 작형이 10 조사일 연속 없으면 재시작
DEFAULT_SERIES_COUNT = 10

# §3 과제·기준일
HORIZONS = tuple(range(1, 8))
TRAIN_WINDOW_DAYS = 1825
MIN_TRAIN_OBSERVATIONS = 400
MAX_STALE_DAYS = 7
VALIDATION = (date(2024, 11, 1), date(2025, 10, 31))
GAP = (date(2025, 11, 1), date(2025, 11, 9))
TEST = (date(2025, 11, 10), date(2026, 10, 23))

# §1, §6 실행·재현성
THREADS = 4
THREAD_ENV = {'TZ': TIMEZONE, 'OMP_NUM_THREADS': str(THREADS), 'OPENBLAS_NUM_THREADS': str(THREADS),
              'MKL_NUM_THREADS': str(THREADS), 'PYTHONHASHSEED': '0'}
DEFAULT_SEED = 42
REPEAT_SEEDS = (42, 43, 44)
TUNING_BUDGET = {'p1': {'trials': 40, 'seconds': 3 * 3600}, 'p2': {'trials': 10, 'seconds': 3600}}
REFIT = 'weekly_first_origin'
TIMEOUT_SECONDS = {'refit': 600, 'predict': 60}

# 담당·모델 (기준서 머리말 표)
MODELS = {'xgb': ('XGBoost', 'A'), 'lgbm': ('LightGBM', 'B'), 'arima': ('AutoARIMA', 'C'), 'ridge': ('Ridge', 'D')}
BASELINE_PREFIX = 'base'

# §10 제출 형식
PHASES = ('smoke', 'p1', 'p2', 'focus', 'test')
ORIGIN_SETS = {'smoke': 'validation', 'p1': 'validation', 'p2': 'validation', 'focus': 'validation', 'test': 'test'}
EXPERIMENT_ID = re.compile(r'^(?P<model>xgb|lgbm|arima|ridge|base)-(?:pooled-)?(?P<phase>smoke|p1|p2|focus|test)-(?P<day>\d{8})-(?P<seq>\d{2})$')
EXPERIMENT_FILES = ('config.json', 'predictions.csv', 'metrics.json', 'environment.txt', 'run.log', 'tuning_log.csv')
CONFIG_REQUIRED = ('experiment_id', 'model', 'owner', 'standard_version', 'git_sha', 'data_version', 'phase', 'origins',
                   'feature_set', 'extra_features', 'target_transform', 'strategy', 'refit', 'params', 'seed', 'runtime',
                   'tuning')
PREDICTION_COLUMNS = ('experiment_id', 'model', 'config_id', 'data_version', 'series_id', 'item_id', 'market',
                      'origin_date', 'target_date', 'horizon', 'predicted_price_raw', 'predicted_price', 'status',
                      'error_code')
STATUSES = ('OK', 'NO_INPUT', 'FIT_FAILED', 'PREDICT_FAILED', 'INVALID_VALUE', 'TIMEOUT')
TUNING_COLUMNS = ('trial', 'config_id', 'params', 'macro_mape', 'seconds', 'status')
BASE_FEATURE_SET = 'base_v1'

# §8.4 채택 기준
ADOPTION = {'min_relative_improvement_pct': 5.0, 'max_macro_rmae': 1.0, 'min_success_rate': 0.99,
            'max_train_seconds_per_series': 30 * 60, 'max_memory_gb': 4, 'tie_relative': 0.02}
SIMPLICITY_ORDER = ('Ridge', 'AutoARIMA', 'LightGBM', 'XGBoost')


def majority(n: int) -> int:
    """계열 승률 과반: floor(N/2) + 1."""
    return n // 2 + 1


def phase_window(phase: str):
    """단계가 쓸 수 있는 기준일 구간. 최종 시험 기준일은 phase='test'만 쓸 수 있다(§7.2)."""
    if phase not in PHASES:
        raise ValueError(f'알 수 없는 단계: {phase}. 가능: {PHASES}')
    return TEST if phase == 'test' else VALIDATION
