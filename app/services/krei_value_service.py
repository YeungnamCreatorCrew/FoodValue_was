"""KREI 관측월보 추출 결과(JSON) → krei_report_value.

추출기(Claude 백필·Gemini 운영·정규식)와 관계없이 같은 JSON 형식을 받는다. 형식과 추출 규칙은
data/krei_values/README.md에 있다.

- 원본 호는 (KREI, MONTHLY_REPORT, source_record_key)의 최신 수집 버전을 쓴다. 발표 시점이 없는 호는 거부한다.
- published_at은 JSON이 아니라 원본 호에서 복사한다(추출기가 발표 시점을 바꿀 수 없게).
- 같은 사실(uk_krei_report_value)은 upsert로 갱신한다. 한 파일은 한 트랜잭션이다.
"""
import json
import re
from datetime import date
from decimal import Decimal, InvalidOperation
from pathlib import Path

from sqlalchemy import delete, select
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.orm import Session

from app.collectors import krei
from app.models.external import ExternalObservation
from app.models.prediction_input import KreiReportValue

METRICS = {'PLANTED_AREA', 'SHIPMENT_AREA', 'YIELD', 'PRODUCTION', 'SHIPMENT', 'ARRIVAL', 'STOCK', 'IMPORT',
           'WHOLESALE_PRICE', 'RETAIL_PRICE'}
KINDS = {'OUTLOOK', 'ACTUAL'}
BASES = {'LEVEL', 'PREV_YEAR', 'NORMAL', 'PREV_MONTH'}
DIRECTIONS = {'UP', 'DOWN', 'FLAT'}
RELATIVE_UNITS = {'%', '%p'}
FIELDS = ('item_name', 'crop_type', 'metric', 'kind', 'target_start', 'target_end', 'basis', 'value', 'value_low',
          'value_high', 'unit', 'direction', 'evidence')
DOCUMENT_FIELDS = {'source_record_key', 'pdf_sha256', 'extractor', 'extractor_version', 'values', 'unmapped'}
KEY = ('item_name', 'crop_type', 'metric', 'kind', 'basis', 'target_start', 'target_end')


class ExtractionError(ValueError):
    pass


def _decimal(raw, where):
    if raw is None:
        return None
    try:
        return Decimal(str(raw))
    except InvalidOperation:
        raise ExtractionError(f'{where}: 숫자가 아님 {raw!r}') from None


def _text(raw, where, *, required=False, limit=None):
    value = raw.strip() if isinstance(raw, str) else raw
    if value in (None, ''):
        if required:
            raise ExtractionError(f'{where}: 비어 있음')
        return None
    if not isinstance(value, str):
        raise ExtractionError(f'{where}: 문자열이 아님')
    if limit and len(value) > limit:
        raise ExtractionError(f'{where}: {limit}자 초과')
    return value


def validate_value(raw: dict, index: int) -> dict:
    """JSON 값 1개 → 테이블 행(observation·추출기 제외). DB 제약보다 먼저, 이유를 알 수 있게 거부한다."""
    where = f'values[{index}]'
    unknown = set(raw) - set(FIELDS)
    if unknown:
        raise ExtractionError(f'{where}: 알 수 없는 필드 {sorted(unknown)}')
    row = {'item_name': _text(raw.get('item_name'), where + '.item_name', required=True, limit=30),
           'crop_type': _text(raw.get('crop_type'), where + '.crop_type', limit=30),
           'metric': raw.get('metric'), 'kind': raw.get('kind'), 'basis': raw.get('basis'),
           'unit': _text(raw.get('unit'), where + '.unit', limit=20),
           'direction': raw.get('direction'),
           'evidence': _text(raw.get('evidence'), where + '.evidence', required=True)}
    for name, allowed in (('metric', METRICS), ('kind', KINDS), ('basis', BASES)):
        if row[name] not in allowed:
            raise ExtractionError(f'{where}.{name}: {row[name]!r} 허용값 아님')
    if row['direction'] is not None and row['direction'] not in DIRECTIONS:
        raise ExtractionError(f'{where}.direction: {row["direction"]!r} 허용값 아님')
    try:
        row['target_start'] = date.fromisoformat(raw.get('target_start') or '')
        row['target_end'] = date.fromisoformat(raw.get('target_end') or '')
    except ValueError:
        raise ExtractionError(f'{where}: target_start·target_end는 YYYY-MM-DD') from None
    if row['target_end'] < row['target_start']:
        raise ExtractionError(f'{where}: target_end < target_start')
    for name in ('value', 'value_low', 'value_high'):
        row[name] = _decimal(raw.get(name), f'{where}.{name}')
    if (row['value_low'] is None) != (row['value_high'] is None):
        raise ExtractionError(f'{where}: value_low·value_high는 같이 채움')
    if row['value_low'] is not None:
        if row['value_low'] > row['value_high']:
            raise ExtractionError(f'{where}: value_low > value_high')
        if row['value'] is None:
            row['value'] = (row['value_low'] + row['value_high']) / 2
    if row['value'] is None and row['direction'] is None:
        raise ExtractionError(f'{where}: value와 direction 중 하나는 있어야 함')
    if row['value'] is not None and row['unit'] is None:
        raise ExtractionError(f'{where}: value가 있으면 unit 필요')
    if row['basis'] != 'LEVEL' and row['value'] is not None and row['unit'] not in RELATIVE_UNITS:
        raise ExtractionError(f'{where}: 비교 기준({row["basis"]}) 값의 단위는 % 또는 %p')
    if row['basis'] == 'LEVEL' and row['unit'] in RELATIVE_UNITS:
        raise ExtractionError(f'{where}: LEVEL 값에 % 단위')
    # 비교 기준 값은 방향을 직접 적어야 한다. 부호로 채우면 "평년과 비슷(-0.1%)"이 DOWN이 되는 실수를 못 잡는다.
    if row['direction'] is None and row['basis'] != 'LEVEL':
        raise ExtractionError(f'{where}: 비교 기준({row["basis"]}) 값은 direction을 직접 적어야 함(문장 기준)')
    return row


