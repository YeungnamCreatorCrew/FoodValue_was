"""여러 Open API 원천을 수집해 external_observation(원본·버전)과 price_daily(예측 대상)에 적재한다.

- 수집 실행마다 external_collection_run에 상태·요청·수신·삽입 건수를 남긴다.
- 같은 원천 키·같은 내용은 다시 저장하지 않고, 내용이 바뀌면 새 버전으로 보존한다.
- KAMIS 가격은 품목의 가격 계열(price_series: 소매·도매)마다 수집한다. price_daily는 수집 직후
  warehouse_service.refresh_price_daily가 원본 최신 버전에서 만든다(정제 단계와 같은 경로).
- 인증키는 환경 변수에서만 읽고 실행 이력·로그에 기록하지 않는다.
"""
import hashlib
import json
import os
from dataclasses import dataclass
from datetime import date, datetime, timedelta
from zoneinfo import ZoneInfo

from sqlalchemy import exists, func, select, update
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.orm import Session

from app.collectors import data_go_kr, ecos, garak, kamis, kosis, krei
from app.collectors.http import CollectorError, fetch_bytes, fetch_json, fetch_text
from app.models.external import ExternalCollectionRun, ExternalObservation, ItemWeatherStation
from app.models.fridge import Item
from app.models.price import RETAIL, PriceSeries
from app.repositories import series_repository
from app.services import warehouse_service
from app.services.fridge_service import today

BACKFILL_DAYS = 1830  # 예측 모델이 사용하는 최대 5년
KOSIS_RECENT_YEARS = 6  # 연간 생산량은 최근 6년을 매번 다시 받아 수정 공표를 반영
OVERLAP_DAYS = 14  # 증분 수집도 최근 2주는 다시 받아 원천 수정을 반영한다.
INSERT_CHUNK = 500
SEOUL = ZoneInfo('Asia/Seoul')


@dataclass
class Credentials:
    kamis_cert_key: str | None = None
    kamis_cert_id: str | None = None
    data_go_kr_key: str | None = None
    kosis_key: str | None = None
    ecos_key: str | None = None
    garak_id: str | None = None
    garak_password: str | None = None

    @classmethod
    def from_env(cls):
        return cls(os.getenv('KAMIS_CERT_KEY') or None, os.getenv('KAMIS_CERT_ID') or None,
                   os.getenv('DATA_GO_KR_SERVICE_KEY') or None, os.getenv('KOSIS_API_KEY') or None,
                   os.getenv('ECOS_API_KEY') or None, os.getenv('GARAK_API_ID') or None,
                   os.getenv('GARAK_API_PASSWORD') or None)


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


def published(value):
    if value is None or isinstance(value, datetime):
        return value
    return datetime(value.year, value.month, value.day, tzinfo=SEOUL)  # 날짜만 주는 원천은 서울 자정


def _store(db, run_id, records):
    inserted = 0
    for offset in range(0, len(records), INSERT_CHUNK):
        rows = [{'collection_run_id': run_id, 'item_id': r.item_id, 'source': r.source, 'dataset': r.dataset,
                 'source_record_key': r.key, 'entity_code': r.entity_code, 'entity_name': r.entity_name,
                 'observed_on': r.observed_on, 'period_start': r.period_start or r.observed_on,
                 'period_end': r.period_end or r.observed_on, 'issued_at': r.issued_at,
                 'published_at': published(r.published_at),
                 'publication_status': 'SOURCE_PROVIDED' if r.published_at else 'UNKNOWN',
                 'units': r.units, 'payload': r.payload, 'payload_sha256': digest(r.payload)}
                for r in records[offset:offset + INSERT_CHUNK]]
        result = db.execute(insert(ExternalObservation).values(rows)
                            .on_conflict_do_nothing(constraint='uk_external_observation')
                            .returning(ExternalObservation.id))
        inserted += len(result.all())
    return inserted


def run_dataset(engine, source, dataset, start, end, collect):
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


def incremental_start(engine, source, dataset, end, *, item_id=None):
    """저장된 최신 관측일 - OVERLAP_DAYS부터. 자료가 없으면 BACKFILL_DAYS 전부터."""
    conditions = [ExternalObservation.source == source, ExternalObservation.dataset == dataset]
    if item_id is not None:
        conditions.append(ExternalObservation.item_id == item_id)
    with Session(engine) as db:
        newest = db.scalar(select(func.max(ExternalObservation.observed_on)).where(*conditions))
    floor = end - timedelta(days=BACKFILL_DAYS)
    return max(floor, newest - timedelta(days=OVERLAP_DAYS)) if newest else floor


