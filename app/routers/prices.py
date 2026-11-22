from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, Path, Query
from sqlalchemy.orm import Session

from app.core.constants import ID_MAX, PAGE_MAX_SIZE
from app.core.db import get_db
from app.core.deps import get_optional_user
from app.models.user import User
from app.schemas.common import Page
from app.schemas.price import FactorHistory, ForecastResponse, PriceCategory, PriceDetail, PriceFactors, PriceHistory, PriceMarket, PriceSort, PriceSummary
from app.services import price_service as service

router=APIRouter(prefix='/prices',tags=['prices'])
Db=Annotated[Session,Depends(get_db)]
Viewer=Annotated[User | None,Depends(get_optional_user)]
Id=Annotated[int,Path(ge=1,le=ID_MAX)]
Market=Annotated[PriceMarket,Query(description='RETAIL 소매(기본) 또는 WHOLESALE 도매')]


def call(fn,*args):
    try:
        return fn(*args)
    except service.NotFoundError:
        raise HTTPException(404,'시세 제공 품목을 찾을 수 없습니다') from None


@router.get('/items',response_model=Page[PriceSummary])
def listing(db:Db,viewer:Viewer,category:PriceCategory | None=None,
            keyword:str | None=Query(None,max_length=50),sort:PriceSort=PriceSort.NAME,
            page:int=Query(1,ge=1),size:int=Query(20,ge=1,le=PAGE_MAX_SIZE),market:Market=PriceMarket.RETAIL):
    return service.list_items(db,category,keyword,sort,page,size,market)


@router.get('/items/{item_id}',response_model=PriceDetail)
def detail(item_id:Id,db:Db,viewer:Viewer,market:Market=PriceMarket.RETAIL):
    return call(service.detail,db,item_id,viewer,market)


# 가격 이력은 웹 상세 차트가 90일·180일·1년을 쓰도록 365일까지 받는다. 14·30일은 기존 호출(홈 등)을 위해 유지한다.
HISTORY_DAYS=(14,30,90,180,365)


@router.get('/items/{item_id}/history',response_model=PriceHistory)
def history(item_id:Id,db:Db,viewer:Viewer,days:int=Query(14,ge=14,le=365),market:Market=PriceMarket.RETAIL):
    if days not in HISTORY_DAYS:
        raise HTTPException(400,'기간은 14, 30, 90, 180, 365일 중 선택해 주세요')
    return call(service.history,db,item_id,days,market)


@router.get('/items/{item_id}/forecast',response_model=ForecastResponse)
def forecast(item_id:Id,db:Db,viewer:Viewer,market:Market=PriceMarket.RETAIL):
    return call(service.forecast,db,item_id,market)


@router.get('/items/{item_id}/factors',response_model=PriceFactors)
def factors(item_id:Id,db:Db,viewer:Viewer,market:Market=PriceMarket.RETAIL):
    return call(service.factors,db,item_id,market)


@router.get('/items/{item_id}/factors/{factor_id}/history',response_model=FactorHistory)
def factor_history(item_id:Id,db:Db,viewer:Viewer,factor_id:str=Path(pattern=r'^[A-Za-z0-9]{1,40}$'),
                   days:int=Query(30,ge=14,le=90),market:Market=PriceMarket.RETAIL):
    if days not in (14,30,90):
        raise HTTPException(400,'기간은 14, 30, 90일 중 선택해 주세요')
    try:
        return call(service.factor_history,db,item_id,factor_id,days,market)
    except service.FactorNotFoundError:
        raise HTTPException(404,'공개 예측에 이 요인의 추이가 없습니다') from None
