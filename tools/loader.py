"""공통 로더(기준서 §9): 스냅샷 읽기, 배추·무 작형 이어 붙이기(§2.3), 기준일 시점 자료와 1차 특징(§3.1, §5.1).

이어 붙이기 함수는 이 파일의 `merge_kinds` 하나만 쓴다. 스냅샷 내보내기와 `check_snapshot`이 이 함수로
`price_daily_merged.csv`를 만들고 다시 계산한다. 로더·평가기는 그 결과 파일을 읽고, 학습 창이나 기준일에 맞춰
다시 계산하지 않는다.

시점 자료·특징: `Snapshot.training_data()`·`origin_inputs()`·`load_as_of()`(§3.1, §5.1). 실행기(run_backtest)만 부른다.
"""
import csv
import json
import math
from collections import Counter
from dataclasses import dataclass
from datetime import date, timedelta
from pathlib import Path

from tools import standard


@dataclass(frozen=True)
class MergedRow:
    price_date: date
    price: int
    kind_code: str
    source_series_id: int
    kind_switch: int


def next_kind(kind: str) -> str:
    cycle = standard.KIND_CYCLE
    return cycle[(cycle.index(kind) + 1) % len(cycle)]


def _start_kind(observed, month: int) -> str:
    """규칙 1: 그 달 우선 작형, 없으면 순환 순서상 우선 작형 다음으로 가장 가까운 관측 작형."""
    cycle = standard.KIND_CYCLE
    first = cycle.index(standard.KIND_PRIORITY_BY_MONTH[month])
    for step in range(len(cycle)):
        kind = cycle[(first + step) % len(cycle)]
        if kind in observed:
            return kind
    raise ValueError('관측된 작형이 없음')


def merge_kinds(observations, survey_days) -> list[MergedRow]:
    """한 계열(품목 × 시장)의 작형별 관측을 기준서 §2.3 규칙으로 이어 붙인다.

    observations: (price_date, kind_code, price, source_series_id) 묶음
    survey_days: KAMIS 조사일(calendar_day.is_market_closed = false) 목록
    반환: 값이 있는 날만, 날짜순. 조사일이 아닌 날의 관측은 쓰지 않는다.
    """
    by_day: dict[date, dict[str, tuple[int, int]]] = {}
    for day, kind, price, source in observations:
        if kind not in standard.KIND_CYCLE:
            raise ValueError(f'알 수 없는 작형 코드 {kind!r}')
        by_day.setdefault(day, {})[kind] = (int(price), int(source))
    if not by_day:
        return []
    first = min(by_day)
    current = previous = None
    streak = Counter()
    missing = 0
    restart = True
    rows = []
    for day in sorted(survey_days):
        if day < first:
            continue
        observed = by_day.get(day, {})
        switched = 0
        if restart:
            if not observed:
                continue
            chosen = _start_kind(observed, day.month)
            switched = int(current is not None and chosen != current)
            current, previous, missing, restart = chosen, None, 0, False
            streak.clear()
        else:
            for kind in standard.KIND_CYCLE:
                streak[kind] = streak[kind] + 1 if kind in observed else 0
            priority = standard.KIND_PRIORITY_BY_MONTH[day.month]
            candidates = {next_kind(current), priority} - {current, previous}
            ready = sorted(k for k in candidates if streak[k] >= standard.KIND_SWITCH_RUN)
            if ready:
                chosen = priority if priority in ready else ready[0]
                previous, current, switched, missing = current, chosen, 1, 0
                streak.clear()
        if current in observed:
            missing = 0
            price, source = observed[current]
            rows.append(MergedRow(day, price, current, source, switched))
        else:
            missing += 1
            if missing >= standard.KIND_RESTART_GAP:
                restart = True
    return rows


def switch_summary(rows):
    """manifest용: 전환일 목록과 연도별 전환 횟수."""
    switches = [(r.price_date.isoformat(), r.kind_code) for r in rows if r.kind_switch]
    per_year = Counter(day[:4] for day, _ in switches)
    return {'switches': switches, 'per_year': dict(sorted(per_year.items()))}


