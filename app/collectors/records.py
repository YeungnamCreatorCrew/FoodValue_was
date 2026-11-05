from dataclasses import dataclass, field
from concurrent.futures import ThreadPoolExecutor
from datetime import date, datetime, timedelta

from app.collectors.http import AuthError, CollectorError


@dataclass
class Record:
    """external_observation 1행에 대응하는 원천 레코드."""
    source: str
    dataset: str
    key: str
    payload: dict
    observed_on: date | None = None
    entity_code: str | None = None
    entity_name: str | None = None
    units: dict = field(default_factory=dict)
    item_id: int | None = None
    issued_at: datetime | None = None  # 예보 발표시각


@dataclass
class Batch:
    records: list[Record]
    requests: int
    partial_error: str | None = None  # 일부 요청만 실패하면 받은 레코드는 보존하고 PARTIAL로 기록한다.


def gather(calls, workers=1):
    """calls: 요청 함수 목록. 함수는 레코드 목록 또는 (레코드 목록, 요청 수)를 반환한다.

    일부 실패는 PARTIAL, 전부 실패하면 마지막 오류를 올린다. 인증 오류는 즉시 중단한다.
    workers > 1이면 함수들을 병렬로 실행한다(기관 서버 부담을 고려해 작게 둔다).
    """
    def run(call):
        try:
            result = call()
        except AuthError:
            raise
        except CollectorError as error:
            return [], 1, error
        records, count = result if isinstance(result, tuple) else (result, 1)
        return records, count, None

    calls = list(calls)
    if workers > 1 and len(calls) > 1:
        with ThreadPoolExecutor(max_workers=workers) as pool:
            outcomes = list(pool.map(run, calls))
    else:
        outcomes = [run(call) for call in calls]
    records, requests, failed = {}, 0, None
    for found, count, error in outcomes:
        requests += count
        failed = error or failed
        for record in found:
            records[record.key] = record
    if failed is not None and not records:
        raise failed
    return Batch(list(records.values()), requests, failed.code if failed else None)


def windows(start: date, end: date, days: int):
    current = start
    while current <= end:
        last = min(end, current + timedelta(days=days - 1))
        yield current, last
        current = last + timedelta(days=1)
