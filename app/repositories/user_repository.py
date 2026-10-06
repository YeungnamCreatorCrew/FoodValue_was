from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.user import User


def get_by_id(db: Session, user_id: int) -> User | None:
    return db.get(User, user_id)


def get_by_email(db: Session, email: str) -> User | None:
    return db.scalar(select(User).where(User.email == email))


def exists_email(db: Session, email: str) -> bool:
    return db.scalar(select(User.id).where(User.email == email)) is not None


def exists_nickname(db: Session, nickname: str) -> bool:
    return db.scalar(select(User.id).where(User.nickname == nickname)) is not None


def add(db: Session, user: User) -> User:
    db.add(user)
    db.commit()
    return user
