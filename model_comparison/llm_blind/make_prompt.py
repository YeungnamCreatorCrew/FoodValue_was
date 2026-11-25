"""LLM 블라인드 예측용 프롬프트 생성기.

기준일 d 하나에 대해 10개 계열의 '그 시점에 알 수 있던 정보'만 담은 프롬프트를 파일로 쓴다.
- 자기 계열 가격: price_date <= d
- 상대 시장 가격·전국 기상: <= d-1 (기준서 §3.1)
- KREI 관측 월보: available_from <= d 23:00 KST
- 달력(요일·휴장·명절)은 미리 확정된 정보라 목표일 값 사용
- 연도는 모두 가린다(날짜는 D-n, 요일, 월-일로만 표시). 모델의 사전 기억으로 시기를 특정하지 못하게 하기 위함

stdout에는 출력 경로 외에 아무것도 쓰지 않는다(정답 노출 방지).
사용: uv run python -m model_comparison.llm_blind.make_prompt 2024-11-04 [--out DIR]
"""
from __future__ import annotations

import argparse
import csv
import re
from datetime import date, datetime, timedelta
from pathlib import Path
from statistics import mean

SNAP = Path('data/snapshots/fv-snap-20261031-v1')
KREI = Path('data/snapshots/FoodValue_KREI_Snapshot_20261118_r2/krei_values.csv')
WD = '월화수목금토일'
COUNTERPART = {1: 2, 2: 1, 7: 8, 8: 7, 9: 10, 10: 9, 9001: 9002, 9002: 9001, 9011: 9012, 9012: 9011}
ORDER = [1, 2, 8, 7, 10, 9, 9001, 9002, 9011, 9012]
KREI_ITEM = {'대파': '대파', '양파': '양파', '깐마늘': '마늘', '배추': '배추', '무': '무'}
KIND_NAME = {'06': '월동', '01': '봄', '02': '고랭지', '03': '가을'}
YEAR_RE = re.compile(r"(19|20)\d{2}\s*년\s*|(?<!\d)(19|20)\d{2}(?=[./-]\d)|['’]\d{2}\s*년\s*|(?<!\d)(19|20)\d{2}(?!\d)")


def rows(name):
    with open(SNAP / name, encoding='utf-8') as f:
        return list(csv.DictReader(f))


def load(d: date):
    """d 이전 자료만 남긴 사전을 돌려준다. 미래 날짜는 처음부터 버린다."""
    meta = {int(r['series_id']): r for r in rows('price_series.csv')}
    prices, kinds, switches = {}, {}, {}
    for r in rows('price_daily.csv') + rows('price_daily_merged.csv'):
        day = date.fromisoformat(r['price_date'])
        if day > d:
            continue
        sid = int(r['series_id'])
        prices.setdefault(sid, {})[day] = int(r['price'])
        if 'kind_code' in r:
            kinds.setdefault(sid, {})[day] = r['kind_code']
            if r['kind_switch'] == '1':
                switches.setdefault(sid, []).append(day)
    weather = {}
    for r in rows('weather_daily.csv'):
        day = date.fromisoformat(r['weather_date'])
        if day <= d - timedelta(days=1):
            weather[day] = r
    calendar = {date.fromisoformat(r['cal_date']): r for r in rows('calendar_day.csv')}
    events = [r for r in rows('calendar_event.csv')]
    krei = []
    limit = datetime.fromisoformat(f'{d.isoformat()}T23:00:00+09:00')
    with open(KREI, encoding='utf-8-sig') as f:
        for r in csv.DictReader(f):
            if datetime.fromisoformat(r['available_from']) <= limit:
                krei.append(r)
    for sid, p in prices.items():
        assert max(p) <= d
    return meta, prices, kinds, switches, weather, calendar, events, krei


def short(day: date, d: date) -> str:
    n = (day - d).days
    return f"{'D' if n == 0 else f'D{n:+d}'}{WD[day.weekday()]}"


def rel(day: date, d: date) -> str:
    n = (day - d).days
    tag = 'D' if n == 0 else (f'D{n:+d}')
    return f'{tag}({WD[day.weekday()]} {day.month:02d}-{day.day:02d})'


def fmt(x) -> str:
    return f'{x:,.0f}'


def pct(a, b):
    return (b / a - 1) * 100


def nearest(p: dict, day: date, back=7):
    for k in range(back + 1):
        if day - timedelta(days=k) in p:
            return p[day - timedelta(days=k)]
    return None


