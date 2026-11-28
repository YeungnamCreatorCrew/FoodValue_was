from datetime import date, timedelta

from sqlalchemy import select

from app.core import constants as C
from app.models.price import ENSEMBLE, RETAIL, PriceModelRun
from app.repositories import indicator_repository, series_repository
from app.repositories import price_repository as repo
from app.schemas.common import Page
from app.schemas.price import (FactorCategory, FactorHistory, FactorHistoryPoint, ForecastPoint, ForecastResponse,
    HistoryPoint, IndicatorSignal, PriceHistories, ListIndicators, PriceDetail, PriceFactor, PriceFactors, PriceGuide, PriceHistory, PriceSummary,
    PriceSummaryText, ValidationRecord, YearRange)
from app.services import price_explanation, price_summary
from app.core.dates import today


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


def summary(item,series,price,previous,run,last,as_of,aliases=()):
    return PriceSummary(id=item.id,name=item.name,aliases=list(aliases),category=item.category,market=series.market,series_id=series.id,
        unit_label=series.unit_label,source=series.source,
        price_date=price.price_date if price else None,current_price=price.price if price else None,
        weekly_change_percent=change(price.price,previous.price) if price and previous else None,
        forecast_price=last.predicted_price if last else None,
        forecast_change_percent=change(last.predicted_price,price.price) if last and price else None,
        forecast_base_date=run.base_date if run else None,quality=run.quality if run else None,
        forecast_target_date=last.target_date if last else None,
        status=state(price,run,as_of))


def list_indicators(db,series_list,as_of):
    """목록 행에 붙일 지표 요약(소매 계열만). 저장된 스냅샷을 그대로 읽는다."""
    retail=[s.id for s in series_list if s.market==RETAIL]
    result={}
    snapshots=indicator_repository.latest_runs_with_position(db,retail,as_of,C.INDICATOR_SPEC_VERSION)
    seasons=indicator_repository.facts_for_runs(db,[run.id for run,_ in snapshots.values()],'SEASONAL')
    for series_id,(run,position) in snapshots.items():
        if run.status=='INSUFFICIENT_DATA' or not run.summary:
            continue
        fact=position.fact if position and isinstance(position.fact,dict) else {}
        year_range=YearRange(low=fact.get('low'),high=fact.get('high'),percentile=fact.get('percentile')) if position else None
        seasonal_fact=seasons.get(run.id) or {}
        result[series_id]=ListIndicators(as_of_date=run.as_of_date,stale=(as_of-run.as_of_date).days>C.INDICATOR_STALE_DAYS,headline=run.summary.get('headline'),
            signals=[IndicatorSignal(**s) for s in run.summary.get('signals',[])],year_range=year_range,
            seasonal_diff_rate=seasonal_fact.get('diffRate'))
    return result


def list_items(db,category,keyword,sort,page,size,market=RETAIL,track=ENSEMBLE):
    as_of=today()
    rows=repo.catalog(db,category,keyword,market)
    prices,previous,runs,forecasts=repo.overview_rows(db,[s for _,s in rows],as_of,track)
    names=repo.aliases(db,[item.id for item,_ in rows])
    result=[summary(item,s,prices.get(s.id),previous.get(s.id),runs.get(s.id),forecasts.get(s.id),as_of,names.get(item.id,()))
            for item,s in rows]
    signals=list_indicators(db,[s for _,s in rows],as_of)
    for row in result:
        row.indicators=signals.get(row.series_id)
    if sort!='name':
        field='weekly_change_percent' if sort=='change' else 'forecast_change_percent'
        result.sort(key=lambda row:(getattr(row,field) is None,getattr(row,field) or 0,row.name,row.id))
    return Page(items=result[(page-1)*size:page*size],page=page,size=size,total=len(result))