def read_table(snapshot: Path, name: str) -> list[dict]:
    """스냅샷 CSV 하나를 dict 행 목록으로 읽는다(값은 문자열)."""
    with open(Path(snapshot) / name, encoding='utf-8', newline='') as f:
        return list(csv.DictReader(f))


def read_calendar(snapshot: Path):
    return [(date.fromisoformat(r['cal_date']), r['is_market_closed'] == 'true')
            for r in read_table(snapshot, 'calendar_day.csv')]


def merge_from_kind_table(kind_rows, calendar) -> dict[int, list[MergedRow]]:
    """price_daily_kind.csv 행 → {가상 계열 id: 이어 붙인 행}."""
    survey = [day for day, closed in calendar if not closed]
    grouped: dict[int, list] = {}
    for r in kind_rows:
        grouped.setdefault(int(r['merged_series_id']), []).append(
            (date.fromisoformat(r['price_date']), r['kind_code'], int(r['price']), int(r['source_series_id'])))
    return {sid: merge_kinds(obs, survey) for sid, obs in sorted(grouped.items())}


# ---- 기준일 시점 자료(§3.1)와 1차 특징(§5.1) ------------------------------------------------------------
#
# 모든 모델은 아래 Snapshot.training_data()·origin_inputs()로만 입력을 받는다. 특징은 계열마다 한 번 계산해 두지만,
# 각 행은 그 기준일까지의 값만 쓰고(시점 규칙), 학습 표본은 목표일 ≤ 재학습 기준일만 고르므로 미래 정보가 들어가지 않는다.
# numpy는 prices 의존성에만 있어 함수 안에서 불러온다(check_snapshot은 numpy 없이 돈다).

def _np():
    import numpy
    return numpy


class NoInput(Exception):
    """기준서 §1·§3.1의 NO_INPUT: 학습 관측 400개 미만, 최신 관측이 7일보다 오래됨, v[d-28..d]에 빈 값."""


@dataclass
class Series:
    series_id: int
    item: str
    market: str
    start: date  # 첫 실제 관측일. 배열 i번째 = start + i일
    actual: object  # 실제 관측 가격(없으면 nan)
    filled: object  # 앞채움(최대 7일) 가격 v
    age: object  # price_age = i − 최신 실제 관측 위치(관측 전이면 큰 수)
    valid: object  # v[i-28..i]에 빈 값이 없음
    base: object  # 시점과 무관한 특징 행렬(BASE_FEATURES 중 h·목표일 무관 항목)
    kind: object | None  # 배추·무: 그날 선택 작형(없으면 None)

    def index(self, day: date) -> int:
        return (day - self.start).days

    def day(self, i: int) -> date:
        return self.start + timedelta(days=int(i))


_BASE_COLUMNS = ('current', 'lag1', 'lag7', 'lag14', 'lag28', 'mean7', 'mean28', 'change7', 'volatility7', 'price_age',
                 'days_since_kind_switch')


