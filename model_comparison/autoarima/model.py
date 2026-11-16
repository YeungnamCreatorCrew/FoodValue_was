"""FoodValue AutoARIMA — 계열별 statsforecast AutoARIMA (기준서 §5.1 AutoARIMA, §5.2 EVENT, §6).

계열 구성: (a) 달력일 계열, 앞채움 최대 7일, 계절 주기 m=7.
  (b) 조사일 계열(m=5)은 스냅샷 manifest에 "주말 미관측 확인" 기록이 있어야 허용되는데
  fv-snap-20261031-v1 manifest에는 그 기록이 없어 구현하지 않는다(README_MODEL.md).

재학습·갱신(§3.4)
- fit(주 1회): 학습 창의 실제 관측으로 달력일 계열을 만들고 차수 탐색 + 계수 추정.
- predict(매 기준일): 같은 차수·계수로 d까지의 새 관측을 넣어 상태만 갱신(statsforecast `forward`)한 뒤 7일 예측.
  차수 재탐색·계수 재추정은 하지 않는다.

외생변수(X)
- 달력: 요일 더미(월요일 기준 6개), 목표일 연중 계절 sin/cos. 모두 날짜만으로 정해지는 값이고 loader와 같은 식.
  미래 7일 값은 inputs.features의 target_weekday·target_season_sin/cos와 같은지 확인한 뒤 쓴다.
- EVENT(2차): 공통 로더가 주는 EVENT 열(history.features·inputs.features, 목표일 기준 값)에서 날짜별 값을 모은다.
  학습 표본의 목표일은 실제 관측일뿐이라 주말·휴장일 값이 비므로, 같은 열에서 명절 시작·끝 날짜를 되살려
  days_to/from은 그대로 다시 계산하고, 영향 기간 여부·전날 공휴일 여부는 README_MODEL.md의 규칙으로 채운다.
  스냅샷 파일은 읽지 않는다.

결측: 앞채움 7일로도 채워지지 않는 긴 공백(학습 창 안, 양 끝 모두 기준일 이전 관측)은 선형 보간한다.
실패는 예외로 올리고 naive로 바꾸지 않는다(공통 평가기가 policy에서 처리).
"""
import math
import warnings
from datetime import date, timedelta

import numpy as np

HORIZON = 7
FORWARD_FILL_DAYS = 7
MAX_WINDOW_DAYS = 1825
EVENT_COLUMNS = ('days_to_major_holiday', 'days_from_major_holiday', 'target_in_event_window',
                 'target_prev_day_holiday')
HOLIDAY_CAP = 45
CALENDAR_OPTIONS = ('none', 'weekday', 'season', 'weekday+season')


def daily_series(prices, end: date, window_days: int):
    """(날짜, 가격) 관측 → end까지 달력일 배열(앞채움 최대 7일, 남는 공백은 선형 보간). 반환: (시작일, 값 배열)."""
    obs = sorted((d, float(p)) for d, p in prices if d <= end)
    if not obs:
        raise ValueError('관측이 없음')
    start = max(obs[0][0], end - timedelta(days=window_days - 1))
    obs = [(d, p) for d, p in obs if d >= start]
    start = obs[0][0]
    n = (end - start).days + 1
    actual = np.full(n, np.nan)
    for d, p in obs:
        actual[(d - start).days] = p
    idx = np.arange(n)
    last = np.maximum.accumulate(np.where(~np.isnan(actual), idx, -1))
    age = idx - last
    values = np.where(age <= FORWARD_FILL_DAYS, actual[last], np.nan)
    if np.isnan(values).any():  # 긴 공백: 양 끝 실제 관측 사이 선형 보간(끝 쪽 공백은 위 age 검사로 기준일 NO_INPUT 처리됨)
        known = ~np.isnan(values)
        values = np.interp(idx, idx[known], values[known])
    return start, values


def calendar_matrix(days, option: str):
    cols = []
    if 'weekday' in option:
        wd = np.array([d.weekday() for d in days])
        cols += [(wd == k).astype(float) for k in range(1, 7)]
    if 'season' in option:
        season = np.array([2 * math.pi * d.timetuple().tm_yday / 365.25 for d in days])
        cols += [np.sin(season), np.cos(season)]
    return np.column_stack(cols) if cols else None


