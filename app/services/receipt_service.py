"""CLOVA 영수증 OCR. 원본 이미지·카드 정보는 DB나 공개 이미지 저장소에 보관하지 않는다."""
import base64
import json
import os
import time
import uuid
from datetime import date, datetime
from decimal import Decimal, InvalidOperation
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

from sqlalchemy import select

from app.core.constants import IMAGE_MAX_BYTES
from app.models.fridge import FridgeReceipt, Item, ItemAlias
from app.services import fridge_service as fridge
from app.services.image_service import _detect


class OcrError(Exception):
    def __init__(self, message, status=502):
        self.status = status
        super().__init__(message)


def recognize(data: bytes):
    endpoint = os.getenv('CLOVA_OCR_RECEIPT_URL')
    secret = os.getenv('CLOVA_OCR_SECRET')
    if not endpoint or not secret:
        raise OcrError('영수증 OCR 설정이 필요합니다', 503)
    if not endpoint.startswith('https://'):
        raise OcrError('OCR URL은 HTTPS여야 합니다', 503)
    kind = _detect(data)
    if len(data) > IMAGE_MAX_BYTES:
        raise OcrError('영수증 이미지는 5MB 이하만 가능합니다', 413)
    if kind is None or kind[1] not in ('png', 'jpg'):
        raise OcrError('영수증은 PNG 또는 JPEG로 올려 주세요', 400)
    body = {'version': 'V2', 'requestId': str(uuid.uuid4()), 'timestamp': int(time.time() * 1000),
            'images': [{'format': kind[1], 'name': 'receipt', 'data': base64.b64encode(data).decode()}]}
    request = Request(endpoint, data=json.dumps(body).encode(),
                      headers={'Content-Type': 'application/json', 'X-OCR-SECRET': secret}, method='POST')
    try:
        with urlopen(request, timeout=30) as res:
            raw = res.read(2 * 1024 * 1024 + 1)
            if len(raw) > 2 * 1024 * 1024:
                raise OcrError('OCR 응답이 너무 큽니다')
            return json.loads(raw)
    except (HTTPError, URLError, TimeoutError, ValueError):
        raise OcrError('영수증 인식 서비스 호출에 실패했습니다') from None


def value(obj):
    if not isinstance(obj, dict):
        return None
    return (obj.get('formatted') or {}).get('value') or obj.get('text')


def number(obj):
    try:
        result = Decimal(str(value(obj)).replace(',', ''))
        return result if result.is_finite() and result >= 0 else None
    except (InvalidOperation, ValueError):
        return None


def parse(payload):
    try:
        image = payload['images'][0]
        if image.get('inferResult') != 'SUCCESS':
            raise OcrError('영수증을 인식하지 못했습니다')
        result = image['receipt']['result']
        candidates = []
        for group in result.get('subResults', []):
            for row in group.get('items', []):
                name = value(row.get('name'))
                if not name:
                    continue
                count = number(row.get('count'))
                price = number((row.get('price') or {}).get('price'))
                candidates.append({'displayName': str(name)[:50],
                                   'quantity': str(count) if count is not None and count > 0 else None,
                                   'purchasePrice': int(price) if price is not None and price <= 2**31 - 1 else None,
                                   'confidence': (row.get('name') or {}).get('confidenceScore'),
                                   'needsReview': True})
                if len(candidates) > 100:
                    raise OcrError('영수증 항목은 100개까지 지원합니다', 400)
        day = None
        date_obj = (result.get('paymentInfo') or {}).get('date') or {}
        formatted = date_obj.get('formatted') or {}
        if all(formatted.get(key) for key in ('year', 'month', 'day')):
            try:
                day = date(int(formatted['year']), int(formatted['month']), int(formatted['day']))
            except (ValueError, TypeError):
                pass
        raw_day = value(date_obj)
        if day is None and raw_day:
            for fmt in ('%Y-%m-%d', '%Y/%m/%d', '%Y.%m.%d', '%Y%m%d'):
                try:
                    day = datetime.strptime(str(raw_day), fmt).date()
                    break
                except ValueError:
                    pass
        if not candidates:
            raise OcrError('인식된 품목이 없습니다. 직접 등록하거나 다른 사진을 사용해 주세요', 400)
        return candidates, day
    except (KeyError, IndexError, TypeError, AttributeError):
        raise OcrError('OCR 응답 형식이 올바르지 않습니다') from None


def upload(db, user, data, purchased_at):
    if purchased_at is not None:
        fridge.validate_date(purchased_at)
    candidates, recognized_day = parse(recognize(data))
    day = purchased_at or recognized_day or fridge.today()
    if day > fridge.today():
        day = fridge.today()
    # 완전 일치만 자동 매칭한다. OCR 수량은 판매 단위 수로, 무게로 추정하지 않는다.
    names = [x['displayName'] for x in candidates]
    master = {x.name: x for x in db.scalars(select(Item).where(Item.name.in_(names))).all()}
    aliases = db.execute(select(ItemAlias.alias, Item).join(Item, Item.id == ItemAlias.item_id)
                         .where(ItemAlias.alias.in_(names))).all()
    master.update(dict(aliases))
    for candidate in candidates:
        item = master.get(candidate['displayName'])
        candidate.update({'itemId': item.id if item else None,
                          'suggestedUnit': item.default_unit if item else None,
                          'suggestedStorage': item.default_storage if item else None})
    row = FridgeReceipt(user_id=user.id, purchased_at=day, candidates=candidates)
    db.add(row)
    db.commit()
    db.refresh(row)
    return receipt_response(row)


def receipt_response(row):
    return {'id': row.id, 'purchasedAt': row.purchased_at,
            'candidates': row.candidates, 'confirmedAt': row.confirmed_at}


def owned(db, user, receipt_id, lock=False):
    query = select(FridgeReceipt).where(FridgeReceipt.id == receipt_id, FridgeReceipt.user_id == user.id)
    row = db.scalar(query.with_for_update() if lock else query)
    if row is None:
        raise fridge.NotFoundError('영수증을 찾을 수 없습니다')
    return row


def confirm(db, user, receipt_id, body):
    receipt = owned(db, user, receipt_id, lock=True)
    if receipt.confirmed_at:
        raise OcrError('이미 등록된 영수증입니다', 409)
    rows = [fridge.build(db, user, item) for item in body.items]
    db.add_all(rows)
    receipt.confirmed_at = datetime.now().replace(microsecond=0)
    db.commit()
    return [fridge.response(row, db.get(Item, row.item_id) if row.item_id else None) for row in rows]
