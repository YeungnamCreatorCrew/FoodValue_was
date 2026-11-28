"""구조적 가격 전달 모델(struct, PR #71) 서비스 예측. 앙상블과 별도 트랙(price_model_run.model_track='STRUCT')으로 저장한다.

- 모델·설정: model_comparison/structural/model.py의 StructuralModel + config.json(t18, 검증 1회 통과 설정). 설정 파일은 고치지 않고
  sha256을 model_version에 남긴다.
- 입력: 앙상블과 같은 서비스 스냅샷(app.services.v2_snapshot, DB → 실험 형식). 실험 실행기(structural.run.run_series)와 같은
  training_data·origin_inputs·후처리(0.5 올림)를 쓴다.
- 다른 점: 실험은 ISO 주의 첫 기준일에만 재학습했고, 서비스는 배치 기준일마다 그날까지 자료로 학습한다(앙상블 서비스와 같음).
  그래서 주의 첫 기준일이 아닌 날은 실험 예측과 다를 수 있다.
- 소매·도매 구분: 모델 기본값은 실험 스냅샷 계열 id(1, 8, …)다. 서비스 스냅샷은 대파·양파·깐마늘이 DB 계열 id라
  스냅샷의 시장 정보로 retail_series·wholesale_series를 만들어 넘긴다.
- 설명(7일 뒤): 예측가 = 현재가 × exp(k_7 × clip(Σ 계수·항)). 원 단위 기여 = (예측가 − 현재가) × (항 j 로그 기여 / 로그 합).
  합이 그대로 보존된다(기준값 = 현재가). 로그 합이 0이거나 k_7 = 0이면 모든 기여가 0이다. 회귀 계수에 대한 분해이며 인과가 아니다.
"""
import hashlib
import json
import math
from dataclasses import dataclass, field
from datetime import date, timedelta
from pathlib import Path

import numpy as np

from tools import loader, run_backtest, standard

ROOT = Path(__file__).resolve().parents[2]
CONFIG_PATH = ROOT / 'model_comparison' / 'structural' / 'config.json'
CALIBRATION_PATH = ROOT / 'model_comparison' / 'structural' / 'service' / 'calibration.json'
MODEL_NAME = 'STRUCT'
EXPLAIN_HORIZON = 7
METHOD = 'STRUCT_TERM_SHARE'
SEASON_FACTOR = 'struct_season'
TOLERANCE = 1e-6  # 분해로 다시 계산한 가격과 모델 출력의 상대 오차 한도


def config_sha256() -> str:
    return hashlib.sha256(CONFIG_PATH.read_bytes()).hexdigest()


MODEL_VERSION = f'struct-t18-{config_sha256()[:8]}'


@dataclass
class StructForecast:
    series_id: int
    item: str
    market: str
    prices: list[float | None]  # 시점 1~7, 후처리(0.5 올림) 가격. 실패면 None
    members: dict[str, list[float | None]] = field(default_factory=dict)
    errors: dict[str, str] = field(default_factory=dict)
    explanation: object = None
    explanation_error: str = ''
    parameters: dict = field(default_factory=dict)  # 계수·k_h·λ(StructuralModel.parameters 요약)


def _config() -> dict:
    return json.loads(CONFIG_PATH.read_text(encoding='utf-8'))


def model_params(snap, config: dict) -> dict:
    retail = [sid for sid in snap.series_ids if snap.series[sid].market == 'RETAIL']
    wholesale = [sid for sid in snap.series_ids if snap.series[sid].market == 'WHOLESALE']
    return {**config['params'], 'retail_series': retail, 'wholesale_series': wholesale}


def _post(values):
    return [float(price) if status == 'OK' else None for _, price, status, _ in run_backtest.prediction_rows(values, 'OK', '')]


def _summary(model) -> dict:
    p = model.parameters()
    return {'market': p['market'], 'terms': p['terms'], 'coef': p['coef'], 'kH': p['k_h'], 'lambda': p['lambda'],
            'usualRatio': p['usual_ratio'], 'samples': p['fit_info'].get('samples')}


def _factor_id(term: str) -> str:
    """항 이름 → 화면 요인 id. 특징 하나로 된 항은 기존 특징 id를 그대로 쓴다."""
    if term == 'season':
        return SEASON_FACTOR
    if term == 'ratio':
        return 'target_counter_ratio'
    if term == 'momentum':
        return 'change7'
    return term.split(':', 1)[1]  # transmission:counter_change7, event:target_in_event_window …


