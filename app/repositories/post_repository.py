from sqlalchemy import func, select
from sqlalchemy.orm import Session

from app.models.comment import Comment
from app.models.post import Post


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
) -> tuple[list[tuple[Post, int]], int]:
    """최신순 목록. (글, 댓글 수) 목록과 전체 건수를 돌려준다. 댓글 수는 서브쿼리로 한 번에 읽는다."""
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
    rows = db.execute(
        select(Post, comment_count)
        .where(*conditions)
        .order_by(Post.created_at.desc(), Post.id.desc())
        .limit(size)
        .offset((page - 1) * size)
    ).all()
    return [(post, count) for post, count in rows], total
