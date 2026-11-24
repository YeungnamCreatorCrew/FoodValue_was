"""가격 배치에서 v2 앙상블을 쓰는 연결부. .env FOODVALUE_PRICE_MODEL=v2 일 때만 켜진다(기본 v5).

- 대상 계열: 실험 품목(대파·양파·깐마늘 KAMIS 계열, 배추·무 MERGED 계열)의 소매·도매. 나머지(작형별 원본 등)는 v5 그대로.
- 한 기준일에 한 번만 DB → 스냅샷 → 10계열 예측을 하고 프로세스 안에서 재사용한다(배치가 계열마다 불러도 학습 1회).
- 공개 기준: 검증 실적(app.services.v2_calibration). 앙상블이 naive보다 나빴던 계열은 BASELINE(직전 가격 유지)으로 공개.
- 결과는 기존 배치와 같은 Prediction 형식이라 저장·API·화면은 그대로 쓴다. SHAP 설명은 아직 없다(explanation=None).
"""
import os
import tempfile
from datetime import date
from pathlib import Path

from app.services import v2_calibration, v2_ensemble, v2_snapshot
from app.services.price_prediction import InsufficientDataError, Prediction
from tools import loader, snapshot, standard

ENV = 'FOODVALUE_PRICE_MODEL'
MERGED_ITEMS = ('배추', '무')
_cache: dict[date, dict] = {}


def enabled() -> bool:
    return os.getenv(ENV, 'v5').strip().lower() == 'v2'


def series_key(item_name: str, source: str, market: str) -> str | None:
    if source == 'KAMIS' and item_name in snapshot.DIRECT_ITEMS:
        return v2_calibration.key(item_name, market)
    if source == 'MERGED' and item_name in MERGED_ITEMS:
        return v2_calibration.key(item_name, market)
    return None


def forecasts(engine, base_date: date, log=print) -> dict[str, v2_ensemble.SeriesForecast]:
    """기준일의 10계열 예측(키 '품목|시장'). 같은 프로세스에서 같은 기준일이면 다시 학습하지 않는다."""
    if base_date not in _cache:
        with tempfile.TemporaryDirectory(prefix='fv-v2-') as folder:
            out = Path(folder) / 'snapshot'
            v2_snapshot.build(engine, base_date, out)
            snap = loader.Snapshot(out)
            result = v2_ensemble.forecast(snap, base_date, log)
        _cache.clear()
        _cache[base_date] = {v2_calibration.key(f.item, f.market): f for f in result.values()}
    return _cache[base_date]


def prediction(engine, key: str, base_date: date, last_price: int) -> Prediction:
    calibration = v2_calibration.load()
    if calibration is None:
        raise RuntimeError(f'v2 검증 실적 파일이 없습니다: {v2_calibration.PATH} (python -m app.v2_calibrate)')
    entry = calibration['series'].get(key)
    forecast = forecasts(engine, base_date).get(key)
    if forecast is None or any(p is None for p in forecast.prices):
        raise InsufficientDataError('v2 앙상블 예측 없음(최근 가격 부족·오래됨)')
    validated = bool(entry) and entry['verdict'] == 'VALIDATED'
    model = 'V2_ENSEMBLE' if validated else 'LAST_PRICE'
    raw = forecast.prices if validated else [float(last_price)] * len(standard.HORIZONS)
    prices = [int(round(p)) for p in raw]
    bounds = [v2_calibration.interval(entry, h, p, naive=not validated) for h, p in zip(standard.HORIZONS, raw)]
    lower = [None if lo is None else max(0, int(round(lo))) for lo, _ in bounds]
    upper = [None if hi is None else int(round(hi)) for _, hi in bounds]
    validation = {k: entry.get(k) for k in ('mape', 'naiveMape', 'improvementPct', 'within5Pct', 'points')} if entry else {}
    evaluation = {model: {'mape': entry['mape'] if validated else entry['naiveMape']} if entry else {'mape': None}}
    metrics = {
        'engine': 'v2', 'modelVersion': v2_ensemble.MODEL_VERSION, 'selectedModel': model,
        'evaluation': evaluation, 'validation': validation,
        'evaluationStart': calibration['evaluationStart'], 'evaluationEnd': calibration['evaluationEnd'],
        'ensemblePrices': [round(p, 2) for p in forecast.prices],
        'members': {name: [None if v is None else round(v, 2) for v in values] for name, values in forecast.members.items()},
        'memberErrors': forecast.errors, 'intervalMethod': 'validation_ratio_quantile', 'nominalCoverage': .95,
    }
    return Prediction(model, 'VALIDATED' if validated else 'BASELINE', prices, lower, upper, metrics)