class EventCalendar:
    """공통 입력의 EVENT 열(목표일 → 4개 값)을 모아 임의 날짜의 값을 돌려준다."""

    def __init__(self):
        self.known: dict[date, tuple] = {}

    def add(self, day: date, row):
        self.known.setdefault(day, tuple(float(v) for v in row))

    def _events(self):
        starts, ends = set(), set()
        for day, (to_major, from_major, _, _) in self.known.items():
            if 0 < to_major < HOLIDAY_CAP:
                starts.add(day + timedelta(days=int(to_major)))
            if 0 < from_major < HOLIDAY_CAP:
                ends.add(day - timedelta(days=int(from_major)))
        events = []
        for s in sorted(starts):
            later = [e for e in ends if s <= e <= s + timedelta(days=10)]
            if later:
                events.append((s, min(later)))
        return events

    def matrix(self, days):
        if len(self.known) != getattr(self, '_cache_size', -1):  # 새 값이 들어오면 재구성 결과를 다시 만든다
            self._cache, self._cache_size = {}, len(self.known)
            self._event_list = self._events()
            self._known_days = sorted(self.known)
            self._known_array = np.array(self._known_days, dtype='datetime64[D]')
        events, known_days = self._event_list, self._known_days
        out = np.zeros((len(days), 4))
        for r, t in enumerate(days):
            if t in self.known:
                out[r] = self.known[t]
                continue
            if t in self._cache:
                out[r] = self._cache[t]
                continue
            to_major = from_major = HOLIDAY_CAP
            for s, e in events:
                if s <= t <= e:
                    to_major = from_major = 0
                elif t < s:
                    to_major = min(to_major, (s - t).days)
                else:
                    from_major = min(from_major, (t - e).days)
            # 영향 기간: 앞뒤로 가장 가까운 알려진 날의 값이 같으면 그 값, 다르면 앞쪽 값
            pos = np.searchsorted(self._known_array, np.datetime64(t))
            before = self.known[known_days[pos - 1]][2] if pos > 0 else 0.0
            in_window = before
            # 전날 공휴일(평일): 되살린 명절 기간의 평일만 알 수 있다
            prev = t - timedelta(days=1)
            prev_holiday = float(prev.weekday() < 5 and any(s <= prev <= e for s, e in events))
            out[r] = self._cache[t] = (min(to_major, HOLIDAY_CAP), min(from_major, HOLIDAY_CAP), in_window, prev_holiday)
        return out


