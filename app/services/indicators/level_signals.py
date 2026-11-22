"""수준 신호 검증: 지금 값이 최근 1년 분포의 아래/위에 있을 때 이후 소매가가 평균으로 돌아오는가.

대상 신호(둘 다 주 평균 기준):
- RETAIL_WHOLESALE_GAP: 소매÷도매 배수 (낮으면 이후 소매 상승, 높으면 이후 소매 하락을 기대)
- PRICE_POSITION: 소매가 자체 (낮으면 이후 소매 상승, 높으면 하락)
정의(검증 전에 고정):
- 신호: 그 주 값이 '그 주까지의 최근 52주' 분포에서 하위 25% 이하(low) / 상위 25% 이상(high). 최소 40주 필요. 미래 분포는 쓰지 않는다.
- 결과: 소매 주평균이 ahead주 뒤 ±1%(LEAD_RETAIL_MOVE) 넘게 오름/내림. 평소 비율 = 신호와 무관한 모든 주의 오름/내림 비율.
- 통계: (low 이후 오른 비율 - 평소 오름) + (high 이후 내린 비율 - 평소 내림). ahead 1~4주 탐색의 최댓값.
- 우연 기준: 신호를 소매 결과에 대해 순환 이동(placebo)하고 같은 탐색을 반복. 이동폭은 양끝 13주 이내 제외.
- 일관성: 2023-01-01 전/후 각각 low·high 두 쪽 모두 평소보다 나아야 한다.
배수 신호에는 소매가 자체의 평균회귀가 섞여 있으므로 '추가 정보' 점검(retail_position이 중간일 때만 본 통계)도 함께 낸다.
"""
import numpy as np
import pandas as pd

from app.core import constants as C
from app.services.indicators.wholesale_lead import Side, _side


def rolling_flags(values: pd.Series, window: int = C.LEVEL_WINDOW_WEEKS, min_weeks: int = C.LEVEL_MIN_WEEKS,
                  low: float = C.LEVEL_LOW, high: float = C.LEVEL_HIGH):
    """각 주의 순위 백분위(그 주 포함 최근 window주 안에서, 동률은 반)를 구해 (low 마스크, high 마스크, 백분위)를 돌려준다."""
    def rank(window_values: np.ndarray) -> float:
        current = window_values[-1]
        if np.isnan(current) or np.isnan(window_values).sum() > len(window_values) - min_weeks:
            return np.nan
        valid = window_values[~np.isnan(window_values)]
        return float(((valid < current).sum() + 0.5 * (valid == current).sum()) / len(valid))
    pct = values.rolling(window, min_periods=1).apply(rank, raw=True)
    return pct <= low, pct >= high, pct


def level_sides(retail: pd.Series, low_flag: pd.Series, high_flag: pd.Series, ahead: int):
    future = retail.shift(-ahead) / retail - 1
    ok = low_flag.notna() & high_flag.notna() & future.notna()
    rose, fell = future > C.LEAD_RETAIL_MOVE, future < -C.LEAD_RETAIL_MOVE
    return (_side(ok & low_flag.eq(True), rose, ok),
            _side(ok & high_flag.eq(True), fell, ok))


def _grid_stat(retail, low_flag, high_flag) -> float:
    best = -np.inf
    for ahead in C.LEVEL_AHEAD_GRID:
        lo, hi = level_sides(retail, low_flag, high_flag, ahead)
        best = max(best, lo.edge + hi.edge)
    return best


def placebo_p(retail, low_flag, high_flag, min_shift: int = 13):
    observed = _grid_stat(retail, low_flag, high_flag)
    lo, hi = low_flag.to_numpy(), high_flag.to_numpy()
    n = len(retail)
    hits = count = 0
    for k in range(min_shift, n - min_shift + 1):
        count += 1
        shifted_lo = pd.Series(np.roll(lo, k), index=retail.index)
        shifted_hi = pd.Series(np.roll(hi, k), index=retail.index)
        if _grid_stat(retail, shifted_lo, shifted_hi) >= observed:
            hits += 1
    return (1 + hits) / (1 + count), observed, count


def consistent_periods(retail, low_flag, high_flag, ahead: int, split: str = C.LEAD_SPLIT_DATE) -> dict:
    cut = pd.Timestamp(split)
    out = {}
    for name, sl in (('before', slice(None, cut - pd.Timedelta(days=1))), ('after', slice(cut, None))):
        lo, hi = level_sides(retail.loc[sl], low_flag.loc[sl], high_flag.loc[sl], ahead)
        out[name] = {'low': lo, 'high': hi, 'ok': lo.edge > 0 and hi.edge > 0}
    out['consistent'] = out['before']['ok'] and out['after']['ok']
    return out


def best_ahead(retail, low_flag, high_flag) -> int:
    return max(C.LEVEL_AHEAD_GRID, key=lambda a: sum(s.edge for s in level_sides(retail, low_flag, high_flag, a)))


def evaluate(retail: pd.Series, signal: pd.Series) -> dict:
    """주평균 소매가와 신호 값(주평균 배수 또는 소매가 자체) → 검증 결과."""
    low, high, _ = rolling_flags(signal)
    valid = signal.notna()
    low, high = low.where(valid), high.where(valid)
    ahead = best_ahead(retail, low, high)
    lo, hi = level_sides(retail, low, high, ahead)
    p, observed, count = placebo_p(retail, low, high)
    periods = consistent_periods(retail, low, high, ahead)
    return {'ahead': ahead, 'low': lo, 'high': hi, 'placebo_p': p, 'observed_edge': observed, 'placebo_count': count,
            'periods': periods, 'passed': p <= C.LEAD_PLACEBO_P and periods['consistent']}


def weak_side(result: dict) -> str | None:
    """한쪽 edge가 다른 쪽의 LEVEL_WEAK_RATIO배보다 작으면 그쪽('low'|'high')은 근거가 약하다."""
    lo, hi = result['low'].edge, result['high'].edge
    if hi < C.LEVEL_WEAK_RATIO * lo:
        return 'high'
    if lo < C.LEVEL_WEAK_RATIO * hi:
        return 'low'
    return None


def stats_for_storage(result: dict, corr_with_wholesale: float | None = None) -> dict:
    """evaluate() 결과를 JSON 저장·응답용 evidence 키(camelCase)로. 배수 신호면 도매 2주 변화와의 상관도 담는다."""
    lo, hi = result['low'], result['high']
    stats = {'lowAfterRate': round(lo.rate, 3), 'lowBaseRate': round(lo.base, 3), 'sampleLow': lo.n,
             'highAfterRate': round(hi.rate, 3), 'highBaseRate': round(hi.base, 3), 'sampleHigh': hi.n,
             'aheadWeeks': result['ahead'], 'retailMove': C.LEAD_RETAIL_MOVE, 'windowWeeks': C.LEVEL_WINDOW_WEEKS,
             'quantileLow': C.LEVEL_LOW, 'quantileHigh': C.LEVEL_HIGH,
             'placeboP': round(result['placebo_p'], 4), 'placeboCount': result['placebo_count'],
             'consistentAcrossPeriods': bool(result['periods']['consistent']), 'weakSide': weak_side(result)}
    if corr_with_wholesale is not None:
        stats['corrWithWholesaleChange'] = round(corr_with_wholesale, 2)
        stats['overlapsLead'] = abs(corr_with_wholesale) >= C.LEVEL_OVERLAP_CORR
    return stats
