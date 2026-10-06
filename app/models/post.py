from datetime import datetime

from sqlalchemy import BigInteger, DateTime, ForeignKey, Integer, String, Text, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.db import Base
from app.models.user import User


class Post(Base):
    """V1__init_schema.sql 의 post 테이블"""

    __tablename__ = "post"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    user_id: Mapped[int] = mapped_column(BigInteger, ForeignKey("users.id"))
    category: Mapped[str] = mapped_column(String(20))
    title: Mapped[str] = mapped_column(String(100))
    content: Mapped[str] = mapped_column(Text)
    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())

    # 목록 조회에서 N+1이 나지 않도록 작성자는 JOIN, 이미지는 IN 한 번으로 함께 읽는다
    author: Mapped[User] = relationship(lazy="joined")
    images: Mapped[list["PostImage"]] = relationship(
        order_by="PostImage.sort_order",
        cascade="all, delete-orphan",
        passive_deletes=True,  # 삭제는 DB의 ON DELETE CASCADE에 맡긴다
        lazy="selectin",
    )


class PostImage(Base):
    """post_image 테이블"""

    __tablename__ = "post_image"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    post_id: Mapped[int] = mapped_column(BigInteger, ForeignKey("post.id", ondelete="CASCADE"))
    url: Mapped[str] = mapped_column(String(500))
    sort_order: Mapped[int] = mapped_column(Integer)
    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())
