"""구조적 가격 전달 모델의 누수·재현성 테스트(합성 자료, 스냅샷 불필요).

    uv run --extra prices python -m pytest model_comparison/structural/test_leakage.py

(a) 기준일 d 이후 가격을 바꿔도 predict(d)가 같다
(b) fit 안에서 표본 기준일 o 이후 가격을 바꿔도 그 표본의 계절 항이 같다
(c) 평소 배수·lambda·k는 fit에 넘어온 학습 표본으로만 정해진다
(d) 같은 입력이면 결과가 1e-6 안에서 같다
(e) model.py는 금지된 라이브러리를 불러오지 않고 파일을 열지 않는다
"""
import ast
import math
from datetime import date, timedelta
from pathlib import Path

import numpy as np
import pytest

from model_comparison.structural import model as structural
from model_comparison.structural.model import StructuralModel, price_grid, season_analog
from tools import standard
from tools.runtime import OriginInputs, TrainingData

MODEL_FILE = Path(structural.__file__)
FEATURES = list(standard.BASE_FEATURES) + list(standard.EXTRA_BUNDLES['MARKET']) + list(standard.EXTRA_BUNDLES['EVENT'])
AS_OF = date(2024, 12, 2)
WINDOW = standard.TRAIN_WINDOW_DAYS


# ---- 합성 자료 ----------------------------------------------------------------------------------------------

def make_world(seed=7, first=date(2018, 1, 1), last=date(2025, 1, 31)):
    """일별 합성 가격. 소매는 도매를 며칠 뒤따라가고 계절 흐름이 있다. 주말은 관측 없음."""
    rng = np.random.default_rng(seed)
    n = (last - first).days + 1
    t = np.arange(n)
    wholesale = 1000 * np.exp(np.cumsum(rng.normal(0, 0.02, n)) + 0.3 * np.sin(2 * np.pi * t / 365.25))
    retail = 3000 * np.exp(0.8 * np.log(np.roll(wholesale, 5) / 1000) + 0.02 * rng.normal(size=n))
    days = [first + timedelta(days=int(i)) for i in t]
    observed = np.array([d.weekday() < 5 for d in days])
    return {'first': first, 'days': days, 'retail': retail, 'wholesale': wholesale, 'observed': observed}


def _filled(values, observed, limit=7):
    out = np.full(len(values), np.nan)
    last = -10 ** 9
    for i in range(len(values)):
        if observed[i]:
            last = i
        if i - last <= limit:
            out[i] = values[last]
    return out


def _events(year):
    """합성 명절: 해마다 날짜가 움직인다(음력 흉내). (시작, 끝, 영향 시작, 영향 끝) 두 개. 영향 기간 = 시작-14 ~ 끝+3(실제 달력과 같은 규칙)."""
    out = []
    for start in (date(year, 2, 1) + timedelta(days=(year * 7) % 20), date(year, 9, 10) + timedelta(days=(year * 3) % 15)):
        end = start + timedelta(days=2)
        out.append((start, end, start - timedelta(days=14), end + timedelta(days=3)))
    return out


def event_row(target):
    """공통 로더 ExtraFeatures.event_row와 같은 정의: (days_to, days_from, 영향 기간 여부), 최대 45."""
    to_major = from_major = 45
    in_window = 0.0
    for year in (target.year - 1, target.year, target.year + 1):
        for start, end, effect_start, effect_end in _events(year):
            if start <= target <= end:
                to_major = from_major = 0
            elif target < start:
                to_major = min(to_major, (start - target).days)
            else:
                from_major = min(from_major, (target - end).days)
            if effect_start <= target <= effect_end:
                in_window = 1.0
    return float(min(to_major, 45)), float(min(from_major, 45)), in_window


def _in_window(day):
    return int(event_row(day)[2])


def _prev_holiday(day):
    return 1 if (day.month, day.day) in ((10, 4), (1, 2)) else 0


