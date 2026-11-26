from datetime import timedelta

from sqlalchemy import exists, func, select

from app.models.item import Item, ItemAlias
from app.models.price import (RETAIL, PriceDaily, PriceForecast, PriceForecastExplanation, PriceForecastFactor, PriceInsight,
    PriceModelRun, PriceSeries)


def escape_like(value: str) -> str:
    return value.replace('\\', '\\\\').replace('%', '\\%').replace('_', '\\_')


def item(db, item_id, market=RETAIL):
    """시세 품목과 그 시장의 가격 계열. 계열이 없으면 (None, None)."""
    row = db.execute(select(Item, PriceSeries).join(PriceSeries, PriceSeries.item_id == Item.id)
                     .where(Item.id == item_id, PriceSeries.market == market)).first()
    return (row[0], row[1]) if row else (None, None)


def published_query(series_id, as_of):
    # 공개는 7개 예측과 가이드가 같은 실행으로 완성된 경우만 허용한다.
    count = (select(func.count(PriceForecast.id)).where(
        PriceForecast.model_run_id == PriceModelRun.id).correlate(PriceModelRun).scalar_subquery())
    return (select(PriceModelRun.id).where(PriceModelRun.series_id == series_id,
        PriceModelRun.base_date <= as_of, PriceModelRun.status == 'SUCCESS', count == 7,
        exists().where(PriceInsight.model_run_id == PriceModelRun.id))
        .order_by(PriceModelRun.base_date.desc(), PriceModelRun.id.desc()).limit(1).correlate(None))


def snapshot(db, series_id, as_of):
    # 한 SELECT에서 실행·7일 예측·가이드를 읽어 결과 교체 중에도 서로 섞이지 않게 한다.
    rows = db.execute(select(PriceModelRun,PriceForecast,PriceInsight)
        .join(PriceForecast,PriceForecast.model_run_id==PriceModelRun.id)
        .join(PriceInsight,PriceInsight.model_run_id==PriceModelRun.id)
        .where(PriceModelRun.id==published_query(series_id,as_of).scalar_subquery())
        .order_by(PriceForecast.target_date)).all()
    if not rows:
        return None, [], None
    return rows[0][0], [row[1] for row in rows], rows[0][2]


def catalog(db, category, keyword, market=RETAIL):
    """해당 시장의 가격 계열이 있는 품목과 계열"""
    conditions = [PriceSeries.market == market, Item.is_price_listed.is_(True)]
    if category:
        conditions.append(Item.category == category)
    if keyword and keyword.strip():
        pattern = '%'+escape_like(keyword.strip())+'%'
        conditions.append(Item.name.ilike(pattern,escape='\\') | exists().where(
            ItemAlias.item_id == Item.id, ItemAlias.alias.ilike(pattern,escape='\\')))
    return [(row[0], row[1]) for row in db.execute(select(Item, PriceSeries).join(PriceSeries, PriceSeries.item_id == Item.id)
                                                   .where(*conditions).order_by(Item.name, Item.id)).all()]


def overview_rows(db, series_list, as_of):
    """목록은 품목 수에 따라 쿼리가 늘지 않도록 일괄 SELECT한다. 결과는 계열 id 기준."""
    ids = [row.id for row in series_list]
    if not ids:
        return {}, {}, {}, {}
    latest_ids = select(PriceDaily.series_id,func.max(PriceDaily.price_date).label('date')).where(
        PriceDaily.series_id.in_(ids),PriceDaily.price_date<=as_of).group_by(PriceDaily.series_id).subquery()
    prices = db.scalars(select(PriceDaily).join(latest_ids,
        (PriceDaily.series_id==latest_ids.c.series_id)&(PriceDaily.price_date==latest_ids.c.date))).all()
    latest = {row.series_id:row for row in prices}
    # 비교일은 최신 관측일-7일. 휴일은 직전 최대 7일까지의 원본을 사용한다.
    dates = [row.price_date for row in prices]
    historical = db.scalars(select(PriceDaily).where(PriceDaily.series_id.in_(ids),
        PriceDaily.price_date>=min(dates)-timedelta(days=14),
        PriceDaily.price_date<=max(dates)-timedelta(days=7)).order_by(PriceDaily.price_date)).all() if dates else []
    previous = {}
    for row in historical:
        cutoff = latest[row.series_id].price_date-timedelta(days=7) if row.series_id in latest else None
        if cutoff and cutoff-timedelta(days=7)<=row.price_date<=cutoff:
            previous[row.series_id] = row
    # 완성된 실행을 일괄 선택한다.
    count = select(func.count(PriceForecast.id)).where(PriceForecast.model_run_id==PriceModelRun.id).correlate(PriceModelRun).scalar_subquery()
    candidates = (select(PriceModelRun.id.label('id'),func.row_number().over(
        partition_by=PriceModelRun.series_id,order_by=(PriceModelRun.base_date.desc(),PriceModelRun.id.desc())).label('rank')).where(PriceModelRun.series_id.in_(ids),
        PriceModelRun.base_date<=as_of,PriceModelRun.status=='SUCCESS',count==7,
        exists().where(PriceInsight.model_run_id==PriceModelRun.id))
        ).subquery()
    rows = db.execute(select(PriceModelRun,PriceForecast).join(candidates,PriceModelRun.id==candidates.c.id)
        .join(PriceForecast,PriceForecast.model_run_id==PriceModelRun.id).where(candidates.c.rank==1)).all()
    runs = {}
    forecasts = {}
    for run,point in rows:
        runs[run.series_id]=run
        if (point.target_date-run.base_date).days==7:
            forecasts[run.series_id]=point
    return latest,previous,runs,forecasts


def aliases(db, item_ids):
    """품목 id → 별칭 목록(가나다순)"""
    if not item_ids:
        return {}
    result = {}
    for item_id, alias in db.execute(select(ItemAlias.item_id, ItemAlias.alias)
                                     .where(ItemAlias.item_id.in_(item_ids)).order_by(ItemAlias.alias)).all():
        result.setdefault(item_id, []).append(alias)
    return result


def explanation(db, run_id):
    """실행의 SHAP 설명 머리와 특징별 행. 설명이 없으면 (None, [])"""
    header = db.get(PriceForecastExplanation, run_id)
    if header is None:
        return None, []
    columns = [PriceForecastFactor.feature, PriceForecastFactor.feature_value, PriceForecastFactor.contribution,
               PriceForecastFactor.history]
    rows = db.execute(select(*columns).where(PriceForecastFactor.model_run_id == run_id)).all()
    return header, [{'feature': f, 'value': v, 'contribution': c, 'history': h} for f, v, c, h in rows]
