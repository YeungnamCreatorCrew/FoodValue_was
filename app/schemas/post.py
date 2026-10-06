from datetime import datetime
from typing import Annotated

from pydantic import AfterValidator, AnyHttpUrl, Field, TypeAdapter, model_validator

from app.core.constants import (
    COMMENT_MAX_LENGTH,
    POST_CONTENT_MAX_LENGTH,
    POST_IMAGE_MAX_COUNT,
    POST_IMAGE_URL_MAX_LENGTH,
    POST_TITLE_MAX_LENGTH,
    PostCategory,
)
from app.schemas.common import CamelModel

_http_url = TypeAdapter(AnyHttpUrl)


def _check_url(v: str) -> str:
    _http_url.validate_python(v)  # javascript: 같은 스킴 차단 (XSS)
    return v


ImageUrl = Annotated[str, Field(max_length=POST_IMAGE_URL_MAX_LENGTH), AfterValidator(_check_url)]
Title = Annotated[str, Field(min_length=1, max_length=POST_TITLE_MAX_LENGTH)]
Content = Annotated[str, Field(min_length=1, max_length=POST_CONTENT_MAX_LENGTH)]
CommentContent = Annotated[str, Field(min_length=1, max_length=COMMENT_MAX_LENGTH)]


def _reject_blank(*values: str | None) -> None:
    if any(v is not None and not v.strip() for v in values):
        raise ValueError("공백만 입력할 수 없습니다")


class PostCreate(CamelModel):
    category: PostCategory
    title: Title
    content: Content
    image_urls: list[ImageUrl] = Field(default_factory=list, max_length=POST_IMAGE_MAX_COUNT)

    @model_validator(mode="after")
    def _not_blank(self):
        _reject_blank(self.title, self.content)
        return self


class PostUpdate(CamelModel):
    """보낸 필드만 수정한다. imageUrls를 보내면 이미지 목록 전체를 교체한다."""

    category: PostCategory | None = None
    title: Title | None = None
    content: Content | None = None
    image_urls: list[ImageUrl] | None = Field(default=None, max_length=POST_IMAGE_MAX_COUNT)

    @model_validator(mode="after")
    def _check(self):
        sent = self.model_fields_set
        if not sent:
            raise ValueError("수정할 항목이 없습니다")
        for name in sent:
            if getattr(self, name) is None:
                raise ValueError(f"{name}는 null일 수 없습니다")
        _reject_blank(self.title, self.content)
        return self


class Author(CamelModel):
    id: int
    nickname: str


class PostSummary(CamelModel):
    id: int
    category: PostCategory
    title: str
    author: Author
    comment_count: int
    has_image: bool
    created_at: datetime


class PostDetail(CamelModel):
    id: int
    category: PostCategory
    title: str
    content: str
    image_urls: list[str]
    author: Author
    is_mine: bool  # 비로그인이면 항상 false
    created_at: datetime
    updated_at: datetime


class CommentBody(CamelModel):
    content: CommentContent

    @model_validator(mode="after")
    def _not_blank(self):
        _reject_blank(self.content)
        return self


class CommentResponse(CamelModel):
    id: int
    post_id: int
    content: str
    author: Author
    is_mine: bool
    created_at: datetime
    updated_at: datetime
