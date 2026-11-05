from dataclasses import dataclass, field
from datetime import date, timedelta

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


@dataclass
class Batch:
    records: list[Record]
    requests: int
    partial_error: str | None = None  # 일부 요청만 실패하면 받은 레코드는 보존하고 PARTIAL로 기록한다.


def gather(calls):
    """calls: (요청 함수) 목록. 일부 실패는 PARTIAL, 전부 실패하면 마지막 오류를 올린다. 인증 오류는 즉시 중단."""
    records, requests, failed = {}, 0, None
    for call in calls:
        requests += 1
        try:
            for record in call():
                records[record.key] = record
        except AuthError:
            raise
        except CollectorError as error:
            failed = error
    if failed is not None and not records:
        raise failed
    return Batch(list(records.values()), requests, failed.code if failed else None)


def windows(start: date, end: date, days: int):
    current = start
    while current <= end:
        last = min(end, current + timedelta(days=days - 1))
        yield current, last
        current = last + timedelta(days=1)
