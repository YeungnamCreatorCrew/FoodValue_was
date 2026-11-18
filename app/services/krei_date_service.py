"""KREI 날짜 메타데이터만 원자적으로 정정한다. 수집/수치 재적재를 호출하지 않는다.

백업·격리 복원·원본 대조는 호출자가 먼저 완료해야 한다. 일반 CLI에서는 자동 실행하지 않는다.
수치 내용/관계는 그대로 두고 기존 published_at 후보와 payload.available_from을 일치시킨다.
"""
from datetime import date, datetime

from sqlalchemy import select, text
from sqlalchemy.orm import Session

from app.collectors import krei
from app.models.external import ExternalObservation
from app.models.prediction_input import KreiReportValue
from app.services.collection_service import digest


class DateCorrectionError(ValueError):
    pass


def apply_corrections(engine, patches):
    """검증된 계획만 적용. 모든 호를 한 트랜잭션으로 잠그고 실패 시 전체 rollback.

    patches: id, before_payload_sha256, before_published_at, value_count, metadata.
    동일 계획의 재실행은 이미 목표 상태인 행을 확인하고 0건 수정으로 끝낸다.
    """
    if engine.url.get_backend_name() != 'postgresql' or engine.url.host not in ('localhost', '127.0.0.1', '::1'):
        raise DateCorrectionError('local PostgreSQL only')
    if len({p['id'] for p in patches}) != len(patches):
        raise DateCorrectionError('duplicate observation in plan')
    changed_reports = changed_dates = changed_values = 0
    with Session(engine) as db, db.begin():
        db.execute(text("SET LOCAL lock_timeout = '5s'"))
        db.execute(text("SET LOCAL statement_timeout = '30s'"))
        # 신규 수치/버전의 동시 추가도 막아 사전 계산 건수를 고정한다.
        db.execute(text('LOCK TABLE external_observation, krei_report_value IN SHARE ROW EXCLUSIVE MODE'))
        for patch in sorted(patches, key=lambda p: p['id']):
            report = db.get(ExternalObservation, patch['id'], with_for_update=True)
            if report is None or (report.source, report.dataset) != (krei.SOURCE, krei.DATASET):
                raise DateCorrectionError('not a KREI monthly observation')
            if digest(report.payload) != report.payload_sha256:
                raise DateCorrectionError('payload hash mismatch')
            metadata = patch['metadata']
            if metadata['available_from_policy'] != krei.DATE_POLICY:
                raise DateCorrectionError('unexpected date policy')
            printed = date.fromisoformat(metadata['imprint_date']) if metadata['imprint_date'] else None
            canonical = krei.date_metadata(report.payload, printed, metadata['imprint_raw'], metadata['issue_no'])
            if metadata.get('imprint_status') == 'VERIFIED_SAME_SHA_MANIFEST' and printed is not None:
                canonical['imprint_status'] = 'VERIFIED_SAME_SHA_MANIFEST'
            if metadata != canonical:
                raise DateCorrectionError('metadata does not match maximum-date policy')
            candidate = datetime.fromisoformat(metadata['available_from']) if metadata['available_from'] else None
            values = list(db.scalars(select(KreiReportValue).where(
                KreiReportValue.observation_id == report.id).order_by(KreiReportValue.id).with_for_update()))
            if len(values) != patch['value_count'] or any(v.published_at != report.published_at for v in values):
                raise DateCorrectionError('value count/date mismatch')
            if candidate is None and values:
                raise DateCorrectionError('cannot clear date of linked values')
            payload = {**report.payload, **metadata}
            # API 원문 등록값은 metadata가 덮어쓸 수 없다.
            if metadata.keys() - krei.date_metadata(report.payload, None, None, None).keys():
                raise DateCorrectionError('unexpected metadata key')
            if (payload == report.payload and candidate == report.published_at):
                continue
            before = datetime.fromisoformat(patch['before_published_at']) if patch['before_published_at'] else None
            if report.payload_sha256 != patch['before_payload_sha256'] or report.published_at != before:
                raise DateCorrectionError('observation changed since plan')
            if candidate is not None and report.published_at is not None and candidate < report.published_at:
                raise DateCorrectionError('refusing earlier availability')
            if candidate != report.published_at:
                changed_dates += 1
                for value in values:
                    value.published_at = candidate
                    changed_values += 1
            report.published_at = candidate
            report.payload = payload
            report.payload_sha256 = digest(payload)
            # publication_status/issued_at/retrieved_at/API 원문/수치 내용은 보존한다.
            changed_reports += 1
    return {'observations_metadata_updated': changed_reports, 'observations_date_updated': changed_dates,
            'values_date_updated': changed_values, 'inserted': 0, 'deleted': 0}
