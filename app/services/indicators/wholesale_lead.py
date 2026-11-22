"""도매가가 먼저 움직이면 소매가가 따라가는가 (WHOLESALE_LEAD).

정의(11/21 검증 수치 193건·72%·44%에 맞춰 역추정한 것이며 원본 코드는 저장소에 없다):
- 일 가격을 ISO 주(월~일) 평균으로 바꾼다. 주에 관측이 LEAD_MIN_WEEK_OBS일 미만이면 그 주는 비운다(채우지 않는다).
- 도매 2주 변화율 = 도매 주평균(t) / 도매 주평균(t-2주) - 1.
- 소매 결과 = 소매 주평균(t+2주) / 소매 주평균(t) - 1. +1% 초과면 '상승', -1% 미만이면 '하락', 그 사이는 보합.
- 상승 신호: 도매 변화 ≥ +5%, 이후 소매 상승 비율을 '평소'(모든 주의 소매 상승 비율)와 비교.
  하락 신호: 도매 변화 ≤ -5%, 이후 소매 하락 비율을 평소 하락 비율과 비교.
- 우연 기준: 도매 변화율 신호를 소매에 대해 순환 이동(placebo)해 같은 통계를 반복하고, 시차(1~4주)·결과 기간(1~4주) 탐색까지
  관측값과 똑같이 적용한 뒤 얻은 최댓값 분포에서 관측값의 p값을 구한다.
"""
from dataclasses import dataclass

import numpy as np
import pandas as pd

from app.core import constants as C
from app.services.indicators.series import weekly_mean

GRID_WEEKS = (1, 2, 3, 4)


def _edges(retail: pd.Series, wholesale: pd.Series, lag: int, ahead: int):
    """(상승 신호 표본 마스크, 하락 신호 표본 마스크, 소매 상승·하락 표시, 평소 비율)를 한 번에 계산."""
    change = wholesale / wholesale.shift(lag) - 1
    future = retail.shift(-ahead) / retail - 1
    ok = change.notna() & future.notna()
    rose, fell = future > C.LEAD_RETAIL_MOVE, future < -C.LEAD_RETAIL_MOVE
    up, down = ok & (change >= C.LEAD_WHOLESALE_MOVE), ok & (change <= -C.LEAD_WHOLESALE_MOVE)
    return up, down, rose, fell, ok


@dataclass(frozen=True)
class Side:
    n: int
    rate: float | None  # 신호 이후 같은 방향으로 움직인 비율
    base: float | None  # 평소(모든 주) 같은 방향 비율

    @property
    def edge(self) -> float:
        return 0.0 if self.rate is None or self.base is None else self.rate - self.base


def _side(mask, hit, ok) -> Side:
    n = int(mask.sum())
    return Side(n, float(hit[mask].mean()) if n else None, float(hit[ok].mean()) if ok.any() else None)


def lead_sides(retail: pd.Series, wholesale: pd.Series, lag: int = C.LEAD_LAG_WEEKS, ahead: int = C.LEAD_AHEAD_WEEKS):
    up, down, rose, fell, ok = _edges(retail, wholesale, lag, ahead)
    return _side(up, rose, ok), _side(down, fell, ok)


def _grid_stat(retail: pd.Series, wholesale: pd.Series) -> float:
    """시차·결과 기간 탐색 중 '상승 edge + 하락 edge'의 최댓값."""
    best = -np.inf
    for lag in GRID_WEEKS:
        for ahead in GRID_WEEKS:
            u, d = lead_sides(retail, wholesale, lag, ahead)
            best = max(best, u.edge + d.edge)
    return best


def placebo_p(retail: pd.Series, wholesale: pd.Series, min_shift: int = 13) -> tuple[float, float, int]:
    """(p값, 관측 통계, placebo 횟수). 도매를 소매에 대해 순환 이동하고 같은 탐색을 반복한다.

    이동폭이 작으면 진짜 관계가 남으므로 양쪽 끝 min_shift주 이내는 쓰지 않는다. p = (1 + 관측 이상인 placebo 수) / (1 + 횟수).
    """
    observed = _grid_stat(retail, wholesale)
    n = len(wholesale)
    values = wholesale.to_numpy()
    shifts = range(min_shift, n - min_shift + 1)
    hits = 0
    for k in shifts:
        shifted = pd.Series(np.roll(values, k), index=wholesale.index)
        if _grid_stat(retail, shifted) >= observed:
            hits += 1
    count = len(shifts)
    return (1 + hits) / (1 + count), observed, count


