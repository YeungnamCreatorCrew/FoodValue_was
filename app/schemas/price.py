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


class PriceMarket(StrEnum):
    RETAIL = 'RETAIL'
    WHOLESALE = 'WHOLESALE'


class PriceSort(StrEnum):
    NAME = 'name'
    CHANGE = 'change'
    FORECAST = 'forecast'


class PriceSummary(CamelModel):
    id: int
    name: str
    aliases: list[str] = Field(default_factory=list)
    category: PriceCategory
    market: PriceMarket
    series_id: int
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
    market: PriceMarket
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
    market: PriceMarket
    series_id: int
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


class PriceSummaryText(CamelModel):
    """AI 예측 요약 문장. generator=GEMINI는 LLM이 다듬은 문장(숫자 검증 통과), TEMPLATE은 고정 문장"""
    headline: str
    detail: str
    categories: dict[str, str] = Field(default_factory=dict)
    generator: str | None = None


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
    summary: PriceSummaryText | None = None
    fridge: FridgeHolding | None


class FactorCategory(CamelModel):
    category: str
    label: str
    contribution: float
    direction: str
    description: str | None = None


class PriceFactor(CamelModel):
    id: str
    label: str
    category: str
    value: float | None
    unit: str
    previous_value: float | None = None
    previous_date: date | None = None
    contribution: float
    direction: str
    has_history: bool


class PriceFactors(CamelModel):
    item_id: int
    market: PriceMarket
    base_date: date | None
    status: str
    explained: bool = False
    unavailable_reason: str | None = None
    model_name: str | None = None
    # 최종 평가(과거 검증) 구간. 모델 채택 여부를 이 기간의 백테스트로 정했다는 근거 표시용
    evaluation_start: date | None = None
    evaluation_end: date | None = None
    method: str | None = None
    horizon_days: int | None = None
    target_date: date | None = None
    current_price: float | None = None
    base_price: float | None = None
    predicted_price: int | None = None
    summary: PriceSummaryText | None = None
    categories: list[FactorCategory] = Field(default_factory=list)
    factors: list[PriceFactor] = Field(default_factory=list)


class FactorHistoryPoint(CamelModel):
    date: date
    value: float | None


class FactorHistory(CamelModel):
    item_id: int
    market: PriceMarket
    factor_id: str
    label: str
    unit: str
    base_date: date
    days: int
    points: list[FactorHistoryPoint]


class IndicatorSignal(CamelModel):
    key: str
    label: str
    state: str | None
    state_label: str


class IndicatorSummary(CamelModel):
    headline: str
    signals: list[IndicatorSignal]


class IndicatorCard(CamelModel):
    key: str
    verdict: str  # FACT | PASS | CONDITIONAL
    state: str | None  # UP | NEUTRAL | DOWN | null
    fact: dict
    evidence: dict
    chart: dict | None = None


class PriceIndicators(CamelModel):
    item_id: int
    market: PriceMarket
    status: str  # READY | STALE | NO_DATA | INSUFFICIENT_HISTORY
    as_of_date: date | None = None
    spec_version: str | None = None
    unavailable_reason: str | None = None
    summary: IndicatorSummary | None = None
    cards: list[IndicatorCard] = Field(default_factory=list)