def _feature_row(world, own, counter, o, h, in_window):
    f = {name: 0.0 for name in FEATURES}
    cur = own[o]
    target = world['days'][o + h]
    to_major, from_major, window_flag = event_row(target)
    f.update(current=cur, lag1=own[o - 1], lag7=own[o - 7], lag14=own[o - 14], lag28=own[o - 28],
             mean7=float(np.mean(own[o - 6:o + 1])), mean28=float(np.mean(own[o - 27:o + 1])),
             change7=cur / own[o - 7] - 1, volatility7=float(np.std(own[o - 6:o + 1])), price_age=0.0,
             target_weekday=float(target.weekday()), horizon=float(h), days_since_kind_switch=90.0,
             counter_price=counter[o - 1], target_counter_ratio=cur / counter[o - 1],
             counter_change7=counter[o - 1] / counter[o - 8] - 1, counter_change28=counter[o - 1] / counter[o - 29] - 1,
             days_to_major_holiday=to_major, days_from_major_holiday=from_major, target_in_event_window=window_flag,
             target_prev_day_holiday=float(_prev_holiday(target)))
    return np.array([f[name] for name in FEATURES])


def make_history(world, series_id=1, as_of=AS_OF, market='retail', ratio_nan_range=None):
    """공통 로더와 같은 규칙(창 1,825일, 표본 조건)의 TrainingData."""
    own_raw = world['retail'] if market == 'retail' else world['wholesale']
    other_raw = world['wholesale'] if market == 'retail' else world['retail']
    own = _filled(own_raw, world['observed'])
    counter = _filled(other_raw, world['observed'])
    a = (as_of - world['first']).days
    window_start = max(0, a - WINDOW + 1)
    rows, targets, horizons, origins = [], [], [], []
    for o in range(window_start + 29, a):
        if np.isnan(own[o - 28:o + 1]).any() or np.isnan(counter[o - 29:o]).any():
            continue
        for h in range(1, 8):
            if o + h > a or not world['observed'][o + h]:
                continue
            row = _feature_row(world, own, counter, o, h, _in_window)
            if ratio_nan_range and ratio_nan_range[0] <= world['days'][o] <= ratio_nan_range[1]:
                row[FEATURES.index('target_counter_ratio')] = np.nan
            rows.append(row)
            targets.append(own_raw[o + h])
            horizons.append(h)
            origins.append(world['days'][o])
    prices = [(world['days'][i], int(own_raw[i])) for i in range(window_start, a + 1) if world['observed'][i]]
    return TrainingData(series_id=series_id, as_of=as_of, features=np.array(rows), targets=np.array(targets),
                        horizons=np.array(horizons), origins=origins, feature_names=list(FEATURES), prices=prices)


def make_inputs(world, series_id=1, origin=AS_OF, market='retail'):
    own_raw = world['retail'] if market == 'retail' else world['wholesale']
    other_raw = world['wholesale'] if market == 'retail' else world['retail']
    own = _filled(own_raw, world['observed'])
    counter = _filled(other_raw, world['observed'])
    o = (origin - world['first']).days
    features = {h: _feature_row(world, own, counter, o, h, _in_window) for h in range(1, 8)}
    start = max(0, o - WINDOW + 1)
    prices = [(world['days'][i], int(own_raw[i])) for i in range(start, o + 1) if world['observed'][i]]
    return OriginInputs(series_id=series_id, origin=origin, features=features, feature_names=list(FEATURES), prices=prices)


@pytest.fixture(scope='module')
def world():
    return make_world()


@pytest.fixture(scope='module')
def history(world):
    return make_history(world)


@pytest.fixture(scope='module')
def inputs(world):
    return make_inputs(world)


def fitted(history, **params):
    model = StructuralModel(**params)
    model.fit(history, 42)
    return model


def copy_history(history, **changes):
    data = dict(series_id=history.series_id, as_of=history.as_of, features=history.features.copy(),
                targets=history.targets.copy(), horizons=history.horizons.copy(), origins=list(history.origins),
                feature_names=list(history.feature_names), prices=list(history.prices))
    data.update(changes)
    return TrainingData(**data)


def perturb_prices(prices, after, factor=3.7):
    return [(d, int(p * factor) if d > after else p) for d, p in prices]


