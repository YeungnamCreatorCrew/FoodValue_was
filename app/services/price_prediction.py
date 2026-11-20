"""시점별 직접 예측. 원천 결측은 타깃으로 학습하지 않고 미래 자료는 참조하지 않는다.

후보: LAST_PRICE, MEAN_7(기준 모델), XGBOOST(가격 특징만), XGBOOST_EXT(가격 + 외부 원천 특징 전부),
XGBOOST_WEIGHTED(가격 모델 + 외부변수 묶음별 전문가 모델의 가중 결합, 가중치는 weighting 참고).
외부 원천은 시간순 백테스트에서 가격만 쓴 모델과 같은 기준으로 비교해 이길 때만 선택된다.
"""
import json
import math
import os
from dataclasses import dataclass
from datetime import date, timedelta
from statistics import mean

from app.services import price_explanation, weighting
from app.services.exogenous import GROUP_FEATURES, Covariates, ExogenousFeatures

HORIZON = 7
MIN_TRAIN = 120
MAX_BACKTEST_DAYS = 240
MAX_FORWARD_FILL_DAYS = 7
MODEL_VERSION = 'direct-xgb-v5-huber'
REFIT_DAYS = 7
EXPERT_REFIT_DAYS = 14  # 묶음별 전문가 모델은 수가 많아 2주마다 재학습한다
MAX_PRICE = 2**31 - 1


PRICE_FEATURES = ['current', 'lag1', 'lag7', 'lag14', 'lag28', 'mean7', 'mean28', 'change7', 'volatility7',
                  'targetWeekday', 'targetSeasonSin', 'targetSeasonCos', 'priceAge']
BASELINES = ['LAST_PRICE', 'MEAN_7']


class InsufficientDataError(Exception):
    pass


class ModelDependencyError(Exception):
    """예측 의존성 문제. 메시지에 비밀값이 없어 그대로 출력해도 된다."""


@dataclass
class Prediction:
    model: str
    quality: str
    prices: list[int]
    lower: list[int | None]
    upper: list[int | None]
    metrics: dict
    explanation: object = None  # price_explanation.Explanation (explain=True이고 학습 모델이 선택됐을 때만)


def normalize(observations: list[tuple[date, int]], base_date: date):
    points = sorted((d, p) for d, p in observations if d <= base_date)
    if not points or len({d for d, _ in points}) != len(points):
        raise InsufficientDataError('가격이 없거나 날짜가 중복됩니다')
    if any(not isinstance(p, int) or isinstance(p, bool) or p <= 0 or p > MAX_PRICE for _, p in points):
        raise ValueError('가격은 양의 INT 값이어야 합니다')
    if (base_date - points[-1][0]).days > MAX_FORWARD_FILL_DAYS:
        raise InsufficientDataError('최신 가격이 7일 이상 지연되었습니다')
    # 최대 5년 자료만 사용해 실행 시간을 제한한다.
    start = max(points[0][0], base_date - timedelta(days=1825))
    actual = dict(points)
    days, values, observed, ages = [], [], [], []
    last_day, last_value = None, None
    for offset in range((base_date - start).days + 1):
        day = start + timedelta(days=offset)
        if day in actual:
            last_day, last_value = day, actual[day]
        age = (day - last_day).days if last_day else MAX_FORWARD_FILL_DAYS + 1
        days.append(day)
        values.append(float(last_value) if last_value and age <= MAX_FORWARD_FILL_DAYS else None)
        observed.append(day in actual)
        ages.append(age)
    return days, values, observed, ages


def features(days, values, ages, origin, horizon):
    if origin < 28 or any(value is None for value in values[origin-28:origin+1]):
        return None
    current = values[origin]
    recent = values[origin-6:origin+1]
    long = values[origin-27:origin+1]
    target = days[origin] + timedelta(days=horizon)
    season = 2 * math.pi * target.timetuple().tm_yday / 365.25
    return [current, values[origin-1], values[origin-7], values[origin-14], values[origin-28],
            mean(recent), mean(long), (current / values[origin-7] - 1),
            math.sqrt(mean((v-mean(recent))**2 for v in recent)),
            target.weekday(), math.sin(season), math.cos(season), ages[origin]]


