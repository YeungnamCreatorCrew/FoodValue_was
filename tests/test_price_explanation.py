import json
import math
import random

import pytest

from app.services import price_explanation as explain
from app.services import price_prediction as model
from app.services import price_summary
from app.services.exogenous import COUNTERPART_FEATURES, Covariates
from app.services.price_batch_service import explanation_rows
from app.services.weighting import Weights
from tests.test_exogenous import leading_series, random_fx


@pytest.fixture(scope='module')
def explained():
    pytest.importorskip('xgboost')
    retail, wholesale = leading_series()
    covariates = Covariates(counterpart=wholesale, fx=random_fx([d for d, _ in retail]))
    plain = model.predict(retail, retail[-1][0], covariates)
    return plain, model.predict(retail, retail[-1][0], covariates, explain=True)


def test_explain_does_not_change_forecast(explained):
    plain, result = explained
    assert (result.prices, result.lower, result.upper, result.model) == (plain.prices, plain.lower, plain.upper, plain.model)
    assert plain.explanation is None


def test_shap_reconciles_with_published_price(explained):
    _, result = explained
    e = result.explanation
    assert result.model in model.BASELINES or e is not None
    assert e.method == explain.METHOD and e.horizon == 7
    # 기대값 + 기여 합 = 반올림 전 예측가. 공개 예측가와는 반올림 차이만 있다.
    assert abs(e.base_price + sum(e.contributions.values()) - result.prices[-1]) < 1
    assert e.predicted_price == result.prices[-1]
    assert set(COUNTERPART_FEATURES) <= set(e.contributions)
    assert e.values['current'] == float(dict(leading_series()[0])[max(dict(leading_series()[0]))])


def test_history_is_point_in_time_and_json_safe(explained):
    _, result = explained
    e = result.explanation
    history = e.history['current']
    assert 0 < len(history) <= explain.HISTORY_DAYS
    assert history[-1][0] == leading_series()[0][-1][0].isoformat()
    rows = explanation_rows(e)
    json.dumps(rows, allow_nan=False)  # NaN이 남아 있으면 JSONB 저장이 실패한다


def test_weighted_combination_matches_published_change():
    xgb = pytest.importorskip('xgboost')
    rng = random.Random(3)
    X = [[rng.random() for _ in range(3)] for _ in range(200)]
    y = [row[0] * .1 - row[1] * .05 for row in X]
    models = {}
    for name, cols in (('XGBOOST', [0]), ('EXPERT_A', [0, 1]), ('EXPERT_B', [0, 2])):
        estimator = xgb.XGBRegressor(n_estimators=20, max_depth=2)
        estimator.fit([[row[c] for c in cols] for row in X], y)
        models[name] = (estimator, cols)
    names = ['p', 'a', 'b']
    row = [.4, .7, .2]
    parts = {n: explain.contributions(est, [row[c] for c in cols], [names[c] for c in cols]) for n, (est, cols) in models.items()}
    weights = Weights({'A': .6, 'B': .3})
    predicted = {n: float(est.predict([[row[c] for c in cols]])[0]) for n, (est, cols) in models.items()}
    change = weights.combine(predicted['XGBOOST'], {'A': predicted['EXPERT_A'], 'B': predicted['EXPERT_B']})
    contrib, bias = explain.combine([(.1, *parts['XGBOOST']), (.6, *parts['EXPERT_A']), (.3, *parts['EXPERT_B'])])
    assert abs(sum(contrib.values()) + bias - change) < 1e-5
    won = explain.to_won(contrib, bias, 2000, 1.0, 0, {}, 7)
    assert abs(won.base_price + sum(won.contributions.values()) - 2000 * (1 + change)) < 1e-3


def test_display_merges_season_and_sorts_by_impact():
    rows = [{'feature': 'targetSeasonSin', 'value': .5, 'contribution': -10},
            {'feature': 'targetSeasonCos', 'value': .1, 'contribution': -5},
            {'feature': 'change7', 'value': -.034, 'contribution': 20},
            {'feature': 'counterLast', 'value': 2000, 'contribution': 3},
            {'feature': 'tempMean7', 'value': None, 'contribution': 0}]
    factors = explain.display_factors(rows, 'RETAIL')
    assert [f['id'] for f in factors] == ['change7', 'targetSeason', 'counterLast', 'tempMean7']
    assert factors[0]['value'] == -3.4 and factors[0]['unit'] == '%' and factors[0]['direction'] == 'UP'
    assert factors[1] == {'id': 'targetSeason', 'label': '예측 대상일의 계절', 'category': 'CALENDAR', 'value': None,
                          'unit': '', 'contribution': -15.0, 'direction': 'DOWN', 'hasHistory': False}
    assert factors[2]['label'] == '도매 가격'
    assert explain.display_factors(rows, 'WHOLESALE')[2]['label'] == '소매 가격'
    assert factors[3]['direction'] == 'NEUTRAL'
    totals = explain.category_totals(factors)
    assert [(c['category'], c['direction']) for c in totals] == [('PRICE', 'UP'), ('CALENDAR', 'DOWN'), ('WEATHER', 'NEUTRAL')]


CATEGORIES = [{'category': 'WEATHER', 'label': '기상 조건', 'contribution': -31.1, 'direction': 'DOWN'},
              {'category': 'PRICE', 'label': '최근 가격 흐름', 'contribution': 45.8, 'direction': 'UP'}]


