"""구조적 가격 전달 모델 (Structural Transmission Model, 실험 접두어 struct).

목표 변수는 로그 변화율 y = log(실제 가격(d+h) / current)이고, 예측가는 current * exp(k_h * y_hat)이다.

    y_hat(h) = a * 전달(counter_change7/28)        도매 -> 소매 전달
             + b * (log(배수) - 평소 배수)          배수 되돌림 (평소 = 학습 표본 최근 N일 중앙값)
             + c * season_analog(h)                 1~K년 전 같은 시기 h일 로그 변화의 가중 평균
             + d * event_term(h)                    명절 영향 기간 등 EVENT 특징
             + e * momentum(change7)                선택

어떤 항을 쓸지는 소매·도매별 항 목록(retail_terms, wholesale_terms)으로 정한다. 도매의 기본은 계절 + 명절이고,
빈 목록이면 naive(현재 가격 유지)다. 구조 변형은 모두 params로 고르며 코드를 바꾸지 않는다(PRD §4.4).

추정은 항 열을 열별 RMS로 나눈 뒤(절편 없음, 중심화 없음) 직접 구현한 L2 수축 최소제곱 ||y - Zw||^2 + lambda ||w||^2
(scipy.linalg.lstsq)을 쓴다. 시점은 묶어서 회귀 1개로 풀고 설계 행렬에 시점별 항은 없다. 수축 강도 lambda와
k_h in [0, 1](기본 시점별 7개. 선택 params retail_k_grid로 소매만 격자를 넓힐 수 있음)은 학습 표본의 마지막 20%(시간순)의 MAPE로 격자에서 고르고, 고른 뒤에는 전체 학습 표본으로
다시 맞춘다. 예측이 NaN·무한이면 그 시점은 None(PRD §10).
무작위 요소가 없어 같은 입력이면 결과가 같다. numpy와 scipy만 쓰고, 파일·DB를 열지 않는다(기준서 §9).

계절 항의 명절 마스크(선택, season_event_mask): 설·추석은 음력이라 양력 364일 전과 날짜가 어긋난다. 켜면 기준일 o, 목표일 o+h,
비교 연도 각 해의 b=o-364k와 b+h 중 하나라도 명절 영향 기간이면 그 표본의 계절 항을 0(NaN과 같은 처리)으로 둔다.
영향 기간 판정은 모델이 받은 입력만으로 한다: fit은 학습 표본의 (목표일 -> target_in_event_window) 대응을 날짜별로 모아 쓰고,
predict는 그 대응과 inputs.features[h]의 target_in_event_window, days_to/from_major_holiday를 쓴다(파일·달력은 읽지 않음).

누수 방지
- fit에서 표본(기준일 o, 시점 h)의 계절 항은 o 이전 가격만으로 만든다(season_analog는 o - 364k + h + 창 <= o인 위치만 읽음).
  history.prices는 재학습 기준일까지 들어 있으므로 표본마다 위치로 잘라 읽는다.
- 평소 배수, 열 크기, lambda, k_h는 fit에 넘어온 학습 표본으로만 계산한다.
- predict는 기준일 이후 가격을 버리고 쓴다.
"""
from __future__ import annotations

import math
from dataclasses import dataclass

import numpy as np
from scipy import linalg

RETAIL_SERIES = (1, 8, 10, 9001, 9011)
WHOLESALE_SERIES = (2, 7, 9, 9002, 9012)
SEASON_LAG_DAYS = 364  # 52주: 요일이 같다
KIND_SINCE_CAP = 90  # days_since_kind_switch 상한(기준서 §5.1)
HORIZONS = tuple(range(1, 8))
TERM_GROUPS = ('transmission', 'ratio', 'season', 'event', 'momentum')
TRANSMISSION_FEATURES = ('counter_change7', 'counter_change28')


# ---- 계절 유사도 -------------------------------------------------------------------------------------------

@dataclass
class PriceGrid:
    """날짜 위치로 읽는 가격 배열. arr[i] = start_ord + i일의 실제 관측(없으면 nan), near = 가까운 관측으로 채운 값."""
    start_ord: int
    arr: object
    near: object
    window: int


