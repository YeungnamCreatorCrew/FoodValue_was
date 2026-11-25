"""블라인드 절차 강제.

- origins.json: dev(개발·보정용, 2023-11~2024-10)와 eval(검증 구간 튜닝 목록에서 4주 간격) 기준일 목록. 첫 eval 프롬프트 전에 고정.
- next <set>: 이전 기준일 예측이 모두 잠겼을 때만 다음 기준일 프롬프트를 만든다.
- lock <set> <date>: preds/<set>/<date>.csv 의 SHA-256 을 lock.log 에 남긴다. 잠긴 뒤 파일이 바뀌면 score 가 거부한다.

예측 파일 형식(10행): series_id,h1,...,h7  — 값은 현재가(v[d]) 대비 % 변화. 0 = naive.
"""
from __future__ import annotations

import csv
import hashlib
import json
import sys
from datetime import date, datetime
from pathlib import Path

ROOT = Path('model_comparison/llm_blind')
SERIES = [1, 2, 8, 7, 10, 9, 9001, 9002, 9011, 9012]


def origins(kind: str) -> list[str]:
    return json.loads((ROOT / 'origins.json').read_text())[kind]


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def locks() -> dict:
    out = {}
    log = ROOT / 'lock.log'
    if log.exists():
        for line in log.read_text().splitlines():
            kind, d, digest, _ = line.split('\t')
            out[(kind, d)] = digest
    return out


def check_pred(path: Path):
    with open(path) as f:
        rows = list(csv.DictReader(f))
    assert [int(r['series_id']) for r in rows] == SERIES, f'{path}: 계열 순서/개수 오류'
    for r in rows:
        for h in range(1, 8):
            v = float(r[f'h{h}'])
            assert -60 < v < 150, f'{path}: 값 범위 이상 {v}'


def cmd_next(kind: str):
    from model_comparison.llm_blind.make_prompt import build
    held = locks()
    for d in origins(kind):
        if (kind, d) in held:
            continue
        out = ROOT / f'{kind}_prompts' / f'{d}.md'
        out.parent.mkdir(parents=True, exist_ok=True)
        if not out.exists():
            out.write_text(build(date.fromisoformat(d)), encoding='utf-8')
        print(out)
        return
    print('모든 기준일 잠김')


def cmd_lock(kind: str, d: str):
    held = locks()
    todo = [o for o in origins(kind) if (kind, o) not in held]
    assert todo and todo[0] == d, f'다음에 잠글 기준일은 {todo[:1]}'
    path = ROOT / 'preds' / kind / f'{d}.csv'
    check_pred(path)
    with open(ROOT / 'lock.log', 'a') as f:
        f.write(f'{kind}\t{d}\t{sha(path)}\t{datetime.now().isoformat(timespec="seconds")}\n')
    print(f'잠금 {kind} {d} {sha(path)[:12]}')


if __name__ == '__main__':
    {'next': lambda: cmd_next(sys.argv[2]), 'lock': lambda: cmd_lock(sys.argv[2], sys.argv[3])}[sys.argv[1]]()
