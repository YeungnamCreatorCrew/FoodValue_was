from datetime import date, datetime
from decimal import Decimal

from sqlalchemy import BigInteger, Date, DateTime, Double, ForeignKey, Integer, Numeric, SmallInteger, String, func
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import Mapped, mapped_column

from app.core.db import Base


RETAIL, WHOLESALE = 'RETAIL', 'WHOLESALE'
COUNTERPART = {RETAIL: WHOLESALE, WHOLESALE: RETAIL}  # 예측 변수로 쓰는 상대 시장
# 예측 모델 트랙(price_model_run.model_track). ENSEMBLE이 기본 공개 트랙(v2 앙상블, v2 대상 밖 계열은 v5)
ENSEMBLE, STRUCT = 'ENSEMBLE', 'STRUCT'
TRACKS = (ENSEMBLE, STRUCT)


class PriceSeries(Base):
    """가격 계열: 품목 × 시장(소매·도매). 계열마다 예측하고, 상대 시장 가격을 예측 변수로 쓴다."""
    __tablename__ = 'price_series'
    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    item_id: Mapped[int] = mapped_column(ForeignKey('item.id'))
    source: Mapped[str] = mapped_column(String(10), server_default='KAMIS')
    market: Mapped[str] = mapped_column(String(10))
    item_code: Mapped[str] = mapped_column(String(3))
    kind_code: Mapped[str] = mapped_column(String(2))
    rank_code: Mapped[str] = mapped_column(String(2))
    unit_quantity: Mapped[Decimal] = mapped_column(Numeric(10, 3))
    unit: Mapped[str] = mapped_column(String(10))
    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())

    @property
    def code(self):
        """KAMIS 수집기·원천 키가 쓰는 품목-품종-등급 표기 (예: 246-00-04)"""
        return f'{self.item_code}-{self.kind_code}-{self.rank_code}'

    @property
    def unit_label(self):
        return f'{Decimal(str(self.unit_quantity)).normalize():f}{self.unit}'  # 1.000 kg → 1kg


class PriceDaily(Base):
    __tablename__ = 'price_daily'
    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    series_id: Mapped[int] = mapped_column(ForeignKey('price_series.id'))
    price_date: Mapped[date] = mapped_column(Date)
    price: Mapped[int] = mapped_column(Integer)
    observation_id: Mapped[int | None] = mapped_column(ForeignKey('external_observation.id'))
    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())


class PriceModelRun(Base):
    __tablename__ = 'price_model_run'
    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    series_id: Mapped[int] = mapped_column(ForeignKey('price_series.id'))
    model_track: Mapped[str] = mapped_column(String(20), server_default=ENSEMBLE)
    base_date: Mapped[date] = mapped_column(Date)
    data_date: Mapped[date | None] = mapped_column(Date)
    status: Mapped[str] = mapped_column(String(20))
    model_name: Mapped[str | None] = mapped_column(String(30))
    model_version: Mapped[str | None] = mapped_column(String(50))
    quality: Mapped[str | None] = mapped_column(String(20))
    metrics: Mapped[dict | None] = mapped_column(JSONB)
    error_code: Mapped[str | None] = mapped_column(String(40))
    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())
    finished_at: Mapped[datetime | None] = mapped_column(DateTime)


class PriceForecast(Base):
    __tablename__ = 'price_forecast'
    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    target_date: Mapped[date] = mapped_column(Date)
    predicted_price: Mapped[int] = mapped_column(Integer)
    lower_price: Mapped[int | None] = mapped_column(Integer)
    upper_price: Mapped[int | None] = mapped_column(Integer)
    model_run_id: Mapped[int] = mapped_column(ForeignKey('price_model_run.id'))
    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())


