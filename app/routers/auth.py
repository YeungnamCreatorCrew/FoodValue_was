from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.db import get_db
from app.schemas.auth import (
    LoginRequest,
    RefreshRequest,
    SignupRequest,
    TokenResponse,
    UserResponse,
)
from app.services import auth_service

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/signup", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def signup(body: SignupRequest, db: Session = Depends(get_db)):
    try:
        return auth_service.signup(db, body.email, body.password, body.nickname)
    except auth_service.DuplicateUserError as e:
        messages = {
            "email": "이미 가입된 이메일입니다",
            "nickname": "이미 사용 중인 닉네임입니다",
        }
        raise HTTPException(
            status.HTTP_409_CONFLICT,
            messages.get(e.field, "이미 사용 중인 이메일 또는 닉네임입니다"),
        ) from None


@router.post("/login", response_model=TokenResponse)
def login(body: LoginRequest, db: Session = Depends(get_db)):
    try:
        access, refresh = auth_service.login(db, body.email, body.password)
    except auth_service.InvalidCredentialsError:
        raise HTTPException(
            status.HTTP_401_UNAUTHORIZED, "이메일 또는 비밀번호가 올바르지 않습니다"
        ) from None
    return TokenResponse(accessToken=access, refreshToken=refresh)


@router.post("/refresh", response_model=TokenResponse)
def refresh(body: RefreshRequest, db: Session = Depends(get_db)):
    try:
        access, new_refresh = auth_service.refresh(db, body.refreshToken)
    except auth_service.InvalidTokenError:
        raise HTTPException(
            status.HTTP_401_UNAUTHORIZED, "유효하지 않은 리프레시 토큰입니다"
        ) from None
    return TokenResponse(accessToken=access, refreshToken=new_refresh)


@router.post("/logout", status_code=status.HTTP_204_NO_CONTENT)
def logout(body: RefreshRequest, db: Session = Depends(get_db)):
    auth_service.logout(db, body.refreshToken)