def _training(vector, values, observed, cutoff, horizon):
    """정답은 시작일 가격 대비 변화율. 학습 범위를 벗어난 가격 수준에서도 예측이 한쪽으로 묶이지 않게 한다."""
    inputs, targets = [], []
    for origin in range(28, cutoff - horizon + 1):
        target = origin + horizon
        if observed[target]:
            row = vector(origin, horizon)
            if row is not None:
                inputs.append(row)
                targets.append(values[target] / values[origin] - 1)
    return inputs, targets


# 실험용: XGBoost 계열이 예측한 변화율 중 이 비율만 반영한다(1 = 그대로, 0.5 = 절반). 직전가 쪽으로 당겨 과한 예측을 줄인다.
DAMPING_ENV = 'FOODVALUE_CHANGE_DAMPING'


def damping():
    return float(os.getenv(DAMPING_ENV) or 1)


def _from_change(current, change):
    return _price(current * (1 + damping() * float(change)))


def training_data(days, values, observed, ages, cutoff, horizon):
    return _training(lambda o, h: features(days, values, ages, o, h), values, observed, cutoff, horizon)


def check_dependencies():
    """예측 전에 XGBoost를 한 번 불러 본다. 실패하면 ModelDependencyError(원인 안내 메시지 포함)."""
    _model()


# 튜닝할 수 있는 XGBoost 하이퍼파라미터의 기본값. 값을 바꾸면 운영 배치·백테스트에 모두 적용된다.
# v4: 대파 실데이터 튜닝(app/price_tuning.py) 결과, 얕은 트리 + 강한 규제가 평가 구간에서 가장 덜 과적합했다. model_comparison/xgboost/README_MODEL.md 참고.
# (v3까지: n_estimators=80, max_depth=3, min_child_weight=1, reg_lambda=1)
# v5: 손실 함수를 제곱오차 → Pseudo-Huber(huber_slope 0.02 = 변화율 2%p)로 바꿨다. 가끔 튀는 가격 변화에 덜 끌려가
#     계절 전체에서 직전가 대비 개선율이 6.6% → 8.4%로 올랐다. model_comparison/xgboost/README_MODEL.md 참고.
XGB_PARAMS = {'n_estimators': 60, 'max_depth': 2, 'learning_rate': .05, 'subsample': 1, 'colsample_bytree': 1,
              'min_child_weight': 10, 'reg_lambda': 10, 'objective': 'reg:pseudohubererror', 'huber_slope': .02}
# 튜닝 실험용: 이 환경변수에 JSON을 넣으면 위 기본값을 덮어쓴다(예: {"n_estimators": 200}). 백테스트 병렬 작업에도 전달된다.
XGB_PARAMS_ENV = 'FOODVALUE_XGB_PARAMS'
# 기본값 밖에서 더 받을 수 있는 값(현재 없음)
EXTRA_PARAMS = set()


def xgb_params():
    raw = os.getenv(XGB_PARAMS_ENV)
    if not raw:
        return dict(XGB_PARAMS)
    override = json.loads(raw)
    unknown = set(override) - set(XGB_PARAMS) - EXTRA_PARAMS
    if unknown:
        raise ValueError(f'{XGB_PARAMS_ENV}에 튜닝 대상이 아닌 값이 있습니다: {sorted(unknown)}')
    return {**XGB_PARAMS, **override}


