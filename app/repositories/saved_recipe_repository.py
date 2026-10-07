from sqlalchemy import func, select
from sqlalchemy.orm import Session, defer

from app.models.saved_recipe import SavedRecipe


def add(db: Session, recipe: SavedRecipe) -> SavedRecipe:
    db.add(recipe)
    db.commit()
    db.refresh(recipe)
    return recipe


def get_owned(db: Session, user_id: int, recipe_id: int) -> SavedRecipe | None:
    return db.scalar(select(SavedRecipe).where(SavedRecipe.id == recipe_id, SavedRecipe.user_id == user_id))


def delete(db: Session, recipe: SavedRecipe) -> None:
    db.delete(recipe)
    db.commit()


def list_page(db: Session, user_id: int, page: int, size: int) -> tuple[list[SavedRecipe], int]:
    """최신순 목록과 전체 건수. 목록에는 content가 필요 없어 읽지 않는다."""
    total = db.scalar(select(func.count()).select_from(SavedRecipe).where(SavedRecipe.user_id == user_id)) or 0
    rows = db.scalars(
        select(SavedRecipe)
        .options(defer(SavedRecipe.content))
        .where(SavedRecipe.user_id == user_id)
        .order_by(SavedRecipe.created_at.desc(), SavedRecipe.id.desc())
        .limit(size)
        .offset((page - 1) * size)
    ).all()
    return list(rows), total