def _build_series(series_id, item, market, observations, switches, kinds, end: date) -> Series:
    """observations: {날짜: 가격}. switches: 작형 전환일 집합. kinds: {날짜: 작형}(배추·무)."""
    np = _np()
    start = min(observations)
    n = (end - start).days + 1
    actual = np.full(n, np.nan)
    for day, price in observations.items():
        actual[(day - start).days] = price
    idx = np.arange(n)
    last = np.where(~np.isnan(actual), idx, -1)
    last = np.maximum.accumulate(last)
    age = np.where(last >= 0, idx - last, 10 ** 6)
    filled = np.where(age <= standard.FORWARD_FILL_DAYS, actual[np.maximum(last, 0)], np.nan)

    def shift(values, k):
        out = np.full(n, np.nan)
        out[k:] = values[:n - k]
        return out

    look = standard.FEATURE_LOOKBACK_DAYS
    window = np.lib.stride_tricks.sliding_window_view
    pad = np.concatenate([np.full(look, np.nan), filled])
    last29 = window(pad, look + 1)  # 행 i = v[i-28..i]
    valid = ~np.isnan(last29).any(axis=1)
    recent, long = last29[:, -7:], last29[:, -28:]
    with np.errstate(invalid='ignore', divide='ignore'):
        mean7, mean28 = recent.mean(axis=1), long.mean(axis=1)
        volatility7 = recent.std(axis=1)  # 모표준편차(ddof=0), 가격 수준
        lag7 = shift(filled, 7)
        change7 = filled / lag7 - 1
    since = np.full(n, float(standard.KIND_SWITCH_CAP_DAYS))
    if switches:
        last_switch = np.full(n, -1)
        for day in switches:
            last_switch[(day - start).days] = (day - start).days
        last_switch = np.maximum.accumulate(last_switch)
        since = np.where(last_switch >= 0, np.minimum(idx - last_switch, standard.KIND_SWITCH_CAP_DAYS),
                         standard.KIND_SWITCH_CAP_DAYS).astype(float)
    base = np.column_stack([filled, shift(filled, 1), lag7, shift(filled, 14), shift(filled, 28), mean7, mean28,
                            change7, volatility7, age.astype(float), since])
    kind = None
    if kinds:
        kind = [None] * n
        current = None
        for i in range(n):
            current = kinds.get(start + timedelta(days=i), current)
            kind[i] = current
    return Series(series_id, item, market, start, actual, filled, age, valid & (age <= standard.FORWARD_FILL_DAYS),
                  base, kind)


def _calendar_columns(target_days, horizons):
    np = _np()
    weekday = np.array([d.weekday() for d in target_days], dtype=float)
    yday = np.array([d.timetuple().tm_yday for d in target_days], dtype=float)
    season = 2 * math.pi * yday / 365.25
    return weekday, np.sin(season), np.cos(season), np.asarray(horizons, dtype=float)


def _assemble(base_rows, weekday, sin, cos, horizon):
    """BASE_FEATURES 순서로 합친다."""
    np = _np()
    b = base_rows
    return np.column_stack([b[:, 0], b[:, 1], b[:, 2], b[:, 3], b[:, 4], b[:, 5], b[:, 6], b[:, 7], b[:, 8], b[:, 9],
                            weekday, sin, cos, horizon, b[:, 10]])