def params_equal(a, b):
    pa, pb = a.parameters(), b.parameters()
    assert pa['lambda'] == pb['lambda']
    assert pa['k_h'] == pb['k_h']
    assert pa['coef'].keys() == pb['coef'].keys()
    for key in pa['coef']:
        assert pa['coef'][key] == pytest.approx(pb['coef'][key], abs=1e-12)
    ua, ub = pa['usual_log_ratio'], pb['usual_log_ratio']
    assert (math.isnan(ua) and math.isnan(ub)) or ua == pytest.approx(ub, abs=1e-12)


# ---- (a) 기준일 이후 가격 ------------------------------------------------------------------------------------

def test_a_predict_ignores_prices_after_origin(history, inputs):
    model = fitted(history)
    base = model.predict(inputs)
    future = [(inputs.origin + timedelta(days=i), 999999 + 1000 * i) for i in range(1, 15)]
    changed = OriginInputs(series_id=inputs.series_id, origin=inputs.origin, features=inputs.features,
                           feature_names=inputs.feature_names, prices=list(inputs.prices) + future)
    assert model.predict(changed) == base


def test_a_fit_ignores_prices_after_refit_date(history, inputs):
    """재학습 기준일 이후 가격을 바꾸면(학습 표본은 그대로) 학습 결과와 예측이 같다."""
    model = fitted(history)
    future = [(history.as_of + timedelta(days=i), 777777) for i in range(1, 40)]
    other = fitted(copy_history(history, prices=list(history.prices) + future))
    params_equal(model, other)
    assert other.predict(inputs) == model.predict(inputs)


def test_a_prediction_depends_on_past_prices(history, inputs):
    """민감도: 1년 전 같은 시기 가격을 바꾸면 예측이 달라진다(계절 항이 실제로 쓰인다는 확인)."""
    model = fitted(history)
    base = model.predict(inputs)
    year_ago = inputs.origin - timedelta(days=364)
    changed_prices = [(d, int(p * 1.5) if year_ago <= d <= year_ago + timedelta(days=10) else p)
                      for d, p in inputs.prices]
    changed = OriginInputs(series_id=inputs.series_id, origin=inputs.origin, features=inputs.features,
                           feature_names=inputs.feature_names, prices=changed_prices)
    assert model.predict(changed) != base


# ---- (b) fit 안의 계절 항 -----------------------------------------------------------------------------------

def test_b_season_analog_ignores_prices_after_origin(history):
    prices = history.prices
    grid = price_grid(prices)
    all_days = sorted({d for d, _ in prices})
    checked = 0
    for o_day in all_days[500::180]:
        o = o_day.toordinal()
        perturbed = price_grid(perturb_prices(prices, o_day))
        for years in (1, 2, 3):
            for weights in ('uniform', (0.5, 0.3, 0.2)):
                h = np.arange(1, 8)
                v1 = season_analog(grid, np.full(7, o), h, years, weights)
                v2 = season_analog(perturbed, np.full(7, o), h, years, weights)
                np.testing.assert_array_equal(v1, v2)
                checked += 1
    assert checked > 10


def test_b_fit_season_equals_truncated_computation(history):
    """표본마다 o 이전 가격만 잘라 만든 격자로 계산한 값 = fit이 쓰는 전체 격자 값."""
    prices = history.prices
    full = price_grid(prices)
    days = sorted({d for d, _ in prices})
    for o_day in days[700::250]:
        o = o_day.toordinal()
        truncated = price_grid(prices, until_ord=o)
        h = np.arange(1, 8)
        np.testing.assert_array_equal(season_analog(full, np.full(7, o), h, 3),
                                      season_analog(truncated, np.full(7, o), h, 3))


def test_b_season_analog_value_is_log_change_of_last_year(history):
    """손으로 계산한 1년 전 h일 로그 변화와 같다(관측이 있는 평일 기준)."""
    prices = dict(history.prices)
    grid = price_grid(history.prices)
    o_day = date(2024, 5, 14)  # 화요일
    base = o_day - timedelta(days=364)
    h = 3
    expected = math.log(prices[base + timedelta(days=h)] / prices[base])
    got = season_analog(grid, np.array([o_day.toordinal()]), np.array([h]), 1)[0]
    assert got == pytest.approx(expected, abs=1e-12)


