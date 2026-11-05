"""외부 원천을 예측 시점 기준으로 특징화한다. DB에 의존하지 않는다.

그룹(특징 묶음)과 원천:
- WHOLESALE: KAMIS 전국 도매가(external_observation)
- WEATHER: 검증된 주산지 ASOS 관측소(external_observation)
- CALENDAR: 천문연 공휴일(external_observation)
- NATIONAL_WEATHER: weather_daily(ACTUAL) 전국 평균·폭염/호우/한파 관측소 비율
- EVENT: calendar_event 설날·추석 영향 기간과 과거 명절 기간의 가격 압력(event_weight)
- SEASONAL: price_change_history의 과거 같은 시기 1~7일 변동률
- PRODUCTION: item_production 연간 전국 생산량의 전년 대비 증감
- FX: exchange_rate_daily 원/미국달러 변화율

시점 규칙: 예측 시작일 d의 입력은 d - 공개지연일 이하에 관측된 값만 사용한다.
- 도매가·ASOS·전국 기상·환율: 1일 지연(배치 시각에 당일 값이 공표되지 않았을 수 있어 보수적으로 둔다).
- 공휴일·명절 기간: 목표일(d+h)의 달력. 법정공휴일은 미리 확정되므로 미래 값으로 사용한다.
- 과거 변동률: 기준일 b, 시점 h의 변동률은 b+h일 가격이 확인된 뒤(b+h <= d)에만 사용한다.
- 연간 생산량: Y년 값은 Y+1년 6월 30일부터 사용한다(공표일을 받지 못해 둔 가정).
값이 없으면 NaN으로 두고 XGBoost의 결측 분기에 맡긴다. 결측을 임의 값으로 채우지 않는다.
"""
import math
from dataclasses import dataclass, field
from datetime import date, timedelta
from statistics import mean, stdev

WHOLESALE_LAG_DAYS = 1
WEATHER_LAG_DAYS = 1
FX_LAG_DAYS = 1
MAX_STALE_DAYS = 7
HOLIDAY_WINDOW_DAYS = 45
MAJOR_HOLIDAYS = ('설날', '추석')
SEASONAL_YEARS = 5  # 과거 같은 시기 변동률은 최근 5년까지
SEASONAL_SPAN_DAYS = 3  # 같은 시기 = 월·일 기준 ±3일
SEASONAL_MIN_YEARS = 2
EVENT_BASELINE_DAYS = 60  # 명절 효과 = 영향 기간 7일 변동률 평균 - 직전 60일 평균
EVENT_MIN_SAMPLES = 5
EVENT_MIN_YEARS = 2
EVENT_SCALE = 0.10  # 7일 변동률 10%p 차이를 tanh(1)≈0.76 압력으로 본다
PRODUCTION_AVAILABLE = (6, 30)  # Y년 생산량은 Y+1년 6월 30일부터
NAN = float('nan')

WHOLESALE_FEATURES = ['wholesaleLast', 'retailWholesaleRatio', 'wholesaleChange7', 'wholesaleChange28', 'wholesaleAge']
WEATHER_FEATURES = ['tempMean7', 'tempMax7', 'tempMin7', 'rainSum7', 'rainSum28', 'humidityMean7', 'sunshineSum7']
CALENDAR_FEATURES = ['targetIsHoliday', 'daysToMajorHoliday', 'daysFromMajorHoliday']
NATIONAL_WEATHER_FEATURES = ['natTempMean7', 'natRainSum28', 'natHeatIndex7', 'natHeatIndex28',
                             'natHeavyRainIndex28', 'natColdIndex28']
EVENT_FEATURES = ['targetInEventWindow', 'eventPressure']
SEASONAL_FEATURES = ['seasonalChange']
PRODUCTION_FEATURES = ['productionYoY']
FX_FEATURES = ['usdKrwChange7', 'usdKrwChange28']

GROUP_FEATURES = {'WHOLESALE': WHOLESALE_FEATURES, 'WEATHER': WEATHER_FEATURES, 'CALENDAR': CALENDAR_FEATURES,
                  'NATIONAL_WEATHER': NATIONAL_WEATHER_FEATURES, 'EVENT': EVENT_FEATURES,
                  'SEASONAL': SEASONAL_FEATURES, 'PRODUCTION': PRODUCTION_FEATURES, 'FX': FX_FEATURES}
