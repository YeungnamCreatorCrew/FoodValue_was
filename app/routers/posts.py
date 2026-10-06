from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.orm import Session

from app.core.constants import (
    PAGE_DEFAULT_SIZE,
    PAGE_MAX_SIZE,
    SEARCH_KEYWORD_MAX_LENGTH,
    PostCategory,
)
from app.core.db import get_db
from app.core.deps import get_current_user, get_optional_user
from app.models.user import User
from app.schemas.common import Page
from app.schemas.post import (
    CommentBody,
    CommentResponse,
    PostCreate,
    PostDetail,
    PostSummary,
    PostUpdate,
)
from app.services import post_service
from app.services.post_service import ForbiddenError, NotFoundError

# 조회(GET)는 공개(get_optional_user), 작성·수정·삭제는 JWT 필수(get_current_user)
router = APIRouter(tags=["posts"])


def _http(e: Exception, what: str) -> HTTPException:
    if isinstance(e, NotFoundError):
        return HTTPException(status.HTTP_404_NOT_FOUND, f"{what}을(를) 찾을 수 없습니다")
    return HTTPException(status.HTTP_403_FORBIDDEN, "작성자만 수정·삭제할 수 있습니다")


@router.get("/posts", response_model=Page[PostSummary])
def list_posts(
    category: PostCategory | None = None,
    keyword: str | None = Query(None, max_length=SEARCH_KEYWORD_MAX_LENGTH),
    page: int = Query(1, ge=1),
    size: int = Query(PAGE_DEFAULT_SIZE, ge=1, le=PAGE_MAX_SIZE),
    db: Session = Depends(get_db),
    _: User | None = Depends(get_optional_user),
):
    return post_service.list_posts(db, category, keyword, page, size)


@router.post("/posts", response_model=PostDetail, status_code=status.HTTP_201_CREATED)
def create_post(body: PostCreate, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    return post_service.create_post(db, user, body)


@router.get("/posts/{post_id}", response_model=PostDetail)
def get_post(
    post_id: int, db: Session = Depends(get_db), viewer: User | None = Depends(get_optional_user)
):
    try:
        return post_service.get_post(db, viewer, post_id)
    except NotFoundError as e:
        raise _http(e, "게시글") from None


@router.patch("/posts/{post_id}", response_model=PostDetail)
def update_post(
    post_id: int, body: PostUpdate, db: Session = Depends(get_db), user: User = Depends(get_current_user)
):
    try:
        return post_service.update_post(db, user, post_id, body)
    except (NotFoundError, ForbiddenError) as e:
        raise _http(e, "게시글") from None


@router.delete("/posts/{post_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(post_id: int, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    try:
        post_service.delete_post(db, user, post_id)
    except (NotFoundError, ForbiddenError) as e:
        raise _http(e, "게시글") from None


@router.get("/posts/{post_id}/comments", response_model=list[CommentResponse])
def list_comments(
    post_id: int, db: Session = Depends(get_db), viewer: User | None = Depends(get_optional_user)
):
    try:
        return post_service.list_comments(db, viewer, post_id)
    except NotFoundError as e:
        raise _http(e, "게시글") from None


@router.post(
    "/posts/{post_id}/comments", response_model=CommentResponse, status_code=status.HTTP_201_CREATED
)
def create_comment(
    post_id: int, body: CommentBody, db: Session = Depends(get_db), user: User = Depends(get_current_user)
):
    try:
        return post_service.create_comment(db, user, post_id, body.content)
    except NotFoundError as e:
        raise _http(e, "게시글") from None


@router.patch("/comments/{comment_id}", response_model=CommentResponse)
def update_comment(
    comment_id: int, body: CommentBody, db: Session = Depends(get_db), user: User = Depends(get_current_user)
):
    try:
        return post_service.update_comment(db, user, comment_id, body.content)
    except (NotFoundError, ForbiddenError) as e:
        raise _http(e, "댓글") from None


@router.delete("/comments/{comment_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_comment(comment_id: int, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    try:
        post_service.delete_comment(db, user, comment_id)
    except (NotFoundError, ForbiddenError) as e:
        raise _http(e, "댓글") from None
