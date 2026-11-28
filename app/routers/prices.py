from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, Path, Query
from sqlalchemy.orm import Session

from app.core.constants import ID_MAX, PAGE_MAX_SIZE
from app.core.db import get_db
from app.schemas.common import Page
from app.schemas.price import (FactorHistory, ForecastResponse, PriceCategory, PriceDetail, PriceFactors, PriceHistory, PriceIndicators,
    PriceHistories, PriceMarket, PriceModelTrack, PriceSort, PriceSummary)
from app.services import indicator_service
from app.services import price_service as service

router=APIRouter(prefix='/prices',tags=['prices'])
Db=Annotated[Session,Depends(get_db)]
Id=Annotated[int,Path(ge=1,le=ID_MAX)]
Market=Annotated[PriceMarket,Query(description='RETAIL 소매(기본) 또는 WHOLESALE 도매')]
# 같은 응답 형식으로 모델 트랙을 고른다. STRUCT 실행이 없는 계열(v2 대상 밖)은 앙상블로 대신하지 않고 NO_FORECAST다.
Model=Annotated[PriceModelTrack,Query(description='ENSEMBLE 앙상블(기본) 또는 STRUCT 구조적 가격 전달 모델')]


def call(fn,*args):
    try:
        return fn(*args)
    except service.NotFoundError:
        raise HTTPException(404,'시세 제공 품목을 찾을 수 없습니다') from None


@router.get('/items',response_model=Page[PriceSummary])
def listing(db:Db,category:PriceCategory | None=None,
            keyword:str | None=Query(None,max_length=50),sort:PriceSort=PriceSort.NAME,
            page:int=Query(1,ge=1),size:int=Query(20,ge=1,le=PAGE_MAX_SIZE),market:Market=PriceMarket.RETAIL,
            model:Model=PriceModelTrack.ENSEMBLE):
    return service.list_items(db,category,keyword,sort,page,size,market,model)


# 가격 이력은 웹 상세 차트가 90일·180일·1년을 쓰도록 365일까지 받는다. 14·30일은 기존 호출(홈 등)을 위해 유지한다.
HISTORY_DAYS=(14,30,90,180,365)


def _item_ids(ids:str=Query(description='품목 id 쉼표 목록(최대 50개). 예: 60,130,131')):
    try:
        values=[int(value) for value in ids.split(',') if value.strip()]
    except ValueError:
        raise HTTPException(400,'품목 id는 숫자를 쉼표로 이어 주세요') from None
    if not values or len(set(values))>PAGE_MAX_SIZE or any(not 1<=value<=ID_MAX for value in values):
        raise HTTPException(400,f'품목 id는 1~{PAGE_MAX_SIZE}개를 지정해 주세요')
    return values


# 여러 품목 이력을 한 요청·SQL 2개로 준다(분석실 미니 그래프의 품목별 N번 호출 대신). /items/{item_id}보다 먼저 선언해야 한다.
@router.get('/items/history',response_model=PriceHistories)
def histories(db:Db,item_ids:Annotated[list[int],Depends(_item_ids)],days:int=Query(14,ge=14,le=365),
              market:Market=PriceMarket.RETAIL):
    if days not in HISTORY_DAYS:
        raise HTTPException(400,'기간은 14, 30, 90, 180, 365일 중 선택해 주세요')
    return service.histories(db,item_ids,days,market)


@router.get('/items/{item_id}',response_model=PriceDetail)
def detail(item_id:Id,db:Db,market:Market=PriceMarket.RETAIL,model:Model=PriceModelTrack.ENSEMBLE):
    return call(service.detail,db,item_id,market,model)


@router.get('/items/{item_id}/history',response_model=PriceHistory)
def history(item_id:Id,db:Db,days:int=Query(14,ge=14,le=365),market:Market=PriceMarket.RETAIL):
    if days not in HISTORY_DAYS:
        raise HTTPException(400,'기간은 14, 30, 90, 180, 365일 중 선택해 주세요')
    return call(service.history,db,item_id,days,market)


@router.get('/items/{item_id}/forecast',response_model=ForecastResponse)
def forecast(item_id:Id,db:Db,market:Market=PriceMarket.RETAIL,model:Model=PriceModelTrack.ENSEMBLE):
    return call(service.forecast,db,item_id,market,model)


@router.get('/items/{item_id}/factors',response_model=PriceFactors)
def factors(item_id:Id,db:Db,market:Market=PriceMarket.RETAIL,model:Model=PriceModelTrack.ENSEMBLE):
    return call(service.factors,db,item_id,market,model)


@router.get('/items/{item_id}/factors/{factor_id}/history',response_model=FactorHistory)
def factor_history(item_id:Id,db:Db,factor_id:str=Path(pattern=r'^[A-Za-z0-9_]{1,40}$'),
                   days:int=Query(30,ge=14,le=90),market:Market=PriceMarket.RETAIL,model:Model=PriceModelTrack.ENSEMBLE):
    if days not in (14,30,90):
        raise HTTPException(400,'기간은 14, 30, 90일 중 선택해 주세요')
    try:
        return call(service.factor_history,db,item_id,factor_id,days,market,model)
    except service.FactorNotFoundError:
        raise HTTPException(404,'공개 예측에 이 요인의 추이가 없습니다') from None


@router.get('/items/{item_id}/indicators',response_model=PriceIndicators)
def indicators(item_id:Id,db:Db,market:Market=PriceMarket.RETAIL):
    return call(indicator_service.indicators,db,item_id,market)
