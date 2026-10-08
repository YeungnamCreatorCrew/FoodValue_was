from datetime import date, datetime
from enum import StrEnum
from pydantic import Field

from app.schemas.common import CamelModel


class PriceCategory(StrEnum):
    VEGETABLE = 'VEGETABLE'
    GRAIN = 'GRAIN'
    FRUIT = 'FRUIT'
    MEAT = 'MEAT'
    SEAFOOD = 'SEAFOOD'
    ETC = 'ETC'


class PriceSort(StrEnum):
    NAME = 'name'
    CHANGE = 'change'
    FORECAST = 'forecast'


class PriceSummary(CamelModel):
    id: int
    name: str
    category: PriceCategory
    unit_label: str | None
    source: str
    price_date: date | None
    current_price: int | None
    weekly_change_percent: float | None
    forecast_price: int | None
    forecast_change_percent: float | None
    forecast_base_date: date | None
    forecast_target_date: date | None
    quality: str | None
    status: str


class HistoryPoint(CamelModel):
    date: date
    price: int | None


class PriceHistory(CamelModel):
    item_id: int
    region: str = 'NATIONAL'
    days: int
    start_date: date
    end_date: date
    points: list[HistoryPoint]


class ForecastPoint(CamelModel):
    target_date: date
    predicted_price: int
    lower_price: int | None
    upper_price: int | None


class ForecastResponse(CamelModel):
    item_id: int
    status: str
    base_date: date | None = None
    data_date: date | None = None
    model_run_id: int | None = None
    model_name: str | None = None
    model_version: str | None = None
    quality: str | None = None
    points: list[ForecastPoint] = Field(default_factory=list)
    metrics: dict | None = None
    latest_attempt_status: str | None = None
    updated_at: datetime | None = None


class PriceGuide(CamelModel):
    recommendation: str
    buy_after_days: int | None
    expected_saving: int | None
    mape: float | None
    factors: list[dict]


class FridgeHolding(CamelModel):
    ingredient_count: int
    quantities: dict[str, str]


class PriceDetail(CamelModel):
    item: PriceSummary
    forecast: ForecastResponse
    guide: PriceGuide | None
    fridge: FridgeHolding | None


class PriceFactors(CamelModel):
    item_id: int
    base_date: date | None
    status: str
    factors: list[dict]
