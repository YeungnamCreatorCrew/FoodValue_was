"""시점별 직접 예측. 원천 결측은 타깃으로 학습하지 않고 미래 자료는 참조하지 않는다.

후보: LAST_PRICE, MEAN_7(기준 모델), XGBOOST(가격 특징만), XGBOOST_EXT(가격 + 외부 원천 특징).
외부 원천은 시간순 백테스트에서 가격만 쓴 모델과 같은 기준으로 비교해 이길 때만 선택된다.
"""
import math
from dataclasses import dataclass
from datetime import date, timedelta
from statistics import mean

from app.services.exogenous import Covariates, ExogenousFeatures

HORIZON = 7
MIN_TRAIN = 120
MAX_BACKTEST_DAYS = 240
MAX_FORWARD_FILL_DAYS = 7
MODEL_VERSION = 'direct-xgb-v2-change-exog'
MAX_PRICE = 2**31 - 1


PRICE_FEATURES = ['current', 'lag1', 'lag7', 'lag14', 'lag28', 'mean7', 'mean28', 'change7', 'volatility7',
                  'targetWeekday', 'targetSeasonSin', 'targetSeasonCos', 'priceAge']
BASELINES = ['LAST_PRICE', 'MEAN_7']


class InsufficientDataError(Exception):
    pass


class ModelDependencyError(Exception):
    pass


@dataclass
class Prediction:
    model: str
    quality: str
    prices: list[int]
    lower: list[int | None]
    upper: list[int | None]
    metrics: dict


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


def _from_change(current, change):
    return _price(current * (1 + float(change)))


def training_data(days, values, observed, ages, cutoff, horizon):
    return _training(lambda o, h: features(days, values, ages, o, h), values, observed, cutoff, horizon)


def _model():
    try:
        from xgboost import XGBRegressor
    except ImportError:
        raise ModelDependencyError('예측 배치에는 uv sync --extra prices가 필요합니다') from None
    return XGBRegressor(n_estimators=80, max_depth=3, learning_rate=.05,
                        objective='reg:squarederror', tree_method='hist', n_jobs=1,
                        random_state=42, subsample=1, colsample_bytree=1)


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


def predict(observations, base_date, covariates: Covariates | None = None):
    days, values, observed, ages = normalize(observations, base_date)
    last = len(days)-1
    if features(days, values, ages, last, 1) is None:
        raise InsufficientDataError('연속된 최근 29일 입력이 필요합니다')
    exogenous = ExogenousFeatures(days, values, covariates) if covariates and not covariates.empty() else None
    learners = ['XGBOOST'] + (['XGBOOST_EXT'] if exogenous and exogenous.names else [])
    candidates = BASELINES + learners
    cache = {}

    def vector(name, origin, horizon):
        key = (name, origin, horizon)
        if key not in cache:
            row = features(days, values, ages, origin, horizon)
            cache[key] = row if row is None or name == 'XGBOOST' else row + exogenous.vector(origin, horizon)
        return cache[key]

    def baseline_guess(name, origin):
        return _price(values[origin] if name == 'LAST_PRICE' else mean(values[origin-6:origin+1]))

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
    models, fitted_at = {}, {}
    selected = baseline = None
    for group_index, group in enumerate(groups):
        for origin in group:
            for horizon in range(1, HORIZON+1):
                target = origin+horizon
                if not observed[target]:
                    continue  # 결측 보정값을 정답으로 삼지 않는다.
                guesses = {name: baseline_guess(name, origin) for name in BASELINES}
                for name in learners:
                    key = (name, horizon)
                    if key not in fitted_at or origin-fitted_at[key] >= 7:
                        # 평가 시점까지 정답이 확인된 표본만으로 7일마다 재학습한다.
                        inputs, targets = _training(lambda o, h: vector(name, o, h), values, observed, origin, horizon)
                        if len(targets) < MIN_TRAIN:
                            break
                        estimator = _model()
                        estimator.fit(inputs, targets)
                        models[key], fitted_at[key] = estimator, origin
                    guesses[name] = _from_change(values[origin], models[key].predict([vector(name, origin, horizon)])[0])
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
    result, lower, upper, interval_metrics = [], [], [], []
    for horizon in range(1,8):
        if selected in learners:
            inputs, targets = _training(lambda o, h: vector(selected, o, h), values, observed, last, horizon)
            estimator = _model()
            estimator.fit(inputs, targets)
            guess = _from_change(values[last], estimator.predict([vector(selected, last, horizon)])[0])
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
    if 'XGBOOST_EXT' in learners:
        feature_sets['XGBOOST_EXT'] = PRICE_FEATURES + exogenous.names
    return Prediction(selected, 'VALIDATED' if validated else 'BASELINE', result, lower, upper,
                      {'selection':{n:_score(r) for n,r in scores[0].items()}, 'evaluation':final_metrics,
                       'candidates':candidates, 'selectedInSelection':selected_in_selection,
                       'selectedModel':selected,'baselineModel':baseline, 'intervals':interval_metrics,
                       'featureSets':feature_sets,
                       'externalGroups':exogenous.groups if exogenous else [],
                       'externalCoverage':exogenous.coverage(evaluate_origins) if exogenous else {},
                       'intervalMethod':'absolute_error_quantile', 'nominalCoverage':.95,
                       'evaluationStart':days[evaluate_origins[0]].isoformat(),
                       'evaluationEnd':days[evaluate_origins[-1]].isoformat(),
                       'sourceObservations':sum(observed), 'refitEveryDays':7})