class PriceInsight(Base):
    __tablename__ = 'price_insight'
    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    recommendation: Mapped[str] = mapped_column(String(20))
    buy_after_days: Mapped[int | None] = mapped_column(Integer)
    expected_saving: Mapped[int | None] = mapped_column(Integer)
    mape: Mapped[Decimal | None] = mapped_column(Numeric(12,4))
    factors: Mapped[list | None] = mapped_column(JSONB)
    summary: Mapped[dict | None] = mapped_column(JSONB)
    summary_generator: Mapped[str | None] = mapped_column(String(20))
    summary_model: Mapped[str | None] = mapped_column(String(60))
    summary_prompt_version: Mapped[str | None] = mapped_column(String(20))
    model_run_id: Mapped[int] = mapped_column(ForeignKey('price_model_run.id'))
    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())


class PriceForecastExplanation(Base):
    """7일 뒤 예측의 SHAP 설명 머리 정보(학습 모델로 공개된 실행만)"""
    __tablename__ = 'price_forecast_explanation'
    model_run_id: Mapped[int] = mapped_column(ForeignKey('price_model_run.id'), primary_key=True)
    horizon_days: Mapped[int] = mapped_column(SmallInteger)
    method: Mapped[str] = mapped_column(String(30))
    current_price: Mapped[Decimal] = mapped_column(Numeric(14, 2))
    damping: Mapped[Decimal] = mapped_column(Numeric(8, 4))
    base_price: Mapped[Decimal] = mapped_column(Numeric(14, 2))
    predicted_price: Mapped[int] = mapped_column(Integer)
    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())


class PriceForecastFactor(Base):
    """특징별 SHAP 기여(원)와 최근 90일 특징값"""
    __tablename__ = 'price_forecast_factor'
    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    model_run_id: Mapped[int] = mapped_column(ForeignKey('price_forecast_explanation.model_run_id'))
    feature: Mapped[str] = mapped_column(String(40))
    feature_value: Mapped[float | None] = mapped_column(Double)
    contribution: Mapped[Decimal] = mapped_column(Numeric(14, 4))
    history: Mapped[list] = mapped_column(JSONB, server_default='[]')
    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())


class BacktestRun(Base):
    __tablename__ = 'backtest_run'
    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    series_id: Mapped[int] = mapped_column(ForeignKey('price_series.id'))
    model_version: Mapped[str] = mapped_column(String(50))
    git_commit: Mapped[str | None] = mapped_column(String(40))
    start_date: Mapped[date] = mapped_column(Date)
    end_date: Mapped[date] = mapped_column(Date)
    every_days: Mapped[int] = mapped_column(SmallInteger)
    summary: Mapped[dict] = mapped_column(JSONB)
    note: Mapped[str | None] = mapped_column(String(200))
    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())


class BacktestOrigin(Base):
    __tablename__ = 'backtest_origin'
    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    backtest_run_id: Mapped[int] = mapped_column(ForeignKey('backtest_run.id', ondelete='CASCADE'))
    base_date: Mapped[date] = mapped_column(Date)
    status: Mapped[str] = mapped_column(String(20))
    model_name: Mapped[str | None] = mapped_column(String(30))
    quality: Mapped[str | None] = mapped_column(String(20))
    detail: Mapped[dict | None] = mapped_column(JSONB)


class BacktestPoint(Base):
    __tablename__ = 'backtest_point'
    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    backtest_run_id: Mapped[int] = mapped_column(ForeignKey('backtest_run.id', ondelete='CASCADE'))
    base_date: Mapped[date] = mapped_column(Date)
    target_date: Mapped[date] = mapped_column(Date)
    horizon: Mapped[int] = mapped_column(SmallInteger)
    model_name: Mapped[str] = mapped_column(String(30))
    quality: Mapped[str] = mapped_column(String(20))
    current_price: Mapped[int] = mapped_column(Integer)
    predicted_price: Mapped[int] = mapped_column(Integer)
    lower_price: Mapped[int | None] = mapped_column(Integer)
    upper_price: Mapped[int | None] = mapped_column(Integer)
    actual_price: Mapped[int] = mapped_column(Integer)
