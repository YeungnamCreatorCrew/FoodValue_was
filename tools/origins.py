"""기준일 목록(§3.3)과 최종 시험 기준일 차단(§7.2).

KAMIS 조사일 = calendar_day.is_market_closed = false. 목록은 스냅샷의 calendar_day.csv로 만든다.
"""
from datetime import date

from tools import standard


def survey_days(calendar):
    """calendar: (날짜, is_market_closed) 묶음. 조사일만 날짜순으로."""
    return sorted(day for day, closed in calendar if not closed)


def build(calendar):
    """{'validation': [...], 'tune': [...], 'test': [...]}. tune = 검증 구간에서 각 주의 첫 조사일."""
    days = survey_days(calendar)
    (v_start, v_end), (t_start, t_end) = standard.VALIDATION, standard.TEST
    validation = [d for d in days if v_start <= d <= v_end]
    test = [d for d in days if t_start <= d <= t_end]
    tune, weeks = [], set()
    for day in validation:
        week = day.isocalendar()[:2]
        if week not in weeks:
            weeks.add(week)
            tune.append(day)
    return {'validation': validation, 'tune': tune, 'test': test}


class ForbiddenOriginError(ValueError):
    """단계에 허용되지 않은 기준일(특히 최종 시험 기준일)을 쓰려고 할 때."""


def guard(phase: str, origins):
    """단계에 맞지 않는 기준일이 하나라도 있으면 실행을 막는다. run_backtest는 실행 전에 반드시 호출한다.

    - test가 아닌 단계(smoke·p1·p2·focus): 검증 구간 기준일만. 간격·최종 시험 구간은 금지.
    - test: 최종 시험 구간 기준일만.
    """
    start, end = standard.phase_window(phase)
    bad = [d for d in origins if not (start <= d <= end)]
    if bad:
        raise ForbiddenOriginError(
            f'{phase} 단계는 {start} ~ {end} 기준일만 쓸 수 있습니다. 벗어난 기준일 {len(bad)}개(예: {bad[0]}). '
            f'최종 시험 기준일은 --phase test에서만 쓸 수 있습니다(기준서 §7.2).')
    return list(origins)


def parse_day(value) -> date:
    return value if isinstance(value, date) else date.fromisoformat(str(value))
