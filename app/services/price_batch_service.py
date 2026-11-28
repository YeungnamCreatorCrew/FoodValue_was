"""가격 계열(소매·도매)별 전국 가격 7일 예측 배치. 실행마다 예측 7개와 가이드를 한 트랜잭션으로 저장한다."""
from datetime import datetime, timedelta
from statistics import mean

from sqlalchemy import select, text
from sqlalchemy.orm import Session

from app.models.item import Item
from app.models.price import (COUNTERPART, ENSEMBLE, RETAIL, STRUCT, PriceForecast, PriceForecastExplanation, PriceForecastFactor,
    PriceInsight, PriceModelRun, PriceSeries)
from app.repositories import covariate_repository, series_repository
from app.services import price_explanation, price_summary, v2_service
from app.services.exogenous import WEATHER_LAG_DAYS, COUNTERPART_LAG_DAYS
from app.core.dates import today
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


BLOCK_LABELS = {'MARKET': '상대 시장 가격', 'WEATHER': '기상(주산지·전국)', 'CALENDAR': '공휴일·명절',
                'SEASONAL': '과거 같은 시기 변동률', 'MACRO': '생산량·환율'}


def _usage(result):
    """외부 원천 사용 여부와 묶음별 가중치. XGBOOST_EXT는 모든 외부 특징을 한 모델에 넣으므로 묶음 가중치가 없다."""
    weighting = result.metrics.get('weighting') or {}
    weights = weighting.get('weights') or {}
    if result.model == 'XGBOOST_WEIGHTED':
        return (lambda block: weights.get(block, 0) > 0), weights
    return (lambda block: result.model == 'XGBOOST_EXT'), {}


def external_factors(covariates,base_date,result,market=RETAIL):
    """모델이 사용할 수 있었던 외부 원천의 최근 관측값. 영향 방향·기여도는 만들지 않는다."""
    used_by, weights = _usage(result)

    def note(block):
        if result.model == 'XGBOOST_WEIGHTED':
            return f'가중 결합 모델에서 이 자료 묶음의 가중치는 {weights.get(block, 0):.2f}입니다.'
        return '외부 원천 특징을 포함한 모델이 선택되었습니다.' if used_by(block) else '과거 검증에서 외부 원천 특징을 포함한 모델이 선택되지 않았습니다.'

    def tag(block):
        return {'usedByModel': used_by(block), **({'modelWeight': round(weights.get(block, 0), 4)} if weights else {})}

    factors=[]
    counter_as_of=base_date-timedelta(days=COUNTERPART_LAG_DAYS)
    counter=[(d,p) for d,p in sorted(covariates.counterpart.items()) if counter_as_of-timedelta(days=7)<=d<=counter_as_of]
    if counter:
        day,price=counter[-1]
        label={'RETAIL':'소매','WHOLESALE':'도매'}[COUNTERPART[market]]
        factors.append({'name':f'{label}가격','kind':'OBSERVATION','source':'KAMIS','market':COUNTERPART[market],
            'latestPrice':round(price),'dataDate':day.isoformat(),**tag('MARKET'),
            'description':f'KAMIS 전국 평균 {label}가격입니다. '+note('MARKET')})
    weather_as_of=base_date-timedelta(days=WEATHER_LAG_DAYS)
    week=[covariates.weather[d] for d in (weather_as_of-timedelta(days=k) for k in range(7)) if d in covariates.weather]
    if week:
        temps=[row['avgTa'] for row in week if row.get('avgTa') is not None]
        rains=[row['sumRn'] for row in week if row.get('sumRn') is not None]
        factors.append({'name':'주산지 기상','kind':'OBSERVATION','source':'KMA','days':len(week),
            'dataDate':weather_as_of.isoformat(),'meanTemperature7':round(mean(temps),1) if temps else None,
            'precipitationSum7':round(sum(rains),1) if rains else None,**tag('WEATHER'),
            'description':'검증된 주산지 관측소의 최근 7일 관측값입니다. '+note('WEATHER')})
    upcoming=[(d,n) for d,n in sorted(covariates.holidays.items()) if base_date<d<=base_date+timedelta(days=7)]
    if upcoming:
        factors.append({'name':'공휴일','kind':'CALENDAR','source':'KASI',**tag('CALENDAR'),
            'holidays':[{'date':d.isoformat(),'name':n} for d,n in upcoming],
            'description':'예측 기간에 포함된 공휴일입니다. '+note('CALENDAR')})
    if weights:
        factors.append({'name':'외부변수 가중치','kind':'MODEL','method':'constrained_ridge_stacking',
            'weights':[{'block':block,'label':BLOCK_LABELS.get(block,block),'weight':round(value,4)}
                       for block,value in weights.items()],
            'description':'가격만 쓴 예측을 각 자료 묶음의 예측이 고치는 정도를 얼마나 반영했는지(0~1)입니다. '
                          '과거 예측 오차로 학습한 결합 비중이며 가격에 대한 인과적 영향이 아닙니다.'})
    return factors


