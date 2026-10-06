from sqlalchemy import exists, func, select
from sqlalchemy.orm import Session, raiseload

from app.models.comment import Comment
from app.models.post import Post, PostImage


def add(db: Session, post: Post) -> Post:
    db.add(post)
    db.commit()
    db.refresh(post)
    return post


def get(db: Session, post_id: int) -> Post | None:
    return db.get(Post, post_id)


def delete(db: Session, post: Post) -> None:
    db.delete(post)
    db.commit()


def _escape_like(keyword: str) -> str:
    return keyword.replace("\\", "\\\\").replace("%", "\\%").replace("_", "\\_")


def list_page(
    db: Session, category: str | None, keyword: str | None, page: int, size: int
) -> tuple[list[tuple[Post, int, bool]], int]:
    """최신순 목록. (글, 댓글 수, 이미지 유무) 목록과 전체 건수를 돌려준다.

    댓글 수와 이미지 유무는 서브쿼리로 한 번에 읽고, 목록에는 이미지 자체가 필요 없어 로드하지 않는다.
    """
    conditions = []
    if category:
        conditions.append(Post.category == category)
    if keyword:
        like = f"%{_escape_like(keyword)}%"
        conditions.append(Post.title.ilike(like, escape="\\") | Post.content.ilike(like, escape="\\"))

    total = db.scalar(select(func.count()).select_from(Post).where(*conditions)) or 0
    comment_count = (
        select(func.count(Comment.id)).where(Comment.post_id == Post.id).correlate(Post).scalar_subquery()
    )
    has_image = exists().where(PostImage.post_id == Post.id).correlate(Post)
    rows = db.execute(
        select(Post, comment_count, has_image)
        .options(raiseload(Post.images))
        .where(*conditions)
        .order_by(Post.created_at.desc(), Post.id.desc())
        .limit(size)
        .offset((page - 1) * size)
    ).all()
    return [(post, count, bool(img)) for post, count, img in rows], total
