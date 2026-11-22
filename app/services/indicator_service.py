"""판단 보조 지표 조회. 저장된 스냅샷만 읽는다(pandas·배치 코드를 import하지 않는다)."""
from app.core import constants as C
from app.models.price import RETAIL
from app.repositories import indicator_repository as repo
from app.schemas.price import IndicatorCard, IndicatorNotice, IndicatorSummary, PriceIndicators
from app.services.fridge_service import today
from app.services.price_service import NotFoundError, require_item


def indicators(db, item_id, market=RETAIL) -> PriceIndicators:
    _, series = require_item(db, item_id, market)  # 시세 제공 품목이 아니면 NotFoundError(404)
    response = PriceIndicators(item_id=item_id, market=series.market, status='NO_DATA')
    if series.market != RETAIL:
        response.unavailable_reason = '도매 계열은 아직 지표를 제공하지 않습니다'
        return response
    as_of = today()
    run = repo.latest_run(db, series.id, as_of, C.INDICATOR_SPEC_VERSION)
    if run is None:
        response.unavailable_reason = '이 품목은 아직 지표를 준비 중입니다'
        return response
    response.as_of_date, response.spec_version = run.as_of_date, run.spec_version
    if run.status == 'INSUFFICIENT_DATA':
        response.status = 'INSUFFICIENT_HISTORY'
        response.unavailable_reason = '지표를 만들 만큼 가격 이력이 쌓이지 않았습니다'
        return response
    response.cards = [IndicatorCard(key=c.indicator_key, verdict=c.verdict, state=c.state, fact=c.fact,
                                    evidence=c.evidence, chart=c.chart) for c in repo.cards(db, run.id)]
    response.notices = [IndicatorNotice(**n) for n in run.notices or []]
    response.summary = IndicatorSummary(**run.summary) if run.summary else None
    stale = (as_of - run.as_of_date).days > C.INDICATOR_STALE_DAYS
    response.status = 'STALE' if stale else 'READY'
    return response
