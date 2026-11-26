"""배추·무 이어 붙인 계열(기준서 §2.3)을 DB에 만든다.

KAMIS는 배추·무를 작형(월동 06·봄 01·고랭지 02·가을 03)별 품종 코드로만 준다. 실험(v1·v2)은 tools.loader.merge_kinds로
작형별 가격을 하나의 계열로 이어 붙여 학습·예측했다. 서비스도 같은 계열에 예측·지표를 붙여야 하므로:

- 품목 '배추'·'무'(목록 노출)를 만들고, 작형별 원본 품목('배추(월동)' 등)은 목록에서 숨긴다(is_price_listed).
- 소매·도매마다 source='MERGED' 계열을 만든다. 코드는 작형 계열의 품목·등급 코드, 품종 코드 '00'.
- price_daily는 작형별 price_daily에 merge_kinds를 그대로 적용해 다시 계산한다(observation_id 없음).
  실험 스냅샷의 price_daily_merged.csv와 같은 함수·같은 조사일(calendar_day.is_market_closed = false)을 쓴다.

여러 번 실행해도 결과가 같다. KAMIS 수집·정제 뒤(price_pipeline)와 단독 명령(app.merged_series)에서 실행한다.
"""
from collections import defaultdict
from datetime import date

from sqlalchemy import delete, select
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.orm import Session

from app.models.item import Item
from app.models.prediction_input import CalendarDay
from app.models.price import PriceDaily, PriceSeries
from tools import loader

BASES = ('배추', '무')
SOURCE = 'MERGED'
KIND_CODE = '00'


class MergeError(Exception):
    pass


def _kind_items(db, base: str) -> list[Item]:
    return db.scalars(select(Item).where(Item.name.like(f'{base}(%')).order_by(Item.id)).all()


def _ensure_item(db, base: str, template: Item) -> Item:
    item = db.scalar(select(Item).where(Item.name == base))
    if item is None:
        item = Item(name=base, category=template.category, default_unit=template.default_unit,
                    default_storage=template.default_storage, food_type=template.food_type,
                    grams_per_unit=template.grams_per_unit, density_g_per_ml=template.density_g_per_ml,
                    price_source=template.price_source, price_unit_label=template.price_unit_label,
                    is_price_listed=True)
        db.add(item)
        db.flush()
    else:
        item.is_price_listed = True
    return item


def _ensure_series(db, item: Item, market: str, sources: list[PriceSeries]) -> PriceSeries:
    specs = {(s.item_code, s.rank_code, s.unit_quantity, s.unit) for s in sources}
    if len(specs) != 1:
        # 기준서 §2.1: 작형별 단위·코드가 다르면 이어 붙이지 않고 팀에 알린다(export_snapshot과 같은 규칙).
        raise MergeError(f'{item.name} {market} 작형별 단위·코드가 다름: {sorted(map(str, specs))}')
    item_code, rank_code, quantity, unit = specs.pop()
    series = db.scalar(select(PriceSeries).where(PriceSeries.item_id == item.id, PriceSeries.market == market))
    if series is None:
        series = PriceSeries(item_id=item.id, source=SOURCE, market=market, item_code=item_code, kind_code=KIND_CODE,
                             rank_code=rank_code, unit_quantity=quantity, unit=unit)
        db.add(series)
        db.flush()
    elif series.source != SOURCE:
        raise MergeError(f'품목 {item.name}({item.id})에 이미 {series.source} {market} 계열이 있음')
    return series


def merged_prices(observations, survey_days) -> dict[date, int]:
    """observations: (날짜, 작형 코드, 가격, 원본 계열 id). 반환: 날짜 → 이어 붙인 가격."""
    return {row.price_date: row.price for row in loader.merge_kinds(observations, survey_days)}


def refresh(engine) -> dict:
    """배추·무 이어 붙인 품목·계열·가격을 만든다. 반환: 품목별 요약."""
    summary = {}
    with Session(engine) as db:
        survey = sorted(db.scalars(select(CalendarDay.cal_date).where(CalendarDay.is_market_closed.is_(False))).all())
        for base in BASES:
            kinds = _kind_items(db, base)
            if not kinds:
                summary[base] = {'status': 'SKIPPED', 'reason': 'NO_KIND_ITEMS'}
                continue
            item = _ensure_item(db, base, kinds[0])
            for kind in kinds:
                kind.is_price_listed = False
            by_market = defaultdict(list)
            for series in db.scalars(select(PriceSeries).where(PriceSeries.item_id.in_([k.id for k in kinds]),
                                                               PriceSeries.source == 'KAMIS')).all():
                by_market[series.market].append(series)
            markets = {}
            for market, sources in sorted(by_market.items()):
                merged = _ensure_series(db, item, market, sources)
                observations = [(day, s.kind_code, price, s.id) for s in sources
                                for day, price in db.execute(select(PriceDaily.price_date, PriceDaily.price)
                                                             .where(PriceDaily.series_id == s.id)).all()]
                prices = merged_prices(observations, survey)
                db.execute(delete(PriceDaily).where(PriceDaily.series_id == merged.id,
                                                    PriceDaily.price_date.not_in(list(prices) or [date(1900, 1, 1)])))
                if prices:
                    rows = [{'series_id': merged.id, 'price_date': day, 'price': price} for day, price in prices.items()]
                    for start in range(0, len(rows), 2000):
                        statement = insert(PriceDaily).values(rows[start:start + 2000])
                        db.execute(statement.on_conflict_do_update(
                            constraint='uk_price_daily', set_={'price': statement.excluded.price,
                                                               'observation_id': None}))
                markets[market] = {'seriesId': merged.id, 'days': len(prices),
                                   'last': max(prices).isoformat() if prices else None,
                                   'sources': [s.id for s in sources]}
            summary[base] = {'status': 'SUCCESS', 'itemId': item.id, 'kindItems': [k.name for k in kinds],
                             'markets': markets}
        db.commit()
    merged_items = [v['itemId'] for v in summary.values() if v.get('status') == 'SUCCESS']
    if merged_items:
        # 지표·목록이 쓰는 1~7일 변동률도 이어 붙인 계열 기준으로 만든다.
        from app.services import warehouse_service
        warehouse_service.refresh_price_change_history(engine, merged_items)
    return summary