class Snapshot:
    """스냅샷 폴더를 한 번 읽어 계열별 시점 자료를 준비한다. 모델 코드는 이 객체를 직접 쓰지 않는다(실행기만 씀)."""

    def __init__(self, folder):
        self.folder = Path(folder)
        manifest = json.loads((self.folder / 'manifest.json').read_text(encoding='utf-8'))
        if manifest.get('snapshot_id') != standard.DATA_VERSION:
            raise ValueError(f'스냅샷 ID {manifest.get("snapshot_id")!r} ≠ {standard.DATA_VERSION!r}')
        self.manifest = manifest
        self.cutoff = date.fromisoformat(manifest['cutoff'])
        self.calendar = read_calendar(self.folder)
        self.series_meta = {int(r['series_id']): r for r in read_table(self.folder, 'price_series.csv')}
        observations, switches, kinds = {}, {}, {}
        for r in read_table(self.folder, 'price_daily.csv'):
            observations.setdefault(int(r['series_id']), {})[date.fromisoformat(r['price_date'])] = int(r['price'])
        for r in read_table(self.folder, 'price_daily_merged.csv'):
            sid, day = int(r['series_id']), date.fromisoformat(r['price_date'])
            observations.setdefault(sid, {})[day] = int(r['price'])
            kinds.setdefault(sid, {})[day] = r['kind_code']
            if r['kind_switch'] == '1':
                switches.setdefault(sid, set()).add(day)
        end = self.cutoff + timedelta(days=max(standard.HORIZONS))
        self.series = {sid: _build_series(sid, meta['item'], meta['market'], observations[sid], switches.get(sid, set()),
                                          kinds.get(sid), end)
                       for sid, meta in sorted(self.series_meta.items())}
        self._extras = None
        self.origins = {name: [date.fromisoformat(r['origin_date'])
                               for r in read_table(self.folder, f'origins_{name}.csv')]
                        for name in ('validation', 'tune', 'test')}

    @property
    def series_ids(self):
        return sorted(self.series)

    def load_as_of(self, series_id: int, d: date, bundles=()):
        """기준서 §9 이름. d 시점에 볼 수 있는 (학습 자료, 예측 입력). 예측 입력이 안 되면 NoInput."""
        return self.training_data(series_id, d, bundles), self.origin_inputs(series_id, d, bundles)

    def training_data(self, series_id: int, as_of: date, bundles=()):
        """재학습 기준일 as_of 시점 학습 표본. 창: as_of 이전 최근 1,825일(as_of 포함).
        표본 (기준일 o, 시점 h): o-28 ≥ 창 시작, 목표일 o+h ≤ as_of이고 실제 관측이 있음, v[o-28..o]에 빈 값 없음.
        """
        from tools.runtime import TrainingData
        np = _np()
        s = self.series[series_id]
        a = s.index(as_of)
        window_start = max(0, a - standard.TRAIN_WINDOW_DAYS + 1)
        observed = int((~np.isnan(s.actual[window_start:a + 1])).sum())
        if observed < standard.MIN_TRAIN_OBSERVATIONS:
            raise NoInput(f'학습 창의 실제 관측 {observed}개 < {standard.MIN_TRAIN_OBSERVATIONS}')
        first_origin = window_start + standard.FEATURE_LOOKBACK_DAYS
        parts = []
        for h in standard.HORIZONS:
            origins = np.arange(first_origin, a - h + 1)
            if origins.size == 0:
                continue
            keep = s.valid[origins] & ~np.isnan(s.actual[origins + h])
            origins = origins[keep]
            parts.append((origins, h))
        origins = np.concatenate([o for o, _ in parts])
        horizons = np.concatenate([np.full(o.size, h) for o, h in parts])
        order = np.lexsort((horizons, origins))
        origins, horizons = origins[order], horizons[order]
        target_idx = origins + horizons
        targets_days = [s.day(i) for i in target_idx]
        features = _assemble(s.base[origins], *_calendar_columns(targets_days, horizons))
        if bundles:
            features = np.column_stack([features, self._extra(series_id, origins, targets_days, bundles)])
        prices = [(s.day(i), int(s.actual[i])) for i in range(window_start, a + 1) if not np.isnan(s.actual[i])]
        return TrainingData(series_id=series_id, as_of=as_of, features=features, targets=s.actual[target_idx],
                            horizons=horizons.astype(int), origins=[s.day(i) for i in origins],
                            feature_names=feature_names(bundles), prices=prices)

    def origin_inputs(self, series_id: int, d: date, bundles=()):
        """기준일 d의 시점 1~7 특징과 d까지의 실제 관측(최근 1,825일)."""
        from tools.runtime import OriginInputs
        np = _np()
        s = self.series[series_id]
        i = s.index(d)
        if i < 0 or i >= len(s.age) or s.age[i] > standard.MAX_STALE_DAYS:
            raise NoInput(f'{d}: 최신 실제 관측이 {standard.MAX_STALE_DAYS}일보다 오래됨')
        if not s.valid[i]:
            raise NoInput(f'{d}: v[d-28..d]에 앞채움으로 못 채운 빈 값')
        horizons = list(standard.HORIZONS)
        targets = [d + timedelta(days=h) for h in horizons]
        rows = _assemble(np.repeat(s.base[i:i + 1], len(horizons), axis=0), *_calendar_columns(targets, horizons))
        if bundles:
            rows = np.column_stack([rows, self._extra(series_id, np.full(len(horizons), i), targets, bundles)])
        start = max(0, i - standard.TRAIN_WINDOW_DAYS + 1)
        prices = [(s.day(j), int(s.actual[j])) for j in range(start, i + 1) if not np.isnan(s.actual[j])]
        return OriginInputs(series_id=series_id, origin=d, features={h: rows[k] for k, h in enumerate(horizons)},
                            feature_names=feature_names(bundles), prices=prices)

    def _extra(self, series_id, origin_idx, target_days, bundles):
        """외부변수 묶음 열(standard.EXTRA_BUNDLES 순서). origin_idx: 표본별 기준일 위치, target_days: 표본별 목표일."""
        np = _np()
        if self._extras is None:
            self._extras = ExtraFeatures(self)
        columns = []
        for bundle in check_bundles(bundles):
            if bundle == 'EVENT':
                columns.append(np.array([self._extras.event_row(t) for t in target_days], dtype=float))
            else:
                columns.append(self._extras.origin_matrix(series_id, [bundle])[origin_idx])
        return np.column_stack(columns)

    # 평가기용(모델에는 주지 않음) -------------------------------------------------------------
    def actual_price(self, series_id: int, day: date):
        s = self.series[series_id]
        i = s.index(day)
        if i < 0 or i >= len(s.actual) or math.isnan(s.actual[i]):
            return None
        return float(s.actual[i])

    def naive(self, series_id: int, d: date):
        """v[d] (앞채움 최대 7일). 저장소 LAST_PRICE."""
        s = self.series[series_id]
        i = s.index(d)
        if i < 0 or math.isnan(s.filled[i]):
            return None
        return float(s.filled[i])

    def mean7(self, series_id: int, d: date):
        """v[d-6..d] 평균(앞채움 포함). 빈 값이 있으면 None. 저장소 MEAN_7."""
        s = self.series[series_id]
        i = s.index(d)
        if i < 6:
            return None
        values = s.filled[i - 6:i + 1]
        return None if _np().isnan(values).any() else float(values.mean())

    def kind_at(self, series_id: int, day: date):
        s = self.series[series_id]
        i = s.index(day)
        return None if s.kind is None or not (0 <= i < len(s.kind)) else s.kind[i]


