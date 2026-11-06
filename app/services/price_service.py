from datetime import timedelta
from decimal import Decimal

from sqlalchemy import select

from app.models.fridge import FridgeIngredient
from app.models.price import RETAIL, PriceModelRun
from app.repositories import series_repository
from app.repositories import price_repository as repo
from app.schemas.common import Page
from app.schemas.price import (ForecastPoint, ForecastResponse, FridgeHolding, HistoryPoint,
    PriceDetail, PriceFactors, PriceGuide, PriceHistory, PriceSummary)
from app.services.fridge_service import today


class NotFoundError(Exception):
    pass


def require_item(db,item_id,market=RETAIL):
    item,series = repo.item(db,item_id,market)
    if item is None:
        raise NotFoundError
    return item,series


def change(current, previous):
    return round((current-previous)/previous*100,2) if current is not None and previous else None


def state(price, run, as_of):
    if price is None:
        return 'NO_DATA'
    if (as_of-price.price_date).days>7 or (run and (as_of-run.base_date).days>1):
        return 'STALE'
    if run is None:
        return 'NO_FORECAST'
    return 'READY' if run.quality=='VALIDATED' else 'BASELINE'


def summary(item,series,price,previous,run,last,as_of):
    return PriceSummary(id=item.id,name=item.name,category=item.category,market=series.market,series_id=series.id,
        unit_label=series.unit_label,source=series.source,
        price_date=price.price_date if price else None,current_price=price.price if price else None,
        weekly_change_percent=change(price.price,previous.price) if price and previous else None,
        forecast_price=last.predicted_price if last else None,
        forecast_change_percent=change(last.predicted_price,price.price) if last and price else None,
        forecast_base_date=run.base_date if run else None,quality=run.quality if run else None,
        forecast_target_date=last.target_date if last else None,
        status=state(price,run,as_of))


def list_items(db,category,keyword,sort,page,size,market=RETAIL):
    as_of=today()
    rows=repo.catalog(db,category,keyword,market)
    prices,previous,runs,forecasts=repo.overview_rows(db,[s for _,s in rows],as_of)
    result=[summary(item,s,prices.get(s.id),previous.get(s.id),runs.get(s.id),forecasts.get(s.id),as_of) for item,s in rows]
    if sort!='name':
        field='weekly_change_percent' if sort=='change' else 'forecast_change_percent'
        result.sort(key=lambda row:(getattr(row,field) is None,getattr(row,field) or 0,row.name,row.id))
    return Page(items=result[(page-1)*size:page*size],page=page,size=size,total=len(result))


def forecast_result(db,item_id,series,as_of,run,points):
    attempt=db.scalar(select(PriceModelRun).where(PriceModelRun.series_id==series.id,
        PriceModelRun.base_date<=as_of).order_by(PriceModelRun.base_date.desc(),PriceModelRun.id.desc()).limit(1))
    result=ForecastResponse(item_id=item_id,market=series.market,series_id=series.id,status='NO_FORECAST',
                            latest_attempt_status=attempt.status if attempt else None)
    if not run:
        if attempt and attempt.status=='INSUFFICIENT_DATA':
            result.status='INSUFFICIENT_DATA'
        return result
    result.base_date=run.base_date
    result.data_date=run.data_date
    result.model_run_id=run.id
    result.model_name=run.model_name
    result.model_version=run.model_version
    result.quality=run.quality
    result.metrics=run.metrics
    result.updated_at=run.finished_at
    result.status='STALE' if (as_of-run.base_date).days>1 or (as_of-run.data_date).days>7 else 'READY' if run.quality=='VALIDATED' else 'BASELINE'
    result.points=[ForecastPoint.model_validate(row) for row in points]
    return result


def forecast(db,item_id,market=RETAIL):
    _,series=require_item(db,item_id,market)
    as_of=today()
    run,points,_=repo.snapshot(db,series.id,as_of)
    return forecast_result(db,item_id,series,as_of,run,points)


def detail(db,item_id,user,market=RETAIL):
    item,series=require_item(db,item_id,market)
    as_of=today()
    prices,previous,runs,forecasts=repo.overview_rows(db,[series],as_of)
    run,points,guide=repo.snapshot(db,series.id,as_of)
    holdings=None
    if user:
        rows=db.scalars(select(FridgeIngredient).where(FridgeIngredient.user_id==user.id,
            FridgeIngredient.item_id==item_id,FridgeIngredient.deleted_at.is_(None),FridgeIngredient.quantity>0)).all()
        quantities={}
        for row in rows:
            quantities[row.unit]=quantities.get(row.unit,Decimal(0))+row.quantity
        holdings=FridgeHolding(ingredient_count=len(rows),quantities={k:str(v) for k,v in quantities.items()})
    return PriceDetail(item=summary(item,series,prices.get(series.id),previous.get(series.id),run,points[-1] if points else None,as_of),
        forecast=forecast_result(db,item_id,series,as_of,run,points),
        guide=PriceGuide.model_validate(guide) if guide else None,fridge=holdings)


def history(db,item_id,days,market=RETAIL):
    _,series=require_item(db,item_id,market)
    end=today()
    start=end-timedelta(days=days-1)
    lookup=dict(series_repository.prices(db,series.id,start,end))
    return PriceHistory(item_id=item_id,market=series.market,days=days,start_date=start,end_date=end,
        points=[HistoryPoint(date=start+timedelta(days=i),price=lookup.get(start+timedelta(days=i))) for i in range(days)])


def factors(db,item_id,market=RETAIL):
    _,series=require_item(db,item_id,market)
    run,points,guide=repo.snapshot(db,series.id,today())
    result=forecast_result(db,item_id,series,today(),run,points)
    return PriceFactors(item_id=item_id,market=series.market,base_date=result.base_date,status=result.status,
                        factors=guide.factors or [] if guide else [])
