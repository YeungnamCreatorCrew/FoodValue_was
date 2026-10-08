"""전국 소매가 예측 배치. 공개는 7일 예측과 가이드를 원자적으로 교체한다."""
from datetime import datetime, timedelta
from statistics import mean

from sqlalchemy import delete, select, text
from sqlalchemy.orm import Session

from app.models.fridge import Item
from app.models.price import PriceDaily, PriceForecast, PriceInsight, PriceModelRun
from app.services.fridge_service import today
from app.services.price_prediction import InsufficientDataError, MODEL_VERSION, predict


class BatchBusyError(Exception):
    pass


def guidance(prices, current, quality):
    # 기준 모델 또는 검증 미완료 모델은 단정적인 구매 권고를 하지 않는다.
    if quality != 'VALIDATED':
        return 'HOLD', None, None
    low = min(prices)
    day = prices.index(low)+1
    if low <= current*.97:
        return 'BUY_LATER',day,current-low
    if prices[-1] >= current*1.03:
        return 'BUY_NOW',None,0
    return 'STABLE',None,0


def _run(engine,item_id,base_date):
    if base_date>today():
        raise ValueError('미래 기준일로 실행할 수 없습니다')
    with Session(engine,expire_on_commit=False) as db:
        item=db.get(Item,item_id)
        if item is None or item.price_source!='KAMIS' or item.food_type!='RAW':
            raise ValueError('예측 MVP는 KAMIS 원물만 지원합니다')
        # 과거 날짜를 다시 실행해 최신 결과를 뒤로 돌리지 않는다.
        newest=db.scalar(select(PriceModelRun.base_date).where(PriceModelRun.item_id==item_id,
            PriceModelRun.status=='SUCCESS').order_by(PriceModelRun.base_date.desc()).limit(1))
        if newest and base_date<newest:
            raise ValueError('최신 공개 기준일보다 과거인 배치는 실행할 수 없습니다')
        rows=db.execute(select(PriceDaily.price_date,PriceDaily.price).where(PriceDaily.item_id==item_id,
            PriceDaily.region=='NATIONAL',PriceDaily.price_date<=base_date,
            PriceDaily.price_date>=base_date-timedelta(days=1854)).order_by(PriceDaily.price_date)).all()
        run=PriceModelRun(item_id=item_id,base_date=base_date,data_date=rows[-1][0] if rows else None,status='RUNNING')
        db.add(run)
        db.commit()
        run_id=run.id
    try:
        result=predict([(d,p) for d,p in rows],base_date)
        if len(result.prices)!=7 or len(result.lower)!=7 or len(result.upper)!=7:
            raise ValueError('예측 결과는 7개여야 합니다')
        current=rows[-1][1]
        recommendation,after,saving=guidance(result.prices,current,result.quality)
        # 실제 시세 통계만 근거로 저장한다. 날씨·생산량 영향이나 SHAP 기여도를 만들어내지 않는다.
        week=[p for d,p in rows if d>=base_date-timedelta(days=6)]
        factors=[{'name':'최근 가격','kind':'OBSERVATION','latestPrice':current,
                  'dataDate':rows[-1][0].isoformat(),'mean7Observed':round(mean(week),2) if week else None,
                  'description':'관측된 최근 가격 통계입니다. 모델의 인과적 기여도가 아닙니다.'}]
        with Session(engine,expire_on_commit=False) as db:
            db.execute(delete(PriceForecast).where(PriceForecast.item_id==item_id,PriceForecast.base_date==base_date))
            db.execute(delete(PriceInsight).where(PriceInsight.item_id==item_id,PriceInsight.base_date==base_date))
            for index,price in enumerate(result.prices):
                db.add(PriceForecast(item_id=item_id,base_date=base_date,target_date=base_date+timedelta(days=index+1),
                    predicted_price=price,lower_price=result.lower[index],upper_price=result.upper[index],model_run_id=run_id))
            score=result.metrics['evaluation'][result.model]
            db.add(PriceInsight(item_id=item_id,base_date=base_date,recommendation=recommendation,
                buy_after_days=after,expected_saving=saving,mape=score['mape'],factors=factors,model_run_id=run_id))
            run=db.get(PriceModelRun,run_id)
            run.status='SUCCESS'
            run.model_name=result.model
            run.model_version=MODEL_VERSION
            run.quality=result.quality
            run.metrics=result.metrics
            run.finished_at=datetime.now()
            db.commit()
            return {'runId':run_id,'status':run.status,'model':run.model_name,'quality':run.quality}
    except Exception as error:
        with Session(engine) as db:
            run=db.get(PriceModelRun,run_id)
            run.status='INSUFFICIENT_DATA' if isinstance(error,InsufficientDataError) else 'FAILED'
            # 접속 주소·비밀정보가 포함될 수 있어 예외 원문은 기록하지 않는다.
            run.error_code=type(error).__name__[:40]
            run.finished_at=datetime.now()
            db.commit()
        if isinstance(error,InsufficientDataError):
            return {'runId':run_id,'status':'INSUFFICIENT_DATA'}
        raise


def run(engine,item_id,base_date=None):
    if engine.dialect.name!='postgresql':
        raise ValueError('예측 공개에는 PostgreSQL이 필요합니다')
    # 잠금용 연결은 commit 후에도 풀에 반환하지 않는다. finally에서 명시적으로 해제한다.
    name=f'foodvalue-price:{item_id}'
    with engine.connect() as lock:
        acquired=lock.scalar(text('SELECT pg_try_advisory_lock(hashtextextended(:name,0))'),{'name':name})
        lock.commit()
        if not acquired:
            raise BatchBusyError('이미 실행 중인 품목입니다')
        try:
            return _run(engine,item_id,base_date or today())
        finally:
            lock.execute(text('SELECT pg_advisory_unlock(hashtextextended(:name,0))'),{'name':name})
            lock.commit()
