from sqlalchemy import func
from sqlalchemy.orm import Session

from app.core.constants import PostCategory
from app.models.comment import Comment
from app.models.post import Post, PostImage
from app.models.user import User
from app.repositories import comment_repository, post_repository
from app.schemas.common import Page
from app.schemas.post import (
    Author,
    CommentResponse,
    PostCreate,
    PostDetail,
    PostSummary,
    PostUpdate,
)


class NotFoundError(Exception):
    pass


class ForbiddenError(Exception):
    pass


def _images(urls: list[str]) -> list[PostImage]:
    return [PostImage(url=url, sort_order=i) for i, url in enumerate(urls)]


def _author(user: User) -> Author:
    return Author(id=user.id, nickname=user.nickname)


def _is_mine(owner_id: int, viewer: User | None) -> bool:
    return viewer is not None and owner_id == viewer.id


def _detail(post: Post, viewer: User | None) -> PostDetail:
    return PostDetail(
        id=post.id,
        category=post.category,
        title=post.title,
        content=post.content,
        image_urls=[img.url for img in post.images],
        author=_author(post.author),
        is_mine=_is_mine(post.user_id, viewer),
        created_at=post.created_at,
        updated_at=post.updated_at,
    )


def _comment(comment: Comment, viewer: User | None) -> CommentResponse:
    return CommentResponse(
        id=comment.id,
        post_id=comment.post_id,
        content=comment.content,
        author=_author(comment.author),
        is_mine=_is_mine(comment.user_id, viewer),
        created_at=comment.created_at,
        updated_at=comment.updated_at,
    )


def _get_post(db: Session, post_id: int) -> Post:
    post = post_repository.get(db, post_id)
    if post is None:
        raise NotFoundError
    return post


def _get_own_post(db: Session, post_id: int, user: User) -> Post:
    post = _get_post(db, post_id)
    if post.user_id != user.id:  # 작성자는 요청 본문이 아니라 인증 정보로만 판단한다
        raise ForbiddenError
    return post


# ---------- 게시글 ----------
def list_posts(
    db: Session, category: PostCategory | None, keyword: str | None, page: int, size: int
) -> Page[PostSummary]:
    keyword = keyword.strip() if keyword else None
    rows, total = post_repository.list_page(db, category, keyword or None, page, size)
    items = [
        PostSummary(
            id=post.id,
            category=post.category,
            title=post.title,
            author=_author(post.author),
            comment_count=count,
            has_image=has_image,
            created_at=post.created_at,
        )
        for post, count, has_image in rows
    ]
    return Page(items=items, page=page, size=size, total=total)


def create_post(db: Session, user: User, body: PostCreate) -> PostDetail:
    post = Post(
        user_id=user.id,
        category=body.category,
        title=body.title.strip(),
        content=body.content,
        images=_images(body.image_urls),
    )
    return _detail(post_repository.add(db, post), user)


def get_post(db: Session, viewer: User | None, post_id: int) -> PostDetail:
    return _detail(_get_post(db, post_id), viewer)


def update_post(db: Session, user: User, post_id: int, body: PostUpdate) -> PostDetail:
    post = _get_own_post(db, post_id, user)
    sent = body.model_fields_set
    if "category" in sent:
        post.category = body.category
    if "title" in sent:
        post.title = body.title.strip()
    if "content" in sent:
        post.content = body.content
    if "image_urls" in sent:
        post.images = _images(body.image_urls)
    post.updated_at = func.now()
    db.commit()
    db.refresh(post)
    return _detail(post, user)


def delete_post(db: Session, user: User, post_id: int) -> None:
    post_repository.delete(db, _get_own_post(db, post_id, user))


# ---------- 댓글 ----------
def list_comments(db: Session, viewer: User | None, post_id: int) -> list[CommentResponse]:
    _get_post(db, post_id)
    return [_comment(c, viewer) for c in comment_repository.list_by_post(db, post_id)]


def create_comment(db: Session, user: User, post_id: int, content: str) -> CommentResponse:
    _get_post(db, post_id)
    comment = Comment(post_id=post_id, user_id=user.id, content=content)
    return _comment(comment_repository.add(db, comment), user)


def _get_own_comment(db: Session, comment_id: int, user: User) -> Comment:
    comment = comment_repository.get(db, comment_id)
    if comment is None:
        raise NotFoundError
    if comment.user_id != user.id:
        raise ForbiddenError
    return comment


def update_comment(db: Session, user: User, comment_id: int, content: str) -> CommentResponse:
    comment = _get_own_comment(db, comment_id, user)
    comment.content = content
    comment.updated_at = func.now()
    db.commit()
    db.refresh(comment)
    return _comment(comment, user)


def delete_comment(db: Session, user: User, comment_id: int) -> None:
    comment_repository.delete(db, _get_own_comment(db, comment_id, user))
