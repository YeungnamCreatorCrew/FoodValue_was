from datetime import date

import numpy as np
import pandas as pd
import pytest

pytest.importorskip('pandas')
from app.services.indicators import wholesale_lead as wl  # noqa: E402


def daily(weekly_values, start='2016-01-04'):
    """주 값 → 평일 5일 일 가격(같은 값에 작은 일 잡음)."""
    rng = np.random.default_rng(0)
    days = pd.bdate_range(start, periods=len(weekly_values) * 5)
    base = np.repeat(np.asarray(weekly_values, dtype=float), 5)
    return pd.Series(base * (1 + rng.normal(0, 0.001, len(base))), index=days)


def random_walk(n, seed):
    return 1000 * np.exp(np.cumsum(np.random.default_rng(seed).normal(0, 0.04, n)))


def test_weekly_mean_leaves_thin_weeks_empty():
    idx = pd.to_datetime(['2024-01-01', '2024-01-02', '2024-01-08', '2024-01-15', '2024-01-16'])
    weekly = wl.weekly_mean(pd.Series([100.0, 110, 200, 300, 330], index=idx))
    assert weekly.iloc[0] == 105 and np.isnan(weekly.iloc[1]) and weekly.iloc[2] == 315  # 1일뿐인 주는 비운다(채우지 않음)


def test_signal_uses_only_past_wholesale():
    w = pd.Series(random_walk(120, 1), index=pd.date_range('2020-01-05', periods=120, freq='W'))
    r = pd.Series(random_walk(120, 2), index=w.index)
    t = 60
    base_up = wl._edges(r, w, 2, 2)[0]
    changed = w.copy()
    changed.iloc[t + 1:] *= 3  # t주 이후 도매가를 바꿔도 t주의 신호(상승 표본 여부)는 같아야 한다
    assert wl._edges(r, changed, 2, 2)[0].iloc[:t + 1].equals(base_up.iloc[:t + 1])


def test_real_lead_passes_and_noise_fails():
    n = 520
    w = random_walk(n, 3)
    r_lead = np.concatenate([[w[0]] * 2, w[:-2]]) * np.exp(np.random.default_rng(4).normal(0, 0.01, n))  # 소매 = 2주 늦은 도매
    passed = wl.validate(daily(r_lead), daily(w))
    assert passed['verdict'] == 'PASS' and passed['placebo_p'] <= 0.05

    failed = wl.validate(daily(random_walk(n, 5)), daily(random_walk(n, 6)))
    assert failed['verdict'] == 'FAILED'


def test_reproduces_1121_numbers_on_snapshot():
    """11/21 대파 검증(상승 193건 72%·평소 44%)과 같은 수치. 스냅샷이 없으면 건너뛴다."""
    import pathlib
    path = pathlib.Path('data/snapshots/fv-snap-20261031-v1/price_daily.csv')
    if not path.exists():
        pytest.skip('snapshot 없음')
    d = pd.read_csv(path, parse_dates=['price_date'])
    retail = d[d.series_id == 1].set_index('price_date').price
    wholesale = d[d.series_id == 2].set_index('price_date').price
    result = wl.validate(retail, wholesale)
    assert result['up'].n == 193 and round(result['up'].rate, 2) == 0.72 and round(result['up'].base, 2) == 0.44
    assert round(result['down'].rate, 2) == 0.71 and round(result['down'].base, 2) == 0.46
    assert result['verdict'] == 'PASS' and result['periods']['consistent']


# ---------------------------------------------------------------- SEASONAL
from app.services.indicators import seasonal as sea  # noqa: E402


def window_series(levels: dict[int, float], end_md=(10, 30), days=28):
    """연도별로 (end_md 기준) 최근 days일 평일을 같은 가격으로. 구간 밖에는 값이 없다."""
    parts = []
    for y, v in levels.items():
        end = pd.Timestamp(year=y, month=end_md[0], day=end_md[1])
        parts.append(pd.Series(float(v), index=pd.bdate_range(end - pd.Timedelta(days=days - 1), end)))
    return pd.concat(parts)


LEVELS = {2020: 100, 2021: 200, 2022: 300, 2023: 400, 2024: 500, 2025: 600, 2026: 450}


def test_normal_uses_only_prior_five_windows():
    fact = sea.seasonal_fact(window_series(LEVELS))
    assert fact['normalYears'] == [2021, 2022, 2023, 2024, 2025] and fact['normalAvg'] == 400  # 2026과 2020은 평년에 없다
    assert fact['diffRate'] == 0.125 and fact['cheaperThanCount'] == 2 and fact['historyYears'] == 6
    assert fact['windowDays'] == 28 and fact['windowObsDays'] == 20 and sea.seasonal_state(fact) == 'UP'


