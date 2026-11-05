"""여러 Open API 원천을 수집해 external_observation(원본·버전)과 price_daily(예측 대상)에 적재한다.

- 수집 실행마다 external_collection_run에 상태·요청·수신·삽입 건수를 남긴다.
- 같은 원천 키·같은 내용은 다시 저장하지 않고, 내용이 바뀌면 새 버전으로 보존한다.
- KAMIS 소매 전국 평균만 price_daily(NATIONAL)에 반영한다. 도매가·기상·공휴일은 price_daily에 섞지 않는다.
- 인증키는 환경 변수에서만 읽고 실행 이력·로그에 기록하지 않는다.
"""
import hashlib
import json
import os
from dataclasses import dataclass
from datetime import timedelta

from sqlalchemy import func, select, update
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.orm import Session

from app.collectors import data_go_kr, kamis
from app.collectors.http import CollectorError, fetch_json, number
from app.models.external import ExternalCollectionRun, ExternalObservation, ItemWeatherStation
from app.models.fridge import Item
from app.models.price import PriceDaily
from app.services.fridge_service import today

BACKFILL_DAYS = 1830  # 예측 모델이 사용하는 최대 5년
OVERLAP_DAYS = 14  # 증분 수집도 최근 2주는 다시 받아 원천 수정을 반영한다.
INSERT_CHUNK = 500


@dataclass
class Credentials:
    kamis_cert_key: str | None = None
    kamis_cert_id: str | None = None
    data_go_kr_key: str | None = None

    @classmethod
    def from_env(cls):
        return cls(os.getenv('KAMIS_CERT_KEY') or None, os.getenv('KAMIS_CERT_ID') or None,
                   os.getenv('DATA_GO_KR_SERVICE_KEY') or None)


def digest(payload: dict) -> str:
    return hashlib.sha256(json.dumps(payload, ensure_ascii=False, sort_keys=True, default=str).encode()).hexdigest()


def _start_run(engine, source, dataset, start, end):
    with Session(engine) as db:
        run = ExternalCollectionRun(source=source, dataset=dataset, start_date=start, end_date=end, status='RUNNING')
        db.add(run)
        db.commit()
        return run.id


def _finish(engine, run_id, status, *, requests=0, received=0, inserted=0, error=None):
    with Session(engine) as db:
        db.execute(update(ExternalCollectionRun).where(ExternalCollectionRun.id == run_id).values(
            status=status, request_count=requests, records_received=received, records_inserted=inserted,
            error_code=error[:120] if error else None, finished_at=func.now()))
        db.commit()


def _store(db, run_id, records):
    inserted = 0
    for offset in range(0, len(records), INSERT_CHUNK):
        rows = [{'collection_run_id': run_id, 'item_id': r.item_id, 'source': r.source, 'dataset': r.dataset,
                 'source_record_key': r.key, 'entity_code': r.entity_code, 'entity_name': r.entity_name,
                 'observed_on': r.observed_on, 'period_start': r.observed_on, 'period_end': r.observed_on,
                 'units': r.units, 'payload': r.payload, 'payload_sha256': digest(r.payload)}
                for r in records[offset:offset + INSERT_CHUNK]]
        result = db.execute(insert(ExternalObservation).values(rows)
                            .on_conflict_do_nothing(constraint='uk_external_observation')
                            .returning(ExternalObservation.id))
        inserted += len(result.all())
    return inserted


def _store_retail(db, item_id, records):
    rows = [{'item_id': item_id, 'region': 'NATIONAL', 'price_date': r.observed_on,
             'price': int(round(number(r.payload.get('price'))))} for r in records]
    for offset in range(0, len(rows), INSERT_CHUNK):
        statement = insert(PriceDaily).values(rows[offset:offset + INSERT_CHUNK])
        db.execute(statement.on_conflict_do_update(constraint='uk_price_daily', set_={'price': statement.excluded.price},
                                                   where=PriceDaily.price != statement.excluded.price))


def run_dataset(engine, source, dataset, start, end, collect, *, retail_item_id=None):
    """collect()가 Batch를 반환하면 한 트랜잭션으로 적재하고 실행 이력을 마무리한다."""
    if start > end:
        return {'source': source, 'dataset': dataset, 'status': 'SKIPPED', 'errorCode': 'EMPTY_RANGE'}
    run_id = _start_run(engine, source, dataset, start, end)
    summary = {'runId': run_id, 'source': source, 'dataset': dataset,
               'startDate': start.isoformat(), 'endDate': end.isoformat()}
    try:
        batch = collect()
    except CollectorError as error:
        _finish(engine, run_id, error.status, error=error.code)
        return {**summary, 'status': error.status, 'errorCode': error.code}
    except Exception as error:
        # 요청 URL에 인증키가 있으므로 예외 원문을 남기지 않는다.
        _finish(engine, run_id, 'FAILED', error=type(error).__name__)
        return {**summary, 'status': 'FAILED', 'errorCode': type(error).__name__}
    with Session(engine) as db:
        inserted = _store(db, run_id, batch.records)
        if retail_item_id is not None and batch.records:
            _store_retail(db, retail_item_id, batch.records)
        db.commit()
    status = 'PARTIAL' if batch.partial_error else 'SUCCESS' if batch.records else 'NO_DATA'
    _finish(engine, run_id, status, requests=batch.requests, received=len(batch.records),
            inserted=inserted, error=batch.partial_error)
    return {**summary, 'status': status, 'requests': batch.requests, 'received': len(batch.records),
            'inserted': inserted, **({'errorCode': batch.partial_error} if batch.partial_error else {})}