def explanation_rows(explanation):
    """Explanation → price_forecast_factor 행. NaN은 NULL로 바꾼다(JSONB는 NaN을 받지 않는다)."""
    if explanation is None:
        return []
    return [{'feature':name,'value':explanation.values.get(name),'contribution':round(value,4),
             'history':[{'date':d,'value':price_explanation.clean(v)} for d,v in explanation.history.get(name,[])]}
            for name,value in explanation.contributions.items()]


HISTORY_DAYS=1854


def load_inputs(db,series,base_date):
    """기준일까지의 계열 가격과 외부 원천. 백테스트도 같은 함수를 써서 운영과 같은 입력을 만든다."""
    rows=series_repository.prices(db,series.id,base_date-timedelta(days=HISTORY_DAYS),base_date)
    # 외부 원천은 기준일까지(공휴일·명절 기간만 목표일까지) 읽는다. 공개지연은 특징 생성 단계에서 다시 적용한다.
    covariates=covariate_repository.load(db,series,base_date-timedelta(days=HISTORY_DAYS),base_date,base_date+timedelta(days=7))
    return rows,covariates


def _v2_key(db,series):
    """v2 대상 계열이면 '품목|시장' 키, 아니면 None(v2가 꺼져 있어도 None)"""
    if not v2_service.enabled():
        return None
    return v2_service.series_key(db.get(Item,series.item_id).name,series.source,series.market)


def _run(engine,series_id,base_date,track=ENSEMBLE):
    if base_date>today():
        raise ValueError('미래 기준일로 실행할 수 없습니다')
    with Session(engine,expire_on_commit=False) as db:
        series=db.get(PriceSeries,series_id)
        if series is None:
            raise ValueError('가격 계열이 없습니다')
        # 과거 날짜를 다시 실행해 최신 결과를 뒤로 돌리지 않는다.
        newest=db.scalar(select(PriceModelRun.base_date).where(PriceModelRun.series_id==series_id,
            PriceModelRun.model_track==track,PriceModelRun.status=='SUCCESS').order_by(PriceModelRun.base_date.desc()).limit(1))
        if newest and base_date<newest:
            raise ValueError('최신 공개 기준일보다 과거인 배치는 실행할 수 없습니다')
        rows,covariates=load_inputs(db,series,base_date)
        item_name=db.get(Item,series.item_id).name
        market=series.market
        v2_key=_v2_key(db,series)
        if track==STRUCT and not v2_key:
            raise ValueError('struct 트랙은 v2 대상 계열(FOODVALUE_PRICE_MODEL=v2)에서만 실행합니다')
        run=PriceModelRun(series_id=series_id,model_track=track,base_date=base_date,data_date=rows[-1][0] if rows else None,status='RUNNING')
        db.add(run)
        db.commit()
        run_id=run.id
    try:
        if v2_key:
            if not rows:
                raise InsufficientDataError('가격 자료 없음')
            result=v2_service.prediction(engine,v2_key,base_date,rows[-1][1],track)
        else:
            result=predict([(d,p) for d,p in rows],base_date,covariates,explain=True)
        if len(result.prices)!=7 or len(result.lower)!=7 or len(result.upper)!=7:
            raise ValueError('예측 결과는 7개여야 합니다')
        current=rows[-1][1]
        recommendation,after,saving=guidance(result.prices,current,result.quality)
        # 실제 시세 통계만 근거로 저장한다. 날씨·생산량 영향이나 SHAP 기여도를 만들어내지 않는다.
        week=[p for d,p in rows if d>=base_date-timedelta(days=6)]
        factors=[{'name':'최근 가격','kind':'OBSERVATION','latestPrice':current,
                  'dataDate':rows[-1][0].isoformat(),'mean7Observed':round(mean(week),2) if week else None,
                  'description':'관측된 최근 가격 통계입니다. 모델의 인과적 기여도가 아닙니다.'}]
        factors+=external_factors(covariates,base_date,result,series.market)
        explanation=result.explanation
        shap_rows=explanation_rows(explanation)
        display=price_explanation.display_factors(shap_rows,market) if shap_rows else []
        # LLM 호출은 DB 연결을 잡지 않은 상태에서 한다. 실패해도 고정 문장으로 대체되어 배치는 계속된다.
        summary,generator,summary_model,prompt_version=price_summary.generate(
            item_name,market,current,result.prices[-1],price_explanation.category_totals(display),display,
            model=price_summary.STRUCT_MODEL if track==STRUCT else price_summary.TREE_MODEL)
        with Session(engine,expire_on_commit=False) as db:
            # 같은 날 다시 실행해도 이전 실행의 예측은 지우지 않는다. 공개는 최신 성공 실행을 고른다.
            for index,price in enumerate(result.prices):
                db.add(PriceForecast(target_date=base_date+timedelta(days=index+1),
                    predicted_price=price,lower_price=result.lower[index],upper_price=result.upper[index],model_run_id=run_id))
            score=result.metrics['evaluation'][result.model]
            db.add(PriceInsight(recommendation=recommendation,
                buy_after_days=after,expected_saving=saving,mape=score['mape'],factors=factors,model_run_id=run_id,
                summary=summary,summary_generator=generator,summary_model=summary_model,summary_prompt_version=prompt_version))
            if explanation:
                db.add(PriceForecastExplanation(model_run_id=run_id,horizon_days=explanation.horizon,method=explanation.method,
                    current_price=round(explanation.current_price,2),damping=explanation.damping,
                    base_price=round(explanation.base_price,2),predicted_price=explanation.predicted_price))
                db.flush()
                db.add_all(PriceForecastFactor(model_run_id=run_id,feature=row['feature'],feature_value=row['value'],
                    contribution=row['contribution'],history=row['history']) for row in shap_rows)
            run=db.get(PriceModelRun,run_id)
            run.status='SUCCESS'
            run.model_name=result.model
            run.model_version=result.metrics.get('modelVersion',MODEL_VERSION)
            run.quality=result.quality
            run.metrics=result.metrics
            run.finished_at=datetime.now()
            db.commit()
            return {'runId':run_id,'track':track,'status':run.status,'model':run.model_name,'quality':run.quality}
    except Exception as error:
        with Session(engine) as db:
            run=db.get(PriceModelRun,run_id)
            run.status='INSUFFICIENT_DATA' if isinstance(error,InsufficientDataError) else 'FAILED'
            # 접속 주소·비밀정보가 포함될 수 있어 예외 원문은 기록하지 않는다.
            run.error_code=type(error).__name__[:40]
            run.finished_at=datetime.now()
            db.commit()
        if isinstance(error,InsufficientDataError):
            return {'runId':run_id,'track':track,'status':'INSUFFICIENT_DATA'}
        raise


