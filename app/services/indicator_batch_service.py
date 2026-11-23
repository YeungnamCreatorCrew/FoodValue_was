"""판단 보조 지표 배치: 가격 이력 → 카드 스냅샷 저장. API 서버는 이 모듈(pandas)을 import하지 않는다.

기준일 이하 가격만 쓴다(as_of로 과거 시점을 다시 만들 수 있다). 검증은 기준일 이하 자료로 만든 것만 재사용하고,
너무 오래됐거나 없으면 다시 만든다.
"""
from datetime import date, timedelta

import pandas as pd
from sqlalchemy.orm import Session

from app.core import constants as C
from app.models.fridge import Item
from app.repositories import indicator_repository as repo
from app.repositories import series_repository
from app.models.price import RETAIL, WHOLESALE
from app.services.indicators import level_signals, price_stats, seasonal, summary, wholesale_lead
from app.services.indicators.series import weekly_mean

LEAD, SEASON = 'WHOLESALE_LEAD', 'SEASONAL'
POSITION, GAP, VOLATILITY = 'PRICE_POSITION', 'RETAIL_WHOLESALE_GAP', 'VOLATILITY'
KIND_SWITCH = 'KIND_SWITCH'
WEIGHT_IN_G = {'g': 1, 'kg': 1000}
NOTICE_TEXT = {
    LEAD: '작형(품종)이 막 바뀌어서 도매 흐름은 잠시 쉬어요. 서로 다른 품종의 가격을 견주면 잘못된 신호가 되기 때문이에요.',
    VOLATILITY: '작형(품종)이 막 바뀌어서 가격 출렁임은 잠시 쉬어요. 같은 품종으로 최근 4주를 견줄 만큼 가격이 쌓이면 다시 보여드려요.',
}


def kind_switch_notice(key):
    return {'key': key, 'reason': KIND_SWITCH, 'text': NOTICE_TEXT[key]}


def lead_blocked_by_switch(retail: pd.Series, wholesale: pd.Series, as_of: date, retail_breaks, wholesale_breaks) -> bool:
    """작형 전환만 아니었다면 도매 흐름 변화를 말할 수 있었는데, 전환을 걸쳐서 뺀 경우."""
    cut = pd.Timestamp(as_of)
    retail_w, wholesale_w = weekly_mean(retail[retail.index <= cut]), weekly_mean(wholesale[wholesale.index <= cut])
    return (wholesale_lead.latest_changes(retail_w, wholesale_w) is not None
            and wholesale_lead.latest_changes(retail_w, wholesale_w, retail_breaks=retail_breaks, wholesale_breaks=wholesale_breaks) is None)


def wholesale_to_retail_unit(retail_series, wholesale_series) -> float | None:
    """도매가에 곱해 소매 단위(예: 1kg) 가격으로 바꾸는 배수. 소매 1kg, 도매 15kg이면 1/15.
    단위 종류가 달라 환산할 수 없으면 None(소매÷도매 배수가 의미 없으므로 그 카드는 만들지 않는다)."""
    r_unit, w_unit = retail_series.unit, wholesale_series.unit
    r_qty, w_qty = float(retail_series.unit_quantity), float(wholesale_series.unit_quantity)
    if r_unit in WEIGHT_IN_G and w_unit in WEIGHT_IN_G:
        r_qty, w_qty = r_qty * WEIGHT_IN_G[r_unit], w_qty * WEIGHT_IN_G[w_unit]
    elif r_unit != w_unit:
        return None
    return r_qty / w_qty if r_qty > 0 and w_qty > 0 else None


def _series(rows) -> pd.Series:
    return pd.Series([p for _, p in rows], index=pd.to_datetime([d for d, _ in rows]), dtype=float)


def _json_safe(value):
    if isinstance(value, dict):
        return {k: _json_safe(v) for k, v in value.items()}
    if isinstance(value, (list, tuple)):
        return [_json_safe(v) for v in value]
    if isinstance(value, date):
        return value.isoformat()
    return value


def seasonal_card(retail: pd.Series, as_of: date):
    fact = seasonal.seasonal_fact(retail, as_of)
    if fact is None:
        return None
    state = seasonal.seasonal_state(fact)
    strength = seasonal.seasonal_strength(retail[retail.index <= pd.Timestamp(as_of)])
    return {'indicator_key': SEASON, 'verdict': 'FACT', 'state': state, 'validation_id': None,
            'fact': _json_safe(fact),
            'evidence': {'text': f'주차(계절)만으로 주간 가격 변동의 약 {max(0, round(strength["r2Adj"] * 100))}%가 설명됩니다(우연 몫 제외).',
                         **strength},
            'chart': _json_safe(seasonal.seasonal_chart(retail, as_of))}


