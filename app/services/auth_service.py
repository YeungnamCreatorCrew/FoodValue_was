import uuid

import jwt
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.core.security import (
    create_access_token,
    decode_access_token,
    generate_refresh_token,
    hash_password,
    hash_refresh_token,
    verify_password,
)
from app.models.user import User
from app.repositories import refresh_token_repository, user_repository


class DuplicateUserError(Exception):
    def __init__(self, field: str) -> None:
        self.field = field


class InvalidCredentialsError(Exception):
    pass


class InvalidTokenError(Exception):
    pass


def signup(db: Session, email: str, password: str, nickname: str) -> User:
    if user_repository.exists_email(db, email):
        raise DuplicateUserError("email")
    if user_repository.exists_nickname(db, nickname):
        raise DuplicateUserError("nickname")
    user = User(email=email, password_hash=hash_password(password), nickname=nickname)
    try:
        return user_repository.add(db, user)
    except IntegrityError:  # 동시 가입 경쟁 상태: DB 유니크 제약이 최종 방어선
        db.rollback()
        raise DuplicateUserError("email or nickname") from None


def _issue_tokens(db: Session, user_id: int, family_id: uuid.UUID) -> tuple[str, str]:
    refresh_token = generate_refresh_token()
    refresh_token_repository.add(db, user_id, family_id, hash_refresh_token(refresh_token))
    return create_access_token(user_id), refresh_token


def login(db: Session, email: str, password: str) -> tuple[str, str]:
    """(accessToken, refreshToken). 로그인마다 새 토큰 계열(family)을 시작한다."""
    user = user_repository.get_by_email(db, email)
    if not verify_password(password, user.password_hash if user else None):
        raise InvalidCredentialsError
    tokens = _issue_tokens(db, user.id, uuid.uuid4())
    db.commit()
    return tokens


def refresh(db: Session, token: str) -> tuple[str, str]:
    """리프레시 토큰을 회전한다. 이미 폐기된 토큰이 다시 오면 탈취로 보고 계열 전체를 폐기한다."""
    row = refresh_token_repository.get_by_hash_for_update(db, hash_refresh_token(token))
    if row is None:
        raise InvalidTokenError
    if row.revoked_at is not None:
        refresh_token_repository.revoke_family(db, row.family_id)
        db.commit()
        raise InvalidTokenError
    if refresh_token_repository.is_expired(db, row):
        db.rollback()
        raise InvalidTokenError
    refresh_token_repository.revoke(db, row)
    tokens = _issue_tokens(db, row.user_id, row.family_id)
    db.commit()
    return tokens


def logout(db: Session, token: str) -> None:
    """해당 로그인 계열의 리프레시 토큰을 모두 폐기한다. 모르는 토큰이어도 조용히 성공(멱등)."""
    row = refresh_token_repository.get_by_hash_for_update(db, hash_refresh_token(token))
    if row is not None:
        refresh_token_repository.revoke_family(db, row.family_id)
    db.commit()


def authenticate(db: Session, token: str) -> User:
    try:
        user_id = decode_access_token(token)
    except jwt.PyJWTError:
        raise InvalidTokenError from None
    user = user_repository.get_by_id(db, user_id)
    if user is None:
        raise InvalidTokenError
    return user