def series_id_for(engine,item_id,market=RETAIL):
    with Session(engine) as db:
        series=series_repository.get(db,item_id,market)
    if series is None:
        raise ValueError('품목에 해당 시장의 가격 계열이 없습니다')
    return series.id


def struct_target(engine,series_id):
    if not v2_service.struct_enabled():
        return False
    with Session(engine) as db:
        series=db.get(PriceSeries,series_id)
        return series is not None and _v2_key(db,series) is not None


def _run_struct(engine,series_id,base_date):
    """struct 트랙 실행. 실패해도 앙상블 실행 결과·배치 종료 코드에 영향을 주지 않는다(결과의 'struct'에만 남김)."""
    try:
        return _run(engine,series_id,base_date,STRUCT)
    except Exception as error:
        # 접속 주소·비밀정보가 포함될 수 있어 예외 원문은 기록하지 않는다.
        return {'track':STRUCT,'status':'FAILED','errorCode':type(error).__name__}


def run(engine,series_id,base_date=None):
    """계열 하나의 예측 배치. 기본(ENSEMBLE) 트랙을 실행하고, struct 대상 계열이면 STRUCT 트랙도 이어서 실행한다."""
    if engine.dialect.name!='postgresql':
        raise ValueError('예측 공개에는 PostgreSQL이 필요합니다')
    # 잠금용 연결은 commit 후에도 풀에 반환하지 않는다. finally에서 명시적으로 해제한다.
    name=f'foodvalue-price-series:{series_id}'
    with engine.connect() as lock:
        acquired=lock.scalar(text('SELECT pg_try_advisory_lock(hashtextextended(:name,0))'),{'name':name})
        lock.commit()
        if not acquired:
            raise BatchBusyError('이미 실행 중인 계열입니다')
        try:
            base_date=base_date or today()
            struct=struct_target(engine,series_id)
            try:
                result=_run(engine,series_id,base_date)
            except Exception:
                if struct:  # 앙상블이 실패해도 struct는 따로 저장한다
                    _run_struct(engine,series_id,base_date)
                raise
            if struct:
                result['struct']=_run_struct(engine,series_id,base_date)
            return result
        finally:
            lock.execute(text('SELECT pg_advisory_unlock(hashtextextended(:name,0))'),{'name':name})
            lock.commit()