def test_b_kind_tol_uses_only_past_switches(history):
    """작형 일치 옵션을 켜도 o 이후 전환 정보는 읽지 않는다(전환일을 o 이후로 옮겨도 같다)."""
    prices = history.prices
    o_day = date(2024, 5, 14)
    o = o_day.toordinal()
    grid = price_grid(prices)
    switches = [date(2022, 3, 1).toordinal(), date(2023, 3, 1).toordinal(), date(2024, 3, 1).toordinal()]
    later = switches + [o + 3, o + 30]
    h = np.arange(1, 8)
    a = season_analog(grid, np.full(7, o), h, 3, 'uniform', structural.kind_since_grid(grid, switches),
                      np.full(7, 40.0), 10.0)
    b = season_analog(grid, np.full(7, o), h, 3, 'uniform', structural.kind_since_grid(grid, later),
                      np.full(7, 40.0), 10.0)
    np.testing.assert_array_equal(a, b)


# ---- (c) 학습 표본으로만 정해지는 값 ----------------------------------------------------------------------

def test_c_usual_ratio_is_median_of_training_samples_last_n_days(history):
    window_days = 91
    model = fitted(history, ratio_window_days=window_days)
    origins = np.array([o.toordinal() for o in history.origins])
    ratio = history.features[:, FEATURES.index('target_counter_ratio')]
    recent = origins > origins.max() - window_days
    uniq, first = np.unique(origins[recent], return_index=True)
    expected = float(np.median(np.log(ratio[recent][first])))
    assert model.parameters()['usual_log_ratio'] == pytest.approx(expected, abs=1e-12)


def test_c_fit_outputs_ignore_data_outside_training_samples(history):
    """학습 표본 밖(재학습 기준일 이후 가격)을 바꿔도 평소 배수·lambda·k·계수가 같다."""
    model = fitted(history, k_mode='per_horizon')
    other = fitted(copy_history(history, prices=perturb_prices(history.prices, history.as_of) +
                                [(history.as_of + timedelta(days=3), 1)]), k_mode='per_horizon')
    params_equal(model, other)


def test_c_selection_uses_only_last_fraction_of_training_samples(history):
    """검증(마지막 20%)에 쓰인 표본이 달라지면 선택이 달라질 수 있고, 같으면 같다 — 표본을 한 번 더 넘겨도 결정적이다."""
    a = fitted(history)
    b = fitted(copy_history(history))
    params_equal(a, b)
    info = a.parameters()['fit_info']
    assert info['selection'] == 'last_fraction'
    assert info['fit_n'] > 0 and info['val_n'] > 0
    assert info['fit_n'] + info['val_n'] <= info['samples']  # 검증 구간과 겹치는 정답은 학습에서 빠진다


def test_c_training_cap_uses_only_recent_samples(history):
    """학습 창 상한(730일)이면 그보다 오래된 표본의 값을 바꿔도 결과가 같다."""
    cap = 730
    origins = np.array([o.toordinal() for o in history.origins])
    old = origins <= history.as_of.toordinal() - cap
    assert old.any()
    features = history.features.copy()
    targets = history.targets.copy()
    features[old, FEATURES.index('counter_change7')] += 0.5
    targets[old] *= 2
    model = fitted(history, train_window_days=cap)
    other = fitted(copy_history(history, features=features, targets=targets), train_window_days=cap)
    params_equal(model, other)


# ---- (d) 결정성 ----------------------------------------------------------------------------------------------

@pytest.mark.parametrize('params', [
    {},
    {'k_mode': 'per_horizon', 'transmission': ['counter_change7', 'counter_change28'], 'season_weights': [0.6, 0.3, 0.1]},
    {'retail_terms': ['transmission', 'ratio', 'season', 'event', 'momentum'], 'h_scale_terms': ['transmission']},
    {'retail_k_grid': [0, 0.25, 0.5, 0.75, 1, 1.25, 1.5]},
])
def test_d_deterministic(history, inputs, params):
    a, b = fitted(history, **params), fitted(history, **params)
    pa, pb = a.predict(inputs), b.predict(inputs)
    assert len(pa) == 7
    np.testing.assert_allclose(pa, pb, rtol=0, atol=1e-6)
    params_equal(a, b)


