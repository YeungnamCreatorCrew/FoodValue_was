from datetime import datetime

from sqlalchemy import BigInteger, DateTime, ForeignKey, Text, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.db import Base
from app.models.user import User


class Comment(Base):
    """V1__init_schema.sql 의 comment 테이블"""

    __tablename__ = "comment"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    post_id: Mapped[int] = mapped_column(BigInteger, ForeignKey("post.id", ondelete="CASCADE"))
    user_id: Mapped[int] = mapped_column(BigInteger, ForeignKey("users.id"))
    content: Mapped[str] = mapped_column(Text)
    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())

    author: Mapped[User] = relationship(lazy="joined")
