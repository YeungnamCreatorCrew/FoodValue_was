"""7일 뒤 예측의 변수별 기여(TreeSHAP)를 원 단위로 만든다.

- XGBoost의 pred_contribs로 특징별 기여와 기대값(bias)을 구한다. 합은 모델이 낸 변화율과 같다(검증함).
- XGBOOST_WEIGHTED는 변화율 = (1-Σw)·가격모델 + Σ w_b·전문가_b 의 선형 결합이라 기여도 같은 가중치로 합친다.
- 가격 = 현재가 × (1 + damping × 변화율) 이므로 원 단위 기여 = 현재가 × damping × 기여(변화율). 합이 그대로 보존된다.
- 기준 모델(LAST_PRICE·MEAN_7)로 공개되는 실행은 설명할 모델이 없어 만들지 않는다.
SHAP은 모델 예측에 대한 기여이며 가격에 대한 인과적 영향이 아니다.
"""
import math
from dataclasses import dataclass, field

METHOD = 'XGBOOST_TREE_SHAP'
HISTORY_DAYS = 90
TOLERANCE = 1e-4

# 화면 분류: PRICE(자기 가격·상대 시장 가격), WEATHER, CALENDAR(요일·계절·공휴일·명절·과거 같은 시기), MACRO(생산량·환율)
# scale: 저장된 모델 입력값에 곱해 화면 단위로 바꾼다(분율 → %).
FEATURES = {
    'current': ('현재 가격', '원', 'PRICE', 1),
    'lag1': ('1일 전 가격', '원', 'PRICE', 1),
    'lag7': ('7일 전 가격', '원', 'PRICE', 1),
    'lag14': ('14일 전 가격', '원', 'PRICE', 1),
    'lag28': ('28일 전 가격', '원', 'PRICE', 1),
    'mean7': ('최근 7일 평균 가격', '원', 'PRICE', 1),
    'mean28': ('최근 28일 평균 가격', '원', 'PRICE', 1),
    'change7': ('최근 7일 가격 변화율', '%', 'PRICE', 100),
    'volatility7': ('최근 7일 가격 변동성', '원', 'PRICE', 1),
    'priceAge': ('최근 가격 경과일', '일', 'PRICE', 1),
    'targetWeekday': ('예측 대상일 요일', '', 'CALENDAR', 1),
    'targetSeasonSin': ('예측 대상일 시기(sin)', '', 'CALENDAR', 1),
    'targetSeasonCos': ('예측 대상일 시기(cos)', '', 'CALENDAR', 1),
    'counterLast': ('{counter} 가격', '원', 'PRICE', 1),
    'targetCounterRatio': ('{counter} 대비 현재 가격 비율', '배', 'PRICE', 1),
    'counterChange7': ('{counter} 가격 7일 변화율', '%', 'PRICE', 100),
    'counterChange28': ('{counter} 가격 28일 변화율', '%', 'PRICE', 100),
    'counterAge': ('{counter} 가격 경과일', '일', 'PRICE', 1),
    'tempMean7': ('주산지 최근 7일 평균기온', '℃', 'WEATHER', 1),
    'tempMax7': ('주산지 최근 7일 최고기온', '℃', 'WEATHER', 1),
    'tempMin7': ('주산지 최근 7일 최저기온', '℃', 'WEATHER', 1),
    'rainSum7': ('주산지 최근 7일 강수량', 'mm', 'WEATHER', 1),
    'rainSum28': ('주산지 최근 28일 강수량', 'mm', 'WEATHER', 1),
    'humidityMean7': ('주산지 최근 7일 평균습도', '%', 'WEATHER', 1),
    'sunshineSum7': ('주산지 최근 7일 일조시간', '시간', 'WEATHER', 1),
    'natTempMean7': ('전국 최근 7일 평균기온', '℃', 'WEATHER', 1),
    'natRainSum28': ('전국 최근 28일 강수량', 'mm', 'WEATHER', 1),
    'natHeatIndex7': ('최근 7일 폭염 지수', '', 'WEATHER', 1),
    'natHeatIndex28': ('최근 28일 폭염 지수', '', 'WEATHER', 1),
    'natHeavyRainIndex28': ('최근 28일 호우 지수', '', 'WEATHER', 1),
    'natColdIndex28': ('최근 28일 한파 지수', '', 'WEATHER', 1),
    'targetIsHoliday': ('예측 대상일 공휴일 여부', '', 'CALENDAR', 1),
    'daysToMajorHoliday': ('다음 명절까지 남은 날', '일', 'CALENDAR', 1),
    'daysFromMajorHoliday': ('지난 명절 이후 지난 날', '일', 'CALENDAR', 1),
    'targetInEventWindow': ('예측 대상일 명절 영향 기간 여부', '', 'CALENDAR', 1),
    'eventPressure': ('과거 명절 기간 가격 압력', '', 'CALENDAR', 1),
    'seasonalChange': ('과거 같은 시기 7일 변동률', '%', 'CALENDAR', 100),
    'productionYoY': ('연간 생산량 전년 대비', '%', 'MACRO', 100),
    'usdKrwChange7': ('원/달러 환율 7일 변화율', '%', 'MACRO', 100),
    'usdKrwChange28': ('원/달러 환율 28일 변화율', '%', 'MACRO', 100),
}
# 따로 보면 의미가 없는 특징 쌍은 화면에서 하나로 합친다(SHAP은 더해도 된다). 값·추이는 보여주지 않는다.
MERGED = {'targetSeason': (('targetSeasonSin', 'targetSeasonCos'), '예측 대상일의 계절', 'CALENDAR')}
CATEGORY_LABELS = {'PRICE': '최근 가격 흐름', 'WEATHER': '기상 조건', 'CALENDAR': '달력·계절', 'MACRO': '생산량·환율'}
COUNTER_LABELS = {'RETAIL': '도매', 'WHOLESALE': '소매'}  # 예측 계열의 상대 시장


