"""v2 특징: v1 공통 로더(기본 15개 + §5.2 묶음) 위에 긴 이력·추가 자료를 붙인다.

시점 규칙은 v1과 같다: 자기 계열은 d까지, 그 밖의 모든 자료(주산지 날씨·반입량·다른 품목 가격)는 d−1까지.
값이 없으면 NaN(채우지 않음). 기준일 의존 특징이라 계열마다 배열(행 i = 기준일 start+i)로 한 번 계산한다.

묶음
- WEATHER_ANOM:   주산지 날씨의 평년 대비 편차(평년 = 지난 1~5년 같은 날 ±3일). 과거 13개 4주 블록의
                  평균기온 편차·강수 편차 → 26개. 계절 자체가 아니라 '평소보다 덥다/비가 많다'만 남긴다
- ORIGIN_WEATHER: 품목 주산지 관측소 평균 날씨. 주 k(=1..52, d−7k ~ d−7k+6) 평균기온·강수합,
                  4주 블록 j(=1..13)의 최저기온 최솟값·최고기온 최댓값 → 130개
- GARAK:          가락시장 반입량(톤). 주 k(=1..8) 합, 최근 7·28일 합의 전년 같은 기간 대비 → 10개
                  오입력 의심값은 스냅샷 정제 단계에서 빈 값으로 저장돼 있다(snapshot.drop_garak_spikes) → NaN
- CROSS_ITEM:     다른 4개 품목(같은 시장)의 d−1 가격 7·28일 변화율 → 8개
- SERIES_ID:      품목 5개 원핫 + 도매 여부(통합 학습에서 계열 구분) → 6개
- PRICE_DYN:      자기 가격(d까지)만으로 만든 동역학 → 11개(추가 자료 불필요)
                  변동 없는 날 비율·마지막 변동 후 일수(가격이 잘 안 바뀌는 소매 계열용), 일별 로그 변화 변동성,
                  56일 범위 안 위치, 91·365일 평균 대비, 전년 대비, 3일 변화,
                  작년 같은 시기 h일 변화(1~3년 전 평균, 목표 시점별) — 계절 흐름을 가격 자체에서 가져온다
"""
import csv
import math
from datetime import date, timedelta
from pathlib import Path

import numpy as np

from tools import loader, standard

WEATHER_WEEKS = 52
EXTREME_BLOCKS = 13  # 4주 블록
GARAK_WEEKS = 8
LAG = standard.EXTRA_LAG_DAYS
V2_BLOCKS = ('ORIGIN_WEATHER', 'WEATHER_ANOM', 'GARAK', 'CROSS_ITEM', 'SERIES_ID', 'PRICE_DYN')
NEEDS_EXTRA = ('ORIGIN_WEATHER', 'WEATHER_ANOM', 'GARAK')  # 추가 자료 폴더가 있어야 하는 묶음
ANOM_BLOCKS = 13  # 4주 블록 × 13 = 52주
ANOM_YEARS = 5
PRICE_DYN_NAMES = ['pd_flat_share28', 'pd_days_since_change', 'pd_logret_vol28', 'pd_range_pos56', 'pd_ratio_mean91',
                   'pd_ratio_mean365', 'pd_yoy', 'pd_chg3', 'pd_analog_n', 'pd_analog_chg7', 'pd_analog_chg_h']
ANALOG_YEARS = 3


def block_names(block: str) -> list[str]:
    if block == 'ORIGIN_WEATHER':
        return ([f'ow_temp_w{k}' for k in range(1, WEATHER_WEEKS + 1)]
                + [f'ow_rain_w{k}' for k in range(1, WEATHER_WEEKS + 1)]
                + [f'ow_tmin_b{j}' for j in range(1, EXTREME_BLOCKS + 1)]
                + [f'ow_tmax_b{j}' for j in range(1, EXTREME_BLOCKS + 1)])
    if block == 'WEATHER_ANOM':
        return ([f'wa_temp_b{j}' for j in range(1, ANOM_BLOCKS + 1)]
                + [f'wa_rain_b{j}' for j in range(1, ANOM_BLOCKS + 1)])
    if block == 'GARAK':
        return [f'garak_w{k}' for k in range(1, GARAK_WEEKS + 1)] + ['garak_yoy7', 'garak_yoy28']
    if block == 'CROSS_ITEM':
        return [f'cross_{item}_{span}' for item in standard.ITEMS for span in ('chg7', 'chg28')]
    if block == 'SERIES_ID':
        return [f'is_{item}' for item in standard.ITEMS] + ['is_wholesale']
    if block == 'PRICE_DYN':
        return PRICE_DYN_NAMES
    raise ValueError(block)


