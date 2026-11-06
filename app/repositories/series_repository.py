"""가격 계열(price_series) 조회. 소매·도매 계열 모두 예측 대상이고 서로를 예측 변수로 쓴다."""
from datetime import date

from sqlalchemy import select

from app.models.price import RETAIL, PriceDaily, PriceSeries


def get(db, item_id, market=RETAIL):
    return db.scalar(select(PriceSeries).where(PriceSeries.item_id == item_id, PriceSeries.market == market))


def by_items(db, item_ids, market=RETAIL) -> dict[int, PriceSeries]:
    if not item_ids:
        return {}
    rows = db.scalars(select(PriceSeries).where(PriceSeries.item_id.in_(item_ids), PriceSeries.market == market)).all()
    return {row.item_id: row for row in rows}


def of_items(db, item_ids) -> list[PriceSeries]:
    """품목들의 모든 계열(소매·도매). 수집·정제 순서를 고정하려고 품목·시장 순으로 정렬한다."""
    if not item_ids:
        return []
    return db.scalars(select(PriceSeries).where(PriceSeries.item_id.in_(item_ids))
                      .order_by(PriceSeries.item_id, PriceSeries.market)).all()


def prices(db, series_id, start: date | None = None, end: date | None = None) -> list[tuple[date, int]]:
    conditions = [PriceDaily.series_id == series_id]
    if start:
        conditions.append(PriceDaily.price_date >= start)
    if end:
        conditions.append(PriceDaily.price_date <= end)
    return [(day, price) for day, price in db.execute(select(PriceDaily.price_date, PriceDaily.price)
                                                      .where(*conditions).order_by(PriceDaily.price_date)).all()]
