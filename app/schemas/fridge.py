from datetime import date, datetime
from decimal import Decimal
from enum import StrEnum
from typing import Annotated

from pydantic import Field, StringConstraints, model_validator

from app.core.constants import ID_MAX
from app.schemas.common import CamelModel


class Storage(StrEnum):
    FRIDGE = 'FRIDGE'
    FREEZER = 'FREEZER'
    ROOM = 'ROOM'


class FoodType(StrEnum):
    RAW = 'RAW'
    PROCESSED = 'PROCESSED'


class Unit(StrEnum):
    G = 'g'
    KG = 'kg'
    ML = 'ml'
    L = 'L'
    EACH = '개'
    BUNCH = '단'
    BLOCK = '모'
    PACK = '팩'
    BAG = '봉'
    CLUSTER = '송이'
    BULB = '구'


class Reason(StrEnum):
    USE = 'USE'
    FINISH = 'FINISH'
    DISCARD = 'DISCARD'


class Sort(StrEnum):
    PURCHASED = 'purchased'
    NAME = 'name'
    NEWEST = 'newest'


Amount = Annotated[Decimal, Field(gt=0, max_digits=12, decimal_places=3)]
Name = Annotated[str, StringConstraints(strip_whitespace=True, min_length=1, max_length=50)]
ItemId = Annotated[int, Field(ge=1, le=ID_MAX)]


class IngredientCreate(CamelModel):
    item_id: ItemId | None = None
    display_name: Name
    quantity: Amount
    unit: Unit
    storage: Storage
    food_type: FoodType | None = None
    purchased_at: date
    grams_per_unit: Amount | None = None
    purchase_price: int | None = Field(None, ge=0, le=2**31 - 1)

    @model_validator(mode='after')
    def check_weight(self):
        fixed = {'g': Decimal(1), 'kg': Decimal(1000)}.get(self.unit)
        if fixed is not None and self.grams_per_unit not in (None, fixed):
            raise ValueError('g/kg 단위의 환산 무게는 변경할 수 없습니다')
        return self


class IngredientUpdate(CamelModel):
    # 수량 변경은 consume에서만 허용한다. 최초 등록량과 사용 이력의 일관성을 유지한다.
    display_name: Name | None = None
    storage: Storage | None = None
    food_type: FoodType | None = None
    purchased_at: date | None = None
    grams_per_unit: Amount | None = None
    purchase_price: int | None = Field(None, ge=0, le=2**31 - 1)

    @model_validator(mode='after')
    def check_fields(self):
        if not self.model_fields_set:
            raise ValueError('수정할 항목이 없습니다')
        for key in self.model_fields_set - {'grams_per_unit', 'purchase_price'}:
            if getattr(self, key) is None:
                raise ValueError(f'{key}는 null일 수 없습니다')
        return self


class Consume(CamelModel):
    reason: Reason = Reason.USE
    amount: Amount | None = None
    used_at: date
    memo: str | None = Field(None, max_length=100)

    @model_validator(mode='after')
    def check_amount(self):
        if self.reason == Reason.USE and self.amount is None:
            raise ValueError('사용량을 입력해 주세요')
        if self.reason == Reason.FINISH and self.amount is not None:
            raise ValueError('다 먹음은 잔량 전체를 차감합니다. amount를 생략하세요')
        return self


class ItemResponse(CamelModel):
    id: int
    name: str
    category: str
    default_unit: str
    default_storage: Storage
    food_type: FoodType
    grams_per_unit: Decimal | None
    density_g_per_ml: Decimal | None
    price_source: str | None
    price_unit_label: str | None


class IngredientResponse(CamelModel):
    id: int
    item_id: int | None
    display_name: str
    quantity: Decimal
    initial_quantity: Decimal
    unit: Unit
    storage: Storage
    purchased_at: date
    grams_per_unit: Decimal | None
    purchase_price: int | None
    created_at: datetime
    updated_at: datetime
    price_available: bool = False
    food_type: FoodType | None = None


class UsageResponse(CamelModel):
    id: int
    used_amount: Decimal
    grams_used: Decimal | None
    reason: Reason
    memo: str | None
    used_at: date
    created_at: datetime


class ReceiptConfirm(CamelModel):
    # 원본 OCR 후보를 그대로 신뢰하지 않고 사용자가 확인한 전체 등록 정보를 받는다.
    items: list[IngredientCreate] = Field(min_length=1, max_length=100)
