"""v2 앙상블의 계열별 검증 실적·예측 구간(서비스 공개 기준).

검증 구간(기준서 v1 검증 244 기준일) 앙상블 예측으로 계열(품목 × 시장)마다:
- 채택: 앙상블 MAPE < 직전 가격(naive) MAPE 이면 VALIDATED, 아니면 BASELINE(서비스는 직전 가격을 그대로 보여 줌).
  실험 평가기(tools.evaluate)와 같은 점·같은 정책(실패한 점은 naive로 대체)으로 계산한다.
- 예측 구간: 시점별 실제/예측 비율의 분위수(80%: 10~90, 95%: 2.5~97.5). 서비스 예측가에 곱해 하한·상한을 만든다.
- 화면 배지용 숫자: MAPE, naive MAPE, 개선율, ±5% 안에 든 비율.

계열 id는 DB마다 다를 수 있어 '품목|시장' 키로 저장한다. 파일: model_comparison/v2/service/calibration.json
만들기: python -m app.v2_calibrate <XGB 검증 폴더> <LGBM 검증 폴더> <ARIMA 검증 폴더>
"""
import json
from collections import defaultdict
from pathlib import Path

import numpy as np

from tools import evaluate, standard

ROOT = Path(__file__).resolve().parents[2]
PATH = ROOT / 'model_comparison' / 'v2' / 'service' / 'calibration.json'
QUANTILES = {'80': (10, 90), '95': (2.5, 97.5)}


def key(item: str, market: str) -> str:
    return f'{item}|{market}'


def _bounds(values):
    values = np.array(values)
    if not values.size:
        return None
    return {level: [round(float(np.percentile(values, lo)), 6), round(float(np.percentile(values, hi)), 6)]
            for level, (lo, hi) in QUANTILES.items()}


def build(snap, member_folders) -> dict:
    from model_comparison.v2 import ensemble

    rows = ensemble.combine([Path(f) for f in member_folders])
    points = evaluate.points_for(rows, snap)

    def policy(p):
        return p['pred'] if p['ok'] else p['naive']

    summary = evaluate.summarize(points, policy)
    ratios, naive_ratios = defaultdict(list), defaultdict(list)
    within = defaultdict(lambda: [0, 0])
    for p in points:
        yhat = policy(p)
        ratios[p['series_id'], p['horizon']].append(p['y'] / yhat)
        naive_ratios[p['series_id'], p['horizon']].append(p['y'] / p['naive'])
        hit = within[p['series_id']]
        hit[0] += abs(p['y'] - yhat) / p['y'] <= .05
        hit[1] += 1
    series = {}
    for sid, stats in summary['series'].items():
        s = snap.series[int(sid)]
        intervals = {str(h): _bounds(ratios[int(sid), h]) for h in standard.HORIZONS}
        naive_intervals = {str(h): _bounds(naive_ratios[int(sid), h]) for h in standard.HORIZONS}
        series[key(s.item, s.market)] = {
            'verdict': 'VALIDATED' if stats['win'] else 'BASELINE',
            'mape': stats['mape'], 'naiveMape': stats['naive_mape'],
            'improvementPct': stats['relative_improvement_pct'], 'points': stats['points'],
            'within5Pct': round(within[int(sid)][0] / within[int(sid)][1] * 100, 2) if within[int(sid)][1] else None,
            'intervals': intervals, 'naiveIntervals': naive_intervals,
        }
    first = min(p['origin'] for p in points)
    last = max(p['origin'] for p in points)
    return {'members': [Path(f).name for f in member_folders], 'dataVersion': standard.DATA_VERSION,
            'evaluationStart': first.isoformat(), 'evaluationEnd': last.isoformat(),
            'macroMape': summary['macro_mape'], 'naiveMacroMape': summary['naive_macro_mape'],
            'improvementPct': summary['relative_improvement_pct'], 'series': series}


def load(path: Path = PATH) -> dict | None:
    return json.loads(path.read_text(encoding='utf-8')) if path.exists() else None


def interval(entry: dict | None, horizon: int, price: float, level: str = '95', naive: bool = False):
    """예측가 × 검증 비율 분위수 → (하한, 상한). naive=True면 직전 가격 기준 구간. 자료가 없으면 (None, None)."""
    bounds = ((entry or {}).get('naiveIntervals' if naive else 'intervals') or {}).get(str(horizon)) or {}
    if level not in bounds:
        return None, None
    lo, hi = bounds[level]
    return price * lo, price * hi