def stat_card(key, fact, state, text):
    """가격 이력 사실 카드(검증 없이 FACT). fact가 없으면 None."""
    if fact is None:
        return None
    return {'indicator_key': key, 'verdict': 'FACT', 'state': state, 'validation_id': None, 'fact': _json_safe(fact),
            'evidence': {'text': text}, 'chart': None}


def level_validation(db, series_id, key, retail: pd.Series, wholesale: pd.Series, as_of: date, force: bool):
    """수준 신호(1년 위치·배수) 검증. 기준일 이하 자료로 만든 최근 검증을 재사용하고, 없거나 오래되면 다시 만든다.
    주 평균이 LEVEL_MIN_VALIDATION_WEEKS 미만이면 검증하지 않는다(None)."""
    spec = C.INDICATOR_SPEC_VERSION
    validation = None if force else repo.validation_before(db, series_id, key, spec, as_of)
    if validation is not None and (as_of - validation.data_end).days <= C.INDICATOR_REVALIDATE_DAYS:
        return validation
    cut = pd.Timestamp(as_of)
    retail, wholesale = retail[retail.index <= cut], wholesale[wholesale.index <= cut]
    retail_w = weekly_mean(retail)
    corr = None
    if key == POSITION:
        signal = retail_w
    else:
        if wholesale.empty:
            return None
        wholesale_w = weekly_mean(wholesale)
        signal = retail_w / wholesale_w
        percentile = level_signals.rolling_flags(signal)[2]
        corr = float(pd.concat([percentile, wholesale_w / wholesale_w.shift(C.LEAD_LAG_WEEKS) - 1], axis=1).corr().iloc[0, 1])
    if signal.notna().sum() < C.LEVEL_MIN_VALIDATION_WEEKS:
        return None
    result = level_signals.evaluate(retail_w, signal)
    stats = level_signals.stats_for_storage(result, corr)
    stats.update({'periodStart': retail.index[0].date().isoformat(), 'periodEnd': retail.index[-1].date().isoformat()})
    return repo.save_validation(db, series_id, key, spec, 'PASS' if result['passed'] else 'FAILED', stats,
                                retail.index[0].date(), retail.index[-1].date())


def position_card(db, series_id, retail, wholesale, as_of, force):
    """1년 중 위치. 검증을 통과하면 '조건부 근거'(싼 쪽만 강하고 비싼 쪽은 약할 수 있다), 아니면 사실 카드."""
    fact = price_stats.position_fact(retail, as_of)
    if fact is None:
        return None
    validation = level_validation(db, series_id, POSITION, retail, wholesale, as_of, force)
    passed = validation is not None and validation.verdict == 'PASS'
    evidence = {'text': '최근 1년 일별 가격 안에서 지금 가격이 어디쯤인지 보여줍니다.'}
    if passed:
        evidence.update(validation.stats, validatedAt=validation.validated_at.date().isoformat())
    return {'indicator_key': POSITION, 'verdict': 'CONDITIONAL' if passed else 'FACT', 'state': price_stats.position_state(fact),
            'validation_id': validation.id if validation else None, 'fact': _json_safe(fact), 'evidence': evidence, 'chart': None}


def gap_card(db, series_id, retail, wholesale, as_of, force):
    """소매÷도매 배수. 검증은 하지만 도매 흐름과 겹쳐서 항상 사실 카드로 둔다(겹침 정도는 evidence에 담는다)."""
    fact = price_stats.gap_fact(retail, wholesale, as_of)
    if fact is None:
        return None
    validation = level_validation(db, series_id, GAP, retail, wholesale, as_of, force)
    evidence = {'text': '소매가가 도매가의 몇 배인지, 최근 1년과 비교합니다.'}
    if validation is not None:
        evidence.update(validation.stats, validationVerdict=validation.verdict,
                        validatedAt=validation.validated_at.date().isoformat())
    return {'indicator_key': GAP, 'verdict': 'FACT', 'state': None, 'validation_id': validation.id if validation else None,
            'fact': _json_safe(fact), 'evidence': evidence, 'chart': None}


