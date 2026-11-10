"""실행 환경(§1.1)과 모델 인터페이스(§9).

모든 실행 진입점(run_backtest 등)은 맨 처음에 apply_environment()를 부른다.
환경변수는 라이브러리를 불러오기 전에 정해져야 스레드 수가 고정된다.
"""
import os
from dataclasses import dataclass, field
from datetime import date
from typing import Protocol

from tools import standard


def apply_environment():
    """기준서 환경변수를 강제로 맞춘다. 사용자가 다른 값을 넣어 두었으면 덮어쓰고 무엇을 바꿨는지 돌려준다."""
    changed = {}
    for key, value in standard.THREAD_ENV.items():
        if os.environ.get(key) != value:
            changed[key] = (os.environ.get(key), value)
            os.environ[key] = value
    return changed


@dataclass
class TrainingData:
    """재학습 시점에 볼 수 있는 학습 표본. 공통 로더가 만든다. 모델은 이 객체로만 학습한다."""
    series_id: int
    as_of: date
    features: object = field(default_factory=list)  # numpy (표본 수 × 15), 열 = feature_names (§5.1)
    targets: object = field(default_factory=list)  # numpy, 목표일 실제 가격(원)
    horizons: object = field(default_factory=list)  # numpy, 1~7
    origins: list[date] = field(default_factory=list)  # 표본 기준일
    feature_names: list[str] = field(default_factory=list)
    prices: list[tuple[date, int]] = field(default_factory=list)  # AutoARIMA 등 계열 모델용 원 계열


@dataclass
class OriginInputs:
    """기준일 d 시점에 볼 수 있는 입력. 공통 로더가 만든다."""
    series_id: int
    origin: date
    features: dict[int, object] = field(default_factory=dict)  # 시점 h → numpy 특징 한 줄
    feature_names: list[str] = field(default_factory=list)
    prices: list[tuple[date, int]] = field(default_factory=list)


class Model(Protocol):
    """모델 담당자가 구현하는 유일한 인터페이스(§9). 스냅샷 파일·DB를 직접 읽지 않는다."""

    def fit(self, history: TrainingData, seed: int) -> None: ...

    def predict(self, inputs: OriginInputs) -> list[float | None]:  # 길이 7, h=1..7
        ...