def window_mean(p, start: date, end: date):
    vals = [v for k, v in p.items() if start <= k <= end]
    return mean(vals) if vals else None


def series_block(sid, d, meta, prices, kinds, switches):
    m = meta[sid]
    p = prices[sid]
    unit = f"{m['unit_quantity']}{m['unit']}"
    market = '소매' if m['market'] == 'RETAIL' else '도매'
    last_day = max(p)
    cur = p[last_day]
    lines = [f"### [{sid}] {m['item']} {market} (단위 {unit})"]
    head = f"현재가(마지막 관측 {rel(last_day, d)}) = {fmt(cur)}원"
    if sid in kinds:
        k = kinds[sid].get(last_day)
        sw = [s for s in switches.get(sid, []) if s <= d]
        since = (d - max(sw)).days if sw else None
        head += f" | 현재 작형 {KIND_NAME.get(k, k)}, 작형 전환 후 {since}일"
    lines.append(head)
    recent = sorted(k for k in p if k > d - timedelta(days=28))
    lines.append('최근 4주 관측: ' + ', '.join(f"{short(k, d)} {fmt(p[k])}" for k in recent))
    weekly = []
    for w in range(25, -1, -1):
        e = d - timedelta(days=7 * w)
        v = window_mean(p, e - timedelta(days=6), e)
        weekly.append('-' if v is None else fmt(v))
    lines.append('주간 평균(26주 전 → 이번 주): ' + ' '.join(weekly))
    for y in (1, 2, 3):
        base = d - timedelta(days=364 * y)
        b0 = nearest(p, base)
        b_prev = window_mean(p, base - timedelta(days=34), base - timedelta(days=28))
        nxt = [nearest(p, base + timedelta(days=h), back=0) for h in range(1, 8)]
        nxt_ok = [v for v in nxt if v is not None]
        if b0 is None or not nxt_ok:
            lines.append(f"{y}년 전 같은 시기: 자료 없음")
            continue
        wk = mean(nxt_ok)
        s = f"{y}년 전 같은 시기: 기준가 {fmt(b0)}원"
        if b_prev:
            s += f", 직전 4주 변화 {pct(b_prev, b0):+.1f}%"
        s += f", 다음 7일 평균 {pct(b0, wk):+.1f}% (일별: " + ' '.join('-' if v is None else f"{pct(b0, v):+.1f}" for v in nxt) + ')'
        s += f", 4주 뒤 {pct(b0, window_mean(p, base + timedelta(days=22), base + timedelta(days=28)) or b0):+.1f}%"
        lines.append(s)
    cp = COUNTERPART[sid]
    q = {k: v for k, v in prices[cp].items() if k <= d - timedelta(days=1)}
    cm = meta[cp]
    crecent = sorted(k for k in q if k > d - timedelta(days=10))
    lines.append(f"상대 시장({'소매' if cm['market'] == 'RETAIL' else '도매'}, 단위 {cm['unit_quantity']}{cm['unit']}, D-1까지): "
                 + ', '.join(f"{short(k, d)} {fmt(q[k])}" for k in crecent))
    c28 = window_mean(q, d - timedelta(days=35), d - timedelta(days=29))
    if crecent and c28:
        lines.append(f"  상대 시장 4주 변화 {pct(c28, q[crecent[-1]]):+.1f}%")
    return '\n'.join(lines)