# ---- 2차 외부변수 묶음(§5.2) ---------------------------------------------------------------------------
#
# 기준일 의존 묶음(MARKET·NATIONAL_WEATHER·MACRO·PRODUCTION)은 계열마다 배열(행 i = 기준일 start+i)로 한 번 계산하고,
# 목표일 의존 묶음(EVENT)은 목표일마다 계산한다. 상대 시장·기상·환율은 d−1까지, 생산량은 Y+1년 6/30부터.
# 값이 없으면 NaN(0이나 평균으로 채우지 않음).

ORIGIN_BUNDLES = ('MARKET', 'NATIONAL_WEATHER', 'MACRO', 'PRODUCTION')


def check_bundles(bundles) -> tuple:
    unknown = [b for b in bundles if b not in standard.EXTRA_BUNDLES]
    if unknown:
        raise ValueError(f'모르는 외부변수 묶음 {unknown}. 가능: {list(standard.EXTRA_BUNDLES)}')
    return tuple(b for b in standard.EXTRA_BUNDLES if b in set(bundles))  # 순서 고정


def feature_names(bundles=()) -> list[str]:
    names = list(standard.BASE_FEATURES)
    for bundle in check_bundles(bundles):
        names += standard.EXTRA_BUNDLES[bundle]
    return names


def _daily_array(values: dict, start: date, n: int, offset: int = 0):
    """{날짜: 값} → 길이 n 배열(행 i = start + i − offset일). 없으면 nan."""
    np = _np()
    out = np.full(n, np.nan)
    for day, value in values.items():
        i = (day - start).days + offset
        if 0 <= i < n and value is not None:
            out[i] = value
    return out