class AutoARIMAModel:
    def __init__(self, transform='log', seasonal=True, season_length=7, calendar_exog='none', event_exog=False,
                 window_days=MAX_WINDOW_DAYS, max_p=5, max_q=5, max_P=2, max_Q=2, max_d=2, max_D=1, stepwise=True,
                 approximation=False, ic='aicc', n_jobs=1, series_mode='calendar_day'):
        if series_mode != 'calendar_day':
            raise ValueError("series_mode는 'calendar_day'(a)만 허용(조사일 계열 (b)는 manifest 조건 미충족)")
        if season_length != 7:
            raise ValueError('달력일 계열의 계절 주기는 7')
        if transform not in ('level', 'log'):
            raise ValueError("transform은 'level' 또는 'log'")
        if calendar_exog not in CALENDAR_OPTIONS:
            raise ValueError(f'calendar_exog는 {CALENDAR_OPTIONS} 중 하나')
        if not (max_p <= 5 and max_q <= 5 and max_P <= 2 and max_Q <= 2):
            raise ValueError('탐색 범위는 p, q ≤ 5, P, Q ≤ 2(§6)')
        if n_jobs != 1:
            raise ValueError('n_jobs=1 고정(§1.1)')
        if not 1 <= window_days <= MAX_WINDOW_DAYS:
            raise ValueError('window_days는 1~1825')
        self.transform, self.seasonal, self.calendar_exog = transform, bool(seasonal), calendar_exog
        self.event_exog, self.window_days = bool(event_exog), int(window_days)
        self.search = dict(max_p=max_p, max_q=max_q, max_P=max_P, max_Q=max_Q, max_d=max_d, max_D=max_D,
                           stepwise=stepwise, approximation=approximation, ic=ic,
                           seasonal=self.seasonal, season_length=season_length if self.seasonal else 1)
        self.model = None
        self.series_id = None
        self.events = EventCalendar()

    # ---- 변환 -------------------------------------------------------------------------------------
    def _to_model(self, values):
        return np.log(values) if self.transform == 'log' else values

    def _from_model(self, values):
        return np.exp(values) if self.transform == 'log' else values

    def _exog(self, days):
        parts = []
        cal = calendar_matrix(days, self.calendar_exog)
        if cal is not None:
            parts.append(cal)
        if self.event_exog:
            parts.append(self.events.matrix(days))
        return np.column_stack(parts) if parts else None

    def _collect_events(self, feature_names, rows_with_dates):
        if not self.event_exog:
            return
        missing = [c for c in EVENT_COLUMNS if c not in feature_names]
        if missing:
            raise ValueError(f'EVENT 열이 공통 입력에 없음: {missing} (extra_features에 "EVENT" 필요)')
        cols = [feature_names.index(c) for c in EVENT_COLUMNS]
        for day, row in rows_with_dates:
            self.events.add(day, np.asarray(row, dtype=float)[cols])

    # ---- 인터페이스 --------------------------------------------------------------------------------
    def fit(self, history, seed: int) -> None:
        from statsforecast.models import AutoARIMA

        self.series_id = history.series_id
        self.feature_names = list(history.feature_names)
        if self.event_exog:
            names = self.feature_names
            features = np.asarray(history.features, dtype=float)
            targets = [o + timedelta(days=int(h)) for o, h in zip(history.origins, history.horizons)]
            self._collect_events(names, zip(targets, features))
        start, values = daily_series(history.prices, history.as_of, self.window_days)
        days = [start + timedelta(days=i) for i in range(len(values))]
        y = self._to_model(values)
        model = AutoARIMA(**self.search)
        with warnings.catch_warnings():  # 최적화 수렴 경고는 결과에 영향 없이 로그만 늘린다
            warnings.simplefilter('ignore', UserWarning)
            model.fit(y, X=self._exog(days))
        self.model = model
        self.fit_as_of = history.as_of

    def predict(self, inputs) -> list[float | None]:
        if self.model is None:
            raise RuntimeError('fit 전에 predict 호출')
        if inputs.series_id != self.series_id:
            raise ValueError('다른 계열의 입력')
        if inputs.origin < self.fit_as_of:
            raise ValueError('학습 기준일 이전 기준일')
        if sorted(inputs.features) != list(range(1, HORIZON + 1)):
            raise ValueError('시점 1~7 특징이 필요')
        d = inputs.origin
        targets = [d + timedelta(days=h) for h in range(1, HORIZON + 1)]
        names = list(inputs.feature_names)
        self._check_calendar(names, inputs.features, targets)
        self._collect_events(names, [(t, inputs.features[h]) for h, t in zip(range(1, HORIZON + 1), targets)])

        start, values = daily_series(inputs.prices, d, self.window_days)
        days = [start + timedelta(days=i) for i in range(len(values))]
        y = self._to_model(values)
        X, X_future = self._exog(days), self._exog(targets)
        # 같은 차수·계수로 d까지의 관측을 걸러 상태만 갱신한 뒤 예측(계수 재추정 없음)
        with warnings.catch_warnings():
            warnings.simplefilter('ignore', UserWarning)
            out = self.model.forward(y=y, h=HORIZON, X=X, X_future=X_future)
        mean = np.asarray(out['mean'], dtype=float)
        return [float(v) for v in self._from_model(mean)]

    def _check_calendar(self, names, features, targets):
        """미래 달력값이 공통 입력(target_weekday·target_season_sin/cos)과 같은지 확인한다."""
        if 'target_weekday' not in names:
            return
        iw, isin = names.index('target_weekday'), names.index('target_season_sin')
        for h, t in zip(range(1, HORIZON + 1), targets):
            row = features[h]
            if int(row[iw]) != t.weekday() or abs(row[isin] - math.sin(2 * math.pi * t.timetuple().tm_yday / 365.25)) > 1e-9:
                raise ValueError(f'달력 외생변수가 공통 입력과 다름: {t}')

    def describe(self):
        """선택된 차수(로그·점검용)."""
        if self.model is None:
            return None
        from statsforecast.arima import arima_string
        return arima_string(self.model.model_)