# ---- 동작 확인(변형 선택, nan 처리) ------------------------------------------------------------------------

@pytest.mark.parametrize('params', [
    {'transmission': ['counter_change28']},
    {'retail_terms': ['transmission', 'season']},
    {'ratio_window_days': 365, 'season_years': 1},
    {'season_kind_tol': 14},
    {'train_window_days': 730},
    {'wholesale_terms': []},
    {'transmission': ['counter_change7', 'counter_change28']},
    {'retail_terms': ['transmission', 'season', 'event']},
    {'ratio_window_days': 28},
    {'season_years': 1},
    {'season_weights': 'uniform'},
    {'k_mode': 'shared'},
    {'train_window_days': 1095},
    {'lambda_grid': [0, 0.1, 1, 10, 100, 1000, 10000]},
    {'season_event_mask': True},
    {'retail_k_grid': [0, 0.25, 0.5, 0.75, 1, 1.25, 1.5]},
])
def test_variants_selectable_by_params(history, inputs, params):
    model = fitted(history, **params)
    out = model.predict(inputs)
    assert len(out) == 7 and all(math.isfinite(v) and v > 0 for v in out)


def test_wholesale_naive_equals_current(world):
    h = make_history(world, series_id=2, market='wholesale')
    i = make_inputs(world, series_id=2, market='wholesale')
    model = fitted(h, wholesale_terms=[])
    current = [i.features[k][FEATURES.index('current')] for k in range(1, 8)]
    assert model.predict(i) == current


def test_wholesale_season_event_runs(world):
    h = make_history(world, series_id=2, market='wholesale')
    i = make_inputs(world, series_id=2, market='wholesale')
    model = fitted(h)
    assert set(model.parameters()['coef']) == {'c', 'd:target_in_event_window', 'd:target_prev_day_holiday'}
    assert all(0 < v for v in model.predict(i))


def test_nan_terms_are_zero_and_counted(world):
    h = make_history(world, ratio_nan_range=(date(2022, 1, 1), date(2022, 6, 30)))
    model = fitted(h)
    counts = model.parameters()['nan_counts']['fit']
    assert counts['ratio'] > 0
    i = make_inputs(world)
    i.features[3][FEATURES.index('target_counter_ratio')] = np.nan
    out = model.predict(i)
    assert all(math.isfinite(v) for v in out)
    assert model.parameters()['nan_counts']['predict']['ratio'] == 1


def test_usual_ratio_nan_turns_ratio_term_off(world):
    """최근 N일 배수가 모두 결측이면 평소 배수를 못 구해 배수 항은 0이 된다(예측은 계속 나온다)."""
    h = make_history(world, ratio_nan_range=(date(2024, 6, 1), date(2024, 12, 2)))
    model = fitted(h)
    assert math.isnan(model.parameters()['usual_log_ratio'])
    out = model.predict(make_inputs(world))
    assert all(math.isfinite(v) for v in out)


def test_k_is_within_unit_interval(history):
    for k_mode in ('shared', 'per_horizon'):
        k = fitted(history, k_mode=k_mode).parameters()['k_h']
        assert len(k) == 7 and all(0.0 <= v <= 1.0 for v in k)


# ---- (e) 금지 라이브러리·파일 접근 ---------------------------------------------------------------------------

BANNED_IMPORTS = {'sklearn', 'xgboost', 'lightgbm', 'statsforecast', 'optuna', 'pandas', 'torch', 'statsmodels',
                  'os', 'pathlib', 'csv', 'json', 'sqlite3', 'psycopg', 'sqlalchemy', 'shutil', 'glob', 'tools'}
BANNED_CALLS = {'open', 'read_csv', 'read_text', 'read_bytes', 'loadtxt', 'genfromtxt', 'load', 'connect', 'system',
                'exec', 'eval', '__import__'}


