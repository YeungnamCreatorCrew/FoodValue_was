"""v2 KREI 묶음: KREI 관측월보 스냅샷(데이터 담당 제공) → 계열·기준일 특징.

스냅샷 폴더(기본 data/snapshots/FoodValue_KREI_Snapshot_20261118/)에서 읽는 것
- manifest.json: snapshot_id, values_rows (행 수 확인)
- krei_values.csv: 수치 1행 = 사실 1개. 쓰는 열: source_record_key, available_from, item_name, crop_type, metric,
  kind, target_start, target_end, basis, value, value_low, value_high, direction
  (데이터 담당과 맞춘 형식. 수정판은 새 snapshot_id 폴더로 받아 --krei로 지정)

시점 규칙
- 다른 추가 자료와 같이 d−1까지: available_from의 날짜 ≤ d−1 인 호만 기준일 d에서 쓴다.
- standard.DATA_CUTOFF 뒤에 공개된 호는 읽지 않는다.
- target_start/target_end(연산 01-01~12-31 등)는 공개 시점 판단에 쓰지 않는다.

특징(추출기 2종에 모두 있는 핵심 수치만 — 2025-03 이후 엽근 재추출 전에도 같은 의미)
- krei_price_outlook_chg   이번 달 도매가격 전망(LEVEL) ÷ 지난달 도매가격 실적(LEVEL) − 1. 같은 호·같은 단위라 단위 무관
- krei_implied_vs_current  우리 계열의 '지난달 실적 기간' 평균 가격 × (1 + 위 변화) ÷ 현재 가격 − 1
                           (KREI 전망을 우리 계열 가격 수준에 옮긴 것. 소매 계열도 같은 방법)
- krei_price_dir_py/nm     가격 전망의 전년/평년 대비 방향 +1·0·−1
- krei_shipment_py         이번 달 전체 출하량 전망의 전년 대비 %(작형 구분 없는 행만)
- krei_days_since          최신 호 공개 후 경과일(1·2월 미발행 기간에는 커진다)
값이 없거나 전망 대상 달(target_end)이 기준일 전에 끝났으면 NaN(12월 전망을 2월에 쓰지 않음).
"""
import csv
import json
import math
from datetime import date, datetime, timedelta
from pathlib import Path

import numpy as np

from tools import standard

ROOT = Path(__file__).resolve().parents[2]
SNAPSHOT_ID = 'FoodValue_KREI_Snapshot_20261118'
KREI_DIR = ROOT / 'data' / 'snapshots' / SNAPSHOT_ID
NAMES = ('krei_price_outlook_chg', 'krei_implied_vs_current', 'krei_price_dir_py', 'krei_price_dir_nm',
         'krei_shipment_py', 'krei_days_since')
# 우리 계열 품목 → (KREI 품목, 도매가격 행의 crop_type). 출하량은 작형 구분 없는 행(crop_type 빈 값)만 쓴다
ITEM_MAP = {'대파': ('대파', ''), '양파': ('양파', ''), '깐마늘': ('마늘', '깐마늘'), '배추': ('배추', ''), '무': ('무', '')}
DIRECTION = {'UP': 1.0, 'FLAT': 0.0, 'DOWN': -1.0}
COLUMNS = ('source_record_key', 'available_from', 'item_name', 'crop_type', 'metric', 'kind', 'target_start',
           'target_end', 'basis', 'value', 'value_low', 'value_high', 'direction')


def _value(row):
    """value, 없으면 범위 중간값, 둘 다 없으면 nan."""
    if row['value'] not in ('', None):
        return float(row['value'])
    if row['value_low'] not in ('', None) and row['value_high'] not in ('', None):
        return (float(row['value_low']) + float(row['value_high'])) / 2
    return math.nan