def station_starts(engine, stations, end):
    """관측소별 증분 시작일. 자료가 없는 관측소(새로 추가·폐지)는 백필 기간 전체를 다시 확인한다."""
    floor = end - timedelta(days=BACKFILL_DAYS)
    with Session(engine) as db:
        latest = dict(db.execute(select(ExternalObservation.entity_code, func.max(ExternalObservation.observed_on))
                                 .where(ExternalObservation.source == data_go_kr.KMA,
                                        ExternalObservation.dataset == data_go_kr.ASOS,
                                        ExternalObservation.entity_code.in_(stations))
                                 .group_by(ExternalObservation.entity_code)).all())
    return {code: max(floor, latest[code] - timedelta(days=OVERLAP_DAYS)) if code in latest else floor
            for code in stations}


def collect_kosis(engine, items, start, end, fetch, credentials):
    """연간 생산량. 수정 공표를 반영하도록 매번 최근 KOSIS_RECENT_YEARS년을 다시 받는다."""
    targets = [(item.id, item.name) for item in items if item.name in kosis.PRODUCTION_SERIES]
    if not credentials.kosis_key:
        return skipped(engine, kosis.SOURCE, kosis.DATASET, 'MISSING_KOSIS_KEY')
    if not targets:
        return skipped(engine, kosis.SOURCE, kosis.DATASET, 'NO_KOSIS_SERIES')
    first_year = start.year if start else end.year - KOSIS_RECENT_YEARS
    return run_dataset(engine, kosis.SOURCE, kosis.DATASET, date(first_year, 1, 1), date(end.year, 12, 31),
                       lambda: kosis.collect(fetch, key=credentials.kosis_key, items=targets,
                                             start_year=first_year, end_year=end.year))


def collect_ecos(engine, start, end, fetch, credentials):
    """일별 원/미국달러 환율. 예측 모델 MACRO 묶음의 FX 특징(7·28일 변화율)으로 쓴다."""
    if not credentials.ecos_key:
        return skipped(engine, ecos.SOURCE, ecos.DATASET, 'MISSING_ECOS_KEY')
    first = start or incremental_start(engine, ecos.SOURCE, ecos.DATASET, end)
    return run_dataset(engine, ecos.SOURCE, ecos.DATASET, first, end,
                       lambda: ecos.collect(fetch, key=credentials.ecos_key, start=first, end=end))


def collect_krei_monthly(engine, *, start_year, end_year, cache_dir, groups=tuple(krei.GROUPS), fetch=fetch_bytes):
    """KREI 관측월보 목록·PDF 텍스트·발행일. 인증키가 필요 없다. 월 1회 정도만 돌리면 된다.

    같은 PDF·같은 목록 내용이면 다시 저장하지 않고, 목록(mod_date 등)이나 PDF가 바뀌면 새 버전으로 남는다.
    """
    return run_dataset(engine, krei.SOURCE, krei.DATASET, date(start_year, 1, 1), date(end_year, 12, 31),
                       lambda: krei.collect(fetch, groups=groups, years=range(start_year, end_year + 1),
                                            cache_dir=cache_dir))


def collect_garak(engine, items, start, end, fetch_text, credentials):
    """가락시장 일별 반입량. 날짜마다 모든 품목이 한 번에 오므로 대상 품목 전체를 하나의 실행으로 받는다."""
    targets = {garak.ITEM_CODES[item.name]: item.id for item in items if item.name in garak.ITEM_CODES}
    if not (credentials.garak_id and credentials.garak_password):
        return skipped(engine, garak.SOURCE, garak.DATASET, 'MISSING_GARAK_CREDENTIALS')
    if not targets:
        return skipped(engine, garak.SOURCE, garak.DATASET, 'NO_GARAK_ITEM')
    # 새로 추가된 품목은 자료가 없으므로 품목별 최신일 중 가장 이른 날부터 받는다.
    first = start or min(incremental_start(engine, garak.SOURCE, garak.DATASET, end, item_id=item_id)
                         for item_id in targets.values())
    first = max(first, garak.FIRST_DAY)
    return run_dataset(engine, garak.SOURCE, garak.DATASET, first, end,
                       lambda: garak.collect(fetch_text, user_id=credentials.garak_id,
                                             password=credentials.garak_password, targets=targets,
                                             start=first, end=end))


def verified_stations(engine, item_ids):
    with Session(engine) as db:
        return sorted(set(db.scalars(select(ItemWeatherStation.station_code).where(
            ItemWeatherStation.item_id.in_(item_ids), ItemWeatherStation.mapping_status == 'VERIFIED')).all()))


def prediction_items(engine, item_ids=None):
    """예측 대상 = 소매 가격 계열이 있는 품목"""
    with Session(engine) as db:
        query = select(Item).where(exists().where(PriceSeries.item_id == Item.id, PriceSeries.market == RETAIL))
        if item_ids:
            query = query.where(Item.id.in_(item_ids))
        return db.scalars(query.order_by(Item.id)).all()