def parse_document(document: dict):
    """JSON 문서 → (source_record_key, extractor, extractor_version, 행 목록)."""
    if not isinstance(document, dict):
        raise ExtractionError('최상위는 객체여야 함')
    unknown = set(document) - DOCUMENT_FIELDS
    if unknown:
        raise ExtractionError(f'알 수 없는 최상위 필드 {sorted(unknown)}')
    # unmapped: 문서에 있었지만 스키마에 없어 뽑지 않은 데이터 기록. 적재하지 않고 형식만 확인한다.
    unmapped = document.get('unmapped', [])
    if not isinstance(unmapped, list) or not all(
            isinstance(entry, dict) and set(entry) <= {'item_name', 'what', 'evidence'}
            and _text(entry.get('what'), 'unmapped.what', required=True) for entry in unmapped):
        raise ExtractionError('unmapped는 {item_name?, what, evidence?} 목록')
    key = _text(document.get('source_record_key'), 'source_record_key', required=True)
    pdf_sha256 = _text(document.get('pdf_sha256'), 'pdf_sha256', required=True)
    if not re.fullmatch(r'[0-9a-f]{64}', pdf_sha256):
        raise ExtractionError('pdf_sha256: 소문자 16진수 64자')
    extractor = _text(document.get('extractor'), 'extractor', required=True, limit=40)
    version = _text(document.get('extractor_version'), 'extractor_version', required=True, limit=40)
    values = document.get('values')
    if not isinstance(values, list) or not values:
        raise ExtractionError('values는 비어 있지 않은 목록이어야 함')
    rows = [validate_value(raw, index) for index, raw in enumerate(values)]
    seen = set()
    for index, row in enumerate(rows):
        fact = tuple(row[name] for name in KEY)
        if fact in seen:
            raise ExtractionError(f'values[{index}]: 같은 사실이 두 번 있음 {fact}')
        seen.add(fact)
    return key, pdf_sha256, extractor, version, rows


def report_version(db, key, pdf_sha256):
    """추출에 쓴 PDF와 같은 내용의 원본 호 버전(여러 개면 최신 수집본).

    KREI가 PDF를 고쳐 올리면 새 버전이 생기는데, 예전 PDF에서 뽑은 JSON이 새 버전에 붙지 않게 PDF 해시로 고른다.
    """
    return db.scalars(select(ExternalObservation).where(
        ExternalObservation.source == krei.SOURCE, ExternalObservation.dataset == krei.DATASET,
        ExternalObservation.source_record_key == key,
        ExternalObservation.payload['pdf_sha256'].astext == pdf_sha256,
    ).order_by(ExternalObservation.retrieved_at.desc(), ExternalObservation.id.desc()).limit(1)).first()


def load_document(engine, document: dict):
    """한 파일 = 그 호 버전의 전체 사실. 파일에 없는 기존 행은 지운다(규칙이 바뀌어 빠진 값이 남지 않게)."""
    key, pdf_sha256, extractor, version, rows = parse_document(document)
    with Session(engine) as db:
        report = report_version(db, key, pdf_sha256)
        if report is None:
            raise ExtractionError(f'같은 PDF의 원본 호 없음: {key} (먼저 python -m app.krei_monthly로 수집, PDF 해시 확인)')
        if report.published_at is None:
            raise ExtractionError(f'발표 시점을 모르는 호라 적재하지 않음: {key}')
        values = [{**row, 'observation_id': report.id, 'published_at': report.published_at,
                   'extractor': extractor, 'extractor_version': version} for row in rows]
        statement = insert(KreiReportValue).values(values)
        keys = {'observation_id', *KEY}
        update = {column: statement.excluded[column] for column in values[0] if column not in keys}
        db.execute(statement.on_conflict_do_update(constraint='uk_krei_report_value', set_=update))
        incoming = {tuple(row[name] for name in KEY) for row in rows}
        existing = db.execute(select(KreiReportValue.id, *(getattr(KreiReportValue, name) for name in KEY))
                              .where(KreiReportValue.observation_id == report.id)).all()
        stale = [row[0] for row in existing if tuple(row[1:]) not in incoming]
        if stale:
            db.execute(delete(KreiReportValue).where(KreiReportValue.id.in_(stale)))
        summary = {'sourceRecordKey': key, 'observationId': report.id,
                   'publishedAt': report.published_at.isoformat(), 'extractor': extractor, 'values': len(values),
                   'removed': len(stale)}
        db.commit()
    return summary


def load_file(engine, path: Path):
    return load_document(engine, json.loads(Path(path).read_text(encoding='utf-8')))