# 목표일(시점)에 따라 값이 달라지는 그룹. 나머지는 예측 시작일에만 의존한다.
TARGET_GROUPS = {'CALENDAR', 'EVENT', 'SEASONAL'}
# 가중치 학습 단위. 서로 강하게 연관된 그룹은 하나의 묶음으로 같은 가중치를 받는다.
BLOCKS = {'MARKET': ('WHOLESALE',), 'WEATHER': ('WEATHER', 'NATIONAL_WEATHER'), 'CALENDAR': ('CALENDAR', 'EVENT'),
          'SEASONAL': ('SEASONAL',), 'MACRO': ('PRODUCTION', 'FX')}


@dataclass(frozen=True)
class EventWindow:
    code: str
    start: date
    end: date
    effect_start: date
    effect_end: date


@dataclass
class Covariates:
    wholesale: dict[date, float] = field(default_factory=dict)
    # 날짜별 주산지 관측소 가중 평균. 키: avgTa, minTa, maxTa, sumRn, avgRhm, sumSsHr
    weather: dict[date, dict[str, float | None]] = field(default_factory=dict)
    holidays: dict[date, str] = field(default_factory=dict)
    holiday_years: set[int] = field(default_factory=set)
    # weather_daily(ACTUAL). 키: avgTemp, precipitation, heatRatio, heavyRainRatio, coldRatio (비율은 %)
    national_weather: dict[date, dict[str, float | None]] = field(default_factory=dict)
    events: list[EventWindow] = field(default_factory=list)
    # price_change_history. 시점(1~7) → 기준일 → 변동률(분율, 0.05 = 5%)
    change_history: dict[int, dict[date, float]] = field(default_factory=dict)
    production: dict[int, float] = field(default_factory=dict)  # 연도 → 톤
    fx: dict[date, float] = field(default_factory=dict)  # 원/미국달러

    def empty(self):
        return not (self.wholesale or self.weather or self.holiday_years or self.national_weather or self.events
                    or any(self.change_history.values()) or self.production or self.fx)


def _finite(value):
    return value is not None and not (isinstance(value, float) and math.isnan(value))


def event_weight(changes7: dict[date, float], windows: list[EventWindow], as_of: date):
    """명절 영향 기간의 가격 압력(-1~1). as_of에 이미 확인된 과거 명절만 사용한다.

    연도별 효과 = 영향 기간 기준일의 7일 변동률 평균 - 직전 60일 평균(같은 해의 평소 흐름을 뺌).
    연도 간 평균을 양의 James-Stein 계수 max(0, 1 - se²/평균²)로 0 쪽으로 줄인다.
    해마다 방향이 엇갈리면(se가 크면) 0이 된다. 마지막으로 tanh(효과/10%p)로 -1~1에 담는다.
    표본이 2개 연도 미만이면 None.
    """
    effects = []
    for window in windows:
        if window.effect_end + timedelta(days=7) > as_of:
            continue  # 영향 기간의 7일 뒤 가격까지 확인돼야 쓴다.
        inside = [v for d, v in changes7.items() if window.effect_start <= d <= window.effect_end]
        before = [v for d, v in changes7.items()
                  if window.effect_start - timedelta(days=EVENT_BASELINE_DAYS) <= d < window.effect_start]
        if len(inside) >= EVENT_MIN_SAMPLES and len(before) >= EVENT_MIN_SAMPLES:
            effects.append(mean(inside) - mean(before))
    if len(effects) < EVENT_MIN_YEARS:
        return None
    effect = mean(effects)
    if effect == 0:
        return 0.0
    se2 = stdev(effects) ** 2 / len(effects)
    shrunk = effect * max(0.0, 1 - se2 / effect ** 2)
    return math.tanh(shrunk / EVENT_SCALE)


