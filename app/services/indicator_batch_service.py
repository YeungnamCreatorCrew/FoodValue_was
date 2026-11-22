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


def lead_card(db, series_id, retail: pd.Series, wholesale: pd.Series, as_of: date, force: bool):
    """검증이 PASS일 때만 카드. 반환: (카드 행 또는 None, 검증 행 또는 None)."""
    spec = C.INDICATOR_SPEC_VERSION
    validation = None if force else repo.validation_before(db, series_id, LEAD, spec, as_of)
    if validation is None or (as_of - validation.data_end).days > C.INDICATOR_REVALIDATE_DAYS:
        cut = pd.Timestamp(as_of)
        result = wholesale_lead.validate(retail[retail.index <= cut], wholesale[wholesale.index <= cut])
        stats = wholesale_lead.stats_for_storage(result)
        validation = repo.save_validation(db, series_id, LEAD, spec, result['verdict'], stats,
                                          result['period_start'], result['period_end'])
    if validation.verdict != 'PASS':
        return None, validation
    cut = pd.Timestamp(as_of)
    retail_w, wholesale_w = weekly_mean(retail[retail.index <= cut]), weekly_mean(wholesale[wholesale.index <= cut])
    latest = wholesale_lead.latest_changes(retail_w, wholesale_w)
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
        cards, validation = [], None
        position = position_card(db, retail_series.id, retail, wholesale, as_of, validate)
        if position:
            cards.append(position)
        season = seasonal_card(retail, as_of)
        if season:
            cards.append(season)
        if not wholesale.empty:
            lead, validation = lead_card(db, retail_series.id, retail, wholesale, as_of, validate)
            if lead:
                cards.append(lead)
            gap = gap_card(db, retail_series.id, retail, wholesale, as_of, validate)
            if gap:
                cards.append(gap)
        cards += [c for c in [stat_card(VOLATILITY, price_stats.volatility_fact(retail, as_of), None,
                                        '최근 4주 가격이 얼마나 출렁였는지, 최근 1년과 비교합니다.')] if c]
        digest = summary.build(name, [{'key': c['indicator_key'], 'state': c['state']} for c in cards])
        status = 'SUCCESS' if cards else 'INSUFFICIENT_DATA'
        lead_verdict = validation.verdict if validation else None  # commit 뒤에는 세션이 닫혀 읽을 수 없다
        repo.replace_run(db, retail_series.id, as_of, data_date, C.INDICATOR_SPEC_VERSION, status, digest, cards)
        db.commit()
    return {'status': status, 'asOfDate': as_of.isoformat(), 'dataDate': data_date.isoformat(),
            'cards': [c['indicator_key'] for c in cards],
            'leadValidation': lead_verdict}
