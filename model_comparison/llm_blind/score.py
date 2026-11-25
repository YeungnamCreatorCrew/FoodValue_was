"""잠긴 LLM 예측 채점. 잠금 해시가 다르거나 잠기지 않은 기준일이 있으면 거부한다.

사용: uv run python -m model_comparison.llm_blind.score dev|eval [--shrink 0.5]
- 예측가 = round(naive × (1 + pct/100) 를 shrink 배 한 변화율)
- 평가 대상: 목표일 실제 가격이 있고 naive가 계산되는 점(기준서 §8.1)
- 비교: naive, mean7, (eval) 앙상블 ens-val-base-arima-validation-20261119-01
"""
from __future__ import annotations

import argparse
import csv
import json
import random
from collections import defaultdict
from datetime import date, timedelta
from pathlib import Path

from model_comparison.llm_blind.protocol import ROOT, SERIES, locks, origins, sha
from tools.loader import Snapshot

ENS = Path('experiments_v2/ens-val-base-arima-validation-20261119-01/predictions.csv')
NAMES = {1: '대파 소매', 2: '대파 도매', 8: '양파 소매', 7: '양파 도매', 10: '깐마늘 소매', 9: '깐마늘 도매',
         9001: '배추 소매', 9002: '배추 도매', 9011: '무 소매', 9012: '무 도매'}


def load_preds(kind):
    held = locks()
    out = {}
    for d in origins(kind):
        path = ROOT / 'preds' / kind / f'{d}.csv'
        assert held.get((kind, d)) == sha(path), f'{d}: 잠기지 않았거나 잠금 뒤 바뀜'
        with open(path) as f:
            for r in csv.DictReader(f):
                out[(int(r['series_id']), d)] = [float(r[f'h{h}']) for h in range(1, 8)]
    return out


def load_ens(wanted):
    out = {}
    if not ENS.exists():
        return out
    with open(ENS) as f:
        for r in csv.DictReader(f):
            if r['origin_date'] in wanted:
                # 실패(NO_INPUT 등)는 기준서 §8.2 policy대로 naive로 대체하도록 None으로 표시
                out[(int(r['series_id']), r['origin_date'], int(r['horizon']))] = (
                    float(r['predicted_price']) if r['predicted_price'] else None)
    return out


def rnd(x):
    return max(1.0, float(int(x + 0.5)))


def points(kind, shrink):
    snap = Snapshot('data/snapshots/fv-snap-20261031-v1')
    preds = load_preds(kind)
    ens = load_ens(set(origins(kind)))
    pts = []
    for (sid, d), pct in preds.items():
        od = date.fromisoformat(d)
        naive = snap.naive(sid, od)
        if naive is None:
            continue
        m7 = snap.mean7(sid, od)
        for h in range(1, 8):
            y = snap.actual_price(sid, od + timedelta(days=h))
            if y is None:
                continue
            p = {'llm': rnd(naive * (1 + shrink * pct[h - 1] / 100)), 'naive': rnd(naive),
                 'mean7': rnd(m7) if m7 else rnd(naive)}
            if (sid, d, h) in ens:
                p['ensemble'] = ens[(sid, d, h)] if ens[(sid, d, h)] is not None else p['naive']
            pts.append({'sid': sid, 'origin': d, 'h': h, 'y': y, 'pct': pct[h - 1], 'actual_pct': (y / naive - 1) * 100, **p})
    return pts


def macro(pts, model):
    by = defaultdict(list)
    for p in pts:
        if model in p:
            by[p['sid']].append(abs(p['y'] - p[model]) / p['y'] * 100)
    per = {sid: sum(v) / len(v) for sid, v in by.items()}
    return sum(per.values()) / len(per), per


def bootstrap(pts, model, n=1000, seed=0):
    months = sorted({p['origin'][:7] for p in pts})
    groups = defaultdict(list)
    for p in pts:
        groups[p['origin'][:7]].append(p)
    rng = random.Random(seed)
    deltas = []
    for _ in range(n):
        sample = [q for m in (rng.choice(months) for _ in months) for q in groups[m]]
        a, _ = macro(sample, 'naive')
        b, _ = macro(sample, model)
        deltas.append(a - b)
    deltas.sort()
    return deltas[int(0.025 * n)], deltas[int(0.975 * n)]


def report(kind, shrink):
    pts = points(kind, shrink)
    models = ['naive', 'mean7', 'llm'] + (['ensemble'] if any('ensemble' in p for p in pts) else [])
    if 'ensemble' in models:
        pts = [p for p in pts if 'ensemble' in p]  # 같은 점만 비교
    res = {'kind': kind, 'shrink': shrink, 'points': len(pts), 'origins': len({p['origin'] for p in pts}), 'models': {}}
    base, base_per = macro(pts, 'naive')
    for m in models:
        mac, per = macro(pts, m)
        wins = sum(1 for sid in per if per[sid] < base_per[sid])
        lo, hi = bootstrap(pts, m) if m != 'naive' else (0, 0)
        res['models'][m] = {'macro_mape': round(mac, 4), 'vs_naive_pct': round((base - mac) / base * 100, 2),
                            'series_wins': wins, 'boot95_delta_pp': [round(lo, 4), round(hi, 4)],
                            'per_series': {NAMES[s]: round(per[s], 3) for s in SERIES if s in per}}
    hz = {}
    for h in range(1, 8):
        sub = [p for p in pts if p['h'] == h]
        if not sub:
            continue
        hz[h] = {m: round(macro(sub, m)[0], 3) for m in models}
    res['by_horizon'] = hz
    # 방향 적중: LLM이 움직임을 예측한 점(|pct|>=0.5)에서 실제 방향이 같은 비율
    moved = [p for p in pts if abs(p['pct']) >= 0.5 and abs(p['actual_pct']) > 0]
    res['direction_hit'] = round(sum(1 for p in moved if (p['pct'] > 0) == (p['actual_pct'] > 0)) / max(1, len(moved)), 3)
    res['direction_n'] = len(moved)
    return res, pts


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('kind')
    ap.add_argument('--shrink', type=float, default=1.0)
    ap.add_argument('--save', action='store_true')
    a = ap.parse_args()
    res, pts = report(a.kind, a.shrink)
    print(json.dumps(res, ensure_ascii=False, indent=1))
    if a.save:
        (ROOT / f'result_{a.kind}_s{a.shrink}.json').write_text(json.dumps(res, ensure_ascii=False, indent=1))
        with open(ROOT / f'points_{a.kind}_s{a.shrink}.csv', 'w', newline='') as f:
            w = csv.DictWriter(f, fieldnames=list(pts[0].keys()))
            w.writeheader()
            w.writerows(pts)


if __name__ == '__main__':
    main()
