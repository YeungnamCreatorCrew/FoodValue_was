"""가격 이력만으로 만드는 사실 카드. 예측 모델이 어떤 변수를 채택했는지와 무관하고, 외부 자료를 쓰지 않는다.

- PRICE_POSITION: 지금 가격이 최근 1년 일별 가격 분포에서 어디쯤인지(순위 백분위, 동률은 반반). 하위 25%/상위 25% 밖일 때만 방향 표시.
- RETAIL_WHOLESALE_GAP: 소매가 ÷ 도매가(배수)가 최근 1년 평소와 비교해 어디쯤인지. 방향 표시 없음(관계가 검증되지 않음).
- VOLATILITY: 최근 28일 (최고-최저) ÷ 평균이 최근 1년 같은 폭 분포에서 어디쯤인지. 방향 표시 없음.
세 카드 모두 '사실'이며 가격이 오른다/내린다는 주장을 하지 않는다. 기준일 이하 가격만 쓴다.
"""
from datetime import date

import numpy as np
import pandas as pd

from app.core import constants as C


def _upto(prices: pd.Series, as_of: date | None) -> pd.Series:
    prices = prices.sort_index()
    return prices[prices.index <= pd.Timestamp(as_of)] if as_of is not None else prices


def percentile(values: pd.Series, current: float) -> float:
    """current의 순위 백분위(0~1). 같은 값은 절반씩 센다."""
    return float(((values < current).sum() + 0.5 * (values == current).sum()) / len(values))


def _last_year(series: pd.Series, end: pd.Timestamp) -> pd.Series:
    return series[(series.index > end - pd.Timedelta(days=C.STATS_WINDOW_DAYS)) & (series.index <= end)]


def position_fact(prices: pd.Series, as_of: date | None = None) -> dict | None:
    prices = _upto(prices, as_of)
    if prices.empty:
        return None
    end = prices.index[-1]
    window = _last_year(prices, end)
    if len(window) < C.STATS_MIN_OBS:
        return None
    current = float(prices.iloc[-1])
    avg = float(window.mean())
    return {'asOfDate': end.date(), 'currentPrice': int(current), 'windowDays': C.STATS_WINDOW_DAYS, 'obsDays': int(len(window)),
            'low': int(window.min()), 'lowDate': window.idxmin().date(), 'high': int(window.max()), 'highDate': window.idxmax().date(),
            'avg': round(avg), 'diffFromAvg': round(current / avg - 1, 3), 'percentile': round(percentile(window, current), 3)}


def position_state(fact: dict) -> str:
    if fact['percentile'] <= C.POSITION_LOW:
        return 'DOWN'
    if fact['percentile'] >= C.POSITION_HIGH:
        return 'UP'
    return 'NEUTRAL'


def gap_fact(retail: pd.Series, wholesale: pd.Series, as_of: date | None = None) -> dict | None:
    both = pd.concat([_upto(retail, as_of).rename('r'), _upto(wholesale, as_of).rename('w')], axis=1).dropna()
    if both.empty:
        return None
    ratio = both.r / both.w
    end = ratio.index[-1]
    window = _last_year(ratio, end)
    if len(window) < C.STATS_MIN_OBS:
        return None
    current = float(ratio.iloc[-1])
    return {'asOfDate': end.date(), 'retailPrice': int(both.r.iloc[-1]), 'wholesalePrice': int(both.w.iloc[-1]),
            'ratio': round(current, 2), 'normalRatio': round(float(window.median()), 2), 'low': round(float(window.min()), 2),
            'high': round(float(window.max()), 2), 'windowDays': C.STATS_WINDOW_DAYS, 'obsDays': int(len(window)),
            'percentile': round(percentile(window, current), 3)}


def volatility_fact(prices: pd.Series, as_of: date | None = None, breaks=()) -> dict | None:
    """breaks: 작형 전환일. 구간은 마지막 전환일(그날부터 새 품종) 이후로 잘라서, 품종 교체 가격 차이를 출렁임으로 세지 않는다."""
    prices = _upto(prices, as_of)
    if prices.empty:
        return None
    end = prices.index[-1]
    days = C.VOLATILITY_WINDOW_DAYS

    switch_days = sorted(pd.Timestamp(b) for b in breaks)

    def spread(t: pd.Timestamp):
        start = t - pd.Timedelta(days=days)
        last = [b for b in switch_days if b <= t]
        w = prices[(prices.index > start) & (prices.index <= t) & (prices.index >= last[-1] if last else True)]
        return float((w.max() - w.min()) / w.mean()) if len(w) >= C.VOLATILITY_MIN_OBS else np.nan

    dates = _last_year(prices, end).index
    history = pd.Series([spread(t) for t in dates], index=dates).dropna()
    current = spread(end)
    if np.isnan(current) or len(history) < C.STATS_MIN_OBS:
        return None
    return {'asOfDate': end.date(), 'windowDays': days, 'recentRange': round(current, 3), 'normalRange': round(float(history.median()), 3),
            'percentile': round(percentile(history, current), 3), 'obsDays': int(len(history))}
