"""가격 배치에서 v2 앙상블·struct 모델을 쓰는 연결부. .env FOODVALUE_PRICE_MODEL=v2 일 때만 켜진다(기본 v5).

- 대상 계열: 실험 품목(대파·양파·깐마늘 KAMIS 계열, 배추·무 MERGED 계열)의 소매·도매. 나머지(작형별 원본 등)는 v5 그대로.
- 트랙 두 개를 따로 저장한다(price_model_run.model_track).
  - ENSEMBLE: v2 앙상블(app.services.v2_ensemble). 기본 공개.
  - STRUCT: 구조적 가격 전달 모델(app.services.struct_service, PR #71). API ?model=STRUCT로 공개. FOODVALUE_STRUCT_MODEL=0이면 끈다.
- 한 기준일에 한 번만 DB → 스냅샷을 만들고 두 트랙을 모두 예측해 프로세스 안에서 재사용한다(배치가 계열마다 불러도 학습 1회).
- 공개 기준: 트랙마다 자기 검증 실적(app.services.v2_calibration 형식). 그 트랙이 naive보다 나빴던(같았던) 계열은
  BASELINE(직전 가격 유지)으로 공개한다. struct 도매는 설계상 naive라 항상 BASELINE이다.
- 결과는 기존 배치와 같은 Prediction 형식이라 저장·API·화면은 그대로 쓴다.
- 7일 뒤 예측의 요인: 앙상블은 XGB·LGBM TreeSHAP 평균 + AutoARIMA 몫, struct는 항별 원 단위 분해.
"""
import os
import tempfile
from dataclasses import dataclass
from datetime import date
from pathlib import Path

from app.models.price import ENSEMBLE, STRUCT
from app.services import struct_service, v2_calibration, v2_ensemble, v2_snapshot
from app.services.price_prediction import InsufficientDataError, Prediction
from tools import loader, snapshot, standard

ENV = 'FOODVALUE_PRICE_MODEL'
STRUCT_ENV = 'FOODVALUE_STRUCT_MODEL'
MERGED_ITEMS = ('배추', '무')


@dataclass(frozen=True)
class Track:
    calibration: Path
    model_name: str  # 검증 통과 계열의 model_name. 아니면 LAST_PRICE
    version: str
    engine: str


TRACKS = {ENSEMBLE: Track(v2_calibration.PATH, 'V2_ENSEMBLE', v2_ensemble.MODEL_VERSION, 'v2'),
          STRUCT: Track(struct_service.CALIBRATION_PATH, struct_service.MODEL_NAME, struct_service.MODEL_VERSION, 'struct')}
_cache: dict[date, dict[str, dict | Exception]] = {}


def enabled() -> bool:
    return os.getenv(ENV, 'v5').strip().lower() == 'v2'


def struct_enabled() -> bool:
    return enabled() and os.getenv(STRUCT_ENV, '1').strip() != '0'


def series_key(item_name: str, source: str, market: str) -> str | None:
    if source == 'KAMIS' and item_name in snapshot.DIRECT_ITEMS:
        return v2_calibration.key(item_name, market)
    if source == 'MERGED' and item_name in MERGED_ITEMS:
        return v2_calibration.key(item_name, market)
    return None


def _keyed(result: dict) -> dict:
    return {v2_calibration.key(f.item, f.market): f for f in result.values()}


