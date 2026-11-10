"""스냅샷(기준서 §2.2) 파일 형식과 공통 계산. export_snapshot과 check_snapshot이 함께 쓴다."""
import csv
import hashlib
from collections import Counter
from datetime import date
from pathlib import Path

from tools import origins, standard

MANIFEST = 'manifest.json'
FORMAT_VERSION = 1

# 파일 이름 → 열. 순서·이름은 기준서 §2.2 표를 따른다.
COLUMNS = {
    'price_series.csv': ('series_id', 'item', 'market', 'item_code', 'kind_code', 'rank_code', 'unit_quantity', 'unit',
                         'source_series_ids'),
    'price_daily.csv': ('series_id', 'price_date', 'price'),
    'price_daily_kind.csv': ('merged_series_id', 'source_series_id', 'kind_code', 'price_date', 'price'),
    'price_daily_merged.csv': ('series_id', 'price_date', 'price', 'kind_code', 'source_series_id', 'kind_switch'),
    'calendar_day.csv': ('cal_date', 'day_of_week', 'is_holiday', 'holiday_name', 'lunar_month', 'lunar_day',
                         'is_lunar_leap', 'is_market_closed'),
    'calendar_event.csv': ('event_code', 'name', 'start_date', 'end_date', 'effect_start_date', 'effect_end_date'),
    'weather_daily.csv': ('weather_date', 'avg_temp', 'max_temp', 'min_temp', 'precipitation', 'avg_humidity',
                          'sunshine_hours', 'heat_station_ratio', 'heavy_rain_station_ratio', 'cold_station_ratio',
                          'station_count'),
    'exchange_rate_daily.csv': ('rate_date', 'currency_code', 'rate', 'unit_label'),
    'item_production.csv': ('item', 'year', 'production_ton', 'published_from'),
    'origins_validation.csv': ('origin_date',),
    'origins_tune.csv': ('origin_date',),
    'origins_test.csv': ('origin_date',),
}
# 날짜가 마감일을 넘으면 안 되는 열(관측 자료). 달력·명절은 미리 확정된 정보라 제외.
OBSERVATION_DATE = {'price_daily.csv': 'price_date', 'price_daily_kind.csv': 'price_date',
                    'price_daily_merged.csv': 'price_date', 'weather_daily.csv': 'weather_date',
                    'exchange_rate_daily.csv': 'rate_date', 'item_production.csv': 'published_from'}
DIRECT_ITEMS = ('대파', '양파', '깐마늘')
MERGED_ID = {value: key for key, value in standard.MERGED_SERIES.items()}  # (품목, 시장) → 9001 …
QUALITY_FROM = date(2023, 1, 1)
FIRST_OBSERVED_BY = date(2019, 11, 1)
FIRST_OBSERVED_LATEST = date(2023, 1, 31)
MIN_COVERAGE = 0.90
# 실험 품목 → KOSIS 생산량 키(§2.2 생산량 품목 매핑)
PRODUCTION_KEY = {'대파': '대파', '양파': '양파', '깐마늘': '마늘', '배추': '배추', '무': '무'}


def cell(value) -> str:
    if value is None:
        return ''
    if isinstance(value, bool):
        return 'true' if value else 'false'
    if isinstance(value, date):
        return value.isoformat()
    text = str(value)
    if '.' in text and text.replace('-', '', 1).replace('.', '', 1).isdigit():
        text = text.rstrip('0').rstrip('.')  # Decimal('12.50') → 12.5, OS·드라이버와 무관하게 같은 글자
    return text


def write_csv(path: Path, name: str, rows) -> int:
    """UTF-8(BOM 없음), LF 줄바꿈으로 쓴다. 같은 내용이면 Windows·Linux에서 SHA-256이 같다."""
    with open(path / name, 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f, lineterminator='\n')
        writer.writerow(COLUMNS[name])
        count = 0
        for row in rows:
            if len(row) != len(COLUMNS[name]):
                raise ValueError(f'{name}: 열 수가 다름 {row!r}')
            writer.writerow([cell(v) for v in row])
            count += 1
    return count


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with open(path, 'rb') as f:
        for chunk in iter(lambda: f.read(1 << 20), b''):
            digest.update(chunk)
    return digest.hexdigest()


def count_rows(path: Path) -> int:
    with open(path, encoding='utf-8', newline='') as f:
        return sum(1 for _ in csv.reader(f)) - 1


def missing_runs(observed: set, survey_days, start: date, end: date, longer_than=standard.MAX_STALE_DAYS):
    """[start, end] 조사일 중 연속 결측이 longer_than 조사일을 넘는 구간 [(첫 결측일, 마지막 결측일, 길이)]."""
    runs, first, last, length = [], None, None, 0
    for day in survey_days:
        if not (start <= day <= end):
            continue
        if day in observed:
            if length > longer_than:
                runs.append((first.isoformat(), last.isoformat(), length))
            length = 0
        else:
            if length == 0:
                first = day
            last, length = day, length + 1
    if length > longer_than:
        runs.append((first.isoformat(), last.isoformat(), length))
    return runs


def series_quality(days: set, survey_days, cutoff: date) -> dict:
    """기준서 §2.1 계열 품질 기준. status: PASS, REVIEW(팀 결정 필요), FAIL."""
    first, last = min(days), max(days)
    window = [d for d in survey_days if QUALITY_FROM <= d <= cutoff]
    coverage = sum(d in days for d in window) / len(window) if window else 0.0
    runs = missing_runs(days, survey_days, QUALITY_FROM, cutoff)
    before = missing_runs(days, survey_days, first, date(QUALITY_FROM.year - 1, 12, 31))
    problems, review = [], []
    if first > FIRST_OBSERVED_LATEST:
        problems.append(f'첫 관측일 {first}이 {FIRST_OBSERVED_LATEST} 이후')
    elif first > FIRST_OBSERVED_BY:
        review.append(f'첫 관측일 {first}이 {FIRST_OBSERVED_BY} 이후(허용, 실제 학습 시작일 기록)')
    if coverage < MIN_COVERAGE:
        problems.append(f'{QUALITY_FROM.year}~ 관측 비율 {coverage:.1%} < {MIN_COVERAGE:.0%}')
    if runs:
        review.append(f'{QUALITY_FROM.year}~ {standard.MAX_STALE_DAYS}조사일 넘는 연속 결측 {len(runs)}구간')
    status = 'FAIL' if problems else 'REVIEW' if review else 'PASS'
    return {'first_date': first.isoformat(), 'last_date': last.isoformat(), 'observations': len(days),
            'coverage_from_2023': round(coverage, 4), 'missing_runs_from_2023': runs,
            'missing_runs_before_2023': before, 'status': status, 'notes': problems + review}


def monthly_counts(days) -> dict:
    counts = Counter(d.strftime('%Y-%m') for d in days)
    return dict(sorted(counts.items()))


def origin_lists(calendar):
    built = origins.build(calendar)
    return {f'origins_{name}.csv': built[name] for name in ('validation', 'tune', 'test')}


def merged_rows_for_csv(merged: dict) -> list:
    return [(sid, r.price_date, r.price, r.kind_code, r.source_series_id, r.kind_switch)
            for sid, rows in sorted(merged.items()) for r in rows]

