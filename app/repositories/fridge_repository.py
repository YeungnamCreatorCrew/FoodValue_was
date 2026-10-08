from sqlalchemy import exists, func, select
from sqlalchemy.orm import Session

from app.models.fridge import FridgeIngredient, Item, ItemAlias
from app.schemas.fridge import FoodType, Sort, Storage


def owned(db: Session, user_id: int, ingredient_id: int, *, lock: bool = False):
    query = select(FridgeIngredient).where(
        FridgeIngredient.id == ingredient_id,
        FridgeIngredient.user_id == user_id,
        FridgeIngredient.deleted_at.is_(None),
    )
    return db.scalar(query.with_for_update() if lock else query)


def escape_like(value: str):
    return value.replace('\\', '\\\\').replace('%', '\\%').replace('_', '\\_')


def items(db: Session, keyword: str | None, page: int, size: int):
    conditions = []
    if keyword and keyword.strip():
        pattern = '%' + escape_like(keyword.strip()) + '%'
        conditions.append(Item.name.ilike(pattern, escape='\\') | exists().where(
            ItemAlias.item_id == Item.id, ItemAlias.alias.ilike(pattern, escape='\\')))
    total = db.scalar(select(func.count()).select_from(Item).where(*conditions)) or 0
    rows = db.scalars(select(Item).where(*conditions).order_by(Item.name, Item.id)
                      .offset((page - 1) * size).limit(size)).all()
    return rows, total


def ingredients(db: Session, user_id: int, storage: Storage | None, food_type: FoodType | None,
                keyword: str | None, sort: Sort, include_empty: bool, page: int, size: int):
    conditions = [FridgeIngredient.user_id == user_id, FridgeIngredient.deleted_at.is_(None)]
    if not include_empty:
        conditions.append(FridgeIngredient.quantity > 0)
    if storage:
        conditions.append(FridgeIngredient.storage == storage)
    if food_type:
        conditions.append(FridgeIngredient.food_type == food_type)
    if keyword and keyword.strip():
        conditions.append(FridgeIngredient.display_name.ilike(
            '%' + escape_like(keyword.strip()) + '%', escape='\\'))
    query = select(FridgeIngredient, Item).outerjoin(Item, Item.id == FridgeIngredient.item_id).where(*conditions)
    total = db.scalar(select(func.count()).select_from(query.subquery())) or 0
    order = {
        Sort.PURCHASED: FridgeIngredient.purchased_at.asc(),
        Sort.NAME: FridgeIngredient.display_name.asc(),
        Sort.NEWEST: FridgeIngredient.created_at.desc(),
    }[sort]
    rows = db.execute(query.order_by(order, FridgeIngredient.id).offset((page - 1) * size).limit(size)).all()
    return rows, total


def usable_names(db: Session, user_id: int, ingredient_ids: list[int]) -> dict[int, str]:
    """내 것이고 삭제되지 않았으며 잔량이 남은 재료의 {id: 이름}. 조건에 안 맞는 id는 빠진다."""
    rows = db.execute(select(FridgeIngredient.id, FridgeIngredient.display_name).where(
        FridgeIngredient.id.in_(ingredient_ids),
        FridgeIngredient.user_id == user_id,
        FridgeIngredient.deleted_at.is_(None),
        FridgeIngredient.quantity > 0,
    )).all()
    return dict(rows)