def skipped(engine, source, dataset, reason):
    run_id = _start_run(engine, source, dataset, None, None)
    _finish(engine, run_id, 'SKIPPED', error=reason)
    return {'runId': run_id, 'source': source, 'dataset': dataset, 'status': 'SKIPPED', 'errorCode': reason}


def incremental_start(engine, source, dataset, end, *, item_id=None, entity_codes=None):
    """저장된 최신 관측일 - OVERLAP_DAYS부터. 자료가 없으면 BACKFILL_DAYS 전부터."""
    conditions = [ExternalObservation.source == source, ExternalObservation.dataset == dataset]
    if item_id is not None:
        conditions.append(ExternalObservation.item_id == item_id)
    if entity_codes is not None:
        conditions.append(ExternalObservation.entity_code.in_(entity_codes))
    with Session(engine) as db:
        if entity_codes:
            # 관측소마다 적재 시점이 다를 수 있어 가장 늦은 관측소를 기준으로 한다.
            latest = db.execute(select(ExternalObservation.entity_code, func.max(ExternalObservation.observed_on))
                                .where(*conditions).group_by(ExternalObservation.entity_code)).all()
            newest = min(day for _, day in latest) if len(latest) == len(set(entity_codes)) else None
        else:
            newest = db.scalar(select(func.max(ExternalObservation.observed_on)).where(*conditions))
    floor = end - timedelta(days=BACKFILL_DAYS)
    return max(floor, newest - timedelta(days=OVERLAP_DAYS)) if newest else floor


def verified_stations(engine, item_ids):
    with Session(engine) as db:
        return sorted(set(db.scalars(select(ItemWeatherStation.station_code).where(
            ItemWeatherStation.item_id.in_(item_ids), ItemWeatherStation.mapping_status == 'VERIFIED')).all()))


def prediction_items(engine, item_ids=None):
    with Session(engine) as db:
        query = select(Item).where(Item.price_source == 'KAMIS', Item.food_type == 'RAW')
        if item_ids:
            query = query.where(Item.id.in_(item_ids))
        return db.scalars(query.order_by(Item.id)).all()


def collect(engine, item_ids=None, *, start=None, end=None, fetch=fetch_json, credentials=None):
    """품목별 KAMIS 소매·도매, 주산지 ASOS 기상, 공휴일을 차례로 수집하고 데이터셋별 결과를 반환한다."""
    if engine.dialect.name != 'postgresql':
        raise ValueError('수집 적재에는 PostgreSQL이 필요합니다')
    credentials = credentials or Credentials.from_env()
    end = min(end or today(), today())
    items = prediction_items(engine, item_ids)
    if item_ids and len(items) != len(set(item_ids)):
        raise ValueError('수집 대상은 KAMIS 원물 품목만 지정할 수 있습니다')
    results = []
    for item in items:
        for dataset in (kamis.RETAIL, kamis.WHOLESALE):
            if not (credentials.kamis_cert_key and credentials.kamis_cert_id):
                results.append({**skipped(engine, kamis.SOURCE, dataset, 'MISSING_KAMIS_CREDENTIALS'), 'itemId': item.id})
                continue
            first = start or incremental_start(engine, kamis.SOURCE, dataset, end, item_id=item.id)
            def call(dataset=dataset, first=first, item=item):
                return kamis.collect(fetch, code=item.price_code, dataset=dataset, item_id=item.id,
                                     unit_label=item.price_unit_label, start=first, end=end,
                                     cert_key=credentials.kamis_cert_key, cert_id=credentials.kamis_cert_id)
            result = run_dataset(engine, kamis.SOURCE, dataset, first, end, call,
                                 retail_item_id=item.id if dataset == kamis.RETAIL else None)
            results.append({**result, 'itemId': item.id})
    if not credentials.data_go_kr_key:
        results.append(skipped(engine, data_go_kr.KMA, data_go_kr.ASOS, 'MISSING_DATA_GO_KR_KEY'))
        results.append(skipped(engine, data_go_kr.KASI, data_go_kr.HOLIDAY, 'MISSING_DATA_GO_KR_KEY'))
        return results
    stations = verified_stations(engine, [item.id for item in items])
    weather_end = min(end, today() - timedelta(days=1))  # ASOS 일자료는 전일까지 제공된다.
    if stations:
        first = start or incremental_start(engine, data_go_kr.KMA, data_go_kr.ASOS, weather_end, entity_codes=stations)
        results.append(run_dataset(engine, data_go_kr.KMA, data_go_kr.ASOS, first, weather_end,
                                   lambda: data_go_kr.collect_asos(fetch, key=credentials.data_go_kr_key,
                                                                   stations=stations, start=first, end=weather_end)))
    else:
        results.append(skipped(engine, data_go_kr.KMA, data_go_kr.ASOS, 'NO_VERIFIED_STATION'))
    # 임시공휴일 지정을 반영하도록 올해·내년은 매번 다시 받는다. 처음이면 백필 기간 전체를 받는다.
    first = start or incremental_start(engine, data_go_kr.KASI, data_go_kr.HOLIDAY, end)
    first = min(first, end.replace(month=1, day=1))
    last = end.replace(year=end.year + 1, month=12, day=31)
    results.append(run_dataset(engine, data_go_kr.KASI, data_go_kr.HOLIDAY, first, last,
                               lambda: data_go_kr.collect_holidays(fetch, key=credentials.data_go_kr_key,
                                                                   years=range(first.year, last.year + 1))))
    return results