def _read(path: Path):
    with open(path, encoding='utf-8', newline='') as f:
        return list(csv.DictReader(f))


def _num(text):
    return float(text) if text not in ('', None) else math.nan


def _window_stat(values, end_lag, length, how):
    """행 i에 대해 values[i−end_lag−length+1 .. i−end_lag]의 통계. nan은 빼고, 유효 값이 70% 미만이면 nan."""
    n = len(values)
    shifted = loader._shift(values, end_lag)
    pad = np.concatenate([np.full(length - 1, np.nan), shifted])
    win = np.lib.stride_tricks.sliding_window_view(pad, length)[:n]
    count = (~np.isnan(win)).sum(axis=1)
    ok = count >= length * .7
    safe = np.where(np.isnan(win), 0.0, win)
    with np.errstate(all='ignore'):
        if how == 'mean':
            stat = safe.sum(axis=1) / np.maximum(count, 1)
        elif how == 'sum':
            stat = safe.sum(axis=1) / np.maximum(count, 1) * length
        elif how == 'min':
            stat = np.where(np.isnan(win), np.inf, win).min(axis=1)
        else:
            stat = np.where(np.isnan(win), -np.inf, win).max(axis=1)
    return np.where(ok, stat, np.nan)


def _past_years_mean(values):
    """날짜 t의 평년값 = 지난 1~5년 같은 날(±3일 평균)의 평균. t보다 앞선 자료만 쓴다(시점 규칙 유지)."""
    pad = np.concatenate([np.full(3, np.nan), values, np.full(3, np.nan)])
    win = np.lib.stride_tricks.sliding_window_view(pad, 7)  # 행 t = values[t−3..t+3]
    count = (~np.isnan(win)).sum(axis=1)
    smooth = np.where(count >= 4, np.where(np.isnan(win), 0, win).sum(axis=1) / np.maximum(count, 1), np.nan)
    # smooth[t]는 t+3까지 쓰지만 아래에서 364일 이상 민 값만 쓰므로 기준일 이후 자료는 들어가지 않는다
    years = [loader._shift(smooth, 364 * k) for k in range(1, ANOM_YEARS + 1)]
    stack = np.vstack(years)
    count = (~np.isnan(stack)).sum(axis=0)
    with np.errstate(all='ignore'):
        mean = np.nansum(stack, axis=0) / np.maximum(count, 1)
    return np.where(count >= 2, mean, np.nan)



