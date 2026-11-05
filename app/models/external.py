from datetime import date, datetime
from decimal import Decimal

from sqlalchemy import ARRAY, BigInteger, Date, DateTime, ForeignKey, Integer, Numeric, SmallInteger, String, Text, func
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import Mapped, mapped_column

from app.core.db import Base


class ExternalCollectionRun(Base):
    __tablename__ = 'external_collection_run'
    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    source: Mapped[str] = mapped_column(String(30))
    dataset: Mapped[str] = mapped_column(String(60))
    start_date: Mapped[date | None] = mapped_column(Date)
    end_date: Mapped[date | None] = mapped_column(Date)
    status: Mapped[str] = mapped_column(String(20))
    request_count: Mapped[int] = mapped_column(Integer, server_default='0')
    records_received: Mapped[int] = mapped_column(Integer, server_default='0')
    records_inserted: Mapped[int] = mapped_column(Integer, server_default='0')
    error_code: Mapped[str | None] = mapped_column(String(120))
    manifest_path: Mapped[str | None] = mapped_column(Text)
    started_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    finished_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))


class ExternalObservation(Base):
    __tablename__ = 'external_observation'
    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    collection_run_id: Mapped[int] = mapped_column(ForeignKey('external_collection_run.id'))
    item_id: Mapped[int | None] = mapped_column(ForeignKey('item.id'))
    source: Mapped[str] = mapped_column(String(30))
    dataset: Mapped[str] = mapped_column(String(60))
    source_record_key: Mapped[str] = mapped_column(String(400))
    entity_code: Mapped[str | None] = mapped_column(String(100))
    entity_name: Mapped[str | None] = mapped_column(String(150))
    observed_on: Mapped[date | None] = mapped_column(Date)
    period_start: Mapped[date | None] = mapped_column(Date)
    period_end: Mapped[date | None] = mapped_column(Date)
    issued_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))
    published_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))
    publication_status: Mapped[str] = mapped_column(String(20), server_default='UNKNOWN')
    retrieved_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    units: Mapped[dict] = mapped_column(JSONB, server_default='{}')
    payload: Mapped[dict] = mapped_column(JSONB)
    payload_sha256: Mapped[str] = mapped_column(String(64))


class ItemWeatherStation(Base):
    __tablename__ = 'item_weather_station'
    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    item_id: Mapped[int] = mapped_column(ForeignKey('item.id'))
    station_code: Mapped[str] = mapped_column(String(20))
    station_name: Mapped[str] = mapped_column(String(100))
    producing_region: Mapped[str] = mapped_column(String(100))
    mapping_status: Mapped[str] = mapped_column(String(20))
    months: Mapped[list[int] | None] = mapped_column(ARRAY(SmallInteger))
    share: Mapped[Decimal | None] = mapped_column(Numeric(6, 5))
    rationale: Mapped[str] = mapped_column(Text)
    valid_from: Mapped[date | None] = mapped_column(Date)
    valid_until: Mapped[date | None] = mapped_column(Date)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
