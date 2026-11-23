"""같은 시기 대비 가격 (SEASONAL). 방향을 주장하지 않는 사실 카드(FACT).

- 이번 구간 = 기준일까지 최근 SEASONAL_WINDOW_DAYS(28)일의 평균 가격.
- 평년 = 과거 5개 연도 각각의 '같은 날짜 기준 28일 구간' 평균의 평균. 기준 연도의 값은 평년에 넣지 않는다.
  달력 월 대신 구간을 쓰는 이유: 월초에 관측이 며칠뿐이면 값이 크게 흔들리고(월 경계 평균 9%p 점프) 방향을 비워야 했다.
- 평년 대비 = 이번 구간 평균 / 평년 - 1. 싼 편/비싼 편은 SEASONAL_BAND 밖일 때만, 이번 구간 관측일이 적으면 방향 없음.
- 구간 관측이 SEASONAL_MIN_WINDOW_OBS일 미만인 과거 연도는 평년·비교에서 뺀다(5개 연도가 모자라면 fact 없음).
- 계절 설명력 = 주간 로그 변화를 같은 ISO 주차 평균으로 설명하는 R². 주차 52개를 쓰는 만큼 우연히도 생기는 몫이 있어
  자유도 보정 값(r2Adj)을 같이 낸다.
"""
from datetime import date

import numpy as np
import pandas as pd

from app.core import constants as C
from app.services.indicators.series import weekly_mean


def window_avg(prices: pd.Series, end: pd.Timestamp, days: int = C.SEASONAL_WINDOW_DAYS):
    """(end-days, end] 구간의 (평균, 관측일 수). 관측이 없으면 (None, 0)."""
    sel = prices[(prices.index > end - pd.Timedelta(days=days)) & (prices.index <= end)]
    return (float(sel.mean()) if len(sel) else None), int(len(sel))


def seasonal_fact(prices: pd.Series, as_of: date | None = None) -> dict | None:
    """기준일(기본: 마지막 관측일) 이하 가격만 써서 fact를 만든다. 평년을 만들 연도가 모자라면 None."""
    prices = prices.sort_index()
    if as_of is not None:
        prices = prices[prices.index <= pd.Timestamp(as_of)]
    if prices.empty:
        return None
    end = prices.index[-1]
    recent, obs_days = window_avg(prices, end)
    first = prices.index[0]
    past: dict[int, float] = {}  # 연도 → 그 해 같은 구간 평균 (과거 가능한 모든 해)
    for k in range(1, end.year - first.year + 2):
        past_end = end - pd.DateOffset(years=k)
        avg, n = window_avg(prices, past_end)
        if avg is not None and n >= C.SEASONAL_MIN_WINDOW_OBS:
            past[past_end.year] = avg
    normal_years = [end.year - k for k in range(1, C.SEASONAL_NORMAL_YEARS + 1)]
    if recent is None or any(y not in past for y in normal_years):
        return None
    normal_avg = float(np.mean([past[y] for y in normal_years]))
    window_start = (end - pd.Timedelta(days=C.SEASONAL_WINDOW_DAYS - 1)).date()
    return {
        'asOfDate': end.date(), 'currentPrice': int(prices.iloc[-1]), 'windowDays': C.SEASONAL_WINDOW_DAYS,
        'windowStart': window_start, 'windowObsDays': obs_days, 'recentAvg': round(recent),
        'normalAvg': round(normal_avg), 'normalYears': sorted(normal_years),
        'diffRate': round(recent / normal_avg - 1, 3),
        'cheaperThanCount': int(sum(v > recent for v in past.values())), 'historyYears': len(past),
    }


def seasonal_state(fact: dict) -> str | None:
    if fact['windowObsDays'] < C.SEASONAL_MIN_WINDOW_OBS:
        return None
    if fact['diffRate'] <= -C.SEASONAL_BAND:
        return 'DOWN'
    if fact['diffRate'] >= C.SEASONAL_BAND:
        return 'UP'
    return 'NEUTRAL'


def seasonal_strength(prices: pd.Series) -> dict:
    """주차(1~52)가 주간 변화를 설명하는 정도. r2는 표본 안 값, r2Adj는 주차 수만큼의 우연 몫을 뺀 값."""
    weekly = weekly_mean(prices)
    change = np.log(weekly).diff()
    frame = pd.DataFrame({'ch': change, 'woy': weekly.index.isocalendar().week.clip(upper=52).values}).dropna()
    n, k = len(frame), frame.woy.nunique()
    residual = frame.ch - frame.groupby('woy').ch.transform('mean')
    r2 = 1 - float(residual.var(ddof=0) / frame.ch.var(ddof=0))
    adj = 1 - (1 - r2) * (n - 1) / (n - k)
    return {'r2': round(r2, 3), 'r2Adj': round(adj, 3), 'weeks': int(n), 'weekNumbers': int(k)}


def seasonal_chart(prices: pd.Series, as_of: date | None = None) -> dict:
    """연도별 주차(1~52) 주간 평균 가격. 관측이 모자란 주는 점을 만들지 않는다. 기준일 이후 값은 쓰지 않는다."""
    prices = prices.sort_index()
    if as_of is not None:
        prices = prices[prices.index <= pd.Timestamp(as_of)]
    weekly = weekly_mean(prices).dropna()
    iso = weekly.index.isocalendar()
    years = []
    for year in sorted(set(iso.year)):
        mask = (iso.year == year).values & (iso.week <= 52).values
        points = [{'week': int(w), 'price': round(float(v))} for w, v in zip(iso.week[mask], weekly[mask])]
        if points:
            years.append({'year': int(year), 'points': points})
    return {'type': 'SEASONAL_OVERLAY', 'currentYear': int(weekly.index[-1].year), 'years': years}
