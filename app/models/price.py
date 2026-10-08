from datetime import date, datetime
from decimal import Decimal

from sqlalchemy import BigInteger, Date, DateTime, ForeignKey, Integer, Numeric, String, func
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import Mapped, mapped_column

from app.core.db import Base


class PriceDaily(Base):
    __tablename__ = 'price_daily'
    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    item_id: Mapped[int] = mapped_column(ForeignKey('item.id'))
    region: Mapped[str] = mapped_column(String(20))
    price_date: Mapped[date] = mapped_column(Date)
    price: Mapped[int] = mapped_column(Integer)
    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())


class PriceModelRun(Base):
    __tablename__ = 'price_model_run'
    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    item_id: Mapped[int] = mapped_column(ForeignKey('item.id'))
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
    item_id: Mapped[int] = mapped_column(ForeignKey('item.id'))
    base_date: Mapped[date] = mapped_column(Date)
    target_date: Mapped[date] = mapped_column(Date)
    predicted_price: Mapped[int] = mapped_column(Integer)
    lower_price: Mapped[int | None] = mapped_column(Integer)
    upper_price: Mapped[int | None] = mapped_column(Integer)
    model_run_id: Mapped[int | None] = mapped_column(ForeignKey('price_model_run.id'))
    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())


class PriceInsight(Base):
    __tablename__ = 'price_insight'
    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    item_id: Mapped[int] = mapped_column(ForeignKey('item.id'))
    base_date: Mapped[date] = mapped_column(Date)
    recommendation: Mapped[str] = mapped_column(String(20))
    buy_after_days: Mapped[int | None] = mapped_column(Integer)
    expected_saving: Mapped[int | None] = mapped_column(Integer)
    mape: Mapped[Decimal | None] = mapped_column(Numeric(12,4))
    factors: Mapped[list | None] = mapped_column(JSONB)
    model_run_id: Mapped[int | None] = mapped_column(ForeignKey('price_model_run.id'))
    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())
