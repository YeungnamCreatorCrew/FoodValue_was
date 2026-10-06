import uuid
from datetime import timedelta

from sqlalchemy import func, select, update
from sqlalchemy.orm import Session

from app.core.constants import REFRESH_TOKEN_EXPIRE_DAYS
from app.models.refresh_token import RefreshToken

# 만료·폐기 시각은 DB 시계(now(), Asia/Seoul)로만 기록·비교해 타임존 어긋남을 피한다.


def add(db: Session, user_id: int, family_id: uuid.UUID, token_hash: str) -> RefreshToken:
    row = RefreshToken(
        user_id=user_id,
        family_id=family_id,
        token_hash=token_hash,
        expires_at=func.now() + timedelta(days=REFRESH_TOKEN_EXPIRE_DAYS),
    )
    db.add(row)
    return row


def get_by_hash_for_update(db: Session, token_hash: str) -> RefreshToken | None:
    """동시에 같은 토큰으로 재발급해도 한 건씩 처리되도록 행을 잠근다."""
    return db.scalar(
        select(RefreshToken).where(RefreshToken.token_hash == token_hash).with_for_update()
    )


def is_expired(db: Session, row: RefreshToken) -> bool:
    return bool(db.scalar(select(row.expires_at <= func.now())))


def revoke(db: Session, row: RefreshToken) -> None:
    row.revoked_at = func.now()


def revoke_family(db: Session, family_id: uuid.UUID) -> None:
    db.execute(
        update(RefreshToken)
        .where(RefreshToken.family_id == family_id, RefreshToken.revoked_at.is_(None))
        .values(revoked_at=func.now())
    )
