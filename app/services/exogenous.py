"""외부 원천(도매가·주산지 기상·공휴일)을 예측 시점 기준으로 특징화한다. DB에 의존하지 않는다.

시점 규칙: 예측 시작일 d의 입력은 d - 공개지연일 이하에 관측된 값만 사용한다.
- KAMIS 도매가: 1일 지연. 배치 시각에 당일 도매가가 아직 공표되지 않았을 수 있어 보수적으로 둔다.
- ASOS 일자료: 1일 지연. 기상청은 전일까지의 일자료를 제공한다.
- 공휴일: 목표일(d+h)의 달력. 법정공휴일은 미리 확정되므로 미래 값으로 사용한다.
값이 없으면 NaN으로 두고 XGBoost의 결측 분기에 맡긴다. 결측을 임의 값으로 채우지 않는다.
"""
import math
from dataclasses import dataclass, field
from datetime import date, timedelta
from statistics import mean

WHOLESALE_LAG_DAYS = 1
WEATHER_LAG_DAYS = 1
MAX_STALE_DAYS = 7
HOLIDAY_WINDOW_DAYS = 45
MAJOR_HOLIDAYS = ('설날', '추석')
NAN = float('nan')

WHOLESALE_FEATURES = ['wholesaleLast', 'retailWholesaleRatio', 'wholesaleChange7', 'wholesaleChange28', 'wholesaleAge']
WEATHER_FEATURES = ['tempMean7', 'tempMax7', 'tempMin7', 'rainSum7', 'rainSum28', 'humidityMean7', 'sunshineSum7']
CALENDAR_FEATURES = ['targetIsHoliday', 'daysToMajorHoliday', 'daysFromMajorHoliday']


@dataclass
class Covariates:
    wholesale: dict[date, float] = field(default_factory=dict)
    # 날짜별 주산지 관측소 가중 평균. 키: avgTa, minTa, maxTa, sumRn, avgRhm, sumSsHr
    weather: dict[date, dict[str, float | None]] = field(default_factory=dict)
    holidays: dict[date, str] = field(default_factory=dict)
    holiday_years: set[int] = field(default_factory=set)

    def empty(self):
        return not (self.wholesale or self.weather or self.holiday_years)


def _finite(value):
    return value is not None and not (isinstance(value, float) and math.isnan(value))


class ExogenousFeatures:
    def __init__(self, days: list[date], values: list[float | None], covariates: Covariates):
        self.days, self.values, self.cov = days, values, covariates
        self.groups = [name for name, present in (('WHOLESALE', covariates.wholesale), ('WEATHER', covariates.weather),
                                                  ('CALENDAR', covariates.holiday_years)) if present]
        self.names = ((WHOLESALE_FEATURES if 'WHOLESALE' in self.groups else []) +
                      (WEATHER_FEATURES if 'WEATHER' in self.groups else []) +
                      (CALENDAR_FEATURES if 'CALENDAR' in self.groups else []))
        self._wholesale = self._forward_fill(covariates.wholesale) if covariates.wholesale else {}
        self._majors = sorted(day for day, name in covariates.holidays.items()
                              if any(key in name for key in MAJOR_HOLIDAYS))
        self._origin_cache = {}

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

    def _wholesale_at(self, day):
        hit = self._wholesale.get(day)
        return hit[0] if hit else None

    def _wholesale_features(self, origin):
        as_of = self.days[origin] - timedelta(days=WHOLESALE_LAG_DAYS)
        hit = self._wholesale.get(as_of)
        if not hit:
            return [NAN] * len(WHOLESALE_FEATURES)
        price, observed = hit
        week, month = self._wholesale_at(as_of - timedelta(days=7)), self._wholesale_at(as_of - timedelta(days=28))
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

    def vector(self, origin: int, horizon: int):
        if origin not in self._origin_cache:
            row = []
            if 'WHOLESALE' in self.groups:
                row += self._wholesale_features(origin)
            if 'WEATHER' in self.groups:
                row += self._weather_features(origin)
            self._origin_cache[origin] = row
        row = list(self._origin_cache[origin])
        if 'CALENDAR' in self.groups:
            row += self._calendar_features(self.days[origin] + timedelta(days=horizon))
        return row

    def coverage(self, origins):
        """평가 시점 중 그룹별 첫 특징이 실제 값으로 채워진 비율."""
        if not origins:
            return {}
        result, offset = {}, 0
        for group, names in (('WHOLESALE', WHOLESALE_FEATURES), ('WEATHER', WEATHER_FEATURES), ('CALENDAR', CALENDAR_FEATURES)):
            if group not in self.groups:
                continue
            filled = sum(_finite(self.vector(origin, 1)[offset]) for origin in origins)
            result[group] = round(filled / len(origins), 4)
            offset += len(names)
        return result
