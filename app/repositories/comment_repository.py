from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.comment import Comment


def add(db: Session, comment: Comment) -> Comment:
    db.add(comment)
    db.commit()
    db.refresh(comment)
    return comment


def get(db: Session, comment_id: int) -> Comment | None:
    return db.get(Comment, comment_id)


def list_by_post(db: Session, post_id: int) -> list[Comment]:
    return list(
        db.scalars(
            select(Comment).where(Comment.post_id == post_id).order_by(Comment.created_at, Comment.id)
        )
    )


def delete(db: Session, comment: Comment) -> None:
    db.delete(comment)
    db.commit()