def common_block(d, weather, calendar, events):
    lines = ['## 공통 정보']
    tgt = []
    for h in range(1, 8):
        t = d + timedelta(days=h)
        c = calendar[t]
        closed = c['is_market_closed'] == 'true'
        tgt.append(f"D+{h}({WD[t.weekday()]} {t.month:02d}-{t.day:02d}{' 휴장' if closed else ''}{' ' + c['holiday_name'] if c['holiday_name'] else ''})")
    lines.append('목표일: ' + ', '.join(tgt))
    for e in events:
        s, en = date.fromisoformat(e['start_date']), date.fromisoformat(e['end_date'])
        es, ee = date.fromisoformat(e['effect_start_date']), date.fromisoformat(e['effect_end_date'])
        name = '설날' if e['event_code'] == 'SEOLLAL' else '추석'
        if -45 <= (s - d).days <= 60:
            lines.append(f"{name}: 연휴 {rel(s, d)}~{rel(en, d)}, 영향 기간 {rel(es, d)}~{rel(ee, d)}")
        elif 0 < (d - en).days <= 30:
            lines.append(f"{name} 연휴가 {(d - en).days}일 전에 끝남")
    w7 = [weather[d - timedelta(days=k)] for k in range(1, 8) if d - timedelta(days=k) in weather]
    w28 = [weather[d - timedelta(days=k)] for k in range(1, 29) if d - timedelta(days=k) in weather]
    if w7:
        t7 = mean(float(r['avg_temp']) for r in w7)
        normals = []
        for y in range(1, 6):
            ws = [weather.get(d - timedelta(days=364 * y + k)) for k in range(1, 8)]
            ws = [float(r['avg_temp']) for r in ws if r]
            if ws:
                normals.append(mean(ws))
        p28 = sum(float(r['precipitation'] or 0) for r in w28)
        pn = []
        for y in range(1, 6):
            ws = [weather.get(d - timedelta(days=364 * y + k)) for k in range(1, 29)]
            pn.append(sum(float(r['precipitation'] or 0) for r in ws if r))
        heat = max(float(r['heat_station_ratio']) for r in w28)
        rain = max(float(r['heavy_rain_station_ratio']) for r in w28)
        cold = max(float(r['cold_station_ratio']) for r in w28)
        lines.append(f"전국 기상(D-1까지): 최근 7일 평균기온 {t7:.1f}℃ (지난 5년 같은 주 {mean(normals):.1f}℃), "
                     f"최근 28일 강수 {p28:.0f}mm (지난 5년 평균 {mean(pn):.0f}mm), "
                     f"28일 중 하루 최대 관측소 비율 폭염 {heat:.0f}%·호우 {rain:.0f}%·한파 {cold:.0f}%")
    return '\n'.join(lines)


def strip_year(text: str) -> str:
    return YEAR_RE.sub('', text or '').strip()


def krei_block(item, d, krei):
    name = KREI_ITEM[item]
    mine = [r for r in krei if r['item_name'] == name]
    if not mine:
        return f"KREI 관측 월보({item}): 공개된 보고서 없음"
    latest_key = max(mine, key=lambda r: r['available_from'])['source_record_key']
    rs = [r for r in mine if r['source_record_key'] == latest_key]
    pub = datetime.fromisoformat(rs[0]['available_from']).date()
    lines = [f"KREI 농업관측 월보({item}) — 최신 보고서 공개 {(d - pub).days}일 전"]
    want = ('WHOLESALE_PRICE', 'SHIPMENT', 'PRODUCTION', 'ARRIVAL', 'STOCK', 'IMPORT')
    seen = set()
    for r in rs:
        if r['metric'] not in want:
            continue
        ev = strip_year(r['evidence'])
        if ev in seen:
            continue
        seen.add(ev)
        ts = date.fromisoformat(r['target_start']) if r['target_start'] else None
        span = f"{ts.month}월" if ts else ''
        crop = f"[{r['crop_type']}]" if r['crop_type'] else ''
        lines.append(f"  - {r['kind']} {r['metric']} {crop}{span}: {ev[:220]}")
        if len(seen) >= 14:
            break
    return '\n'.join(lines)


def build(d: date) -> str:
    meta, prices, kinds, switches, weather, calendar, events, krei = load(d)
    parts = [f"# 기준일 D (연도 비공개) = {WD[d.weekday()]}요일 {d.month:02d}-{d.day:02d}",
             common_block(d, weather, calendar, events)]
    done_items = set()
    for sid in ORDER:
        item = meta[sid]['item']
        parts.append(series_block(sid, d, meta, prices, kinds, switches))
        if sid == ORDER[ORDER.index(sid)] and item not in done_items and meta[COUNTERPART[sid]]['item'] == item \
                and ORDER.index(COUNTERPART[sid]) < ORDER.index(sid):
            parts.append(krei_block(item, d, krei))
            done_items.add(item)
    return '\n\n'.join(parts) + '\n'


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('origin')
    ap.add_argument('--out', default='model_comparison/llm_blind/prompts')
    a = ap.parse_args()
    d = date.fromisoformat(a.origin)
    out = Path(a.out)
    out.mkdir(parents=True, exist_ok=True)
    path = out / f'{d.isoformat()}.md'
    path.write_text(build(d), encoding='utf-8')
    print(path)


if __name__ == '__main__':
    main()