def lead_card(db, series_id, retail: pd.Series, wholesale: pd.Series, as_of: date, force: bool, retail_breaks=(), wholesale_breaks=()):
    """검증이 PASS일 때만 카드. 작형 전환(retail_breaks·wholesale_breaks)을 걸친 변화는 검증과 카드에서 뺀다. 반환: (카드 행 또는 None, 검증 행 또는 None)."""
    spec = C.INDICATOR_SPEC_VERSION
    validation = None if force else repo.validation_before(db, series_id, LEAD, spec, as_of)
    if validation is None or (as_of - validation.data_end).days > C.INDICATOR_REVALIDATE_DAYS:
        cut = pd.Timestamp(as_of)
        result = wholesale_lead.validate(retail[retail.index <= cut], wholesale[wholesale.index <= cut], retail_breaks, wholesale_breaks)
        stats = wholesale_lead.stats_for_storage(result)
        validation = repo.save_validation(db, series_id, LEAD, spec, result['verdict'], stats,
                                          result['period_start'], result['period_end'])
    if validation.verdict != 'PASS':
        return None, validation
    cut = pd.Timestamp(as_of)
    retail_w, wholesale_w = weekly_mean(retail[retail.index <= cut]), weekly_mean(wholesale[wholesale.index <= cut])
    latest = wholesale_lead.latest_changes(retail_w, wholesale_w, retail_breaks=retail_breaks, wholesale_breaks=wholesale_breaks)
    if latest is None:
        return None, validation
    card = {'indicator_key': LEAD, 'verdict': 'PASS', 'validation_id': validation.id,
            'state': wholesale_lead.lead_state(latest['wholesaleChange2w']), 'fact': _json_safe(latest),
            'evidence': {**validation.stats, 'validatedAt': validation.validated_at.date().isoformat()},
            'chart': wholesale_lead.indexed_chart(retail_w, wholesale_w)}
    return card, validation


def run(engine, item_id: int, as_of: date | None = None, validate: bool = False):
    """소매 계열 기준 지표 스냅샷을 만든다. 반환: {'status','asOfDate','dataDate','cards':[키...]}"""
    with Session(engine) as db:
        retail_series, wholesale_series = series_repository.get(db, item_id, RETAIL), series_repository.get(db, item_id, WHOLESALE)
        if retail_series is None:
            raise ValueError('품목에 소매 가격 계열이 없습니다')
        name = db.get(Item, item_id).name
        end = as_of or date.max
        retail = _series(series_repository.prices(db, retail_series.id, end=end))
        wholesale = _series(series_repository.prices(db, wholesale_series.id, end=end)) if wholesale_series else pd.Series(dtype=float)
        if retail.empty:
            raise ValueError('소매 가격이 없습니다')
        data_date = retail.index[-1].date()
        as_of = as_of or data_date
        retail_breaks = [d for d in series_repository.kind_switch_dates(db, retail_series.id) if d <= as_of]
        cards, validation, notices = [], None, []
        position = position_card(db, retail_series.id, retail, wholesale, as_of, validate)
        if position:
            cards.append(position)
        season = seasonal_card(retail, as_of)
        if season:
            cards.append(season)
        if not wholesale.empty:
            wholesale_breaks = [d for d in series_repository.kind_switch_dates(db, wholesale_series.id) if d <= as_of]
            lead, validation = lead_card(db, retail_series.id, retail, wholesale, as_of, validate, retail_breaks, wholesale_breaks)
            if lead:
                cards.append(lead)
            elif validation.verdict == 'PASS' and lead_blocked_by_switch(retail, wholesale, as_of, retail_breaks, wholesale_breaks):
                notices.append(kind_switch_notice(LEAD))
            unit_scale = wholesale_to_retail_unit(retail_series, wholesale_series)
            gap = gap_card(db, retail_series.id, retail, wholesale * unit_scale, as_of, validate) if unit_scale else None
            if gap:
                cards.append(gap)
        volatility = price_stats.volatility_fact(retail, as_of, retail_breaks)
        if volatility is None and retail_breaks and price_stats.volatility_fact(retail, as_of) is not None:
            notices.append(kind_switch_notice(VOLATILITY))
        cards += [c for c in [stat_card(VOLATILITY, volatility, None, '최근 4주 가격이 얼마나 출렁였는지, 최근 1년과 비교합니다.')] if c]
        digest = summary.build(name, [{'key': c['indicator_key'], 'state': c['state']} for c in cards])
        status = 'SUCCESS' if cards else 'INSUFFICIENT_DATA'
        lead_verdict = validation.verdict if validation else None  # commit 뒤에는 세션이 닫혀 읽을 수 없다
        repo.replace_run(db, retail_series.id, as_of, data_date, C.INDICATOR_SPEC_VERSION, status, digest, cards, notices)
        db.commit()
    return {'status': status, 'asOfDate': as_of.isoformat(), 'dataDate': data_date.isoformat(),
            'cards': [c['indicator_key'] for c in cards],
            'leadValidation': lead_verdict}
