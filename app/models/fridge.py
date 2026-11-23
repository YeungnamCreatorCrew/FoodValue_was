from datetime import date, datetime
from decimal import Decimal

from sqlalchemy import BigInteger, Boolean, Date, DateTime, ForeignKey, Integer, Numeric, String, func, true
from sqlalchemy.dialects.postgresql import JSONB
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


class FridgeIngredient(Base):
    __tablename__ = 'fridge_ingredient'
    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))
    item_id: Mapped[int | None] = mapped_column(ForeignKey('item.id', ondelete='SET NULL'))
    display_name: Mapped[str] = mapped_column(String(50))
    quantity: Mapped[Decimal] = mapped_column(Numeric(12, 3))
    initial_quantity: Mapped[Decimal] = mapped_column(Numeric(12, 3))
    unit: Mapped[str] = mapped_column(String(10))
    storage: Mapped[str] = mapped_column(String(10))
    food_type: Mapped[str] = mapped_column(String(10), server_default='RAW')
    purchased_at: Mapped[date] = mapped_column(Date)
    grams_per_unit: Mapped[Decimal | None] = mapped_column(Numeric(12, 3))
    purchase_price: Mapped[int | None] = mapped_column(Integer)
    deleted_at: Mapped[datetime | None] = mapped_column(DateTime)
    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())


class IngredientUsage(Base):
    __tablename__ = 'ingredient_usage'
    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    fridge_ingredient_id: Mapped[int] = mapped_column(ForeignKey('fridge_ingredient.id', ondelete='CASCADE'))
    used_amount: Mapped[Decimal] = mapped_column(Numeric(12, 3))
    grams_used: Mapped[Decimal | None] = mapped_column(Numeric(18, 3))
    reason: Mapped[str] = mapped_column(String(10), server_default='USE')
    memo: Mapped[str | None] = mapped_column(String(100))
    used_at: Mapped[date] = mapped_column(Date)
    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())


class ItemNutrition(Base):
    __tablename__ = 'item_nutrition'
    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    item_id: Mapped[int] = mapped_column(ForeignKey('item.id', ondelete='CASCADE'))
    edible_ratio: Mapped[Decimal | None] = mapped_column(Numeric(5, 2))
    carbohydrate_g: Mapped[Decimal | None] = mapped_column(Numeric(7, 2))
    protein_g: Mapped[Decimal | None] = mapped_column(Numeric(7, 2))
    fat_g: Mapped[Decimal | None] = mapped_column(Numeric(7, 2))
    sodium_mg: Mapped[Decimal | None] = mapped_column(Numeric(8, 2))
    sugars_g: Mapped[Decimal | None] = mapped_column(Numeric(7, 2))
    cholesterol_mg: Mapped[Decimal | None] = mapped_column(Numeric(8, 2))
    source: Mapped[str] = mapped_column(String(20))
    basis: Mapped[str] = mapped_column(String(10), server_default='100G')


class FridgeReceipt(Base):
    __tablename__ = 'fridge_receipt'
    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))
    purchased_at: Mapped[date] = mapped_column(Date)
    candidates: Mapped[list] = mapped_column(JSONB)
    confirmed_at: Mapped[datetime | None] = mapped_column(DateTime)
    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())