def explain(model, inputs, snap, sid, as_of, bundles, horizon=EXPLAIN_HORIZON):
    """7일 뒤 예측의 항별 원 단위 기여(price_explanation.Explanation). 모델 내부 계산을 읽기만 한다(predict는 바꾸지 않음)."""
    from app.services import price_explanation

    horizons = np.array(standard.HORIZONS)
    X = np.asarray([inputs.features[h] for h in standard.HORIZONS], dtype=float)
    raw = model.predict(inputs)[horizon - 1]  # predict가 계절 항(_last_season)을 남긴다
    season = model._last_season
    Z, names, _ = model._build_terms(X, horizons, season, model.usual_ratio)
    logs = Z[horizon - 1] * model.coef
    total = float(logs.sum())
    k = float(model.k_h[horizon - 1])
    current = float(X[horizon - 1, model._idx['current']])
    predicted = current * math.exp(k * float(np.clip(total, -model.y_clip, model.y_clip)))
    if raw is None or abs(predicted - raw) > TOLERANCE * raw:
        raise ValueError('항 분해 가격이 모델 예측과 다름')
    delta = predicted - current
    contributions, values = {}, {}
    names_in = list(inputs.feature_names)
    for term, part in zip(names, logs):
        fid = _factor_id(term)
        contributions[fid] = contributions.get(fid, 0.0) + (delta * float(part) / total if total and k else 0.0)
        if fid == SEASON_FACTOR:
            s = season[horizon - 1]
            values[fid] = price_explanation.clean(math.expm1(s)) if np.isfinite(s) else None
        else:
            values[fid] = price_explanation.clean(X[horizon - 1, names_in.index(fid)])
    history = {}
    for fid in contributions:
        if fid in price_explanation.NO_HISTORY:
            continue
        j = names_in.index(fid)
        points = []
        for back in range(price_explanation.HISTORY_DAYS - 1, -1, -1):
            day = as_of - timedelta(days=back)
            try:
                value = snap.origin_inputs(sid, day, bundles).features[horizon][j]
            except loader.NoInput:
                value = None
            points.append((day.isoformat(), price_explanation.clean(value)))
        history[fid] = points
    return price_explanation.Explanation(horizon=horizon, current_price=current, damping=k, base_price=current,
                                         predicted_price=int(round(predicted)), contributions=contributions,
                                         values=values, history=history, method=METHOD)


def forecast(snap: loader.Snapshot, as_of: date, log=print) -> dict[int, StructForecast]:
    """스냅샷의 모든 계열을 as_of 기준으로 예측한다. 한 계열 실패가 다른 계열을 막지 않는다."""
    config = _config()
    bundles = loader.check_bundles(config['extra_features'])
    cls = run_backtest.load_class(config['class'])
    params = model_params(snap, config)
    result = {}
    for sid in snap.series_ids:
        s = snap.series[sid]
        out = StructForecast(sid, s.item, s.market, [None] * len(standard.HORIZONS))
        try:
            model = cls(**params)
            model.fit(snap.training_data(sid, as_of, bundles), config.get('seed', 42))
            inputs = snap.origin_inputs(sid, as_of, bundles)
            out.prices = _post(model.predict(inputs))
            out.parameters = _summary(model)
        except loader.NoInput:
            out.errors[MODEL_NAME] = 'NO_INPUT'
        except Exception as error:  # noqa: BLE001 — 실험 실행기와 같이 기록하고 계속한다
            out.errors[MODEL_NAME] = type(error).__name__
            log(f'struct {sid} 실패: {type(error).__name__}: {error}')
        out.members = {MODEL_NAME: out.prices}
        if out.parameters and model.column_names and out.prices[EXPLAIN_HORIZON - 1] is not None:
            try:
                out.explanation = explain(model, inputs, snap, sid, as_of, bundles)
            except Exception as error:  # noqa: BLE001 — 설명 실패가 예측 공개를 막지 않는다
                out.explanation_error = type(error).__name__
                log(f'struct {sid} 설명 실패: {type(error).__name__}: {error}')
        result[sid] = out
    log(f'struct: {len(result)}계열')
    return result