def forecasts(engine, base_date: date, log=print, track: str = ENSEMBLE) -> dict:
    """기준일의 10계열 예측(키 '품목|시장'). 같은 프로세스에서 같은 기준일이면 다시 학습하지 않는다.
    스냅샷은 한 번 만들어 켜진 트랙을 모두 예측한다. 한 트랙의 오류는 그 트랙을 요청할 때만 다시 던진다."""
    if base_date not in _cache:
        runners = {ENSEMBLE: v2_ensemble.forecast}
        if struct_enabled() or track == STRUCT:
            runners[STRUCT] = struct_service.forecast
        entry = {}
        with tempfile.TemporaryDirectory(prefix='fv-v2-') as folder:
            out = Path(folder) / 'snapshot'
            v2_snapshot.build(engine, base_date, out)
            snap = loader.Snapshot(out)
            for name, runner in runners.items():
                try:
                    entry[name] = _keyed(runner(snap, base_date, log))
                except Exception as error:  # noqa: BLE001 — 한 트랙 실패가 다른 트랙을 막지 않는다
                    entry[name] = error
                    log(f'{name} 예측 실패: {type(error).__name__}: {error}')
        _cache.clear()
        _cache[base_date] = entry
    result = _cache[base_date].get(track)
    if result is None:
        raise RuntimeError(f'{track} 트랙 예측이 꺼져 있습니다')
    if isinstance(result, Exception):
        raise result
    return result


def prediction(engine, key: str, base_date: date, last_price: int, track: str = ENSEMBLE) -> Prediction:
    spec = TRACKS[track]
    calibration = v2_calibration.load(spec.calibration)
    if calibration is None:
        command = 'python -m app.v2_calibrate' if track == ENSEMBLE else 'python -m app.struct_calibrate'
        raise RuntimeError(f'{track} 검증 실적 파일이 없습니다: {spec.calibration} ({command})')
    entry = calibration['series'].get(key)
    forecast = forecasts(engine, base_date, track=track).get(key)
    if forecast is None or any(p is None for p in forecast.prices):
        raise InsufficientDataError(f'{track} 예측 없음(최근 가격 부족·오래됨)')
    validated = bool(entry) and entry['verdict'] == 'VALIDATED'
    model = spec.model_name if validated else 'LAST_PRICE'
    raw = forecast.prices if validated else [float(last_price)] * len(standard.HORIZONS)
    prices = [int(round(p)) for p in raw]
    bounds = [v2_calibration.interval(entry, h, p, naive=not validated) for h, p in zip(standard.HORIZONS, raw)]
    lower = [None if lo is None else max(0, int(round(lo))) for lo, _ in bounds]
    upper = [None if hi is None else int(round(hi)) for _, hi in bounds]
    # 화면 실적 배지: 공개한 방식의 실적. 직전 가격 유지로 공개하면 그 방식의 오차(naive)를 보여 준다.
    validation = ({'mape': entry['mape'] if validated else entry['naiveMape'], 'naiveMape': entry['naiveMape'],
                   'improvementPct': entry['improvementPct'] if validated else 0.0,
                   'within5Pct': entry['within5Pct'] if validated else None, 'points': entry['points']}
                  if entry else {})
    evaluation = {model: {'mape': entry['mape'] if validated else entry['naiveMape']} if entry else {'mape': None}}
    model_prices = [round(p, 2) for p in forecast.prices]
    extra = ({'ensemblePrices': model_prices} if track == ENSEMBLE else
             {'structPrices': model_prices, 'parameters': forecast.parameters,
              'configSha256': calibration.get('configSha256')})
    metrics = {
        'engine': spec.engine, 'modelTrack': track, 'modelVersion': spec.version, 'selectedModel': model,
        'evaluation': evaluation, 'validation': validation,
        'evaluationStart': calibration['evaluationStart'], 'evaluationEnd': calibration['evaluationEnd'],
        **extra,
        'members': {name: [None if v is None else round(v, 2) for v in values] for name, values in forecast.members.items()},
        'memberErrors': forecast.errors, 'intervalMethod': 'validation_ratio_quantile', 'nominalCoverage': .95,
        **({'explanationError': forecast.explanation_error} if forecast.explanation_error else {}),
    }
    explanation = forecast.explanation if validated else None  # 직전 가격 유지로 공개하면 설명할 모델이 없다(v5와 같음)
    if explanation is not None:
        explanation.predicted_price = prices[explanation.horizon - 1]
    return Prediction(model, 'VALIDATED' if validated else 'BASELINE', prices, lower, upper, metrics, explanation)