def test_e_no_banned_imports_or_file_access():
    tree = ast.parse(MODEL_FILE.read_text(encoding='utf-8'))
    imported = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            imported |= {a.name.split('.')[0] for a in node.names}
        elif isinstance(node, ast.ImportFrom):
            imported.add((node.module or '').split('.')[0])
    assert not imported & BANNED_IMPORTS, imported & BANNED_IMPORTS
    assert imported <= {'__future__', 'math', 'dataclasses', 'numpy', 'scipy'}, imported
    calls = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Call):
            f = node.func
            calls.add(f.id if isinstance(f, ast.Name) else f.attr if isinstance(f, ast.Attribute) else '')
    assert not calls & BANNED_CALLS, calls & BANNED_CALLS


def test_e_no_banned_modules_loaded_by_model_import():
    """model.py를 불러오는 것만으로 금지 모듈이 새로 올라오지 않는다(별도 프로세스에서 확인)."""
    import subprocess
    import sys
    code = ("import sys; import model_comparison.structural.model; "
            "bad=[m for m in ('sklearn','xgboost','lightgbm','statsforecast','optuna') if m in sys.modules]; "
            "print(bad); sys.exit(1 if bad else 0)")
    root = Path(__file__).resolve().parents[2]
    result = subprocess.run([sys.executable, '-c', code], cwd=root, capture_output=True, text=True)
    assert result.returncode == 0, result.stdout + result.stderr


# ---- PRD §10 기본형 --------------------------------------------------------------------------------------------

def test_v0_matches_prd_section_10(history):
    model = StructuralModel()
    assert model.season_weights == (0.5, 0.3, 0.2) and model.season_years == 3 and model.season_window == 3
    assert model.k_mode == 'per_horizon' and model.k_grid == [0.0, 0.25, 0.5, 0.75, 1.0]
    assert model.lambda_grid == [100.0, 10.0, 1.0, 0.1, 0.0]
    assert model.select_loss == 'mape' and model.train_window_days is None and model.ratio_window_days == 91
    assert model.transmission == ('counter_change7',)
    assert model.event_features == ('target_in_event_window', 'target_prev_day_holiday')
    assert 'momentum' not in model.terms['retail'] and 'momentum' not in model.terms['wholesale']
    assert model.terms['wholesale'] == ('season', 'event')
    model.fit(history, 42)
    p = model.parameters()
    assert set(p['coef']) == {'a:counter_change7', 'b', 'c', 'd:target_in_event_window', 'd:target_prev_day_holiday'}
    assert len(p['k_h']) == 7 and all(k in model.k_grid for k in p['k_h'])


def test_season_weights_renormalize_missing_years(history):
    """없는 해는 빼고 가중을 다시 정규화한다(1년만 있을 때 값 = 1년 전 로그 변화)."""
    grid = price_grid(history.prices)
    start = min(d for d, _ in history.prices)
    o_day = start + timedelta(days=364 + 40)  # 창 첫 날 + 1년 조금 뒤라 k=1만 있다
    while o_day.weekday() >= 5:
        o_day += timedelta(days=1)
    o = o_day.toordinal()
    assert o_day - timedelta(days=364) >= start and o_day - timedelta(days=728) < start
    one = season_analog(grid, np.array([o]), np.array([2]), 1, 'uniform')[0]
    three = season_analog(grid, np.array([o]), np.array([2]), 3, (0.5, 0.3, 0.2))[0]
    assert three == pytest.approx(one, abs=1e-12)


def test_season_all_missing_is_zero_term_and_counted(history):
    """셋 다 없는 표본은 NaN -> 0이고 횟수에 잡힌다."""
    model = fitted(history)
    assert model.parameters()['nan_counts']['fit']['season'] > 0


def test_nonfinite_prediction_returns_none(history, inputs):
    model = fitted(history)
    model.coef = np.full_like(model.coef, np.nan)
    assert model.predict(inputs) == [None] * 7
    model.coef = np.full_like(model.coef, 1e9)  # y_clip 때문에 유한하다
    assert all(v is not None and math.isfinite(v) for v in model.predict(inputs))


# ---- 계절 항 명절 마스크(season_event_mask) ---------------------------------------------------------------------

GOLDEN_V0_RETAIL = [725.746317, 733.081691, 739.020019, 738.900886, 738.900886, 737.848691, 737.848691]
GOLDEN_V0_WHOLESALE = [162.631403, 162.701454, 162.356042, 162.383716, 162.383716, 162.565607, 162.565607]


