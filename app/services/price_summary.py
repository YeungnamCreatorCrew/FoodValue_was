"""예측 화면 문장. 배치에서 실행마다 한 번 만들어 price_insight.summary에 저장한다(요청 시점에는 LLM을 부르지 않는다).

- headline(예측가 요약)은 숫자를 정확히 보여야 해서 항상 고정 문장으로 만든다.
- detail(요인 요약)·categories(분류별 설명)는 Gemini가 다듬는다. 입력은 예측값과 SHAP 분류 합계·상위 요인뿐이다.
- Gemini 키가 없거나, 호출·JSON·검증(입력에 없는 숫자, 길이, 분류 불일치)에 실패하면 고정 문장을 쓴다. 배치는 실패시키지 않는다.
"""
import json
import re

from app.core.constants import GEMINI_MAX_RETRIES, GEMINI_TIMEOUT_SECONDS

PROMPT_VERSION = 'price-summary-v1'
MAX_SENTENCE = 120
CAUSAL_WORDS = ('때문', '원인', '탓', '덕분')  # SHAP은 인과가 아니므로 이런 표현이 있으면 고정 문장을 쓴다
MARKET_LABELS = {'RETAIL': '소매', 'WHOLESALE': '도매'}

_PROMPT = """너는 식자재 가격 예측 서비스의 설명 문장을 다듬는다. 아래 JSON은 XGBoost 모델의 7일 뒤 가격 예측과
변수 분류별 SHAP 기여(원)다. 이 정보만으로 한국어 존댓말 문장을 JSON으로 써라.

규칙:
- 출력 형식: {{"detail": "문장 1개", "categories": {{"분류코드": "문장 1~2개", ...}}}}
- categories의 키는 입력 categories의 category 값과 정확히 같아야 한다(추가·누락 금지).
- 각 값은 {max_len}자 이내.
- 숫자는 입력에 있는 값만 쓴다. 새 숫자·날짜·비율을 만들지 않는다. 숫자를 안 써도 된다.
- SHAP은 모델 예측에 대한 기여다. "때문에", "원인", "~해서 올랐다"처럼 인과를 단정하지 말고
  "가격을 높이는(낮추는) 방향으로 작용했습니다"처럼 쓴다.
- 입력에 없는 사건(태풍, 작황 등)을 지어내지 않는다.
- detail은 분류들이 어느 방향으로 작용했는지 한 문장으로 요약한다.

입력:
{payload}
"""


def _won(value):
    return f'{round(value):,}원'


def headline(name, market, current, forecast):
    change = forecast - current
    percent = abs(change) / current * 100 if current else 0
    subject = f'현재 {_won(current)}인 {name} {MARKET_LABELS.get(market, "")}가격은 7일 후 {_won(forecast)}으로'
    if change == 0:
        return f'{subject} 보합을 유지할 것으로 예측되었습니다.'
    amount = f'약 {percent:.1f}%' if round(percent, 1) >= .1 else f'{_won(abs(change))}'  # 0.0%로 보이는 작은 변화는 원으로 쓴다
    return f'{subject} {amount} {"낮아질" if change < 0 else "높아질"} 것으로 예측되었습니다.'


def template(categories):
    """고정 문장. categories: price_explanation.category_totals 결과"""
    if not categories:
        return {'detail': '이번 예측은 최근 가격을 기준으로 한 기준 모델을 사용해 변수별 영향은 제공하지 않습니다.',
                'categories': {}}
    down = [c['label'] for c in categories if c['direction'] == 'DOWN']
    up = [c['label'] for c in categories if c['direction'] == 'UP']
    parts = ([f'{"·".join(down)}{_topic(down[-1])} 하락 방향'] if down else []) + \
            ([f'{"·".join(up)}{_topic(up[-1])} 상승 방향'] if up else [])
    detail = f'이번 예측에서 {", ".join(parts)}으로 작용했습니다.' if parts else '이번 예측에서 뚜렷한 방향으로 작용한 요인 분류는 없습니다.'
    texts = {}
    for c in categories:
        if c['direction'] == 'NEUTRAL':
            texts[c['category']] = f'{c["label"]}의 SHAP 기여 합계는 중립입니다.'
        else:
            texts[c['category']] = (f'{c["label"]}{_topic(c["label"])} 이번 모델 예측에서 가격을 '
                                    f'{"낮추는" if c["direction"] == "DOWN" else "높이는"} 방향으로 작용했습니다.')
    return {'detail': detail, 'categories': texts}


