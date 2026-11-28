"""판단 보조 지표 저장·조회."""
from datetime import date

from sqlalchemy import delete, func, select

from app.models.indicator import PriceIndicatorCard, PriceIndicatorRun, PriceIndicatorValidation


def latest_run(db, series_id, as_of: date, spec_version):
    return db.scalar(select(PriceIndicatorRun).where(
        PriceIndicatorRun.series_id == series_id, PriceIndicatorRun.spec_version == spec_version,
        PriceIndicatorRun.as_of_date <= as_of).order_by(PriceIndicatorRun.as_of_date.desc(), PriceIndicatorRun.id.desc()).limit(1))


def latest_runs_with_position(db, series_ids, as_of: date, spec_version):
    """목록용 일괄 조회: 계열 id → (최신 실행, PRICE_POSITION 카드 또는 None). 쿼리 수는 품목 수와 무관하다."""
    if not series_ids:
        return {}
    ranked = select(PriceIndicatorRun.id.label('id'), func.row_number().over(
        partition_by=PriceIndicatorRun.series_id,
        order_by=(PriceIndicatorRun.as_of_date.desc(), PriceIndicatorRun.id.desc())).label('rank')).where(
        PriceIndicatorRun.series_id.in_(series_ids), PriceIndicatorRun.spec_version == spec_version,
        PriceIndicatorRun.as_of_date <= as_of).subquery()
    runs = db.scalars(select(PriceIndicatorRun).join(ranked, PriceIndicatorRun.id == ranked.c.id)
                      .where(ranked.c.rank == 1)).all()
    positions = {c.run_id: c for c in db.scalars(select(PriceIndicatorCard).where(
        PriceIndicatorCard.run_id.in_([r.id for r in runs]), PriceIndicatorCard.indicator_key == 'PRICE_POSITION')).all()}
    return {r.series_id: (r, positions.get(r.id)) for r in runs}


def cards(db, run_id) -> list[PriceIndicatorCard]:
    return list(db.scalars(select(PriceIndicatorCard).where(PriceIndicatorCard.run_id == run_id)
                           .order_by(PriceIndicatorCard.id)).all())


def facts_for_runs(db, run_ids, key):
    """목록의 같은 실행들에서 특정 지표 fact를 한 번에 읽는다(품목별 추가 조회 없음)."""
    if not run_ids:
        return {}
    return dict(db.execute(select(PriceIndicatorCard.run_id, PriceIndicatorCard.fact).where(
        PriceIndicatorCard.run_id.in_(run_ids), PriceIndicatorCard.indicator_key == key)).all())


def validation_before(db, series_id, key, spec_version, as_of: date):
    """기준일 이하의 가격으로 만든(data_end ≤ as_of) 가장 최근 검증. 기준일 이후 자료로 만든 검증은 쓰지 않는다."""
    return db.scalar(select(PriceIndicatorValidation).where(
        PriceIndicatorValidation.series_id == series_id, PriceIndicatorValidation.indicator_key == key,
        PriceIndicatorValidation.spec_version == spec_version, PriceIndicatorValidation.data_end <= as_of)
        .order_by(PriceIndicatorValidation.data_end.desc(), PriceIndicatorValidation.id.desc()).limit(1))


def save_validation(db, series_id, key, spec_version, verdict, stats, data_start, data_end):
    row = db.scalar(select(PriceIndicatorValidation).where(
        PriceIndicatorValidation.series_id == series_id, PriceIndicatorValidation.indicator_key == key,
        PriceIndicatorValidation.spec_version == spec_version, PriceIndicatorValidation.data_end == data_end))
    if row is None:
        row = PriceIndicatorValidation(series_id=series_id, indicator_key=key, spec_version=spec_version,
                                       data_start=data_start, data_end=data_end)
        db.add(row)
    row.verdict, row.stats, row.data_start = verdict, stats, data_start
    db.flush()
    return row


def replace_run(db, series_id, as_of, data_date, spec_version, status, summary, card_rows, notices=()):
    """같은 계열·기준일·규칙 버전의 실행을 카드와 함께 교체한다(재실행해도 중복 없음). 호출자가 commit한다."""
    old = db.scalars(select(PriceIndicatorRun.id).where(
        PriceIndicatorRun.series_id == series_id, PriceIndicatorRun.as_of_date == as_of,
        PriceIndicatorRun.spec_version == spec_version)).all()
    if old:
        db.execute(delete(PriceIndicatorCard).where(PriceIndicatorCard.run_id.in_(old)))
        db.execute(delete(PriceIndicatorRun).where(PriceIndicatorRun.id.in_(old)))
        db.flush()
    run = PriceIndicatorRun(series_id=series_id, as_of_date=as_of, data_date=data_date, spec_version=spec_version,
                            status=status, summary=summary, notices=list(notices))
    db.add(run)
    db.flush()
    for row in card_rows:
        db.add(PriceIndicatorCard(run_id=run.id, **row))
    db.flush()
    return run