def last_year_only_origin(world, years=1):
    """올해 o..o+7은 명절 영향 기간이 아니고, 작년 b=o-364는 영향 기간인 평일 기준일."""
    day = date(2023, 1, 2)
    while day < date(2024, 11, 20):
        if day.weekday() < 5 and world['observed'][(day - world['first']).days]:
            this_year = [event_row(day + timedelta(days=i))[2] for i in range(0, 8)]
            base = event_row(day - timedelta(days=364))[2]
            if not any(this_year) and base == 1:
                return day
        day += timedelta(days=1)
    raise AssertionError('조건에 맞는 기준일이 없음')


def test_mask_off_keeps_v0_predictions(world, history, inputs):
    """꺼짐(기본)이면 마스크 도입 전과 예측이 같다(골든 값은 도입 전 모델에서 뽑음)."""
    for params in ({}, {'season_event_mask': False}):
        got = fitted(history, **params).predict(inputs)
        np.testing.assert_allclose(got, GOLDEN_V0_RETAIL, rtol=0, atol=1e-6)
    h = make_history(world, series_id=2, market='wholesale')
    i = make_inputs(world, series_id=2, market='wholesale')
    np.testing.assert_allclose(fitted(h).predict(i), GOLDEN_V0_WHOLESALE, rtol=0, atol=1e-6)


def test_mask_zeroes_season_when_only_last_year_is_in_event(world, history):
    """올해 o와 o+h는 명절이 아닌데 작년 b만 명절 기간이면, 켰을 때만 계절 항이 0(nan)이 된다."""
    o_day = last_year_only_origin(world)
    inp = make_inputs(world, origin=o_day)
    assert all(inp.features[h][FEATURES.index('target_in_event_window')] == 0 for h in range(1, 8))
    off, on = fitted(history), fitted(history, season_event_mask=True)
    assert np.isfinite(off.season_values(inp)).any()
    assert np.isnan(on.season_values(inp)).all()
    assert on.predict(inp) != off.predict(inp)


def test_mask_leaves_unrelated_samples_alone(world, history):
    """과거 b·b+h도, o·o+h도 명절이 아니면 켜도 계절 항이 같다."""
    day = date(2024, 5, 14)
    assert not any(event_row(day + timedelta(days=i))[2] for i in range(0, 8))
    assert not any(event_row(day - timedelta(days=364 * k) + timedelta(days=i))[2] for k in (1, 2, 3) for i in range(0, 8))
    inp = make_inputs(world, origin=day)
    off, on = fitted(history), fitted(history, season_event_mask=True)
    np.testing.assert_array_equal(off.season_values(inp), on.season_values(inp))


def test_mask_decision_ignores_data_after_refit_and_origin(world, history):
    """재학습 기준일·예측 기준일 이후 데이터를 바꿔도 마스크 판정과 예측이 같다."""
    o_day = last_year_only_origin(world)
    inp = make_inputs(world, origin=o_day)
    model = fitted(history, season_event_mask=True)
    base_season, base_pred = model.season_values(inp), model.predict(inp)
    future = [(history.as_of + timedelta(days=i), 555555) for i in range(1, 30)]
    other = fitted(copy_history(history, prices=list(history.prices) + future), season_event_mask=True)
    later = [(o_day + timedelta(days=i), 888888) for i in range(1, 15)]
    inp2 = OriginInputs(series_id=inp.series_id, origin=inp.origin, features=inp.features,
                        feature_names=inp.feature_names, prices=list(inp.prices) + later)
    np.testing.assert_array_equal(other.season_values(inp2), base_season)
    assert other.predict(inp2) == base_pred
    assert other.event_days.t_to == model.event_days.t_to and other.event_days.t_from == model.event_days.t_from


