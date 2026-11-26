from datetime import date, datetime
from zoneinfo import ZoneInfo


def today() -> date:
    return datetime.now(ZoneInfo('Asia/Seoul')).date()
