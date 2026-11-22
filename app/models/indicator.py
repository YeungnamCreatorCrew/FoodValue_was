from datetime import date, datetime

from sqlalchemy import BigInteger, Date, DateTime, ForeignKey, String, func
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import Mapped, mapped_column

from app.core.db import Base


class PriceIndicatorValidation(Base):
    __tablename__ = 'price_indicator_validation'
    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    series_id: Mapped[int] = mapped_column(ForeignKey('price_series.id'))
    spec_version: Mapped[str] = mapped_column(String(20))
    indicator_key: Mapped[str] = mapped_column(String(30))
    verdict: Mapped[str] = mapped_column(String(12))
    stats: Mapped[dict] = mapped_column(JSONB)
    data_start: Mapped[date] = mapped_column(Date)
    data_end: Mapped[date] = mapped_column(Date)
    validated_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())


class PriceIndicatorRun(Base):
    __tablename__ = 'price_indicator_run'
    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    series_id: Mapped[int] = mapped_column(ForeignKey('price_series.id'))
    as_of_date: Mapped[date] = mapped_column(Date)
    data_date: Mapped[date] = mapped_column(Date)
    spec_version: Mapped[str] = mapped_column(String(20))
    status: Mapped[str] = mapped_column(String(20))
    summary: Mapped[dict | None] = mapped_column(JSONB)
    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())


class PriceIndicatorCard(Base):
    __tablename__ = 'price_indicator_card'
    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    run_id: Mapped[int] = mapped_column(ForeignKey('price_indicator_run.id'))
    indicator_key: Mapped[str] = mapped_column(String(30))
    validation_id: Mapped[int | None] = mapped_column(ForeignKey('price_indicator_validation.id'))
    verdict: Mapped[str] = mapped_column(String(12))
    state: Mapped[str | None] = mapped_column(String(10))
    fact: Mapped[dict] = mapped_column(JSONB)
    evidence: Mapped[dict] = mapped_column(JSONB)
    chart: Mapped[dict | None] = mapped_column(JSONB)
    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())