def test_mask_in_fit_zeroes_event_samples(world, history):
    """fit에서 목표일이 영향 기간인 표본은 계절 항이 0이 되고, 횟수가 기록된다."""
    off, on = fitted(history), fitted(history, season_event_mask=True)
    o = np.array([d.toordinal() for d in history.origins])
    h = history.horizons
    season = season_analog(price_grid(history.prices), o, h, 3)
    flag_t = history.features[:, FEATURES.index('target_in_event_window')] == 1
    must = int((flag_t & np.isfinite(season)).sum())
    masked = on.parameters()['fit_info']['season_masked']
    assert masked >= must > 0
    nan_on = on.parameters()['nan_counts']['fit']['season']
    nan_off = off.parameters()['nan_counts']['fit']['season']
    assert nan_on - nan_off == masked
    assert off.parameters()['fit_info']['season_masked'] == 0


def test_mask_origin_flag_from_features_matches_calendar(world, history):
    """기준일 o의 영향 기간 판정(목표일 days_to/from에서 h를 반영)이 정할 수 있는 경우 실제와 같다."""
    from model_comparison.structural.model import origin_event_flag
    ev = fitted(history, season_event_mask=True).event_days
    assert ev.t_to == 14 and ev.t_from == 3  # 학습 표본에서 규칙(시작 14일 전 ~ 끝 3일 후)을 되찾는다
    decided = 0
    day = date(2022, 1, 3)
    while day < date(2024, 11, 20):
        rows = [event_row(day + timedelta(days=i)) for i in range(1, 8)]
        got = origin_event_flag(ev, day.toordinal(), list(range(1, 8)), [r[0] for r in rows], [r[1] for r in rows])
        if not np.isnan(got):
            assert got == event_row(day)[2], day
            decided += 1
        day += timedelta(days=1)
    assert decided > 600


def test_mask_requires_event_features(world):
    """EVENT 묶음이 없으면 마스크를 켤 수 없다."""
    h = make_history(world)
    keep = [i for i, n in enumerate(FEATURES) if n not in standard.EXTRA_BUNDLES['EVENT']]
    cut = copy_history(h, features=h.features[:, keep], feature_names=[FEATURES[i] for i in keep])
    with pytest.raises(ValueError):
        StructuralModel(season_event_mask=True).fit(cut, 42)


# ---- retail_k_grid(소매만 k 격자 확대, 탐색 변형. PRD §4.3의 k in [0, 1]과 다름) ---------------------------------------

K_WIDE = [0, 0.25, 0.5, 0.75, 1, 1.25, 1.5]


def test_retail_k_grid_none_is_same_as_default(history, inputs, world):
    """기본값(None)이면 k_grid와 같게 동작한다: 파라미터·예측이 같다(소매·도매)."""
    assert StructuralModel().retail_k_grid is None
    wh = make_history(world, series_id=2, market='wholesale')
    wi = make_inputs(world, series_id=2, market='wholesale')
    for hist, inp in ((history, inputs), (wh, wi)):
        a, b = fitted(hist), fitted(hist, retail_k_grid=None)
        np.testing.assert_allclose(a.predict(inp), b.predict(inp), rtol=0, atol=0)
        assert a.parameters()['k_h'] == b.parameters()['k_h']
        params_equal(a, b)


def test_retail_k_grid_same_values_as_k_grid_is_identical(history, inputs):
    grid = [0.0, 0.25, 0.5, 0.75, 1.0]
    a, b = fitted(history), fitted(history, retail_k_grid=grid)
    np.testing.assert_allclose(a.predict(inputs), b.predict(inputs), rtol=0, atol=0)


def test_retail_k_grid_applies_to_retail_only(history, world):
    retail = fitted(history, retail_k_grid=K_WIDE)
    assert all(k in K_WIDE for k in retail.parameters()['k_h'])
    for k_mode in ('shared', 'per_horizon'):
        r = fitted(history, retail_k_grid=K_WIDE, k_mode=k_mode).parameters()['k_h']
        assert len(r) == 7 and all(0.0 <= v <= 1.5 for v in r)
    wholesale = fitted(make_history(world, series_id=2, market='wholesale'), retail_k_grid=K_WIDE)
    assert all(0.0 <= k <= 1.0 and k in wholesale.k_grid for k in wholesale.parameters()['k_h'])


@pytest.mark.parametrize('bad', [[-0.25, 1.0], [0, 3.5], []])
def test_retail_k_grid_out_of_range_is_rejected(bad):
    with pytest.raises(ValueError):
        StructuralModel(retail_k_grid=bad)