def test_not_enough_years_returns_none():
    assert sea.seasonal_fact(window_series({2024: 100, 2025: 100, 2026: 100})) is None


def test_thin_past_window_is_dropped_so_fact_is_none():
    prices = window_series(LEVELS)
    thin = prices[(prices.index.year != 2023) | (prices.index.dayofyear % 4 == 0)]  # 2023 구간 관측을 10일 미만으로
    assert sea.seasonal_fact(thin) is None


def test_fact_ignores_data_after_as_of():
    prices = window_series(LEVELS)
    future = pd.Series(9999.0, index=pd.bdate_range('2026-11-02', periods=5))
    a = sea.seasonal_fact(prices, as_of=date(2026, 10, 30))
    b = sea.seasonal_fact(pd.concat([prices, future]), as_of=date(2026, 10, 30))
    assert a == b and a['asOfDate'] == date(2026, 10, 30)


def test_no_gap_at_month_start():
    """11/5처럼 월초에도 값이 나온다(달력 월 방식은 이번 달 관측이 모자라 방향을 비웠다)."""
    fact = sea.seasonal_fact(window_series(LEVELS, end_md=(11, 5)))
    assert fact is not None and fact['windowObsDays'] == 20 and sea.seasonal_state(fact) == 'UP'


def test_state_needs_enough_window_obs():
    assert sea.seasonal_state({'windowObsDays': 5, 'diffRate': -0.3}) is None
    assert sea.seasonal_state({'windowObsDays': 20, 'diffRate': -0.149}) == 'DOWN'
    assert sea.seasonal_state({'windowObsDays': 20, 'diffRate': 0.05}) == 'NEUTRAL'


def test_seasonal_on_snapshot():
    """대파 스냅샷(~2026-10-30). 28일 구간 방식은 달력 월 방식(-14.9%)과 같은 방향이다."""
    import pathlib
    path = pathlib.Path('data/snapshots/fv-snap-20261031-v1/price_daily.csv')
    if not path.exists():
        pytest.skip('snapshot 없음')
    d = pd.read_csv(path, parse_dates=['price_date'])
    retail = d[d.series_id == 1].set_index('price_date').price
    fact = sea.seasonal_fact(retail)
    assert fact['normalYears'] == [2021, 2022, 2023, 2024, 2025] and fact['historyYears'] == 10
    assert fact['diffRate'] == -0.156 and sea.seasonal_state(fact) == 'DOWN' and fact['cheaperThanCount'] == 9
    strength = sea.seasonal_strength(retail)
    assert round(strength['r2'], 2) == 0.19 and strength['r2Adj'] < strength['r2']
    chart = sea.seasonal_chart(retail)
    assert chart['currentYear'] == 2026 and chart['years'][0]['year'] == 2016


# ---------------------------------------------------------------- 요약 문장
from app.services.indicators import summary as summ  # noqa: E402


def test_headline_matches_prototype_and_josa():
    cards = [{'key': 'SEASONAL', 'state': 'DOWN'}, {'key': 'WHOLESALE_LEAD', 'state': 'NEUTRAL'}]
    assert summ.build('대파', cards)['headline'] == '대파는 지금 평년보다 싼 편이고, 당장 가격을 움직일 신호는 보이지 않습니다.'
    assert summ.topic('대파') == '대파는' and summ.topic('양배추') == '양배추는' and summ.topic('쌀') == '쌀은' and summ.topic('A5') == 'A5은(는)'


def test_summary_without_direction_and_without_cards():
    only_lead = summ.build('대파', [{'key': 'WHOLESALE_LEAD', 'state': 'UP'}])
    assert only_lead['signals'][0]['stateLabel'] == '상승 신호' and '오를 수 있는 신호' in only_lead['headline']
    unknown = summ.build('대파', [{'key': 'SEASONAL', 'state': None}])
    assert unknown['signals'][0]['stateLabel'] == '참고' and '평년과 비교한 참고' in unknown['headline']
    assert summ.build('대파', []) is None


# ---------------------------------------------------------------- 가격 이력 사실 카드
from app.services.indicators import price_stats as ps  # noqa: E402


def two_years(values_last_year, start='2025-01-01'):
    days = pd.bdate_range(start, periods=len(values_last_year))
    return pd.Series(np.asarray(values_last_year, dtype=float), index=days)