def price_grid(prices, window: int = 3, until_ord: int | None = None) -> PriceGrid:
    """(날짜, 가격) 목록 -> PriceGrid. until_ord가 있으면 그 날짜(서수) 이후 관측은 버린다.

    near[i]: 실제 관측이 있으면 그 값, 없으면 +-window일 안에서 가장 가까운 관측(같은 거리면 이른 날).
    """
    pairs = [(d.toordinal(), float(p)) for d, p in prices if p is not None and p > 0]
    if until_ord is not None:
        pairs = [(o, p) for o, p in pairs if o <= until_ord]
    if not pairs:
        return PriceGrid(0, np.zeros(0), np.zeros(0), window)
    days = np.array([o for o, _ in pairs])
    values = np.array([p for _, p in pairs])
    start = int(days.min())
    arr = np.full(int(days.max()) - start + 1, np.nan)
    arr[days - start] = values
    return PriceGrid(start, arr, near_fill(arr, window), window)


def near_fill(arr, window: int):
    """빈 칸(nan)을 +-window일 안에서 가장 가까운 값으로 채운다(같은 거리면 이른 날)."""
    near = arr.copy()
    for step in range(1, window + 1):
        for sign in (-1, 1):  # -1: step일 이른 값, +1: step일 늦은 값
            shifted = np.full_like(arr, np.nan)
            if sign < 0:
                shifted[step:] = arr[:-step]
            else:
                shifted[:-step] = arr[step:]
            fill = np.isnan(near) & ~np.isnan(shifted)
            near[fill] = shifted[fill]
    return near


# ---- 명절 영향 기간(입력에서만 만든 날짜별 대응) -----------------------------------------------------------------

@dataclass
class EventDays:
    """fit 표본에서 모은 (날짜 -> 영향 기간 여부)와, 영향 기간 규칙의 문턱.

    flags: 날짜 위치별 0/1(알 수 없으면 nan, +-fill일 안 가장 가까운 날 값으로 채움).
    t_to, t_from: 영향 기간이던 표본의 days_to(명절 시작 전)·days_from(끝난 뒤) 최댓값. 기준일 o의 판정에 쓴다.
    """
    start_ord: int
    flags: object
    t_to: float
    t_from: float
    cap: float

    def lookup(self, ords):
        """날짜(서수) 배열 -> 0/1/nan(모름)."""
        ords = np.asarray(ords, dtype=np.int64)
        i = ords - self.start_ord
        ok = (i >= 0) & (i < len(self.flags))
        out = np.full(ords.shape, np.nan)
        out[ok] = self.flags[i[ok]]
        return out


def build_event_days(target_ord, flag, days_to, days_from, fill: int = 3) -> EventDays | None:
    """표본의 목표일(서수)·target_in_event_window·days_to/from으로 EventDays를 만든다. 쓸 표본이 없으면 None."""
    target_ord = np.asarray(target_ord, dtype=np.int64)
    flag, days_to, days_from = (np.asarray(v, dtype=float) for v in (flag, days_to, days_from))
    ok = np.isfinite(flag)
    if not ok.any():
        return None
    start = int(target_ord[ok].min())
    arr = np.full(int(target_ord[ok].max()) - start + 1, np.nan)
    arr[target_ord[ok] - start] = flag[ok]
    cap = float(np.nanmax(np.concatenate([days_to[ok], days_from[ok]])))
    on = ok & (flag == 1)
    before = on & (days_from >= cap)  # 이전 명절 직후가 아닌 영향 기간 = 시작 전 구간
    after = on & (days_to >= cap)  # 다음 명절 직전이 아닌 영향 기간 = 끝난 뒤 구간
    t_to = float(days_to[before].max()) if before.any() else -1.0
    t_from = float(days_from[after].max()) if after.any() else -1.0
    return EventDays(start, near_fill(arr, fill), t_to, t_from, cap)


def origin_event_flag(ev: EventDays, origin_ord: int, horizons, days_to, days_from) -> float:
    """예측 기준일 o의 영향 기간 여부. 목표일 행(h, days_to/from)에서 o의 값을 구할 수 있으면 그것으로 판정한다.

    o보다 뒤인 목표일 t=o+h가 명절 시작 전이면 days_to(o) = days_to(t) + h, 끝난 뒤(h일을 빼도 o가 끝난 뒤)면
    days_from(o) = days_from(t) - h로 정확히 구해진다. 명절 중이거나 걸쳐 있으면 정할 수 없어 다음 행을 본다.
    모든 행이 정할 수 없으면 fit 표본 대응에서 +-fill일 안 가장 가까운 날 값을 쓰고, 그것도 없으면 nan(마스크 안 함).
    """
    for h, to, frm in zip(horizons, days_to, days_from):
        if 0 < to < ev.cap:
            return float(to + h <= ev.t_to)
        if 0 < frm < ev.cap and frm - h >= 1:
            return float(frm - h <= ev.t_from)
    return float(ev.lookup([origin_ord])[0])