def consistent_periods(retail: pd.Series, wholesale: pd.Series, split: str = C.LEAD_SPLIT_DATE) -> dict:
    """두 기간 각각에서 상승·하락 신호가 평소보다 나은지(edge > 0)."""
    cut = pd.Timestamp(split)
    out = {}
    for name, sl in (('before', slice(None, cut - pd.Timedelta(days=1))), ('after', slice(cut, None))):
        up, down = lead_sides(retail.loc[sl], wholesale.loc[sl])
        out[name] = {'up': up, 'down': down, 'ok': up.edge > 0 and down.edge > 0}
    out['consistent'] = out['before']['ok'] and out['after']['ok']
    return out


def validate(retail_daily: pd.Series, wholesale_daily: pd.Series) -> dict:
    """일 가격 두 계열 → 검증 결과(통계·p값·일관성·verdict)."""
    both = pd.concat([retail_daily.rename('r'), wholesale_daily.rename('w')], axis=1).dropna()
    retail, wholesale = weekly_mean(both.r), weekly_mean(both.w)
    up, down = lead_sides(retail, wholesale)
    p, observed, count = placebo_p(retail, wholesale)
    periods = consistent_periods(retail, wholesale)
    passed = p <= C.LEAD_PLACEBO_P and periods['consistent']
    return {'up': up, 'down': down, 'placebo_p': p, 'observed_edge': observed, 'placebo_count': count, 'periods': periods,
            'verdict': 'PASS' if passed else 'FAILED', 'period_start': both.index.min().date(), 'period_end': both.index.max().date()}


def latest_changes(retail: pd.Series, wholesale: pd.Series, lag: int = C.LEAD_LAG_WEEKS) -> dict | None:
    """가장 최근 주(주 평균이 있고 lag주 전 값도 있는 주)의 도매·소매 lag주 변화율(소수). 없으면 None."""
    change_w = wholesale / wholesale.shift(lag) - 1
    change_r = retail / retail.shift(lag) - 1
    valid = change_w.notna() & change_r.notna()
    if not valid.any():
        return None
    week = valid[valid].index[-1]
    return {'weekEnd': week.date(), 'wholesaleChange2w': round(float(change_w[week]), 3),
            'retailChange2w': round(float(change_r[week]), 3)}


def lead_state(wholesale_change: float) -> str:
    if wholesale_change >= C.LEAD_WHOLESALE_MOVE:
        return 'UP'
    if wholesale_change <= -C.LEAD_WHOLESALE_MOVE:
        return 'DOWN'
    return 'NEUTRAL'


def indexed_chart(retail: pd.Series, wholesale: pd.Series, weeks: int = C.INDICATOR_CHART_WEEKS) -> dict | None:
    """최근 weeks주 도매·소매 주평균을 첫 주=100으로 바꾼 지수. 둘 중 하나라도 빈 주는 점을 만들지 않는다."""
    both = pd.concat([wholesale.rename('w'), retail.rename('r')], axis=1).dropna().tail(weeks)
    if len(both) < 2:
        return None
    index = both / both.iloc[0] * 100
    return {'type': 'INDEXED_LINES', 'baseDate': both.index[0].date().isoformat(),
            'points': [{'date': day.date().isoformat(), 'wholesale': round(float(row.w), 1), 'retail': round(float(row.r), 1)}
                       for day, row in index.iterrows()]}


def stats_for_storage(result: dict) -> dict:
    """validate() 결과를 JSON 저장·응답용 evidence 키(camelCase)로."""
    up, down, periods = result['up'], result['down'], result['periods']
    return {'upAfterRate': round(up.rate, 3), 'baseUpRate': round(up.base, 3), 'sampleUp': up.n,
            'downAfterRate': round(down.rate, 3), 'baseDownRate': round(down.base, 3), 'sampleDown': down.n,
            'threshold': C.LEAD_WHOLESALE_MOVE, 'retailMove': C.LEAD_RETAIL_MOVE,
            'lagWeeks': C.LEAD_LAG_WEEKS, 'aheadWeeks': C.LEAD_AHEAD_WEEKS,
            'placeboP': round(result['placebo_p'], 4), 'placeboCount': result['placebo_count'],
            'consistentAcrossPeriods': bool(periods['consistent']),
            'periodStart': result['period_start'].isoformat(), 'periodEnd': result['period_end'].isoformat()}
