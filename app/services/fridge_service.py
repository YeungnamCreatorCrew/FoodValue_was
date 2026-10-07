from datetime import date, datetime
from decimal import Decimal
from zoneinfo import ZoneInfo

from sqlalchemy import func, select
from sqlalchemy.orm import Session

from app.models.fridge import FridgeIngredient, IngredientUsage, Item, ItemNutrition
from app.repositories import fridge_repository as repo
from app.schemas.common import Page
from app.schemas.fridge import IngredientCreate, IngredientResponse, IngredientUpdate, ItemResponse, Reason, UsageResponse


class NotFoundError(Exception):
    pass


class InvalidOperationError(Exception):
    pass


def today():
    return datetime.now(ZoneInfo('Asia/Seoul')).date()


def validate_date(value: date):
    if value > today():
        raise InvalidOperationError('구입일·사용일은 미래 날짜일 수 없습니다')


def get_owned(db, user, ingredient_id, *, lock=False):
    row = repo.owned(db, user.id, ingredient_id, lock=lock)
    if row is None:
        raise NotFoundError('재료를 찾을 수 없습니다')
    return row


def response(row, item=None):
    result = IngredientResponse.model_validate(row)
    result.price_available = item is not None and item.price_source is not None
    return result


def list_items(db, keyword, page, size):
    rows, total = repo.items(db, keyword, page, size)
    return Page(items=[ItemResponse.model_validate(x) for x in rows], page=page, size=size, total=total)


def list_ingredients(db, user, **kwargs):
    rows, total = repo.ingredients(db, user.id, **kwargs)
    return Page(items=[response(row, item) for row, item in rows],
                page=kwargs['page'], size=kwargs['size'], total=total)


def conversion(unit, override, item):
    if unit in ('g', 'kg'):
        fixed = Decimal(1) if unit == 'g' else Decimal(1000)
        if override is not None and override != fixed:
            raise InvalidOperationError('g/kg 단위의 환산 무게는 변경할 수 없습니다')
        return fixed
    if override is not None:
        return override
    if item is None:
        return None
    if unit in ('ml', 'L') and item.density_g_per_ml is not None:
        value = item.density_g_per_ml * (1000 if unit == 'L' else 1)
        if value >= Decimal('1000000000'):
            raise InvalidOperationError('환산 무게가 저장 범위를 초과합니다')
        return value
    if unit == item.default_unit:
        return item.grams_per_unit
    return None


def build(db: Session, user, body: IngredientCreate):
    validate_date(body.purchased_at)
    item = db.get(Item, body.item_id) if body.item_id else None
    if body.item_id and item is None:
        raise InvalidOperationError('품목이 존재하지 않습니다')
    values = body.model_dump()
    values['food_type'] = body.food_type or (item.food_type if item else 'RAW')
    values['grams_per_unit'] = conversion(body.unit, body.grams_per_unit, item)
    return FridgeIngredient(user_id=user.id, initial_quantity=body.quantity, **values)


def create(db, user, body):
    row = build(db, user, body)
    db.add(row)
    db.commit()
    db.refresh(row)
    return response(row, db.get(Item, row.item_id) if row.item_id else None)


def detail(db, user, ingredient_id):
    row = get_owned(db, user, ingredient_id)
    return response(row, db.get(Item, row.item_id) if row.item_id else None)


def update(db, user, ingredient_id, body: IngredientUpdate):
    row = get_owned(db, user, ingredient_id, lock=True)
    values = body.model_dump(exclude_unset=True)
    if 'purchased_at' in values:
        validate_date(values['purchased_at'])
        latest = db.scalar(select(func.min(IngredientUsage.used_at)).where(
            IngredientUsage.fridge_ingredient_id == row.id))
        if latest and values['purchased_at'] > latest:
            raise InvalidOperationError('구입일은 이미 기록된 사용일보다 늦을 수 없습니다')
    if 'grams_per_unit' in values:
        # 명시적 null은 환산 정보 제거. 고정 g/kg는 유지한다.
        values['grams_per_unit'] = conversion(row.unit, values['grams_per_unit'], None)
    for key, value in values.items():
        setattr(row, key, value)
    row.updated_at = func.now()
    db.commit()
    return detail(db, user, ingredient_id)


def delete(db, user, ingredient_id):
    row = get_owned(db, user, ingredient_id, lock=True)
    row.deleted_at = row.updated_at = func.now()
    db.commit()


def consume(db, user, ingredient_id, body):
    row = get_owned(db, user, ingredient_id, lock=True)
    validate_date(body.used_at)
    if body.used_at < row.purchased_at:
        raise InvalidOperationError('사용일은 구입일보다 빠를 수 없습니다')
    amount = body.amount if body.amount is not None else row.quantity
    if amount <= 0 or amount > row.quantity:
        raise InvalidOperationError('사용량은 0보다 크고 잔량 이하여야 합니다')
    grams = amount * row.grams_per_unit if row.grams_per_unit else None
    if grams is not None and grams >= Decimal('1000000000000000'):
        raise InvalidOperationError('사용 무게가 저장 범위를 초과합니다')
    db.add(IngredientUsage(fridge_ingredient_id=row.id, used_amount=amount,
                           grams_used=grams, reason=body.reason, memo=body.memo, used_at=body.used_at))
    row.quantity -= amount
    row.updated_at = func.now()
    db.commit()
    return detail(db, user, ingredient_id)