class V2Features:
    """v1 Snapshot + v2 추가 자료 폴더 → 계열별 기준일 특징 행렬."""

    def __init__(self, snap: loader.Snapshot, extra_dir: Path | None):
        self.snap = snap
        self.extra = Path(extra_dir) if extra_dir is not None else None
        self._loaded = False
        self._cache = {}

    def _load(self):
        """추가 자료 폴더는 ORIGIN_WEATHER·WEATHER_ANOM·GARAK에만 필요하다. 처음 필요할 때 읽는다."""
        if self._loaded:
            return
        if self.extra is None or not (self.extra / 'item_station.csv').exists():
            raise FileNotFoundError(f'v2 추가 자료 폴더가 없음: {self.extra} (ORIGIN_WEATHER·WEATHER_ANOM·GARAK에 필요)')
        extra = self.extra
        self.item_stations = {}
        for r in _read(extra / 'item_station.csv'):
            self.item_stations.setdefault(r['item'], []).append(int(r['stn_id']))
        self.weather = {}  # (stn, date) → (avg, min, max, rain)
        for r in _read(extra / 'asos_station_daily.csv'):
            rain = 0.0 if r['sum_rn'] == '' else float(r['sum_rn'])  # ASOS는 무강수일 강수량을 빈 값으로 준다
            self.weather[int(r['stn_id']), date.fromisoformat(r['obs_date'])] = (
                _num(r['avg_ta']), _num(r['min_ta']), _num(r['max_ta']), rain)
        self.garak = {}
        for r in _read(extra / 'garak_arrivals_daily.csv'):
            # 빈 ton = 스냅샷 정제(snapshot clean)에서 뺀 오입력 의심값 → NaN(창 통계에서 빠짐). 0톤과 다르다
            self.garak[r['item'], date.fromisoformat(r['arrival_date'])] = _num(r['ton'])
        garak_days = [d for _, d in self.garak]
        self.garak_span = (min(garak_days), max(garak_days)) if garak_days else (date.max, date.min)
        self._loaded = True

    # 품목 단위 일별 배열(계열 시작일 기준, 앞에 여유 head일)
    def _item_daily(self, item, start, n, head):
        self._load()
        days = [start + timedelta(days=i - head) for i in range(n + head)]
        stations = self.item_stations[item]
        cols = np.full((len(days), 4), np.nan)
        for i, d in enumerate(days):
            values = [self.weather.get((s, d)) for s in stations]
            values = np.array([v for v in values if v is not None], dtype=float)
            if values.size:
                with np.errstate(all='ignore'):
                    cols[i] = np.nanmean(values, axis=0)
        first, last = self.garak_span
        garak = np.array([self.garak.get((item, d), 0.0 if first <= d <= last else np.nan) for d in days],
                         dtype=float)  # 자료 기간 안에서 행이 없는 날(일요일 등) = 경매 없음 = 0톤
        return cols, garak

    def origin_block(self, series_id: int, block: str):
        key = (series_id, block)
        if key in self._cache:
            return self._cache[key]
        s = self.snap.series[series_id]
        n = len(s.actual)
        head = 400 + 364 * ANOM_YEARS if block == 'WEATHER_ANOM' else 400  # 계열 시작 전 자료도 쓴다
        if block == 'SERIES_ID':
            row = [float(s.item == item) for item in standard.ITEMS] + [float(s.market == 'WHOLESALE')]
            out = np.tile(row, (n, 1))
        elif block == 'CROSS_ITEM':
            out = self._cross(s, n)
        elif block == 'PRICE_DYN':
            out = price_dynamics(s.filled)
        else:
            weather, garak = self._item_daily(s.item, s.start, n, head)
            if block == 'WEATHER_ANOM':
                cols = []
                for k, how in ((0, 'mean'), (3, 'sum')):  # 평균기온, 강수
                    daily = weather[:, k]
                    anomaly = daily - _past_years_mean(daily)
                    cols += [_window_stat(anomaly, LAG + 28 * (j - 1), 28, how) for j in range(1, ANOM_BLOCKS + 1)]
            elif block == 'ORIGIN_WEATHER':
                temp, tmin, tmax, rain = weather[:, 0], weather[:, 1], weather[:, 2], weather[:, 3]
                cols = [_window_stat(temp, LAG + 7 * (k - 1), 7, 'mean') for k in range(1, WEATHER_WEEKS + 1)]
                cols += [_window_stat(rain, LAG + 7 * (k - 1), 7, 'sum') for k in range(1, WEATHER_WEEKS + 1)]
                cols += [_window_stat(tmin, LAG + 28 * (j - 1), 28, 'min') for j in range(1, EXTREME_BLOCKS + 1)]
                cols += [_window_stat(tmax, LAG + 28 * (j - 1), 28, 'max') for j in range(1, EXTREME_BLOCKS + 1)]
            else:
                cols = [_window_stat(garak, LAG + 7 * (k - 1), 7, 'sum') for k in range(1, GARAK_WEEKS + 1)]
                for span in (7, 28):
                    now = _window_stat(garak, LAG, span, 'sum')
                    year_ago = _window_stat(garak, LAG + 364, span, 'sum')
                    with np.errstate(all='ignore'):
                        cols.append(np.where(year_ago > 0, now / year_ago - 1, np.nan))
            out = np.column_stack(cols)[head:]
        self._cache[key] = out
        return out

    def analog_by_horizon(self, series_id, origin_idx, horizons):
        s = self.snap.series[series_id]
        out = np.full(len(origin_idx), np.nan)
        for h in np.unique(horizons):
            key = (series_id, 'analog', int(h))
            if key not in self._cache:
                self._cache[key] = _analog(s.filled, int(h))[0]
            rows = horizons == h
            out[rows] = self._cache[key][origin_idx[rows]]
        return out

    def _cross(self, s, n):
        cols = []
        by_key = {(x.item, x.market): x for x in self.snap.series.values()}
        for item in standard.ITEMS:
            other = by_key.get((item, s.market))
            if other is None or other.series_id == s.series_id:
                cols += [np.full(n, np.nan), np.full(n, np.nan)]
                continue
            offset = (other.start - s.start).days
            aligned = np.full(n, np.nan)
            lo, hi = max(0, offset), min(n, offset + len(other.filled))
            aligned[lo:hi] = other.filled[lo - offset:hi - offset]
            now = loader._shift(aligned, LAG)
            with np.errstate(all='ignore'):
                cols.append(now / loader._shift(aligned, LAG + 7) - 1)
                cols.append(now / loader._shift(aligned, LAG + 28) - 1)
        return np.column_stack(cols)