def collect(engine, item_ids=None, *, start=None, end=None, fetch=fetch_json, fetch_text=fetch_text, credentials=None):
    """품목별 KAMIS 소매·도매 계열, 가락 반입량, 주산지 ASOS 기상, 공휴일을 차례로 수집하고 데이터셋별 결과를 반환한다.

    fetch는 JSON 원천, fetch_text는 XML 원천(가락시장)에 쓴다.
    """
    if engine.dialect.name != 'postgresql':
        raise ValueError('수집 적재에는 PostgreSQL이 필요합니다')
    credentials = credentials or Credentials.from_env()
    end = min(end or today(), today())
    items = prediction_items(engine, item_ids)
    if item_ids and len(items) != len(set(item_ids)):
        raise ValueError('수집 대상은 소매 가격 계열이 있는 품목만 지정할 수 있습니다')
    with Session(engine, expire_on_commit=False) as db:
        series = series_repository.of_items(db, [item.id for item in items])
    results, firsts = [], []
    for row in series:
        dataset = kamis.MARKET_DATASETS[row.market]
        if not (credentials.kamis_cert_key and credentials.kamis_cert_id):
            results.append({**skipped(engine, kamis.SOURCE, dataset, 'MISSING_KAMIS_CREDENTIALS'), 'itemId': row.item_id})
            continue
        first = start or incremental_start(engine, kamis.SOURCE, dataset, end, item_id=row.item_id)
        def call(dataset=dataset, first=first, row=row):
            return kamis.collect(fetch, code=row.code, dataset=dataset, item_id=row.item_id,
                                 unit_label=row.unit_label, start=first, end=end,
                                 cert_key=credentials.kamis_cert_key, cert_id=credentials.kamis_cert_id)
        results.append({**run_dataset(engine, kamis.SOURCE, dataset, first, end, call), 'itemId': row.item_id})
        firsts.append(first)
    kamis.clear_daily_cache()
    if firsts:
        # 예측 대상 가격은 원본 최신 버전에서 다시 만든다(정제 단계와 같은 함수).
        warehouse_service.refresh_price_daily(engine, [item.id for item in items], since=min(firsts))
    results.append(collect_kosis(engine, items, start, end, fetch, credentials))
    results.append(collect_ecos(engine, start, end, fetch, credentials))
    results.append(collect_garak(engine, items, start, end, fetch_text, credentials))
    if not credentials.data_go_kr_key:
        results.append(skipped(engine, data_go_kr.KMA, data_go_kr.ASOS, 'MISSING_DATA_GO_KR_KEY'))
        results.append(skipped(engine, data_go_kr.KMA, data_go_kr.VILAGE, 'MISSING_DATA_GO_KR_KEY'))
        results.append(skipped(engine, data_go_kr.KASI, data_go_kr.HOLIDAY, 'MISSING_DATA_GO_KR_KEY'))
        return results
    # 품목 주산지(검증) 관측소 + weather_daily 전국 집계용 관측소
    stations = sorted(set(verified_stations(engine, [item.id for item in items])) | set(data_go_kr.NATIONAL_STATIONS))
    weather_end = min(end, today() - timedelta(days=1))  # ASOS 일자료는 전일까지 제공된다.
    starts = {code: start for code in stations} if start else station_starts(engine, stations, weather_end)
    first = min(starts.values())
    results.append(run_dataset(engine, data_go_kr.KMA, data_go_kr.ASOS, first, weather_end,
                               lambda: data_go_kr.collect_asos(fetch, key=credentials.data_go_kr_key,
                                                               stations=starts, end=weather_end)))
    # 단기예보는 매 실행 시 최신 발표본 1회분을 받는다(과거 발표본은 API에서 제공하지 않음).
    base = data_go_kr.vilage_base(datetime.now(SEOUL))
    results.append(run_dataset(engine, data_go_kr.KMA, data_go_kr.VILAGE, base.date(), base.date() + timedelta(days=4),
                               lambda: data_go_kr.collect_vilage(fetch, key=credentials.data_go_kr_key, base=base)))
    # 임시공휴일 지정을 반영하도록 올해·내년은 매번 다시 받는다. 처음이면 백필 기간 전체를 받는다.
    first = start or incremental_start(engine, data_go_kr.KASI, data_go_kr.HOLIDAY, end)
    first = min(first, end.replace(month=1, day=1))
    last = end.replace(year=end.year + 1, month=12, day=31)
    results.append(run_dataset(engine, data_go_kr.KASI, data_go_kr.HOLIDAY, first, last,
                               lambda: data_go_kr.collect_holidays(fetch, key=credentials.data_go_kr_key,
                                                                   years=range(first.year, last.year + 1))))
    return results

