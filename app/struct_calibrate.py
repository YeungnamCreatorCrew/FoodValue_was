"""실행: python -m app.struct_calibrate [model_comparison/structural/results/val-t18]
구조적 가격 전달 모델(struct)의 저장된 검증 1회 예측(PR #71, 244 기준일)으로 계열별 채택·예측 구간·실적을 만들어
model_comparison/structural/service/calibration.json에 쓴다. 모델을 다시 돌리지 않는다(검증 구간은 이미 한 번 봤다).
규칙은 앙상블과 같다(app.services.v2_calibration.build): 계열 MAPE < naive MAPE면 VALIDATED, 아니면 BASELINE.
"""
import argparse
import json
from pathlib import Path

from app.services import struct_service, v2_calibration
from tools import evaluate, loader

DEFAULT_FOLDER = struct_service.ROOT / 'model_comparison' / 'structural' / 'results' / 'val-t18'


def main(argv=None):
    parser = argparse.ArgumentParser(description='struct 계열별 검증 실적·예측 구간')
    parser.add_argument('folder', nargs='?', type=Path, default=DEFAULT_FOLDER)
    parser.add_argument('--snapshot', type=Path, default=evaluate.DEFAULT_SNAPSHOT)
    parser.add_argument('--out', type=Path, default=struct_service.CALIBRATION_PATH)
    args = parser.parse_args(argv)
    config = json.loads((args.folder / 'config.json').read_text(encoding='utf-8'))
    if config.get('kind') != 'validation_full':
        parser.error(f'{args.folder.name}: 검증 전체(validation_full) 실행 결과만 쓸 수 있음')
    result = v2_calibration.build(loader.Snapshot(args.snapshot), [args.folder])
    result['configSha256'] = struct_service.config_sha256()
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(result, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    print(f"struct 검증 macro MAPE {result['macroMape']:.4f}% (naive {result['naiveMacroMape']:.4f}%, "
          f"개선 {result['improvementPct']:+.2f}%) → {args.out}")
    for name, s in result['series'].items():
        print(f"  {name:16} {s['verdict']:9} MAPE {s['mape']:.3f}% naive {s['naiveMape']:.3f}% ±5% 안 {s['within5Pct']}%")


if __name__ == '__main__':
    main()