def _topic(word):
    """받침에 따라 은/는"""
    code = ord(word[-1]) - 0xAC00
    return '은' if 0 <= code <= 11171 and code % 28 else '는'


def payload(name, market, current, forecast, categories, factors):
    return {'item': name, 'market': MARKET_LABELS.get(market, market), 'currentPrice': round(current),
            'forecastPrice7d': round(forecast), 'changePercent': round((forecast - current) / current * 100, 1),
            'categories': [{'category': c['category'], 'label': c['label'], 'direction': c['direction'],
                            'shapWon': c['contribution']} for c in categories],
            'topFactors': [{'label': f['label'], 'category': f['category'], 'direction': f['direction'],
                            'shapWon': f['contribution']} for f in factors[:5]]}


def _numbers(text):
    return {n.replace(',', '') for n in re.findall(r'\d[\d,]*(?:\.\d+)?', text)}


def _allowed(data):
    allowed = {'7'}

    def walk(value):
        if isinstance(value, bool):
            return
        if isinstance(value, (int, float)):
            for v in (value, abs(value)):
                allowed.update({str(v), f'{v:g}', str(round(v)), f'{v:.1f}'})
        elif isinstance(value, dict):
            for item in value.values():
                walk(item)
        elif isinstance(value, list):
            for item in value:
                walk(item)
        elif isinstance(value, str):
            allowed.update(_numbers(value))
    walk(data)
    return {a.lstrip('-') for a in allowed}


def validate(result, data):
    """Gemini 출력 검증. 통과하면 정리된 dict, 아니면 None"""
    if not isinstance(result, dict) or not isinstance(result.get('detail'), str) or not isinstance(result.get('categories'), dict):
        return None
    expected = {c['category'] for c in data['categories']}
    if set(result['categories']) != expected:
        return None
    texts = [result['detail'], *result['categories'].values()]
    if any(not isinstance(t, str) or not t.strip() or len(t) > MAX_SENTENCE for t in texts):
        return None
    if any(word in t for t in texts for word in CAUSAL_WORDS):
        return None
    allowed = _allowed(data)
    if any(not _numbers(t) <= allowed for t in texts):
        return None
    return {'detail': result['detail'].strip(), 'categories': {k: v.strip() for k, v in result['categories'].items()}}


def _call_gemini(prompt):
    from google import genai
    from google.genai import types

    from app.core.config import get_settings
    api_key, model = get_settings().require_gemini()
    client = genai.Client(api_key=api_key, http_options=types.HttpOptions(timeout=GEMINI_TIMEOUT_SECONDS * 1000))
    response = client.models.generate_content(model=model, contents=prompt,
                                              config=types.GenerateContentConfig(response_mime_type='application/json'))
    return response.text or '', model


def generate(name, market, current, forecast, categories, factors):
    """(summary, generator, model, prompt_version). 기준 모델 실행(categories 없음)은 LLM을 부르지 않는다."""
    summary = {'headline': headline(name, market, current, forecast)}
    fallback = template(categories)
    if categories:
        data = payload(name, market, current, forecast, categories, factors)
        prompt = _PROMPT.format(max_len=MAX_SENTENCE, payload=json.dumps(data, ensure_ascii=False))
        for _ in range(1 + GEMINI_MAX_RETRIES):
            try:
                text, model = _call_gemini(prompt)
                checked = validate(json.loads(text), data)
            except Exception:  # 키 없음·네트워크·JSON 오류 모두 고정 문장으로 대체한다. 원문은 남기지 않는다.
                checked, model = None, None
                if not _retryable():
                    break
            if checked:
                return {**summary, **checked}, 'GEMINI', model, PROMPT_VERSION
    return {**summary, **fallback}, 'TEMPLATE', None, PROMPT_VERSION


def _retryable():
    from app.core.config import get_settings
    settings = get_settings()
    return bool(settings.gemini_api_key and settings.gemini_model)