def forecast_result(db,item_id,series,as_of,run,points,track=ENSEMBLE):
    attempt=db.scalar(select(PriceModelRun).where(PriceModelRun.series_id==series.id,PriceModelRun.model_track==track,
        PriceModelRun.base_date<=as_of).order_by(PriceModelRun.base_date.desc(),PriceModelRun.id.desc()).limit(1))
    result=ForecastResponse(item_id=item_id,market=series.market,series_id=series.id,model_track=track,status='NO_FORECAST',
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
    result.validation=validation_record(run)
    result.updated_at=run.finished_at
    result.status='STALE' if (as_of-run.base_date).days>1 or (as_of-run.data_date).days>7 else 'READY' if run.quality=='VALIDATED' else 'BASELINE'
    result.points=[ForecastPoint.model_validate(row) for row in points]
    return result


def forecast(db,item_id,market=RETAIL,track=ENSEMBLE):
    _,series=require_item(db,item_id,market)
    as_of=today()
    run,points,_=repo.snapshot(db,series.id,as_of,track)
    return forecast_result(db,item_id,series,as_of,run,points,track)


def detail(db,item_id,market=RETAIL,track=ENSEMBLE):
    item,series=require_item(db,item_id,market)
    as_of=today()
    prices,previous,runs,forecasts=repo.overview_rows(db,[series],as_of,track)
    run,points,guide=repo.snapshot(db,series.id,as_of,track)
    names=repo.aliases(db,[item_id])
    return PriceDetail(item=summary(item,series,prices.get(series.id),previous.get(series.id),run,points[-1] if points else None,
                                    as_of,names.get(item_id,())),
        forecast=forecast_result(db,item_id,series,as_of,run,points,track),
        guide=PriceGuide.model_validate(guide) if guide else None,summary=summary_text(guide,run))


def history(db,item_id,days,market=RETAIL):
    _,series=require_item(db,item_id,market)
    end=today()
    start=end-timedelta(days=days-1)
    lookup=dict(series_repository.prices(db,series.id,start,end))
    return PriceHistory(item_id=item_id,market=series.market,days=days,start_date=start,end_date=end,
        points=history_points(lookup,start,days))


def history_points(lookup,start,days):
    """날짜별 점(관측이 없는 날은 price=None). 단건·묶음 이력이 같은 규칙을 쓴다."""
    return [HistoryPoint(date=start+timedelta(days=i),price=lookup.get(start+timedelta(days=i))) for i in range(days)]


def histories(db,item_ids,days,market=RETAIL):
    """여러 품목의 최근 days일 이력. 품목 수와 관계없이 SQL 2개(품목·계열, 가격)로 읽는다."""
    end=today()
    start=end-timedelta(days=days-1)
    ids=list(dict.fromkeys(item_ids))  # 순서를 지키며 중복 제거
    found=repo.items(db,ids,market)
    prices=series_repository.prices_by_series(db,[series.id for _,series in found.values()],start,end)
    items=[PriceHistory(item_id=item_id,market=market,days=days,start_date=start,end_date=end,
                        points=history_points(prices[found[item_id][1].id],start,days)) for item_id in ids if item_id in found]
    return PriceHistories(market=market,days=days,start_date=start,end_date=end,items=items,
                          missing_item_ids=[item_id for item_id in ids if item_id not in found])


def summary_text(guide,run=None):
    """저장된 요약 문장. 기준 모델 실행은 저장된 '…로 예측되었습니다'를 쓰지 않고 직전 가격을 그대로 보여준다고 밝힌다."""
    if run is not None and run.quality=='BASELINE':
        return PriceSummaryText(**price_summary.baseline_summary(),generator='TEMPLATE')
    if guide is None or not guide.summary:
        return None
    return PriceSummaryText(**guide.summary,generator=guide.summary_generator)


def _previous(history,base_date,days=7):
    """기준일과 정확히 7일 전의 같은 특징값. 근처 날짜로 대신하지 않는다."""
    target=(base_date-timedelta(days=days)).isoformat()
    hit=next((point for point in history if point['date']==target),None)
    return (hit['value'],date.fromisoformat(target)) if hit and hit['value'] is not None else (None,None)


def validation_record(run):
    """v2 실행 metrics의 검증 실적 → ValidationRecord. 없으면 None(v5 실행)."""
    metrics=run.metrics if run is not None and isinstance(run.metrics,dict) else {}
    record=metrics.get('validation')
    if not isinstance(record,dict) or not record:
        return None
    start,end=_evaluation_period(run)
    return ValidationRecord(mape=record.get('mape'),naive_mape=record.get('naiveMape'),
                            improvement_pct=record.get('improvementPct'),within5_pct=record.get('within5Pct'),
                            points=record.get('points'),evaluation_start=start,evaluation_end=end)


def _evaluation_period(run):
    """실행 metrics에 저장된 최종 평가 구간(과거 검증 기간). 없거나 형식이 다르면 (None, None)."""
    metrics=run.metrics if isinstance(run.metrics,dict) else {}
    try:
        return date.fromisoformat(metrics['evaluationStart']),date.fromisoformat(metrics['evaluationEnd'])
    except (KeyError,TypeError,ValueError):
        return None,None


def factors(db,item_id,market=RETAIL,track=ENSEMBLE):
    """7일 뒤 예측의 변수별 SHAP 기여(원). 기준 모델로 공개된 실행은 설명이 없다(unavailableReason=BASELINE_MODEL)."""
    _,series=require_item(db,item_id,market)
    as_of=today()
    run,points,guide=repo.snapshot(db,series.id,as_of,track)
    result=forecast_result(db,item_id,series,as_of,run,points,track)
    response=PriceFactors(item_id=item_id,market=series.market,model_track=track,base_date=result.base_date,status=result.status,
                          model_name=result.model_name,summary=summary_text(guide,run))
    if run is None:
        response.unavailable_reason='NO_FORECAST'
        return response
    response.evaluation_start,response.evaluation_end=_evaluation_period(run)
    response.validation=validation_record(run)
    header,rows=repo.explanation(db,run.id)
    if header is None:
        response.unavailable_reason='BASELINE_MODEL' if run.quality=='BASELINE' else 'NOT_EXPLAINED'
        return response
    display=price_explanation.display_factors(rows,series.market)
    histories={row['feature']:row['history'] or [] for row in rows}
    texts=response.summary.categories if response.summary else {}
    response.explained=True
    response.method=header.method
    response.horizon_days=header.horizon_days
    response.target_date=run.base_date+timedelta(days=header.horizon_days)
    response.current_price=float(header.current_price)
    response.base_price=float(header.base_price)
    response.predicted_price=header.predicted_price
    response.categories=[FactorCategory(**c,description=texts.get(c['category']))
                         for c in price_explanation.category_totals(display)]
    items=[]
    for factor in display:
        previous,previous_date=(_previous(histories.get(factor['id'],[]),run.base_date) if factor['hasHistory'] else (None,None))
        items.append(PriceFactor(**factor,previous_value=price_explanation.display_value(factor['id'],previous),
                                 previous_date=previous_date))
    response.factors=items
    return response


class FactorNotFoundError(Exception):
    pass


def factor_history(db,item_id,factor_id,days,market=RETAIL,track=ENSEMBLE):
    """공개 실행 기준일까지 최근 days일의 특징값(화면 단위). 배치가 예측 시점에 저장한 값이다."""
    _,series=require_item(db,item_id,market)
    run,_,_=repo.snapshot(db,series.id,today(),track)
    header,rows=repo.explanation(db,run.id) if run else (None,[])
    row=next((r for r in rows if r['feature']==factor_id),None)
    if row is None:
        raise FactorNotFoundError
    start=run.base_date-timedelta(days=days-1)
    points=[FactorHistoryPoint(date=point['date'],value=price_explanation.display_value(factor_id,point['value']))
            for point in row['history'] or [] if date.fromisoformat(point['date'])>=start]
    meta=price_explanation.FEATURES.get(factor_id,(factor_id,'','PRICE',1))
    return FactorHistory(item_id=item_id,market=series.market,factor_id=factor_id,
                         label=price_explanation.label(factor_id,series.market),unit=meta[1],
                         base_date=run.base_date,days=days,points=points)
