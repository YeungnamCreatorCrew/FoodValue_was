"""V2 예측 입력 정형 테이블. 수집 원천(external_observation)·price_daily에서 파생해 적재한다."""
from datetime import date, datetime
from decimal import Decimal

from sqlalchemy import BigInteger, Boolean, Date, DateTime, ForeignKey, Integer, Numeric, SmallInteger, String, func
from sqlalchemy.orm import Mapped, mapped_column

from app.core.db import Base


class WeatherDaily(Base):
    __tablename__ = 'weather_daily'
    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    weather_date: Mapped[date] = mapped_column(Date)
    data_type: Mapped[str] = mapped_column(String(10))
    avg_temp: Mapped[Decimal | None] = mapped_column(Numeric(4, 1))
    max_temp: Mapped[Decimal | None] = mapped_column(Numeric(4, 1))
    min_temp: Mapped[Decimal | None] = mapped_column(Numeric(4, 1))
    precipitation: Mapped[Decimal | None] = mapped_column(Numeric(6, 1))
    avg_humidity: Mapped[Decimal | None] = mapped_column(Numeric(4, 1))
    sunshine_hours: Mapped[Decimal | None] = mapped_column(Numeric(4, 1))
    heat_station_ratio: Mapped[Decimal | None] = mapped_column(Numeric(5, 2))
    heavy_rain_station_ratio: Mapped[Decimal | None] = mapped_column(Numeric(5, 2))
    cold_station_ratio: Mapped[Decimal | None] = mapped_column(Numeric(5, 2))
    station_count: Mapped[int | None] = mapped_column(Integer)
    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())


class CalendarDay(Base):
    __tablename__ = 'calendar_day'
    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    cal_date: Mapped[date] = mapped_column(Date)
    day_of_week: Mapped[int] = mapped_column(SmallInteger)
    is_holiday: Mapped[bool] = mapped_column(Boolean)
    holiday_name: Mapped[str | None] = mapped_column(String(30))
    lunar_month: Mapped[int] = mapped_column(SmallInteger)
    lunar_day: Mapped[int] = mapped_column(SmallInteger)
    is_lunar_leap: Mapped[bool] = mapped_column(Boolean)
    is_market_closed: Mapped[bool] = mapped_column(Boolean)
    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())


class CalendarEvent(Base):
    __tablename__ = 'calendar_event'
    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    event_code: Mapped[str] = mapped_column(String(30))
    name: Mapped[str] = mapped_column(String(50))
    start_date: Mapped[date] = mapped_column(Date)
    end_date: Mapped[date] = mapped_column(Date)
    effect_start_date: Mapped[date] = mapped_column(Date)
    effect_end_date: Mapped[date] = mapped_column(Date)
    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())


class PriceChangeHistory(Base):
    __tablename__ = 'price_change_history'
    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    series_id: Mapped[int] = mapped_column(ForeignKey('price_series.id'))
    price_year: Mapped[int] = mapped_column(SmallInteger)
    month_day: Mapped[str] = mapped_column(String(5))
    horizon_days: Mapped[int] = mapped_column(SmallInteger)
    base_price: Mapped[int] = mapped_column(Integer)
    change_rate: Mapped[Decimal] = mapped_column(Numeric(6, 2))
    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())


class ItemProduction(Base):
    __tablename__ = 'item_production'
    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    item_id: Mapped[int] = mapped_column(ForeignKey('item.id'))
    measure_type: Mapped[str] = mapped_column(String(20))
    period_type: Mapped[str] = mapped_column(String(10))
    period_start: Mapped[date] = mapped_column(Date)
    period_end: Mapped[date] = mapped_column(Date)
    volume: Mapped[Decimal] = mapped_column(Numeric(14, 1))
    volume_unit: Mapped[str] = mapped_column(String(10))
    is_estimate: Mapped[bool] = mapped_column(Boolean)
    source: Mapped[str] = mapped_column(String(20))
    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())


class ExchangeRateDaily(Base):
    __tablename__ = 'exchange_rate_daily'
    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    rate_date: Mapped[date] = mapped_column(Date)
    currency_code: Mapped[str] = mapped_column(String(10))
    rate: Mapped[Decimal] = mapped_column(Numeric(12, 4))
    unit_label: Mapped[str] = mapped_column(String(30))
    source: Mapped[str] = mapped_column(String(20), server_default='ECOS')
    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())


class EventItemWeight(Base):
    __tablename__ = 'event_item_weight'
    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    event_code: Mapped[str] = mapped_column(String(30))
    item_id: Mapped[int | None] = mapped_column(ForeignKey('item.id'))
    category: Mapped[str | None] = mapped_column(String(20))
    weight: Mapped[Decimal] = mapped_column(Numeric(4, 2))
    weight_source: Mapped[str] = mapped_column(String(10))
    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())