def _ffill(values, limit=standard.FORWARD_FILL_DAYS):
    np = _np()
    idx = np.arange(len(values))
    last = np.maximum.accumulate(np.where(~np.isnan(values), idx, -1))
    filled = values[np.maximum(last, 0)]
    return np.where((last >= 0) & (idx - last <= limit), filled, np.nan)


def _shift(values, k):
    np = _np()
    out = np.full(len(values), np.nan)
    if k < len(values):
        out[k:] = values[:len(values) - k]
    return out


def _window_total(values, span, scale=1.0):
    """[i−span+1..i]의 평균 × span × scale. 유효 값이 span의 70% 미만이면 nan(저장소 national weather와 같음)."""
    np = _np()
    pad = np.concatenate([np.full(span - 1, np.nan), values])
    win = np.lib.stride_tricks.sliding_window_view(pad, span)
    count = (~np.isnan(win)).sum(axis=1)
    with np.errstate(invalid='ignore'):
        total = np.nanmean(np.where(count[:, None] > 0, win, 0), axis=1) * span * scale
    return np.where(count >= span * .7, total, np.nan)


def _window_mean(values, span, minimum):
    np = _np()
    pad = np.concatenate([np.full(span - 1, np.nan), values])
    win = np.lib.stride_tricks.sliding_window_view(pad, span)
    count = (~np.isnan(win)).sum(axis=1)
    with np.errstate(invalid='ignore'):
        avg = np.nansum(win, axis=1) / np.maximum(count, 1)
    return np.where(count >= minimum, avg, np.nan)