class ExogenousFeatures:
    def __init__(self, days: list[date], values: list[float | None], covariates: Covariates):
        self.days, self.values, self.cov = days, values, covariates
        present = {'WHOLESALE': covariates.wholesale, 'WEATHER': covariates.weather,
                   'CALENDAR': covariates.holiday_years, 'NATIONAL_WEATHER': covariates.national_weather,
                   'EVENT': covariates.events and covariates.holiday_years,
                   'SEASONAL': any(covariates.change_history.values()), 'PRODUCTION': covariates.production,
                   'FX': covariates.fx}
        self.groups = [group for group in GROUP_FEATURES if present[group]]
        self.names = [name for group in self.groups for name in GROUP_FEATURES[group]]
        self.blocks = {block: [g for g in members if g in self.groups] for block, members in BLOCKS.items()
                       if any(g in self.groups for g in members)}
        self._wholesale = self._forward_fill(covariates.wholesale) if covariates.wholesale else {}
        self._fx = self._forward_fill(covariates.fx) if covariates.fx else {}
        self._majors = sorted(day for day, name in covariates.holidays.items()
                              if any(key in name for key in MAJOR_HOLIDAYS))
        self._changes7 = covariates.change_history.get(7, {})
        self._origin_cache, self._target_cache, self._pressure_cache = {}, {}, {}

    def _forward_fill(self, series):
        """날짜별 (최근 관측값, 관측일). 원천 결측은 최대 MAX_STALE_DAYS까지만 이어 쓴다."""
        start = min(self.days[0] - timedelta(days=40), min(series))
        end = self.days[-1]
        filled, last = {}, None
        for offset in range((end - start).days + 1):
            day = start + timedelta(days=offset)
            if day in series:
                last = (series[day], day)
            if last and (day - last[1]).days <= MAX_STALE_DAYS:
                filled[day] = last
        return filled

    @staticmethod
    def _filled(series, day):
        hit = series.get(day)
        return hit[0] if hit else None

    # ------------------------------------------------------------ 예측 시작일에만 의존하는 그룹
    def _wholesale_features(self, origin):
        as_of = self.days[origin] - timedelta(days=WHOLESALE_LAG_DAYS)
        hit = self._wholesale.get(as_of)
        if not hit:
            return [NAN] * len(WHOLESALE_FEATURES)
        price, observed = hit
        week = self._filled(self._wholesale, as_of - timedelta(days=7))
        month = self._filled(self._wholesale, as_of - timedelta(days=28))
        current = self.values[origin]
        return [price, current / price if current and price else NAN,
                price / week - 1 if week else NAN, price / month - 1 if month else NAN,
                float((self.days[origin] - observed).days)]

    def _weather_features(self, origin):
        as_of = self.days[origin] - timedelta(days=WEATHER_LAG_DAYS)
        rows = [self.cov.weather.get(as_of - timedelta(days=k)) for k in range(28)]

        def column(name, span):
            return [row[name] for row in rows[:span] if row and _finite(row.get(name))]

        def avg(name, span=7, minimum=5):
            data = column(name, span)
            return mean(data) if len(data) >= minimum else NAN

        def total(name, span, minimum):
            data = column(name, span)
            return mean(data) * span if len(data) >= minimum else NAN  # 일부 결측은 평균으로 기간 합을 환산

        maxima, minima = column('maxTa', 7), column('minTa', 7)
        return [avg('avgTa'), max(maxima) if len(maxima) >= 5 else NAN, min(minima) if len(minima) >= 5 else NAN,
                total('sumRn', 7, 5), total('sumRn', 28, 20), avg('avgRhm'), total('sumSsHr', 7, 5)]

    def _national_weather_features(self, origin):
        """전국 평균 기온·강수와 극한 기상 지수. 지수 = 기간 중 (해당 기준을 넘은 관측소 비율)의 일별 합.

        예: 28일 중 3일 동안 관측소 절반이 호우였다면 natHeavyRainIndex28 = 1.5. 피해의 넓이와 지속을 함께 본다.
        """
        as_of = self.days[origin] - timedelta(days=WEATHER_LAG_DAYS)
        rows = [self.cov.national_weather.get(as_of - timedelta(days=k)) for k in range(28)]

        def column(name, span):
            return [row[name] for row in rows[:span] if row and _finite(row.get(name))]

        def total(name, span, scale=1.0):
            data = column(name, span)
            return mean(data) * span * scale if len(data) >= span * .7 else NAN

        temps = column('avgTemp', 7)
        return [mean(temps) if len(temps) >= 5 else NAN, total('precipitation', 28),
                total('heatRatio', 7, .01), total('heatRatio', 28, .01),
                total('heavyRainRatio', 28, .01), total('coldRatio', 28, .01)]

    def _production_features(self, origin):
        day = self.days[origin]
        month, dom = PRODUCTION_AVAILABLE
        known = [year for year in self.cov.production if day >= date(year + 1, month, dom)]
        if not known:
            return [NAN]
        latest = max(known)
        previous = self.cov.production.get(latest - 1)
        return [self.cov.production[latest] / previous - 1 if previous else NAN]

    def _fx_features(self, origin):
        as_of = self.days[origin] - timedelta(days=FX_LAG_DAYS)
        rate = self._filled(self._fx, as_of)
        week = self._filled(self._fx, as_of - timedelta(days=7))
        month = self._filled(self._fx, as_of - timedelta(days=28))
        return [rate / week - 1 if rate and week else NAN, rate / month - 1 if rate and month else NAN]

    # ------------------------------------------------------------ 목표일에 의존하는 그룹
    def _calendar_features(self, target: date):
        years = self.cov.holiday_years
        window = timedelta(days=HOLIDAY_WINDOW_DAYS)
        if target.year not in years:
            return [NAN] * len(CALENDAR_FEATURES)
        after = [(day - target).days for day in self._majors if target <= day <= target + window]
        before = [(target - day).days for day in self._majors if target - window <= day <= target]
        to_major = min(after) if after else HOLIDAY_WINDOW_DAYS if (target + window).year in years else NAN
        from_major = min(before) if before else HOLIDAY_WINDOW_DAYS if (target - window).year in years else NAN
        return [1.0 if target in self.cov.holidays else 0.0, float(to_major), float(from_major)]

    def pressure(self, code: str, as_of: date):
        usable = tuple(w for w in self.cov.events if w.code == code and w.effect_end + timedelta(days=7) <= as_of)
        if usable not in self._pressure_cache:
            self._pressure_cache[usable] = event_weight(self._changes7, list(usable), as_of)
        return self._pressure_cache[usable]

    def _event_features(self, origin_day: date, target: date):
        if target.year not in self.cov.holiday_years:
            return [NAN] * len(EVENT_FEATURES)
        window = next((w for w in self.cov.events if w.effect_start <= target <= w.effect_end), None)
        if window is None:
            return [0.0, 0.0]
        weight = self.pressure(window.code, origin_day)
        return [1.0, NAN if weight is None else weight]

    def _seasonal_features(self, origin_day: date, horizon: int):
        """과거 해의 같은 시기(월·일 ±3일)에 같은 시점으로 본 변동률의 연도 평균의 평균."""
        changes = self.cov.change_history.get(horizon, {})
        month, dom = (2, 28) if (origin_day.month, origin_day.day) == (2, 29) else (origin_day.month, origin_day.day)
        yearly = []
        for back in range(1, SEASONAL_YEARS + 1):
            center = date(origin_day.year - back, month, dom)
            rows = [changes[d] for d in (center + timedelta(days=k) for k in range(-SEASONAL_SPAN_DAYS, SEASONAL_SPAN_DAYS + 1))
                    if d in changes and d + timedelta(days=horizon) <= origin_day]
            if rows:
                yearly.append(mean(rows))
        return [mean(yearly) if len(yearly) >= SEASONAL_MIN_YEARS else NAN]

    def _origin_group(self, group, origin):
        key = (group, origin)
        if key not in self._origin_cache:
            self._origin_cache[key] = {'WHOLESALE': self._wholesale_features, 'WEATHER': self._weather_features,
                                       'NATIONAL_WEATHER': self._national_weather_features,
                                       'PRODUCTION': self._production_features, 'FX': self._fx_features}[group](origin)
        return self._origin_cache[key]

    def _target_group(self, group, origin, horizon):
        key = (group, origin, horizon)
        if key not in self._target_cache:
            origin_day = self.days[origin]
            target = origin_day + timedelta(days=horizon)
            if group == 'CALENDAR':
                row = self._calendar_features(target)
            elif group == 'EVENT':
                row = self._event_features(origin_day, target)
            else:
                row = self._seasonal_features(origin_day, horizon)
            self._target_cache[key] = row
        return self._target_cache[key]

    def group_vector(self, origin: int, horizon: int, groups):
        row = []
        for group in self.groups:
            if group in groups:
                row += (self._target_group(group, origin, horizon) if group in TARGET_GROUPS
                        else self._origin_group(group, origin))
        return row

    def vector(self, origin: int, horizon: int):
        return self.group_vector(origin, horizon, self.groups)

    def block_names(self, block):
        return [name for group in self.blocks[block] for name in GROUP_FEATURES[group]]

    def coverage(self, origins):
        """평가 시점 중 그룹별 첫 특징이 실제 값으로 채워진 비율."""
        if not origins:
            return {}
        return {group: round(sum(_finite(self.group_vector(origin, 1, {group})[0]) for origin in origins) / len(origins), 4)
                for group in self.groups}
