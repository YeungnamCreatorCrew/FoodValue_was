"""실행: python -m app.v2_calibrate experiments_v2/<XGB 검증> experiments_v2/<LGBM 검증> experiments/arima-p2-20261112-01
현재 앙상블 구성원의 검증(validation) 예측 폴더로 계열별 채택·예측 구간·실적을 만들어
model_comparison/v2/service/calibration.json에 쓴다(app.services.v2_calibration 참고). 스냅샷은 실험 스냅샷을 쓴다.
"""
import argparse
import json
from pathlib import Path

from app.services import v2_calibration
from tools import evaluate, loader


def main(argv=None):
    parser = argparse.ArgumentParser(description='v2 앙상블 계열별 검증 실적·예측 구간')
    parser.add_argument('folders', nargs='+', type=Path)
    parser.add_argument('--snapshot', type=Path, default=evaluate.DEFAULT_SNAPSHOT)
    parser.add_argument('--out', type=Path, default=v2_calibration.PATH)
    args = parser.parse_args(argv)
    for folder in args.folders:
        config = json.loads((folder / 'config.json').read_text(encoding='utf-8'))
        if config.get('origin_list') != 'validation':
            parser.error(f'{folder.name}: 검증(validation) 기준일 결과만 쓸 수 있음')
    result = v2_calibration.build(loader.Snapshot(args.snapshot), args.folders)
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(result, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    print(f"앙상블 검증 macro MAPE {result['macroMape']:.4f}% (naive {result['naiveMacroMape']:.4f}%, "
          f"개선 {result['improvementPct']:+.2f}%) → {args.out}")
    for name, s in result['series'].items():
        print(f"  {name:16} {s['verdict']:9} MAPE {s['mape']:.2f}% naive {s['naiveMape']:.2f}% ±5% 안 {s['within5Pct']}%")


if __name__ == '__main__':
    main()
