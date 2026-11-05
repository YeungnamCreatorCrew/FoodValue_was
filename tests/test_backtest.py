"""과거 기준일 재현 백테스트의 비교·집계 규칙. 모델 정확도가 아니라 계산 방식만 검증한다."""
from datetime import date
from types import SimpleNamespace

from app.price_backtest import base_dates, records_for, summarize


def test_records_compare_only_observed_targets_against_last_price():
    base = date(2026, 10, 2)  # 금요일. 토·일 가격은 KAMIS 미조사
    rows = [(date(2026, 10, 1), 900), (base, 1000)]
    result = SimpleNamespace(model='XGBOOST_WEIGHTED', quality='VALIDATED', prices=[1010, 1020, 1030, 1040, 1050, 1060, 1070],
                             lower=[990] * 7, upper=[1100] * 7)
    actual = {date(2026, 10, 5): 1100, date(2026, 10, 6): 950, date(2026, 10, 9): 1000}
    records = records_for(base, result, rows, actual)
    assert [r['horizon'] for r in records] == [3, 4, 7]
    assert records[0]['currentPrice'] == 1000 and records[0]['predicted'] == 1030 and records[0]['recommendation'] == 'BUY_NOW'
    summary = summarize(records)['overall']
    assert summary['points'] == 3
    assert summary['mape'] == round((70 / 1100 + 90 / 950 + 70 / 1000) * 100 / 3, 3)
    assert summary['naiveMape'] == round((100 / 1100 + 50 / 950 + 0) * 100 / 3, 3)
    # 실제로 움직인 2건 중 상승(10/5)만 맞힘. 변동 없는 10/9는 방향 평가에서 제외
    assert summary['directionAccuracy'] == 0.5 and summary['directionSamples'] == 2
    assert summary['intervalCoverage'] == round(2 / 3, 3)  # 950은 하한 990 밖
    assert summarize([]) == {'points': 0}


def test_base_dates_step():
    assert base_dates(date(2026, 1, 1), date(2026, 1, 15), 7) == [date(2026, 1, 1), date(2026, 1, 8), date(2026, 1, 15)]
