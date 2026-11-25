"""재학습 기준일 하나에서 계열별 추정 파라미터(a~e, k_h, lambda, 평소 배수, nan 횟수)를 JSON으로 낸다(README 표용).

    uv run --extra prices python -m model_comparison.structural.dump_params \\
        --config model_comparison/structural/config.json --origin 2025-01-06 --series 1,2,9001

공통 로더(tools.loader)로 만든 학습 표본만 쓰고, 검증 구간 기준일만 허용한다(시험 구간 거부). model.py와 별개의 점검 도구다.
"""
import argparse
import json
from datetime import date
from pathlib import Path

from tools import evaluate, loader, origins, standard
from tools.run_backtest import load_class


def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument('--config', required=True, type=Path)
    parser.add_argument('--origin', required=True, help='재학습 기준일 YYYY-MM-DD(검증 구간)')
    parser.add_argument('--series', help='계열 id 쉼표 목록. 기본 전체')
    parser.add_argument('--snapshot', type=Path, default=evaluate.DEFAULT_SNAPSHOT)
    parser.add_argument('--out', type=Path, help='JSON 저장 경로. 없으면 화면에만')
    args = parser.parse_args(argv)
    config = json.loads(args.config.read_text(encoding='utf-8'))
    day = date.fromisoformat(args.origin)
    origins.guard('p1', [day])
    snap = loader.Snapshot(args.snapshot)
    bundles = loader.check_bundles(config['extra_features'])
    ids = [int(s) for s in args.series.split(',')] if args.series else snap.series_ids
    cls = load_class(config['class'])
    result = {}
    for sid in ids:
        model = cls(**config['params'])
        model.fit(snap.training_data(sid, day, bundles), config['seed'])
        result[str(sid)] = model.parameters()
    text = json.dumps(result, ensure_ascii=False, indent=2)
    if args.out:
        args.out.write_text(text + '\n', encoding='utf-8')
    print(text)
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
