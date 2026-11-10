"""공통 로더(기준서 §9). 지금은 스냅샷 읽기와 배추·무 작형 이어 붙이기(§2.3)만 있다.

이어 붙이기 함수는 이 파일의 `merge_kinds` 하나만 쓴다. 스냅샷 내보내기와 `check_snapshot`이 이 함수로
`price_daily_merged.csv`를 만들고 다시 계산한다. 로더·평가기는 그 결과 파일을 읽고, 학습 창이나 기준일에 맞춰
다시 계산하지 않는다.

`load_as_of(series_id, d)`(§3.1 시점 규칙, §5 특징)는 loader 담당이 이 파일에 추가한다.
"""
import csv
from collections import Counter
from dataclasses import dataclass
from datetime import date
from pathlib import Path

from tools import standard


@dataclass(frozen=True)
class MergedRow:
    price_date: date
    price: int
    kind_code: str
    source_series_id: int
    kind_switch: int


def next_kind(kind: str) -> str:
    cycle = standard.KIND_CYCLE
    return cycle[(cycle.index(kind) + 1) % len(cycle)]


def _start_kind(observed, month: int) -> str:
    """규칙 1: 그 달 우선 작형, 없으면 순환 순서상 우선 작형 다음으로 가장 가까운 관측 작형."""
    cycle = standard.KIND_CYCLE
    first = cycle.index(standard.KIND_PRIORITY_BY_MONTH[month])
    for step in range(len(cycle)):
        kind = cycle[(first + step) % len(cycle)]
        if kind in observed:
            return kind
    raise ValueError('관측된 작형이 없음')


def merge_kinds(observations, survey_days) -> list[MergedRow]:
    """한 계열(품목 × 시장)의 작형별 관측을 기준서 §2.3 규칙으로 이어 붙인다.

    observations: (price_date, kind_code, price, source_series_id) 묶음
    survey_days: KAMIS 조사일(calendar_day.is_market_closed = false) 목록
    반환: 값이 있는 날만, 날짜순. 조사일이 아닌 날의 관측은 쓰지 않는다.
    """
    by_day: dict[date, dict[str, tuple[int, int]]] = {}
    for day, kind, price, source in observations:
        if kind not in standard.KIND_CYCLE:
            raise ValueError(f'알 수 없는 작형 코드 {kind!r}')
        by_day.setdefault(day, {})[kind] = (int(price), int(source))
    if not by_day:
        return []
    first = min(by_day)
    current = previous = None
    streak = Counter()
    missing = 0
    restart = True
    rows = []
    for day in sorted(survey_days):
        if day < first:
            continue
        observed = by_day.get(day, {})
        switched = 0
        if restart:
            if not observed:
                continue
            chosen = _start_kind(observed, day.month)
            switched = int(current is not None and chosen != current)
            current, previous, missing, restart = chosen, None, 0, False
            streak.clear()
        else:
            for kind in standard.KIND_CYCLE:
                streak[kind] = streak[kind] + 1 if kind in observed else 0
            priority = standard.KIND_PRIORITY_BY_MONTH[day.month]
            candidates = {next_kind(current), priority} - {current, previous}
            ready = sorted(k for k in candidates if streak[k] >= standard.KIND_SWITCH_RUN)
            if ready:
                chosen = priority if priority in ready else ready[0]
                previous, current, switched, missing = current, chosen, 1, 0
                streak.clear()
        if current in observed:
            missing = 0
            price, source = observed[current]
            rows.append(MergedRow(day, price, current, source, switched))
        else:
            missing += 1
            if missing >= standard.KIND_RESTART_GAP:
                restart = True
    return rows


def switch_summary(rows):
    """manifest용: 전환일 목록과 연도별 전환 횟수."""
    switches = [(r.price_date.isoformat(), r.kind_code) for r in rows if r.kind_switch]
    per_year = Counter(day[:4] for day, _ in switches)
    return {'switches': switches, 'per_year': dict(sorted(per_year.items()))}


def read_table(snapshot: Path, name: str) -> list[dict]:
    """스냅샷 CSV 하나를 dict 행 목록으로 읽는다(값은 문자열)."""
    with open(Path(snapshot) / name, encoding='utf-8', newline='') as f:
        return list(csv.DictReader(f))


def read_calendar(snapshot: Path):
    return [(date.fromisoformat(r['cal_date']), r['is_market_closed'] == 'true')
            for r in read_table(snapshot, 'calendar_day.csv')]


def merge_from_kind_table(kind_rows, calendar) -> dict[int, list[MergedRow]]:
    """price_daily_kind.csv 행 → {가상 계열 id: 이어 붙인 행}."""
    survey = [day for day, closed in calendar if not closed]
    grouped: dict[int, list] = {}
    for r in kind_rows:
        grouped.setdefault(int(r['merged_series_id']), []).append(
            (date.fromisoformat(r['price_date']), r['kind_code'], int(r['price']), int(r['source_series_id'])))
    return {sid: merge_kinds(obs, survey) for sid, obs in sorted(grouped.items())}
