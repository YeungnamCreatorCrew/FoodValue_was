from pydantic import BaseModel, ConfigDict
from pydantic.alias_generators import to_camel


class CamelModel(BaseModel):
    """API 명세의 camelCase(accessToken, itemId ...)에 맞춘 응답·요청 베이스"""

    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True, from_attributes=True)


class Page[T](CamelModel):
    items: list[T]
    page: int
    size: int
    total: int