def test_percentile_ties_count_half():
    assert ps.percentile(pd.Series([1, 2, 2, 3]), 2) == 0.5
    assert ps.percentile(pd.Series([1, 2, 3, 4]), 1) == 0.125


def test_position_fact_and_state_bands():
    prices = two_years(list(range(100, 100 + 260)))  # 계속 오르는 가격: 마지막 값이 1년 최고
    fact = ps.position_fact(prices)
    assert fact['high'] == 359 and fact['currentPrice'] == 359 and fact['percentile'] > 0.99 and ps.position_state(fact) == 'UP'
    low = ps.position_fact(two_years(list(range(359, 99, -1))))
    assert ps.position_state(low) == 'DOWN'
    mid = ps.position_fact(two_years([100] * 130 + [200] * 130 + [150]))
    assert ps.position_state(mid) == 'NEUTRAL'


def test_stats_need_enough_history_and_ignore_future():
    assert ps.position_fact(two_years([100] * 50)) is None
    prices = two_years(list(range(100, 360)))
    cut = prices.index[200].date()
    a = ps.position_fact(prices, as_of=cut)
    b = ps.position_fact(pd.concat([prices, pd.Series([9999.0], index=[prices.index[-1] + pd.Timedelta(days=1)])]), as_of=cut)
    assert a == b and a['asOfDate'] == cut


def test_gap_fact_uses_common_dates():
    retail = two_years([200] * 200 + [260])
    wholesale = two_years([100] * 200 + [100])
    fact = ps.gap_fact(retail, wholesale)
    assert fact['ratio'] == 2.6 and fact['normalRatio'] == 2.0 and fact['retailPrice'] == 260 and fact['percentile'] > 0.99
    assert ps.gap_fact(retail, wholesale.iloc[:10]) is None


def test_volatility_fact_flags_recent_swings():
    calm = [100.0] * 250
    swing = [100, 130, 90, 140, 100, 150, 95, 135, 100, 145, 90, 140, 100, 150, 95, 135, 100, 145, 90, 140]
    fact = ps.volatility_fact(two_years(calm + swing))
    assert fact['recentRange'] > fact['normalRange'] and fact['percentile'] > 0.9 and fact['windowDays'] == 28
    assert ps.volatility_fact(two_years([100.0] * 40)) is None


def test_summary_with_position_chip_and_position_only_headline():
    cards = [{'key': 'PRICE_POSITION', 'state': 'UP'}]
    result = summ.build('대파', cards)
    assert result['signals'][0] == {'key': 'PRICE_POSITION', 'label': '1년 중 위치', 'state': 'UP', 'stateLabel': '비싼 편'}
    assert result['headline'] == '대파는 지금 최근 1년 가격 중 비싼 편입니다.'


# ---------------------------------------------------------------- 수준 신호(배수·1년 위치) 검증
from app.services.indicators import level_signals as lv  # noqa: E402


def weekly_index(n):
    return pd.date_range('2016-01-03', periods=n, freq='W')


def test_rolling_flags_do_not_use_later_data():
    values = pd.Series(random_walk(120, 11), index=weekly_index(120))
    low, high, pct = lv.rolling_flags(values)
    changed = values.copy()
    changed.iloc[80:] *= 5  # 80주 이후를 바꿔도 79주까지의 순위 백분위는 같아야 한다
    _, _, pct2 = lv.rolling_flags(changed)
    assert pct.iloc[:80].equals(pct2.iloc[:80]) and pct.iloc[:39].isna().all()


def test_mean_reverting_series_passes_and_random_walk_fails():
    rng = np.random.default_rng(21)
    n = 520
    level = np.zeros(n)
    for i in range(1, n):  # 강한 평균회귀(AR 0.6)
        level[i] = 0.6 * level[i - 1] + rng.normal(0, 1)
    reverting = pd.Series(1000 * np.exp(0.08 * level), index=weekly_index(n))
    assert lv.evaluate(reverting, reverting)['passed']
    walk = pd.Series(random_walk(n, 22), index=weekly_index(n))
    assert not lv.evaluate(walk, walk)['passed']


def test_level_sides_edge_signs():
    index = weekly_index(60)
    retail = pd.Series(100.0, index=index)
    retail.iloc[20:] = 120.0  # 20주에 소매가 오른다
    low = pd.Series(False, index=index)
    low.iloc[19] = True  # 19주가 low 신호 → 1주 뒤 +20% 상승
    high = pd.Series(False, index=index)
    lo, hi = lv.level_sides(retail, low, high, ahead=1)
    assert lo.n == 1 and lo.rate == 1.0 and lo.edge > 0.9 and hi.n == 0