def _model():
    try:
        from xgboost import XGBRegressor
    except ImportError:
        raise ModelDependencyError('예측 배치에는 uv sync --extra prices가 필요합니다') from None
    except Exception as error:  # 설치는 됐지만 네이티브 라이브러리를 못 불러온 경우(XGBoostError)
        raise ModelDependencyError('xgboost 라이브러리를 불러오지 못했습니다. macOS는 brew install libomp가 필요합니다 '
                                   f'({type(error).__name__})') from None
    return XGBRegressor(**xgb_params(), tree_method='hist', n_jobs=1, random_state=42)


def _score(records):
    if not records:
        return None
    return {'mae': mean(abs(y-p) for y,p in records),
            'mape': mean(abs(y-p)/y*100 for y,p in records), 'samples':len(records)}


def _quantile(values, probability):
    ordered = sorted(values)
    return ordered[min(len(ordered)-1, max(0, math.ceil((len(ordered)+1)*probability)-1))]


def _price(value):
    if not math.isfinite(value):
        raise ValueError('모델이 유한하지 않은 값을 반환했습니다')
    return min(MAX_PRICE, max(1, round(value)))


def _better(candidate, baseline):
    return candidate['mape'] < baseline['mape']*.99 and candidate['mae'] <= baseline['mae']


def _model_names(name, exogenous, experts):
    """모델별 입력 특징 이름. vector()가 만드는 순서와 같다."""
    if name == 'XGBOOST':
        return list(PRICE_FEATURES)
    if name == 'XGBOOST_EXT':
        return PRICE_FEATURES + exogenous.names
    block = next(b for b, n in experts.items() if n == name)
    return PRICE_FEATURES + [f for group in exogenous.groups if group in exogenous.blocks[block]
                             for f in GROUP_FEATURES[group]]


def _explain(estimators, selected, experts, final_weights, exogenous, vector, days, values, ages, last, change, guess):
    """공개 예측(7일 뒤)의 SHAP 기여와 최근 90일 특징값. 예측에 쓴 모델을 그대로 설명한다."""
    parts = {}
    for name, estimator in estimators.items():
        parts[name] = price_explanation.contributions(estimator, vector(name, last, HORIZON),
                                                      _model_names(name, exogenous, experts))
    if selected == 'XGBOOST_WEIGHTED':
        weights = {b: final_weights.values.get(b, 0.0) for b in experts}
        rest = 1 - sum(weights.values())
        combined = [(rest, *parts['XGBOOST'])] + [(weights[b], *parts[n]) for b, n in experts.items()]
        contrib, bias = price_explanation.combine(combined)
    else:
        contrib, bias = parts[selected]
    if abs(sum(contrib.values()) + bias - change) > price_explanation.TOLERANCE:
        raise price_explanation.ExplanationError('결합한 SHAP 합이 공개 변화율과 다릅니다')
    names = PRICE_FEATURES + (exogenous.names if exogenous else [])

    def full(origin):
        row = features(days, values, ages, origin, HORIZON)
        if row is None:
            return None
        return dict(zip(names, row + (exogenous.vector(origin, HORIZON) if exogenous and exogenous.names else [])))

    now = full(last)
    history = {name: [] for name in contrib}
    for origin in range(max(0, last - price_explanation.HISTORY_DAYS + 1), last + 1):
        row = full(origin)
        if row is None:
            continue
        for name in contrib:
            history[name].append((days[origin].isoformat(), price_explanation.clean(row.get(name))))
    return price_explanation.to_won(contrib, bias, values[last], damping(), guess,
                                    {name: now.get(name) for name in contrib}, HORIZON, history)


