from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from sqlalchemy.orm import Session

from app.core.db import get_db
from app.models.user import User
from app.services import auth_service

_bearer = HTTPBearer(auto_error=False)


def get_current_user(
    credentials: HTTPAuthorizationCredentials | None = Depends(_bearer),
    db: Session = Depends(get_db),
) -> User:
    """JWT Bearer 인증. 보호할 라우터는 이 의존성을 쓴다."""
    unauthorized = HTTPException(
        status.HTTP_401_UNAUTHORIZED,
        "인증이 필요합니다",
        headers={"WWW-Authenticate": "Bearer"},
    )
    if credentials is None:
        raise unauthorized
    try:
        return auth_service.authenticate(db, credentials.credentials)
    except auth_service.InvalidTokenError:
        raise unauthorized from None


def get_optional_user(
    credentials: HTTPAuthorizationCredentials | None = Depends(_bearer),
    db: Session = Depends(get_db),
) -> User | None:
    """공개 조회용. 토큰이 없으면 None(비로그인), 있는데 잘못됐으면 401."""
    if credentials is None:
        return None
    return get_current_user(credentials, db)