def usages(db, user, ingredient_id, page, size):
    get_owned(db, user, ingredient_id)
    condition = IngredientUsage.fridge_ingredient_id == ingredient_id
    total = db.scalar(select(func.count()).select_from(IngredientUsage).where(condition)) or 0
    rows = db.scalars(select(IngredientUsage).where(condition)
                      .order_by(IngredientUsage.used_at.desc(), IngredientUsage.id.desc())
                      .offset((page - 1) * size).limit(size)).all()
    return Page(items=[UsageResponse.model_validate(x) for x in rows], page=page, size=size, total=total)


def summary(db, user):
    rows = db.execute(select(FridgeIngredient.storage, func.count(), func.min(FridgeIngredient.purchased_at))
                      .where(FridgeIngredient.user_id == user.id, FridgeIngredient.deleted_at.is_(None),
                             FridgeIngredient.quantity > 0).group_by(FridgeIngredient.storage)).all()
    counts = {key: 0 for key in ('FRIDGE', 'FREEZER', 'ROOM')}
    for storage, count, _ in rows:
        counts[storage] = count
    return {'total': sum(counts.values()), 'byStorage': counts,
            'oldestPurchasedAt': min((day for _, _, day in rows), default=None)}


# 성인 1명 일일 영양성분 기준치. 부족 판정 대상은 탄수화물·단백질·지방.
# 나트륨·당류·콜레스테롤은 상한 성격으로 부족 판정하지 않는다.
NUTRIENTS = {
    'carbohydrate_g': ('carbohydrate', 324, 'g', 'MINIMUM'),
    'protein_g': ('protein', 55, 'g', 'MINIMUM'),
    'fat_g': ('fat', 54, 'g', 'MINIMUM'),
    'sodium_mg': ('sodium', 2000, 'mg', 'LIMIT'),
    'sugars_g': ('sugars', 100, 'g', 'LIMIT'),
    'cholesterol_mg': ('cholesterol', 300, 'mg', 'LIMIT'),
}


def nutrition(db, user):
    rows = db.execute(select(FridgeIngredient, ItemNutrition).outerjoin(
        ItemNutrition, ItemNutrition.item_id == FridgeIngredient.item_id).where(
        FridgeIngredient.user_id == user.id, FridgeIngredient.deleted_at.is_(None),
        FridgeIngredient.quantity > 0)).all()
    totals = {key: Decimal(0) for key in NUTRIENTS}
    missing = {key: [] for key in NUTRIENTS}
    excluded = []
    for row, data in rows:
        factor = None
        cause = None
        if data is None:
            cause = 'NUTRITION_UNKNOWN'
        elif data.basis == '100ML':
            if row.unit in ('ml', 'L'):
                factor = row.quantity * (1000 if row.unit == 'L' else 1) / 100
            else:
                cause = 'VOLUME_UNKNOWN'
        elif row.grams_per_unit is None:
            cause = 'WEIGHT_UNKNOWN'
        elif data.edible_ratio is None:
            cause = 'EDIBLE_RATIO_UNKNOWN'
        else:
            factor = row.quantity * row.grams_per_unit * data.edible_ratio / 100 / 100
        if cause:
            excluded.append({'id': row.id, 'displayName': row.display_name, 'reason': cause})
        for key in NUTRIENTS:
            value = getattr(data, key, None) if data else None
            if cause or value is None:
                missing[key].append(row.id)
            else:
                totals[key] += factor * value
    result = []
    for key, (name, reference, unit, direction) in NUTRIENTS.items():
        amount = totals[key]
        complete = not missing[key]
        status = ('EXCESS' if amount > reference else 'WITHIN_LIMIT') if direction == 'LIMIT' else ('SUFFICIENT' if amount >= reference else 'LOW')
        if missing[key] and amount < reference:
            status = 'INCOMPLETE'
        result.append({'name': name, 'unit': unit, 'amount': amount.quantize(Decimal('.01')),
                       'dailyReference': reference, 'percent': (amount / reference * 100).quantize(Decimal('.01')),
                       'direction': direction, 'status': status, 'complete': complete,
                       'missingIngredientIds': missing[key],
                       'shortfall': max(Decimal(0), reference - amount).quantize(Decimal('.01')) if direction == 'MINIMUM' and complete else None})
    return {'basis': 'CURRENT_INVENTORY', 'adultCount': 1, 'days': 1,
            'ingredientCount': len(rows), 'complete': all(not x for x in missing.values()),
            'nutrients': result, 'excludedIngredients': excluded}