def predict(observations, base_date, covariates: Covariates | None = None, explain: bool = False):
    """explain=True면 7일 뒤 예측의 변수별 기여(SHAP)와 최근 90일 특징값을 함께 만든다. 예측값은 같다."""
    days, values, observed, ages = normalize(observations, base_date)
    last = len(days)-1
    if features(days, values, ages, last, 1) is None:
        raise InsufficientDataError('연속된 최근 29일 입력이 필요합니다')
    exogenous = ExogenousFeatures(days, values, covariates) if covariates and not covariates.empty() else None
    external = bool(exogenous and exogenous.names)
    learners = ['XGBOOST'] + (['XGBOOST_EXT', 'XGBOOST_WEIGHTED'] if external else [])
    candidates = BASELINES + learners
    blocks = list(exogenous.blocks) if external else []
    # 묶음별 전문가 모델: 가격 특징 + 그 묶음의 외부 특징. 묶음이 하나뿐이면 XGBOOST_EXT와 입력이 같아 그대로 쓴다.
    experts = {block: 'XGBOOST_EXT' if len(blocks) == 1 else f'EXPERT_{block}' for block in blocks}
    fitted_names = ['XGBOOST'] + (['XGBOOST_EXT'] if external else []) + \
        [name for name in experts.values() if name != 'XGBOOST_EXT']
    refit_every = {name: EXPERT_REFIT_DAYS if name.startswith('EXPERT_') else REFIT_DAYS for name in fitted_names}
    cache = {}

    def vector(name, origin, horizon):
        key = (name, origin, horizon)
        if key not in cache:
            row = features(days, values, ages, origin, horizon)
            if row is not None and name == 'XGBOOST_EXT':
                row = row + exogenous.vector(origin, horizon)
            elif row is not None and name.startswith('EXPERT_'):
                row = row + exogenous.group_vector(origin, horizon, exogenous.blocks[name[len('EXPERT_'):]])
            cache[key] = row
        return cache[key]

    def fit(name, cutoff, horizon):
        inputs, targets = _training(lambda o, h: vector(name, o, h), values, observed, cutoff, horizon)
        if len(targets) < MIN_TRAIN:
            return None
        estimator = _model()
        estimator.fit(inputs, targets)
        return estimator

    def baseline_guess(name, origin):
        return _price(values[origin] if name == 'LAST_PRICE' else mean(values[origin-6:origin+1]))

    # 가중치는 예측 시작일까지 정답이 확인된 과거 예측 오차로만 정한다. 7일마다 다시 고른다.
    history = []
    weight_state = {}

    def weights_at(origin):
        if 'at' not in weight_state or origin - weight_state['at'] >= REFIT_DAYS:
            weight_state.update(at=origin, weights=weighting.choose([s for s in history if s[1] <= origin], blocks))
        return weight_state['weights']

    # 시간순으로 선택 / 오차 보정 / 최종 평가를 분리한다. 각 경계에 7일 간격을 둔다.
    origins = [i for i in range(28, last-6) if features(days, values, ages, i, 1) is not None]
    origins = origins[-MAX_BACKTEST_DAYS:]
    if len(origins) < 200:
        raise InsufficientDataError('모델 선택·구간 보정·평가를 위한 과거 자료가 부족합니다')
    cut1 = len(origins)//2
    cut2 = cut1 + (len(origins)-cut1)//2
    select_origins = origins[:cut1]
    calibrate_origins = [i for i in origins[cut1:cut2] if i > select_origins[-1]+7]
    evaluate_origins = [i for i in origins[cut2:] if calibrate_origins and i > calibrate_origins[-1]+7]
    if len(calibrate_origins) < 30 or len(evaluate_origins) < 14:
        raise InsufficientDataError('구간 보정·최종 평가 자료가 부족합니다')
    groups = [select_origins, calibrate_origins, evaluate_origins]
    scores = [{name: [] for name in candidates} for _ in groups]
    residuals = [[] for _ in range(HORIZON)]
    evaluation_predictions = [[] for _ in range(HORIZON)]
    evaluation_weights = {block: [] for block in blocks}
    models, fitted_at = {}, {}
    selected = baseline = None
    for group_index, group in enumerate(groups):
        for origin in group:
            for horizon in range(1, HORIZON+1):
                target = origin+horizon
                if not observed[target]:
                    continue  # 결측 보정값을 정답으로 삼지 않는다.
                guesses = {name: baseline_guess(name, origin) for name in BASELINES}
                changes = {}
                for name in fitted_names:
                    key = (name, horizon)
                    if key not in fitted_at or origin-fitted_at[key] >= refit_every[name]:
                        # 평가 시점까지 정답이 확인된 표본만으로 주기적으로 재학습한다.
                        estimator = fit(name, origin, horizon)
                        if estimator is None:
                            break
                        models[key], fitted_at[key] = estimator, origin
                    changes[name] = float(models[key].predict([vector(name, origin, horizon)])[0])
                else:
                    guesses['XGBOOST'] = _from_change(values[origin], changes['XGBOOST'])
                    if external:
                        guesses['XGBOOST_EXT'] = _from_change(values[origin], changes['XGBOOST_EXT'])
                        expert_changes = {block: changes[name] for block, name in experts.items()}
                        weights = weights_at(origin)
                        guesses['XGBOOST_WEIGHTED'] = _from_change(
                            values[origin], weights.combine(changes['XGBOOST'], expert_changes))
                        history.append((origin, target, horizon, values[target]/values[origin]-1,
                                        changes['XGBOOST'], expert_changes))
                        if group_index == 2 and horizon == 1:
                            for block in blocks:
                                evaluation_weights[block].append(weights.values[block])
                if len(guesses) != len(candidates):
                    continue
                truth = values[target]
                for name, guess in guesses.items():
                    scores[group_index][name].append((truth, guess))
                if selected:
                    if group_index == 1:
                        residuals[horizon-1].append(abs(truth-guesses[selected]))
                    elif group_index == 2:
                        evaluation_predictions[horizon-1].append((truth,guesses[selected]))
        if group_index == 0:
            metrics = {name:_score(rows) for name,rows in scores[0].items()}
            if any(value is None or value['samples'] < 30 for value in metrics.values()):
                raise InsufficientDataError('학습·모델 선택 표본이 부족합니다')
            baseline = min(BASELINES,key=lambda name:metrics[name]['mape'])
            passing = [name for name in learners if _better(metrics[name], metrics[baseline])]
            selected = min(passing, key=lambda name: metrics[name]['mape']) if passing else baseline
    final_metrics = {name:_score(rows) for name,rows in scores[2].items()}
    if any(value is None or value['samples'] < 14 for value in final_metrics.values()):
        raise InsufficientDataError('최종 평가 표본이 부족합니다')
    selected_in_selection = selected
    validated = selected in learners and _better(final_metrics[selected], final_metrics[baseline])
    # 최종 평가에서 탈락하면 선택 구간에서 정한 기준 모델을 사용한다.
    if selected in learners and not validated:
        selected = baseline
        # 다른 모델의 오차로 구간을 만들지 않는다. 기준 모델도 동일 날짜로 다시 계산한다.
        residuals = [[] for _ in range(HORIZON)]
        evaluation_predictions = [[] for _ in range(HORIZON)]
        for group_index, group in ((1,calibrate_origins),(2,evaluate_origins)):
            for origin in group:
                guess = baseline_guess(selected, origin)
                for h in range(1,8):
                    if observed[origin+h]:
                        truth = values[origin+h]
                        if group_index == 1:
                            residuals[h-1].append(abs(truth-guess))
                        else:
                            evaluation_predictions[h-1].append((truth,guess))
    # 공개용 가중치: 백테스트에서 정답이 확인된 모든 과거 예측 오차(최근 WINDOW개)로 정한다.
    final_weights = weighting.choose(history, blocks) if external else None
    needed = {'XGBOOST': ['XGBOOST'], 'XGBOOST_EXT': ['XGBOOST_EXT'],
              'XGBOOST_WEIGHTED': list(dict.fromkeys(['XGBOOST', *experts.values()]))}.get(selected, [])
    result, lower, upper, interval_metrics = [], [], [], []
    explanation = explanation_error = None
    for horizon in range(1,8):
        if selected in learners:
            estimators = {name: fit(name, last, horizon) for name in needed}
            changes = {name: float(estimator.predict([vector(name, last, horizon)])[0]) for name, estimator in estimators.items()}
            change = (final_weights.combine(changes['XGBOOST'], {b: changes[n] for b, n in experts.items()})
                      if selected == 'XGBOOST_WEIGHTED' else changes[selected])
            guess = _from_change(values[last], change)
            if explain and horizon == HORIZON:
                try:
                    explanation = _explain(estimators, selected, experts, final_weights, exogenous, vector, days,
                                           values, ages, last, change, guess)
                except price_explanation.ExplanationError as error:
                    # 설명 실패는 예측 공개를 막지 않는다. 설명 없이 공개하고 사유를 남긴다.
                    explanation_error = str(error)
        else:
            guess = baseline_guess(selected, last)
        result.append(guess)
        errors, evaluation = residuals[horizon-1], evaluation_predictions[horizon-1]
        # 시점별 보정 표본이 부족하면 구간을 표시하지 않는다. 명목 95% 포함률을 보장하지 않는다.
        width = math.ceil(_quantile(errors,.95)) if len(errors) >= 30 and len(evaluation) >= 10 else None
        lower.append(max(0,guess-width) if width is not None else None)
        upper.append(min(MAX_PRICE,guess+width) if width is not None else None)
        interval_metrics.append({'horizon':horizon,'calibrationSamples':len(errors),
                                 'evaluationSamples':len(evaluation),
                                 'coverage': mean(max(0,p-width) <= y <= min(MAX_PRICE,p+width) for y,p in evaluation) if width is not None else None,
                                 'meanWidth': mean(min(MAX_PRICE,p+width)-max(0,p-width) for _,p in evaluation) if width is not None else None})
    feature_sets = {'XGBOOST': PRICE_FEATURES}
    if external:
        feature_sets['XGBOOST_EXT'] = PRICE_FEATURES + exogenous.names
        feature_sets['XGBOOST_WEIGHTED'] = PRICE_FEATURES + exogenous.names
    weighting_metrics = {
        'method': 'constrained_ridge_stacking', 'blocks': exogenous.blocks,
        'blockFeatures': {block: exogenous.block_names(block) for block in blocks},
        **final_weights.as_dict(),
        'evaluationMeanWeights': {block: round(mean(rows), 4) if rows else None
                                  for block, rows in evaluation_weights.items()},
        'expertRefitEveryDays': EXPERT_REFIT_DAYS, 'windowDays': weighting.WINDOW_DAYS, 'kappas': list(weighting.KAPPAS),
        'minGain': weighting.MIN_GAIN, 'minSamples': weighting.MIN_SAMPLES,
    } if external else None
    return Prediction(selected, 'VALIDATED' if validated else 'BASELINE', result, lower, upper, explanation=explanation, metrics=
                      {'selection':{n:_score(r) for n,r in scores[0].items()}, 'evaluation':final_metrics,
                       'candidates':candidates, 'selectedInSelection':selected_in_selection,
                       'selectedModel':selected,'baselineModel':baseline, 'intervals':interval_metrics,
                       'featureSets':feature_sets,
                       'externalGroups':exogenous.groups if exogenous else [],
                       'externalCoverage':exogenous.coverage(evaluate_origins) if exogenous else {},
                       'weighting': weighting_metrics,
                       'intervalMethod':'absolute_error_quantile', 'nominalCoverage':.95,
                       'evaluationStart':days[evaluate_origins[0]].isoformat(),
                       'evaluationEnd':days[evaluate_origins[-1]].isoformat(),
                       'sourceObservations':sum(observed), 'refitEveryDays':REFIT_DAYS,
                       **({'explanationError': explanation_error} if explanation_error else {})})