class ExplanationError(Exception):
    pass


@dataclass
class Explanation:
    """원 단위 설명. contributions·values의 키는 모델 특징 이름. history: 특징 → [(날짜, 모델 입력값)]."""
    horizon: int
    current_price: float
    damping: float
    base_price: float
    predicted_price: int
    contributions: dict[str, float]
    values: dict[str, float | None]
    history: dict[str, list[tuple]] = field(default_factory=dict)
    method: str = METHOD


def clean(value):
    """NaN·무한대·numpy 수를 JSON·DB에 넣을 수 있는 float 또는 None으로 바꾼다."""
    if value is None:
        return None
    value = float(value)
    return value if math.isfinite(value) else None


def contributions(estimator, row, names):
    """특징별 기여(변화율 단위)와 기대값. 합이 모델 예측과 다르면 실패한다."""
    if len(row) != len(names):
        raise ExplanationError('특징 이름과 입력 길이가 다릅니다')
    from xgboost import DMatrix
    matrix = DMatrix([[math.nan if v is None else float(v) for v in row]], missing=math.nan)
    contrib = estimator.get_booster().predict(matrix, pred_contribs=True)[0]
    predicted = float(estimator.predict([row])[0])
    if abs(float(contrib.sum()) - predicted) > TOLERANCE:
        raise ExplanationError('SHAP 합이 모델 예측과 다릅니다')
    return dict(zip(names, (float(v) for v in contrib[:-1]))), float(contrib[-1])


def combine(parts):
    """[(가중치, 기여, 기대값)]의 선형 결합"""
    total, bias = {}, 0.0
    for weight, contrib, base in parts:
        bias += weight * base
        for name, value in contrib.items():
            total[name] = total.get(name, 0.0) + weight * value
    return total, bias


def to_won(change_contrib, bias, current, damping, predicted_price, values, horizon, history=None):
    scale = current * damping
    return Explanation(horizon=horizon, current_price=current, damping=damping,
                       base_price=current * (1 + damping * bias), predicted_price=predicted_price,
                       contributions={name: value * scale for name, value in change_contrib.items()},
                       values={name: clean(value) for name, value in values.items()}, history=history or {})


def label(feature, market):
    text = FEATURES.get(feature, (feature,))[0]
    return text.format(counter=COUNTER_LABELS.get(market, '상대 시장'))


def display_value(feature, value):
    if value is None or feature not in FEATURES:
        return value
    return round(value * FEATURES[feature][3], 4)


def display_factors(rows, market):
    """DB 행(feature, value, contribution) → 화면 요인 목록. 계절 sin·cos는 합치고 기여 절댓값 순으로 정렬한다."""
    by_name = {row['feature']: row for row in rows}
    factors = []
    used = set()
    for key, (members, text, category) in MERGED.items():
        present = [by_name[m] for m in members if m in by_name]
        if present:
            used.update(m for m in members)
            total = sum(float(r['contribution']) for r in present)
            factors.append({'id': key, 'label': text, 'category': category, 'value': None, 'unit': '',
                            'contribution': round(total, 1), 'direction': direction(total), 'hasHistory': False})
    for name, row in by_name.items():
        if name in used:
            continue
        meta = FEATURES.get(name, (name, '', 'PRICE', 1))
        contribution = float(row['contribution'])
        factors.append({'id': name, 'label': label(name, market), 'category': meta[2],
                        'value': display_value(name, row['value']), 'unit': meta[1],
                        'contribution': round(contribution, 1), 'direction': direction(contribution),
                        'hasHistory': True})
    factors.sort(key=lambda f: (-abs(f['contribution']), f['id']))
    return factors


def direction(value):
    return 'UP' if value > 0 else 'DOWN' if value < 0 else 'NEUTRAL'


def category_totals(factors):
    totals = {}
    for factor in factors:
        totals[factor['category']] = totals.get(factor['category'], 0.0) + factor['contribution']
    return [{'category': c, 'label': CATEGORY_LABELS[c], 'contribution': round(v, 1), 'direction': direction(round(v, 1))}
            for c, v in sorted(totals.items(), key=lambda kv: -abs(kv[1])) if c in CATEGORY_LABELS]
