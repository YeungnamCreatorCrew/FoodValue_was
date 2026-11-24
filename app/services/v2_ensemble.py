"""v2 앙상블 예측(서비스). 팀 확정 구성(model_comparison/v2/README '현재 앙상블 구성', PR #60):

- XGBoost  model_comparison/v2/configs/v1feat_xgb_tuned.json   (10계열 통합 학습)
- LightGBM model_comparison/v2/configs/v1feat_lgbm.json        (10계열 통합 학습)
- AutoARIMA model_comparison/autoarima/config_p2_event.json     (계열별)
- 같은 비중 평균(model_comparison.v2.ensemble.combine과 같은 규칙: OK인 구성원만 평균)

실험 코드(run_pooled.Matrices, run_backtest.prediction_rows, Snapshot.training_data/origin_inputs)를 그대로 불러
같은 특징·같은 후처리로 예측한다. 실험은 주 1회(주 첫 기준일) 재학습했고, 서비스는 배치 기준일마다 그날까지 자료로
학습한다(같은 창 1,825일). 입력 스냅샷은 app.services.v2_snapshot이 DB에서 만든다.
"""
import json
import time
from dataclasses import dataclass, field
from datetime import date
from pathlib import Path

import numpy as np

from tools import loader, run_backtest, standard

ROOT = Path(__file__).resolve().parents[2]
MODEL_VERSION = 'v2-ensemble-xgb_tuned+lgbm+arima_p2'
POOLED = {'XGBOOST': ROOT / 'model_comparison/v2/configs/v1feat_xgb_tuned.json',
          'LIGHTGBM': ROOT / 'model_comparison/v2/configs/v1feat_lgbm.json'}
ARIMA = ('AUTOARIMA', ROOT / 'model_comparison/autoarima/config_p2_event.json')


@dataclass
class SeriesForecast:
    series_id: int  # 스냅샷 계열 id(대파·양파·깐마늘은 DB 계열 id, 배추·무는 9001…)
    item: str
    market: str
    prices: list[float | None]  # 시점 1~7, 앙상블 평균(반올림 전). 모든 구성원 실패면 None
    members: dict[str, list[float | None]] = field(default_factory=dict)  # 구성원별 후처리 가격
    errors: dict[str, str] = field(default_factory=dict)


def _post(values, status='OK', error=''):
    """실험과 같은 §8.3 후처리 → 가격 7개(실패는 None)."""
    return [float(price) if s == 'OK' else None for _, price, s, _ in run_backtest.prediction_rows(values, status, error)]


def _pooled(snap, as_of: date, config_path: Path, log):
    from model_comparison.v2 import features as F
    from model_comparison.v2.run_pooled import Matrices

    config = json.loads(config_path.read_text(encoding='utf-8'))
    bundles = loader.check_bundles(config.get('bundles', []))
    blocks = [b for b in F.V2_BLOCKS if b in config.get('blocks', [])]
    if set(blocks) & set(F.NEEDS_EXTRA):
        raise ValueError(f'{config_path.name}: 서비스 입력에 없는 v2 추가 자료 묶음 {blocks}')
    window = int(config.get('window_days', standard.TRAIN_WINDOW_DAYS))
    started = time.perf_counter()
    mats = Matrices(snap, F.V2Features(snap, None, None), bundles, blocks)
    parts = [mats.training(sid, snap.series[sid].index(as_of), window) for sid in snap.series_ids]
    parts = [p for p in parts if p is not None]
    if not parts:
        raise loader.NoInput('학습 표본 없음')
    X, y, h, g, age = (np.concatenate([p[k] for p in parts]) for k in range(5))
    model = run_backtest.load_class(config['class'])(**config.get('params', {}))
    model.fit(X, y, h, mats.names, config.get('seed', 42), groups=g, ages=age)
    out = {}
    for sid in snap.series_ids:
        x = mats.inputs(sid, snap.series[sid].index(as_of))
        if x is None:
            out[sid] = ([None] * len(standard.HORIZONS), 'NO_INPUT')
            continue
        values = model.predict(x, np.array(standard.HORIZONS))
        out[sid] = (_post([None if np.isnan(v) else float(v) for v in values]), '')
    log(f'{config_path.stem}: 표본 {len(y)}개, {time.perf_counter() - started:.0f}s')
    return out, model, mats


def _arima(snap, as_of: date, log):
    name, path = ARIMA
    config = json.loads(path.read_text(encoding='utf-8'))
    bundles = loader.check_bundles(config.get('extra_features', []))
    cls = run_backtest.load_class(config['class'])
    out, started = {}, time.perf_counter()
    for sid in snap.series_ids:
        try:
            model = cls(**config['params'])
            model.fit(snap.training_data(sid, as_of, bundles), config.get('seed', 42))
            out[sid] = (_post(model.predict(snap.origin_inputs(sid, as_of, bundles))), '')
        except loader.NoInput:
            out[sid] = ([None] * len(standard.HORIZONS), 'NO_INPUT')
        except Exception as error:  # noqa: BLE001 — 한 계열 실패가 다른 계열을 막지 않게(실험과 같음)
            out[sid] = ([None] * len(standard.HORIZONS), type(error).__name__)
    log(f'{name}: {len(out)}계열, {time.perf_counter() - started:.0f}s')
    return out


def combine(members: dict[str, list[float | None]]) -> list[float | None]:
    """같은 비중 평균. 시점마다 값이 있는 구성원만 평균(ensemble.combine과 같은 규칙)."""
    result = []
    for i in range(len(standard.HORIZONS)):
        values = [m[i] for m in members.values() if m[i] is not None]
        result.append(float(np.mean(values)) if values else None)
    return result


def forecast(snap: loader.Snapshot, as_of: date, log=print) -> dict[int, SeriesForecast]:
    """스냅샷의 모든 계열을 as_of 기준으로 예측한다. 반환: 스냅샷 계열 id → SeriesForecast."""
    member_out, errors = {}, {}
    for name, path in POOLED.items():
        try:
            member_out[name] = _pooled(snap, as_of, path, log)[0]
        except Exception as error:  # noqa: BLE001
            errors[name] = type(error).__name__
            log(f'{name} 실패: {type(error).__name__}: {error}')
    try:
        member_out[ARIMA[0]] = _arima(snap, as_of, log)
    except Exception as error:  # noqa: BLE001
        errors[ARIMA[0]] = type(error).__name__
        log(f'{ARIMA[0]} 실패: {type(error).__name__}: {error}')
    result = {}
    for sid in snap.series_ids:
        s = snap.series[sid]
        members = {name: out[sid][0] for name, out in member_out.items()}
        member_errors = {**errors, **{name: out[sid][1] for name, out in member_out.items() if out[sid][1]}}
        result[sid] = SeriesForecast(sid, s.item, s.market, combine(members), members, member_errors)
    return result
