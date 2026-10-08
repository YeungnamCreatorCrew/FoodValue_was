from datetime import timedelta

from sqlalchemy import exists, func, select

from app.models.fridge import Item, ItemAlias
from app.models.price import PriceDaily, PriceForecast, PriceInsight, PriceModelRun
from app.repositories.fridge_repository import escape_like


def item(db, item_id):
    return db.scalar(select(Item).where(Item.id == item_id, Item.price_source.is_not(None)))


def latest_price(db, item_id, as_of):
    return db.scalar(select(PriceDaily).where(PriceDaily.item_id == item_id,
        PriceDaily.region == 'NATIONAL', PriceDaily.price_date <= as_of)
        .order_by(PriceDaily.price_date.desc()).limit(1))


def published_query(item_id, as_of):
    # 공개는 7개 예측과 가이드가 같은 실행으로 완성된 경우만 허용한다.
    count = (select(func.count(PriceForecast.id)).where(
        PriceForecast.model_run_id == PriceModelRun.id).correlate(PriceModelRun).scalar_subquery())
    return (select(PriceModelRun.id).where(PriceModelRun.item_id == item_id,
        PriceModelRun.base_date <= as_of, PriceModelRun.status == 'SUCCESS', count == 7,
        exists().where(PriceInsight.model_run_id == PriceModelRun.id))
        .order_by(PriceModelRun.base_date.desc(), PriceModelRun.id.desc()).limit(1).correlate(None))


def snapshot(db, item_id, as_of):
    # 한 SELECT에서 실행·7일 예측·가이드를 읽어 결과 교체 중에도 서로 섞이지 않게 한다.
    rows = db.execute(select(PriceModelRun,PriceForecast,PriceInsight)
        .join(PriceForecast,PriceForecast.model_run_id==PriceModelRun.id)
        .join(PriceInsight,PriceInsight.model_run_id==PriceModelRun.id)
        .where(PriceModelRun.id==published_query(item_id,as_of).scalar_subquery())
        .order_by(PriceForecast.target_date)).all()
    if not rows:
        return None, [], None
    return rows[0][0], [row[1] for row in rows], rows[0][2]


def catalog(db, category, keyword, as_of):
    conditions = [Item.price_source.is_not(None)]
    if category:
        conditions.append(Item.category == category)
    if keyword and keyword.strip():
        pattern = '%'+escape_like(keyword.strip())+'%'
        conditions.append(Item.name.ilike(pattern,escape='\\') | exists().where(
            ItemAlias.item_id == Item.id, ItemAlias.alias.ilike(pattern,escape='\\')))
    return db.scalars(select(Item).where(*conditions).order_by(Item.name,Item.id)).all()


def overview_rows(db, items, as_of):
    """목록은 품목 수에 따라 쿼리가 늘지 않도록 일괄 SELECT한다."""
    ids = [row.id for row in items]
    if not ids:
        return {}, {}, {}, {}
    latest_ids = select(PriceDaily.item_id,func.max(PriceDaily.price_date).label('date')).where(
        PriceDaily.item_id.in_(ids),PriceDaily.region=='NATIONAL',PriceDaily.price_date<=as_of).group_by(PriceDaily.item_id).subquery()
    prices = db.scalars(select(PriceDaily).join(latest_ids,
        (PriceDaily.item_id==latest_ids.c.item_id)&(PriceDaily.price_date==latest_ids.c.date))
        .where(PriceDaily.region=='NATIONAL')).all()
    latest = {row.item_id:row for row in prices}
    # 비교일은 최신 관측일-7일. 휴일은 직전 최대 7일까지의 원본을 사용한다.
    dates = [row.price_date for row in prices]
    historical = db.scalars(select(PriceDaily).where(PriceDaily.item_id.in_(ids),
        PriceDaily.region=='NATIONAL',PriceDaily.price_date>=min(dates)-timedelta(days=14),
        PriceDaily.price_date<=max(dates)-timedelta(days=7)).order_by(PriceDaily.price_date)).all() if dates else []
    previous = {}
    for row in historical:
        cutoff = latest[row.item_id].price_date-timedelta(days=7) if row.item_id in latest else None
        if cutoff and cutoff-timedelta(days=7)<=row.price_date<=cutoff:
            previous[row.item_id] = row
    # 완성된 실행을 일괄 선택한다.
    count = select(func.count(PriceForecast.id)).where(PriceForecast.model_run_id==PriceModelRun.id).correlate(PriceModelRun).scalar_subquery()
    candidates = (select(PriceModelRun.id.label('id'),func.row_number().over(
        partition_by=PriceModelRun.item_id,order_by=(PriceModelRun.base_date.desc(),PriceModelRun.id.desc())).label('rank')).where(PriceModelRun.item_id.in_(ids),
        PriceModelRun.base_date<=as_of,PriceModelRun.status=='SUCCESS',count==7,
        exists().where(PriceInsight.model_run_id==PriceModelRun.id))
        ).subquery()
    rows = db.execute(select(PriceModelRun,PriceForecast).join(candidates,PriceModelRun.id==candidates.c.id)
        .join(PriceForecast,PriceForecast.model_run_id==PriceModelRun.id).where(candidates.c.rank==1)).all()
    runs = {}
    forecasts = {}
    for run,point in rows:
        runs[run.item_id]=run
        if (point.target_date-point.base_date).days==7:
            forecasts[run.item_id]=point
    return latest,previous,runs,forecasts
