from datetime import datetime
from decimal import Decimal

from sqlalchemy import BigInteger, Boolean, DateTime, ForeignKey, Numeric, String, func, true
from sqlalchemy.orm import Mapped, mapped_column

from app.core.db import Base


class Item(Base):
    __tablename__ = 'item'
    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    name: Mapped[str] = mapped_column(String(50))
    category: Mapped[str] = mapped_column(String(20))
    default_unit: Mapped[str] = mapped_column(String(10))
    default_storage: Mapped[str] = mapped_column(String(10))
    food_type: Mapped[str] = mapped_column(String(10), server_default='RAW')
    grams_per_unit: Mapped[Decimal | None] = mapped_column(Numeric(12, 3))
    density_g_per_ml: Mapped[Decimal | None] = mapped_column(Numeric(12, 3))
    price_source: Mapped[str | None] = mapped_column(String(10))
    price_unit_label: Mapped[str | None] = mapped_column(String(30))
    is_price_listed: Mapped[bool] = mapped_column(Boolean, server_default=true())  # 시세 목록·검색 노출. 작형별 원본 품목은 False
    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())


class ItemAlias(Base):
    __tablename__ = 'item_alias'
    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    item_id: Mapped[int] = mapped_column(ForeignKey('item.id', ondelete='CASCADE'))
    alias: Mapped[str] = mapped_column(String(50))
    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())