def _rolling(values, length, how, min_share=.7):
    return _window_stat(values, 0, length, how) if how != 'std' else _rolling_std(values, length, min_share)


def _rolling_std(values, length, min_share=.7):
    n = len(values)
    pad = np.concatenate([np.full(length - 1, np.nan), values])
    win = np.lib.stride_tricks.sliding_window_view(pad, length)[:n]
    count = (~np.isnan(win)).sum(axis=1)
    with np.errstate(all='ignore'):
        out = np.nanstd(np.where(count[:, None] > 0, win, 0.0), axis=1)
    return np.where(count >= length * min_share, out, np.nan)


def price_dynamics(filled):
    """자기 가격 v(앞채움)로 만든 기준일 특징(PRICE_DYN_NAMES 중 시점 무관 9개 + analog 자리 2개 중 1개).
    행 i는 v[..i]만 쓴다. pd_analog_chg_h(시점별)는 rows()에서 따로 붙인다."""
    v = np.asarray(filled, dtype=float)
    n = len(v)
    prev = loader._shift(v, 1)
    with np.errstate(all='ignore'):
        flat = np.where(np.isnan(v) | np.isnan(prev), np.nan, (v == prev).astype(float))
        logret = np.log(v / prev)
    flat_share = _window_stat(flat, 0, 28, 'mean')
    changed = np.where(flat == 0, np.arange(n), -1)
    last_change = np.maximum.accumulate(changed)
    since = np.where(last_change >= 0, np.minimum(np.arange(n) - last_change, 90), 90).astype(float)
    since = np.where(np.isnan(v), np.nan, since)
    vol = _rolling_std(logret, 28)
    lo, hi = _window_stat(v, 0, 56, 'min'), _window_stat(v, 0, 56, 'max')
    with np.errstate(all='ignore'):
        pos = np.where(hi > lo, (v - lo) / (hi - lo), .5)
        pos = np.where(np.isnan(lo) | np.isnan(v), np.nan, pos)
        r91 = v / _window_stat(v, 0, 91, 'mean') - 1
        r365 = v / _window_stat(v, 0, 365, 'mean', ) - 1
        yoy = v / loader._shift(v, 364) - 1
        chg3 = v / loader._shift(v, 3) - 1
    analog7, count = _analog(v, 7)
    return np.column_stack([flat_share, since, vol, pos, r91, r365, yoy, chg3, count, analog7])


def _analog(v, h):
    """행 i: 1~3년 전 같은 시기의 h일 변화 v[i−364k+h]/v[i−364k] − 1 의 평균(h ≤ 7 이라 모두 i 이전 자료)."""
    changes = []
    for k in range(1, ANALOG_YEARS + 1):
        lag = 364 * k
        with np.errstate(all='ignore'):
            changes.append(loader._shift(v, lag - h) / loader._shift(v, lag) - 1)
    stack = np.vstack(changes)
    count = (~np.isnan(stack)).sum(axis=0)
    with np.errstate(all='ignore'):
        mean = np.nansum(stack, axis=0) / np.maximum(count, 1)
    return np.where(count > 0, mean, np.nan), count.astype(float)


def feature_names(bundles, blocks) -> list[str]:
    names = loader.feature_names(bundles)
    for block in V2_BLOCKS:
        if block in blocks:
            names += block_names(block)
    return names


def rows(snap: loader.Snapshot, v2: V2Features, series_id: int, origin_idx, horizons, bundles, blocks):
    """계열 하나의 (기준일 위치, 시점) 표본 → 특징 행렬(feature_names 순서)."""
    s = snap.series[series_id]
    origin_idx = np.asarray(origin_idx)
    horizons = np.asarray(horizons)
    targets = [s.day(i + h) for i, h in zip(origin_idx, horizons)]
    parts = [loader._assemble(s.base[origin_idx], *loader._calendar_columns(targets, horizons))]
    if bundles:
        parts.append(snap._extra(series_id, origin_idx, targets, bundles))
    for block in V2_BLOCKS:
        if block in blocks:
            parts.append(v2.origin_block(series_id, block)[origin_idx])
            if block == 'PRICE_DYN':
                parts.append(v2.analog_by_horizon(series_id, origin_idx, horizons))
    return np.column_stack(parts)
