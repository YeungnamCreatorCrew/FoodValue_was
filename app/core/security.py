import hashlib
import secrets
import uuid
from datetime import datetime, timedelta, timezone

import jwt
from argon2 import PasswordHasher
from argon2.exceptions import InvalidHashError, VerificationError

from app.core.config import get_settings
from app.core.constants import (
    ACCESS_TOKEN_EXPIRE_MINUTES,
    JWT_ALGORITHM,
    JWT_AUDIENCE,
    JWT_ISSUER,
)

_hasher = PasswordHasher()  # argon2id
# 없는 이메일로 로그인해도 해시 비교 시간을 맞추기 위한 더미 해시
_DUMMY_HASH = _hasher.hash("dummy-password-for-timing")


def hash_password(password: str) -> str:
    return _hasher.hash(password)


def verify_password(password: str, password_hash: str | None) -> bool:
    """password_hash가 None(사용자 없음)이어도 더미 해시와 비교해 응답 시간을 맞춘다."""
    try:
        _hasher.verify(password_hash or _DUMMY_HASH, password)
    except (VerificationError, InvalidHashError):
        return False
    return password_hash is not None


def create_access_token(user_id: int, now: datetime | None = None) -> str:
    now = now or datetime.now(timezone.utc)
    payload = {
        "sub": str(user_id),
        "iss": JWT_ISSUER,
        "aud": JWT_AUDIENCE,
        "iat": now,
        "exp": now + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES),
        "jti": uuid.uuid4().hex,
    }
    return jwt.encode(payload, get_settings().jwt_secret_key, algorithm=JWT_ALGORITHM)


def decode_access_token(token: str) -> int:
    """검증에 실패하면 jwt.PyJWTError. 성공하면 user_id."""
    payload = jwt.decode(
        token,
        get_settings().jwt_secret_key,
        algorithms=[JWT_ALGORITHM],
        audience=JWT_AUDIENCE,
        issuer=JWT_ISSUER,
        options={"require": ["sub", "exp", "iat", "iss", "aud"]},
    )
    try:
        return int(payload["sub"])
    except ValueError as e:
        raise jwt.InvalidTokenError("invalid sub") from e


def generate_refresh_token() -> str:
    return secrets.token_urlsafe(48)


def hash_refresh_token(token: str) -> str:
    """DB에는 원문 대신 이 SHA-256 hex만 저장한다."""
    return hashlib.sha256(token.encode()).hexdigest()