class KreiSnapshot:
    def __init__(self, folder: Path, cutoff: date = standard.DATA_CUTOFF):
        folder = Path(folder)
        if not (folder / 'krei_values.csv').exists():
            raise FileNotFoundError(f'KREI 스냅샷 폴더가 없음: {folder}')
        self.manifest = json.loads((folder / 'manifest.json').read_text(encoding='utf-8'))
        with open(folder / 'krei_values.csv', encoding='utf-8-sig', newline='') as f:
            rows = list(csv.DictReader(f))
        missing = [c for c in COLUMNS if rows and c not in rows[0]]
        if missing:
            raise ValueError(f'krei_values.csv에 필요한 열이 없음: {missing}')
        if 'values_rows' in self.manifest and self.manifest['values_rows'] != len(rows):
            raise ValueError(f'krei_values.csv 행 수 {len(rows)} ≠ manifest values_rows {self.manifest["values_rows"]}')
        reports = {}
        for r in rows:
            moment = datetime.fromisoformat(r['available_from'])
            if moment.date() > cutoff:
                continue
            reports.setdefault(r['source_record_key'], (moment, []))[1].append(r)
        self.reports = sorted(reports.values(), key=lambda x: x[0])  # [(available_from, rows)]
        self.dropped_after_cutoff = len({r['source_record_key'] for r in rows}) - len(reports)
        self._summary = {}

    def summary(self, item: str):
        """품목의 호별 요약 [(사용 가능 첫 기준일, 공개일, dict)]. 그 품목 행이 없는 호는 뺀다."""
        if item in self._summary:
            return self._summary[item]
        name, crop = ITEM_MAP[item]
        out = []
        for moment, rows in self.reports:
            mine = [r for r in rows if r['item_name'] == name]
            if not mine:
                continue
            price = [r for r in mine if r['metric'] == 'WHOLESALE_PRICE' and r['crop_type'] == crop]
            outlook = sorted((r for r in price if r['kind'] == 'OUTLOOK' and r['basis'] == 'LEVEL'),
                             key=lambda r: r['target_start'])
            actual = sorted((r for r in price if r['kind'] == 'ACTUAL' and r['basis'] == 'LEVEL'),
                            key=lambda r: r['target_start'])
            s = {'outlook': math.nan, 'actual': math.nan, 'actual_period': None, 'dir_py': math.nan,
                 'dir_nm': math.nan, 'shipment_py': math.nan, 'outlook_end': None, 'shipment_end': None}
            if outlook:
                o = outlook[0]
                s['outlook'] = _value(o)
                s['outlook_end'] = date.fromisoformat(o['target_end'])
                for basis, key in (('PREV_YEAR', 'dir_py'), ('NORMAL', 'dir_nm')):
                    d = [r for r in price if r['kind'] == 'OUTLOOK' and r['basis'] == basis
                         and r['target_start'] == o['target_start'] and r['direction'] in DIRECTION]
                    if d:
                        s[key] = DIRECTION[d[0]['direction']]
            if actual:
                a = actual[-1]
                s['actual'] = _value(a)
                s['actual_period'] = (date.fromisoformat(a['target_start']), date.fromisoformat(a['target_end']))
            ship = sorted((r for r in mine if r['metric'] == 'SHIPMENT' and r['kind'] == 'OUTLOOK'
                           and r['basis'] == 'PREV_YEAR' and r['crop_type'] == ''), key=lambda r: r['target_start'])
            if ship:
                s['shipment_py'] = _value(ship[0])
                s['shipment_end'] = date.fromisoformat(ship[0]['target_end'])
            out.append((moment.date() + timedelta(days=standard.EXTRA_LAG_DAYS), moment.date(), s))
        self._summary[item] = out
        return out

    def features(self, item: str, start: date, filled):
        """계열 하나의 기준일별 특징 행렬(행 i = 기준일 start+i, 열 = NAMES)."""
        filled = np.asarray(filled, dtype=float)
        n = len(filled)
        out = np.full((n, len(NAMES)), np.nan)
        reports = self.summary(item)
        if not reports:
            return out
        firsts = [(first - start).days for first, _, _ in reports]  # 이 위치부터 사용 가능
        k = -1
        for i in range(n):
            while k + 1 < len(reports) and firsts[k + 1] <= i:
                k += 1
            if k < 0:
                continue
            _, published, s = reports[k]
            d = start + timedelta(days=i)
            chg = s['outlook'] / s['actual'] - 1 if s['actual'] and not math.isnan(s['actual']) else math.nan
            implied = math.nan
            if s['actual_period'] is not None and not math.isnan(chg) and not math.isnan(filled[i]):
                lo = max((s['actual_period'][0] - start).days, 0)
                hi = min((s['actual_period'][1] - start).days, i)  # 기준일 d 이후 가격은 쓰지 않는다
                if hi >= lo:
                    window = filled[lo:hi + 1]
                    if (~np.isnan(window)).sum() >= 5:
                        implied = np.nanmean(window) * (1 + chg) / filled[i] - 1
            dir_py, dir_nm, ship = s['dir_py'], s['dir_nm'], s['shipment_py']
            if s['outlook_end'] is None or d > s['outlook_end']:  # 전망 대상 달이 지났으면 전망 값은 쓰지 않는다
                chg = implied = dir_py = dir_nm = math.nan
            if s['shipment_end'] is None or d > s['shipment_end']:
                ship = math.nan
            out[i] = (chg, implied, dir_py, dir_nm, ship, float((d - published).days))
        return out