class ExtraFeatures:
    """스냅샷의 외부 자료로 §5.2 묶음을 만든다. Snapshot이 처음 필요할 때 만든다."""

    def __init__(self, snap):
        self.snap = snap
        folder = snap.folder
        self.weather = {date.fromisoformat(r['weather_date']): r for r in read_table(folder, 'weather_daily.csv')}
        self.fx = {date.fromisoformat(r['rate_date']): float(r['rate'])
                   for r in read_table(folder, 'exchange_rate_daily.csv') if r['currency_code'] == 'USD' and r['rate']}
        self.production: dict[str, dict[int, tuple[float, date]]] = {}
        for r in read_table(folder, 'item_production.csv'):
            self.production.setdefault(r['item'], {})[int(r['year'])] = (
                float(r['production_ton']), date.fromisoformat(r['published_from']))
        self.events = [(date.fromisoformat(r['start_date']), date.fromisoformat(r['end_date']),
                        date.fromisoformat(r['effect_start_date']), date.fromisoformat(r['effect_end_date']))
                       for r in read_table(folder, 'calendar_event.csv')]
        self.holiday = {day: closed_holiday for day, closed_holiday in
                        ((date.fromisoformat(r['cal_date']), r['is_holiday'] == 'true')
                         for r in read_table(folder, 'calendar_day.csv'))}
        self.counterpart = {}
        by_key = {(s.item, s.market): sid for sid, s in snap.series.items()}
        for sid, s in snap.series.items():
            other = 'WHOLESALE' if s.market == 'RETAIL' else 'RETAIL'
            self.counterpart[sid] = by_key.get((s.item, other))
        self._origin_cache = {}
        self._target_cache = {}

    def origin_matrix(self, series_id: int, bundles) -> object:
        """행 i = 기준일 start+i의 기준일 의존 묶음 값(bundles 순서)."""
        np = _np()
        s = self.snap.series[series_id]
        n = len(s.actual)
        columns = []
        for bundle in bundles:
            key = (series_id, bundle)
            if key not in self._origin_cache:
                self._origin_cache[key] = getattr(self, f'_{bundle.lower()}')(s, n)
            columns.append(self._origin_cache[key])
        return np.column_stack(columns) if columns else np.zeros((n, 0))

    def _market(self, s, n):
        np = _np()
        cid = self.counterpart.get(s.series_id)
        if cid is None:
            return np.full((n, 4), np.nan)
        c = self.snap.series[cid]
        offset = (c.start - s.start).days  # c의 j번째 = s의 j+offset번째
        aligned = np.full(n, np.nan)
        lo, hi = max(0, offset), min(n, offset + len(c.filled))
        aligned[lo:hi] = c.filled[lo - offset:hi - offset]
        lag = standard.EXTRA_LAG_DAYS
        price = _shift(aligned, lag)
        with np.errstate(invalid='ignore', divide='ignore'):
            ratio = s.filled / price
            change7 = price / _shift(aligned, lag + 7) - 1
            change28 = price / _shift(aligned, lag + 28) - 1
        if s.kind is not None and c.kind is not None:  # 이어 붙인 배추·무: 작형이 다르면 비율은 결측
            for i in range(n):
                j = i - lag - offset
                other = c.kind[j] if 0 <= j < len(c.kind) else None
                if s.kind[i] is None or other is None or s.kind[i] != other:
                    ratio[i] = np.nan
        return np.column_stack([price, ratio, change7, change28])

    def _national_weather(self, s, n):
        np = _np()

        def column(name):
            values = {d: (float(r[name]) if r[name] != '' else (0.0 if name == 'precipitation' else None))
                      for d, r in self.weather.items()}
            return _shift(_daily_array(values, s.start, n), standard.EXTRA_LAG_DAYS)

        temp = column('avg_temp')
        rain = column('precipitation')
        heat, heavy, cold = column('heat_station_ratio'), column('heavy_rain_station_ratio'), column('cold_station_ratio')
        return np.column_stack([_window_mean(temp, 7, 5), _window_total(rain, 28),
                                _window_total(heat, 7, .01), _window_total(heat, 28, .01),
                                _window_total(heavy, 28, .01), _window_total(cold, 28, .01)])

    def _macro(self, s, n):
        np = _np()
        head = 40  # 계열 시작 전 환율도 써서 초반 변화율을 만든다
        full = _ffill(_daily_array(self.fx, s.start - timedelta(days=head), n + head))
        lag = standard.EXTRA_LAG_DAYS
        now = _shift(full, lag)[head:]
        with np.errstate(invalid='ignore', divide='ignore'):
            change7 = now / _shift(full, lag + 7)[head:] - 1
            change28 = now / _shift(full, lag + 28)[head:] - 1
        return np.column_stack([change7, change28])

    def _production(self, s, n):
        np = _np()
        table = self.production.get(s.item, {})
        out = np.full(n, np.nan)
        usable = sorted((published, year) for year, (_, published) in table.items())
        for i in range(n):
            day = s.start + timedelta(days=i)
            known = [year for published, year in usable if published <= day]
            if known:
                latest = max(known)
                if latest - 1 in table and table[latest - 1][0]:
                    out[i] = table[latest][0] / table[latest - 1][0] - 1
        return out[:, None]

    def event_row(self, target: date):
        """목표일 명절 특징 4개: 설·추석 시작일까지 일수, 끝난 뒤 일수(명절 중 0, 최대 45), 영향 기간 여부, 전날 평일 공휴일."""
        if target in self._target_cache:
            return self._target_cache[target]
        cap = standard.HOLIDAY_WINDOW_DAYS
        to_major = from_major = cap
        in_window = 0.0
        for start, end, effect_start, effect_end in self.events:
            if start <= target <= end:
                to_major = from_major = 0
            elif target < start:
                to_major = min(to_major, (start - target).days)
            else:
                from_major = min(from_major, (target - end).days)
            if effect_start <= target <= effect_end:
                in_window = 1.0
        previous = target - timedelta(days=1)
        prev_holiday = float(self.holiday.get(previous, False) and previous.weekday() < 5)
        row = (float(min(to_major, cap)), float(min(from_major, cap)), in_window, prev_holiday)
        self._target_cache[target] = row
        return row