def test_template_sentences(monkeypatch):
    def offline(prompt):
        raise ConnectionError
    monkeypatch.setattr(price_summary, '_call_gemini', offline)
    summary, generator, llm, version = price_summary.generate('대파', 'RETAIL', 3004, 2903, CATEGORIES, [])
    assert summary['headline'] == '현재 3,004원인 대파 소매가격은 7일 후 2,903원으로 약 3.4% 낮아질 것으로 예측되었습니다.'
    assert (generator, llm, version) == ('TEMPLATE', None, price_summary.PROMPT_VERSION)
    template = price_summary.template(CATEGORIES)
    assert template['detail'] == '이번 예측에서 기상 조건은 하락 방향, 최근 가격 흐름은 상승 방향으로 작용했습니다.'
    assert template['categories']['WEATHER'] == '기상 조건은 이번 모델 예측에서 가격을 낮추는 방향으로 작용했습니다.'
    assert price_summary.template([])['categories'] == {}


@pytest.fixture
def no_gemini_key(monkeypatch):
    """키가 있는 것처럼 Gemini 경로를 연다(실제 호출은 각 테스트가 가짜로 바꾼다)."""
    monkeypatch.setattr(price_summary, '_llm_enabled', lambda: True)


def test_gemini_text_is_used_when_valid(monkeypatch, no_gemini_key):
    answer = {'detail': '기상 조건은 가격을 낮추는 쪽, 최근 가격 흐름은 높이는 쪽으로 작용했습니다.',
              'categories': {'WEATHER': '최근 기상 조건이 예측가를 약 31.1원 낮추는 방향으로 작용했습니다.',
                             'PRICE': '최근 가격 흐름은 예측가를 높이는 방향으로 작용했습니다.'}}
    monkeypatch.setattr(price_summary, '_call_gemini', lambda prompt: (json.dumps(answer, ensure_ascii=False), 'gemini-test'))
    summary, generator, llm, _ = price_summary.generate('대파', 'RETAIL', 3004, 2903, CATEGORIES, [])
    assert (generator, llm) == ('GEMINI', 'gemini-test')
    assert summary['categories'] == answer['categories'] and summary['headline'].startswith('현재 3,004원')


@pytest.mark.parametrize('answer', [
    {'detail': '태풍 3개가 영향을 주어 15% 오를 것입니다.', 'categories': {'WEATHER': '낮춤', 'PRICE': '높임'}},  # 지어낸 숫자
    {'detail': '요약', 'categories': {'WEATHER': '낮춤'}},  # 분류 누락
    {'detail': '가' * 200, 'categories': {'WEATHER': '낮춤', 'PRICE': '높임'}},  # 너무 김
    {'detail': '기온 때문에 내렸습니다.', 'categories': {'WEATHER': '낮춤', 'PRICE': '높임'}},  # 인과 단정
    {'detail': '대파 가격은 7일 뒤 2903원으로 3.4% 하락합니다.', 'categories': {'WEATHER': '낮춤', 'PRICE': '높임'}},  # headline 반복
    'not json',
])
def test_invalid_gemini_output_falls_back_to_template(monkeypatch, no_gemini_key, answer):
    text = answer if isinstance(answer, str) else json.dumps(answer, ensure_ascii=False)
    calls = []
    monkeypatch.setattr(price_summary, '_call_gemini', lambda prompt: (calls.append(1), (text, 'gemini-test'))[1])
    summary, generator, llm, _ = price_summary.generate('대파', 'RETAIL', 3004, 2903, CATEGORIES, [])
    assert (generator, llm) == ('TEMPLATE', None)
    assert summary['categories'] == price_summary.template(CATEGORIES)['categories']
    assert len(calls) == 1  # 무료 플랜 한도 때문에 재시도하지 않는다


def test_missing_key_and_baseline_never_call_gemini(monkeypatch):
    def fail(prompt):
        raise RuntimeError('GEMINI_API_KEY 없음')
    monkeypatch.setattr(price_summary, '_call_gemini', fail)
    monkeypatch.setattr(price_summary, '_llm_enabled', lambda: False)
    assert price_summary.generate('대파', 'RETAIL', 3004, 2903, CATEGORIES, [])[1] == 'TEMPLATE'
    called = []
    monkeypatch.setattr(price_summary, '_call_gemini', lambda prompt: called.append(1))
    summary, generator, _, _ = price_summary.generate('대파', 'RETAIL', 3004, 3004, [], [])
    assert not called and generator == 'TEMPLATE' and '보합' in summary['headline']


def test_clean_handles_nan():
    assert explain.clean(math.nan) is None and explain.clean(float('inf')) is None and explain.clean(1) == 1.0


def test_tiny_change_is_written_in_won():
    assert price_summary.headline('대파', 'WHOLESALE', 2707, 2706).endswith('2,706원으로 1원 낮아질 것으로 예측되었습니다.')


def test_quota_error_stops_further_calls_for_this_batch(monkeypatch):
    monkeypatch.setattr(price_summary, '_quota_exhausted', False)
    monkeypatch.delenv(price_summary.LLM_ENV, raising=False)
    from app.core.config import get_settings
    settings = get_settings()
    monkeypatch.setattr(settings, 'gemini_api_key', 'test-key')
    monkeypatch.setattr(settings, 'gemini_model', 'gemini-test')
    calls = []

    class Quota(Exception):
        code = 429

    def quota(prompt):
        calls.append(1)
        raise Quota()
    monkeypatch.setattr(price_summary, '_call_gemini', quota)
    for _ in range(3):  # 품목 3개 배치
        assert price_summary.generate('대파', 'RETAIL', 3004, 2903, CATEGORIES, [])[1] == 'TEMPLATE'
    assert len(calls) == 1


def test_llm_can_be_turned_off_by_env(monkeypatch):
    monkeypatch.setattr(price_summary, '_quota_exhausted', False)
    monkeypatch.setenv(price_summary.LLM_ENV, '0')
    assert price_summary._llm_enabled() is False