def kind_since_grid(grid: PriceGrid, switch_ords) -> object:
    """격자 위치 x마다 min(90, x - (x 이하 최근 작형 전환일)). 전환일이 없으면 90."""
    n = len(grid.arr)
    out = np.full(n, float(KIND_SINCE_CAP))
    if not len(switch_ords):
        return out
    idx = np.arange(n)
    last = np.full(n, -1)
    for s in switch_ords:
        j = int(s) - grid.start_ord
        if 0 <= j < n:
            last[j] = j
    last = np.maximum.accumulate(last)
    return np.where(last >= 0, np.minimum(idx - last, KIND_SINCE_CAP), KIND_SINCE_CAP).astype(float)


DEFAULT_SEASON_WEIGHTS = (0.5, 0.3, 0.2)  # 1·2·3년 전(PRD §10)


def season_weights_for(weights, years: int):
    """'uniform' 또는 해별 가중 목록 -> 길이 years 목록(k=1..years). 없는 해는 season_analog가 빼고 다시 정규화한다."""
    if isinstance(weights, str):
        if weights != 'uniform':
            raise ValueError("season_weights는 'uniform' 또는 해별 가중 목록")
        return [1.0] * years
    weights = [float(w) for w in weights]
    if len(weights) < years or min(weights[:years]) < 0 or sum(weights[:years]) <= 0:
        raise ValueError(f'season_weights는 season_years({years}) 이상 길이의 0 이상 값')
    return weights[:years]


def season_analog(grid: PriceGrid, origin_ord, horizons, years: int = 3, weights=DEFAULT_SEASON_WEIGHTS,
                  kind_since=None, kind_now=None, kind_tol=None):
    """기준일 o(서수), 시점 h마다 1~years년 전 같은 시기의 h일 로그 변화 가중 평균.

    k년 전 시작점 b = o - 364k, 끝점 = b + h. 각 점은 +-window일 안 가장 가까운 관측을 쓴다.
    가중은 해별 목록(기본 0.5·0.3·0.2)이나 'uniform'이고, 관측이 없는 해는 빼고 다시 정규화한다.
    끝점 + window가 o 이하인 위치만 읽으므로 o 이후 가격은 결과에 영향을 주지 않는다.
    kind_tol이 있으면 (k년 전 시작점의 days_since_kind_switch)와 kind_now의 차이가 kind_tol 이하인 해만 쓴다.
    쓸 수 있는 해가 없으면 nan.
    """
    o = np.asarray(origin_ord, dtype=np.int64) - grid.start_ord
    h = np.asarray(horizons, dtype=np.int64)
    n = len(grid.near)
    wk = season_weights_for(weights, int(years))
    num = np.zeros(o.shape)
    den = np.zeros(o.shape)
    if n == 0:
        return np.full(o.shape, np.nan)
    for k in range(1, int(years) + 1):
        base = o - SEASON_LAG_DAYS * k
        end = base + h
        ok = (base >= 0) & (end >= 0) & (end < n) & (end + grid.window <= o)
        base_c = np.clip(base, 0, max(n - 1, 0))
        end_c = np.clip(end, 0, max(n - 1, 0))
        p0, p1 = grid.near[base_c], grid.near[end_c]
        ok &= ~np.isnan(p0) & ~np.isnan(p1)
        if kind_tol is not None and kind_since is not None and kind_now is not None:
            ok &= np.abs(kind_since[base_c] - np.asarray(kind_now, dtype=float)) <= kind_tol
        w = wk[k - 1]
        with np.errstate(invalid='ignore', divide='ignore'):
            change = np.log(p1 / p0)
        ok &= np.isfinite(change)
        num += np.where(ok, w * np.where(ok, change, 0.0), 0.0)
        den += np.where(ok, w, 0.0)
    with np.errstate(invalid='ignore', divide='ignore'):
        return np.where(den > 0, num / den, np.nan)


# ---- 수축 최소제곱 -----------------------------------------------------------------------------------------

def ridge_solve(Z, y, lam: float):
    """min ||y - Z w||^2 + lam ||w||^2 (절편 없음, 표본 가중 없음). 증강 행렬의 최소제곱으로 푼다(lam=0이어도 안정)."""
    n, p = Z.shape
    if p == 0:
        return np.zeros(0)
    if lam > 0:
        A = np.vstack([Z, math.sqrt(lam) * np.eye(p)])
        b = np.concatenate([y, np.zeros(p)])
    else:
        A, b = Z, y
    return linalg.lstsq(A, b, lapack_driver='gelsd')[0]


class StructuralModel:
    def __init__(self, retail_series=RETAIL_SERIES, wholesale_series=WHOLESALE_SERIES,
                 retail_terms=('transmission', 'ratio', 'season', 'event'),
                 wholesale_terms=('season', 'event'),
                 transmission=('counter_change7',),
                 ratio_window_days=91,
                 season_years=3, season_weights=DEFAULT_SEASON_WEIGHTS, season_window=3, season_kind_tol=None,
                 event_features=('target_in_event_window', 'target_prev_day_holiday'),
                 h_scale_terms=(), season_event_mask=False, event_fill_days=3,
                 lambda_grid=(0.0, 0.1, 1.0, 10.0, 100.0),
                 k_mode='per_horizon', k_grid=(0.0, 0.25, 0.5, 0.75, 1.0), retail_k_grid=None,
                 select_loss='mape', val_fraction=0.2, min_fit_samples=100, min_val_samples=30,
                 train_window_days=None, y_clip=1.0, **unknown):
        if unknown:
            raise ValueError(f'알 수 없는 params: {sorted(unknown)}')
        self.retail_series = {int(s) for s in retail_series}
        self.wholesale_series = {int(s) for s in wholesale_series}
        self.terms = {'retail': tuple(retail_terms), 'wholesale': tuple(wholesale_terms)}
        for group, terms in self.terms.items():
            bad = [t for t in terms if t not in TERM_GROUPS]
            if bad:
                raise ValueError(f'{group} 항 이름 오류 {bad}. 가능: {TERM_GROUPS}')
        self.transmission = tuple(transmission)
        bad = [t for t in self.transmission if t not in TRANSMISSION_FEATURES]
        if bad:
            raise ValueError(f'transmission은 {TRANSMISSION_FEATURES} 중에서: {bad}')
        self.ratio_window_days = int(ratio_window_days)
        self.season_years = int(season_years)
        self.season_weights = season_weights if isinstance(season_weights, str) else tuple(season_weights)
        season_weights_for(self.season_weights, self.season_years)  # 값 검사
        self.season_window = int(season_window)
        self.season_kind_tol = None if season_kind_tol is None else float(season_kind_tol)
        self.event_features = tuple(event_features)
        self.h_scale_terms = tuple(h_scale_terms)
        self.season_event_mask = bool(season_event_mask)
        self.event_fill_days = int(event_fill_days)
        bad = [t for t in self.h_scale_terms if t not in TERM_GROUPS]
        if bad:
            raise ValueError(f'h_scale_terms 이름 오류 {bad}')
        self.lambda_grid = sorted({float(v) for v in lambda_grid}, reverse=True)  # 같으면 센 수축을 우선
        if not self.lambda_grid or min(self.lambda_grid) < 0:
            raise ValueError('lambda_grid는 0 이상 값이 하나 이상')
        if k_mode not in ('shared', 'per_horizon'):
            raise ValueError("k_mode는 'shared' 또는 'per_horizon'")
        self.k_mode = k_mode
        self.k_grid = sorted({float(v) for v in k_grid})
        if not self.k_grid or self.k_grid[0] < 0 or self.k_grid[-1] > 1:
            raise ValueError('k_grid는 [0, 1] 안')
        # 소매 계열만 쓰는 k 격자(탐색 변형, PRD §4.3의 [0, 1]을 넓힘). None이면 k_grid와 같다.
        self.retail_k_grid = None if retail_k_grid is None else sorted({float(v) for v in retail_k_grid})
        if self.retail_k_grid is not None and (not self.retail_k_grid or self.retail_k_grid[0] < 0
                                               or self.retail_k_grid[-1] > 3):
            raise ValueError('retail_k_grid는 [0, 3] 안')
        if select_loss not in ('mape', 'abs', 'sq'):
            raise ValueError("select_loss는 'mape', 'abs', 'sq' 중 하나")
        self.select_loss = select_loss
        self.val_fraction = float(val_fraction)
        self.min_fit_samples = int(min_fit_samples)
        self.min_val_samples = int(min_val_samples)
        self.train_window_days = None if train_window_days is None else int(train_window_days)
        self.y_clip = float(y_clip)
        # 학습 결과
        self.fitted = False
        self.series_id = None
        self.market = None
        self.feature_names = None
        self.column_names: list[str] = []
        self.coef = np.zeros(0)
        self.k_h = np.zeros(len(HORIZONS))
        self.lam = None
        self.usual_ratio = float('nan')  # log 배수의 평소 값
        self.switch_ords: list[int] = []
        self.event_days = None
        self.nan_counts = {'fit': {}, 'fit_samples': 0, 'predict': {}, 'predict_rows': 0}
        self.fit_info: dict = {}

    # ---- 항 만들기 -----------------------------------------------------------------------------------------

    def _group_terms(self):
        return self.terms[self.market]

    def _column(self, X, name):
        return X[:, self._idx[name]]

    def _build_terms(self, X, horizons, season, usual_ratio):
        """(표본 x 항) 행렬과 항 이름. nan 항은 0으로 두고, 항별 nan 개수를 함께 돌려준다."""
        cols, names = [], []
        scale_h = np.asarray(horizons, dtype=float) / 7.0

        def add(name, group, values):
            values = np.asarray(values, dtype=float)
            values = np.where(np.isfinite(values), values, np.nan)
            if group in self.h_scale_terms:
                values = values * scale_h
            cols.append(values)
            names.append(name)

        terms = self._group_terms()
        for group in TERM_GROUPS:  # 항 순서 고정
            if group not in terms:
                continue
            if group == 'transmission':
                for feature in self.transmission:
                    with np.errstate(invalid='ignore', divide='ignore'):
                        add(f'transmission:{feature}', group, np.log1p(self._column(X, feature)))
            elif group == 'ratio':
                with np.errstate(invalid='ignore', divide='ignore'):
                    add('ratio', group, np.log(self._column(X, 'target_counter_ratio')) - usual_ratio)
            elif group == 'season':
                add('season', group, season)
            elif group == 'event':
                for feature in self.event_features:
                    add(f'event:{feature}', group, self._column(X, feature))
            elif group == 'momentum':
                with np.errstate(invalid='ignore', divide='ignore'):
                    add('momentum', group, np.log1p(self._column(X, 'change7')))
        if not cols:
            return np.zeros((len(X), 0)), [], {}
        Z = np.column_stack(cols)
        nan_mask = np.isnan(Z)
        counts = {name: int(nan_mask[:, j].sum()) for j, name in enumerate(names)}
        return np.where(nan_mask, 0.0, Z), names, counts

    def _needed_features(self):
        need = ['current']
        terms = self._group_terms()
        if 'transmission' in terms:
            need += list(self.transmission)
        if 'ratio' in terms:
            need.append('target_counter_ratio')
        if 'event' in terms:
            need += list(self.event_features)
        if 'momentum' in terms:
            need.append('change7')
        if self.season_kind_tol is not None and 'season' in terms:
            need.append('days_since_kind_switch')
        if self.season_event_mask and 'season' in terms:
            need += ['target_in_event_window', 'days_to_major_holiday', 'days_from_major_holiday']
        return need

    def _setup_columns(self, feature_names):
        self.feature_names = list(feature_names)
        self._idx = {name: i for i, name in enumerate(self.feature_names)}
        missing = [n for n in self._needed_features() if n not in self._idx]
        if missing:
            raise ValueError(f'필요한 특징이 없음(extra_features 확인): {missing}')

    def _season_values(self, grid, origin_ord, horizons, X, kind_since):
        kind_now = self._column(X, 'days_since_kind_switch') if (
            self.season_kind_tol is not None and 'days_since_kind_switch' in self._idx) else None
        return season_analog(grid, origin_ord, horizons, self.season_years, self.season_weights,
                             kind_since, kind_now, self.season_kind_tol)

    def _past_event_hit(self, origin_ord, horizons):
        """비교 연도마다 b=o-364k와 b+h 중 하나라도 영향 기간이면 True(모르는 날은 False)."""
        hit = np.zeros(len(origin_ord), dtype=bool)
        for k in range(1, self.season_years + 1):
            base = origin_ord - SEASON_LAG_DAYS * k
            for day in (base, base + horizons):
                hit |= self.event_days.lookup(day) == 1
        return hit

    def _event_hit_fit(self, origin_ord, horizons, X):
        hit = self._past_event_hit(origin_ord, horizons)
        hit |= self.event_days.lookup(origin_ord) == 1  # 기준일 o
        hit |= self._column(X, 'target_in_event_window') == 1  # 목표일 o+h
        return hit

    def _event_hit_predict(self, origin_ord, horizons, X):
        o = np.full(len(horizons), origin_ord, dtype=np.int64)
        hit = self._past_event_hit(o, horizons)
        hit |= self._column(X, 'target_in_event_window') == 1
        flag_o = origin_event_flag(self.event_days, origin_ord, horizons, self._column(X, 'days_to_major_holiday'),
                                   self._column(X, 'days_from_major_holiday'))
        hit |= flag_o == 1
        return hit

    def _usual_ratio(self, X, origin_ord):
        """학습 표본 중 마지막 기준일에서 ratio_window_days일 안 기준일들의 log 배수 중앙값(기준일당 1개)."""
        if 'ratio' not in self._group_terms() or len(origin_ord) == 0:
            return float('nan')
        with np.errstate(invalid='ignore', divide='ignore'):
            logr = np.log(self._column(X, 'target_counter_ratio'))
        recent = origin_ord > origin_ord.max() - self.ratio_window_days
        uniq, first = np.unique(origin_ord[recent], return_index=True)
        values = logr[recent][first]
        values = values[np.isfinite(values)]
        return float(np.median(values)) if len(values) else float('nan')

    # ---- 학습 ----------------------------------------------------------------------------------------------

    def fit(self, history, seed: int) -> None:
        sid = int(history.series_id)
        if sid in self.retail_series:
            self.market = 'retail'
        elif sid in self.wholesale_series:
            self.market = 'wholesale'
        else:
            raise ValueError(f'소매·도매를 알 수 없는 계열: {sid}')
        self.series_id = sid
        self._setup_columns(history.feature_names)

        X = np.asarray(history.features, dtype=float)
        targets = np.asarray(history.targets, dtype=float).reshape(-1)
        horizons = np.asarray(history.horizons, dtype=int).reshape(-1)
        origin_ord = np.array([o.toordinal() for o in history.origins], dtype=np.int64)
        if X.ndim != 2 or X.shape != (len(targets), len(self.feature_names)):
            raise ValueError('학습 자료 모양이 맞지 않음')
        as_of_ord = history.as_of.toordinal()
        self.event_days = None
        if self.season_event_mask and 'season' in self._group_terms():  # 필터링 전 모든 학습 표본의 (목표일 -> 영향 기간)
            self.event_days = build_event_days(
                origin_ord + np.asarray(history.horizons, dtype=np.int64), self._column(X, 'target_in_event_window'),
                self._column(X, 'days_to_major_holiday'), self._column(X, 'days_from_major_holiday'),
                self.event_fill_days)
        current = self._column(X, 'current')
        with np.errstate(invalid='ignore', divide='ignore'):
            y = np.log(targets / current)
        keep = np.isfinite(y) & (current > 0) & (targets > 0)
        if self.train_window_days is not None:
            keep &= origin_ord > as_of_ord - self.train_window_days
        X, y, horizons, origin_ord = X[keep], y[keep], horizons[keep], origin_ord[keep]
        order = np.lexsort((horizons, origin_ord))  # 시간순(기준일, 시점)
        X, y, horizons, origin_ord = X[order], y[order], horizons[order], origin_ord[order]
        if len(y) < self.min_fit_samples:
            raise ValueError(f'학습 표본 {len(y)}개 < {self.min_fit_samples}')

        terms = self._group_terms()
        self.fit_info = {'samples': int(len(y)), 'market': self.market, 'terms': list(terms)}
        self.nan_counts = {'fit': {}, 'fit_samples': int(len(y)), 'predict': {}, 'predict_rows': 0}
        if not terms:  # 완전 naive
            self.column_names, self.coef = [], np.zeros(0)
            self.k_h = np.zeros(len(HORIZONS))
            self.lam, self.usual_ratio, self.switch_ords = 0.0, float('nan'), []
            self.fitted = True
            return

        # 작형 전환일 복원(학습 표본의 days_since_kind_switch만 사용)
        self.switch_ords = []
        if self.season_kind_tol is not None and 'days_since_kind_switch' in self._idx:
            since = self._column(X, 'days_since_kind_switch')
            known = since < KIND_SINCE_CAP
            self.switch_ords = sorted({int(o - s) for o, s in zip(origin_ord[known], since[known])})

        # 계절 항: 표본마다 그 기준일 이전 가격만 쓴다(재학습 기준일 이후 관측은 격자에 넣지 않음)
        grid = price_grid(history.prices, self.season_window, until_ord=as_of_ord)
        kind_since = kind_since_grid(grid, self.switch_ords) if self.season_kind_tol is not None else None
        season = (self._season_values(grid, origin_ord, horizons, X, kind_since)
                  if 'season' in terms else np.full(len(y), np.nan))
        masked = 0
        if self.event_days is not None:
            hit = self._event_hit_fit(origin_ord, horizons, X)
            masked = int((hit & ~np.isnan(season)).sum())
            season = np.where(hit, np.nan, season)
        self.fit_info['season_masked'] = masked

        # lambda·k 선택: 학습 표본의 마지막 20%(시간순, 기준일 기준)
        lam, k_h, selection = self._select(X, y, horizons, origin_ord, season)
        self.lam, self.k_h = lam, k_h

        # 전체 학습 표본으로 다시 맞춘다
        self.usual_ratio = self._usual_ratio(X, origin_ord)
        Z, names, counts = self._build_terms(X, horizons, season, self.usual_ratio)
        scale = self._scale(Z)
        self.coef = ridge_solve(Z / scale, y, lam) / scale
        self.column_names = names
        self.nan_counts['fit'] = counts
        self.fit_info.update(selection)
        self.fitted = True

    @staticmethod
    def _scale(Z):
        if Z.shape[1] == 0:
            return np.ones(0)
        rms = np.sqrt((Z ** 2).mean(axis=0))
        return np.where(rms > 1e-12, rms, 1.0)

    def _loss(self, err):
        """err = y - k*ŷ(로그). mape: 예측가/정답 = exp(-err)이므로 |exp(-err) - 1|(가격 MAPE와 같다)."""
        if self.select_loss == 'mape':
            return np.abs(np.expm1(-np.clip(err, -50, 50)))
        return np.abs(err) if self.select_loss == 'abs' else err ** 2

    def _k_grid_for_market(self):
        return self.retail_k_grid if (self.market == 'retail' and self.retail_k_grid is not None) else self.k_grid

    def _select(self, X, y, horizons, origin_ord, season):
        k_grid = self._k_grid_for_market()
        uniq = np.unique(origin_ord)
        cut = uniq[min(len(uniq) - 1, int(len(uniq) * (1 - self.val_fraction)))]
        fit_mask = (origin_ord < cut) & (origin_ord + horizons < cut)  # 검증 구간 정답이 학습에 섞이지 않게 거른다
        val_mask = origin_ord >= cut
        default = {'selection': 'fallback', 'lambda': float(self.lambda_grid[len(self.lambda_grid) // 2])}
        shared_k = float(self.k_grid[-1])
        if fit_mask.sum() < self.min_fit_samples or val_mask.sum() < self.min_val_samples:
            k_h = np.full(len(HORIZONS), shared_k)
            return default['lambda'], k_h, {**default, 'fit_n': int(fit_mask.sum()), 'val_n': int(val_mask.sum())}
        usual = self._usual_ratio(X[fit_mask], origin_ord[fit_mask])
        Zf, _, _ = self._build_terms(X[fit_mask], horizons[fit_mask], season[fit_mask], usual)
        Zv, _, _ = self._build_terms(X[val_mask], horizons[val_mask], season[val_mask], usual)
        scale = self._scale(Zf)
        yf, yv, hv = y[fit_mask], y[val_mask], horizons[val_mask]
        best = None
        for lam in self.lambda_grid:
            w = ridge_solve(Zf / scale, yf, lam) / scale
            pred = np.clip(Zv @ w, -self.y_clip, self.y_clip)
            if self.k_mode == 'shared':
                losses = [float(self._loss(yv - k * pred).mean()) for k in k_grid]
                j = int(np.argmin(losses))
                total, k_vec = losses[j], np.full(len(HORIZONS), k_grid[j])
            else:
                k_vec, total = np.zeros(len(HORIZONS)), 0.0
                for h in HORIZONS:
                    m = hv == h
                    if not m.any():
                        k_vec[h - 1] = shared_k
                        continue
                    losses = [float(self._loss(yv[m] - k * pred[m]).sum()) for k in k_grid]
                    j = int(np.argmin(losses))
                    k_vec[h - 1], total = k_grid[j], total + losses[j]
                total /= len(yv)
            if best is None or total < best[0] - 1e-15:
                best = (total, lam, k_vec)
        naive_loss = float(self._loss(yv).mean())
        info = {'selection': 'last_fraction', 'fit_n': int(fit_mask.sum()), 'val_n': int(val_mask.sum()),
                'val_loss': best[0], 'val_loss_naive': naive_loss}
        return best[1], best[2], info

    # ---- 예측 ----------------------------------------------------------------------------------------------

    def predict(self, inputs) -> list[float | None]:
        if not self.fitted:
            raise RuntimeError('fit을 먼저 불러야 함')
        if int(inputs.series_id) != self.series_id:
            raise ValueError('학습한 계열과 예측 입력 계열이 다름')
        if list(inputs.feature_names) != self.feature_names:
            raise ValueError('특징 이름이 학습 때와 다름')
        horizons = sorted(inputs.features)
        if horizons != list(HORIZONS):
            raise ValueError('시점 1~7이 필요함')
        X = np.asarray([inputs.features[h] for h in horizons], dtype=float)
        current = self._column(X, 'current')
        if not np.isfinite(current).all() or (current <= 0).any():
            raise ValueError('current가 유효하지 않음')
        if not self.column_names:  # naive
            return [float(c) for c in current]
        origin_ord = inputs.origin.toordinal()
        grid = price_grid(inputs.prices, self.season_window, until_ord=origin_ord)  # 기준일 이후 관측은 버림
        kind_since = kind_since_grid(grid, self.switch_ords) if self.season_kind_tol is not None else None
        o = np.full(len(horizons), origin_ord, dtype=np.int64)
        h = np.asarray(horizons, dtype=np.int64)
        season = (self._season_values(grid, o, h, X, kind_since) if 'season' in self._group_terms()
                  else np.full(len(h), np.nan))
        if self.event_days is not None:
            season = np.where(self._event_hit_predict(origin_ord, h, X), np.nan, season)
        self._last_season = season
        Z, names, counts = self._build_terms(X, h, season, self.usual_ratio)
        for name, c in counts.items():
            self.nan_counts['predict'][name] = self.nan_counts['predict'].get(name, 0) + c
        self.nan_counts['predict_rows'] += len(h)
        yhat = np.clip(Z @ self.coef, -self.y_clip, self.y_clip)
        out = []
        for c, k, v in zip(current, self.k_h, yhat):
            value = float(c * math.exp(k * v)) if math.isfinite(v) else float('nan')
            out.append(value if math.isfinite(value) else None)  # NaN·무한은 None(실행기가 실패로 기록, PRD §10)
        return out

    def season_values(self, inputs):
        """predict가 쓰는 계절 항 값(시점 1~7). 마스크되었거나 비교 연도가 없으면 nan(항은 0). 시험·점검용."""
        self.predict(inputs)
        return self._last_season.copy()

    # ---- 점검·보고용 ---------------------------------------------------------------------------------------

    def parameters(self) -> dict:
        """README 파라미터 표용 사본. a(전달) b(배수) c(계절) d(명절) e(모멘텀)은 원 단위 계수."""
        letter = {'transmission': 'a', 'ratio': 'b', 'season': 'c', 'event': 'd', 'momentum': 'e'}
        coef = {}
        for name, value in zip(self.column_names, self.coef):
            key = letter[name.split(':')[0]]
            coef[f'{key}:{name.split(":", 1)[1]}' if ':' in name else key] = float(value)
        return {'series_id': self.series_id, 'market': self.market, 'terms': list(self._group_terms()),
                'coef': coef, 'k_h': [float(v) for v in self.k_h], 'lambda': self.lam,
                'usual_log_ratio': self.usual_ratio,
                'usual_ratio': float(math.exp(self.usual_ratio)) if math.isfinite(self.usual_ratio) else None,
                'n_params': int(len(self.coef)), 'nan_counts': self.nan_counts, 'fit_info': self.fit_info}
