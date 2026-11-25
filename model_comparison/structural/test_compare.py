"""compare.py(C5 보고 도구) 점검. 기존 검증 실험 폴더를 '모델'처럼 넣어, 그 폴더 자신의 metrics.json과 값이 같은지 본다.
struct 검증 예측은 쓰지 않는다(아직 없음).

    uv run --extra prices python -m pytest model_comparison/structural/test_compare.py
"""
import json
from pathlib import Path

import pytest

from model_comparison.structural import compare

HAS_SNAPSHOT = (compare.DEFAULT_SNAPSHOT / 'manifest.json').exists()
SELF = compare.ROOT / 'experiments' / 'lgbm-p1-20261111-01'
HAS_SELF = (SELF / 'predictions.csv').exists()
needs_data = pytest.mark.skipif(not (HAS_SNAPSHOT and HAS_SELF), reason='스냅샷 또는 기존 실험 없음')


@pytest.fixture(scope='module')
def snap():
    from tools import loader
    return loader.Snapshot(compare.DEFAULT_SNAPSHOT)


@pytest.fixture(scope='module')
def report_with_comparators(snap):
    return compare.build_report(SELF, snap)


def test_series_lists_are_disjoint_and_cover_ten():
    assert set(compare.RETAIL_IDS).isdisjoint(compare.WHOLESALE_IDS)
    assert compare.ALL_IDS == (1, 2, 7, 8, 9, 10, 9001, 9002, 9011, 9012)
    assert compare.RETAIL_IDS == (1, 8, 10, 9001, 9011) and compare.WHOLESALE_IDS == (2, 7, 9, 9002, 9012)


def test_smoke_and_test_origins_are_refused(tmp_path):
    for config in ({'kind': 'smoke', 'origins': 'validation'}, {'origins': 'test'}, {'origins': 'validation', 'month': '2025-01'}):
        (tmp_path / 'config.json').write_text(json.dumps(config), encoding='utf-8')
        with pytest.raises(ValueError):
            compare.check_model_folder(tmp_path)


def test_default_out_dir_only_inside_runs_struct():
    assert compare.default_out_dir(SELF) is None
    assert compare.default_out_dir(compare.STRUCT_RUNS / 'val-x') == (compare.STRUCT_RUNS / 'val-x').resolve()


def test_comparator_config_check_rejects_partial_runs(tmp_path):
    (tmp_path / 'config.json').write_text(json.dumps({'origin_list': 'validation', 'month': '2025-01', 'series': [1, 2]}))
    check = compare.check_comparator(tmp_path)
    assert not check['eligible'] and len(check['reasons']) == 2


@needs_data
def test_comparator_representatives_are_eligible_and_documented():
    audit = {row['folder']: row for row in compare.audit_comparator_candidates()}
    for label, folder, phase, why, note in compare.COMPARATORS:
        path = compare.ROOT / folder
        assert path.exists(), folder
        assert compare.check_comparator(path)['eligible'], (label, compare.check_comparator(path))
        assert why
    # 팀 표시가 없는 모델(XGBoost·Ridge)의 p2 대표는 자격 있는 p2 중 검증 macro MAPE 최저
    chosen = {label: Path(folder).name for label, folder, *_ in compare.COMPARATORS}
    for prefix, label in (('xgb-p2', 'XGBoost p2'), ('ridge-p2', 'Ridge p2')):
        candidates = [r for name, r in audit.items() if name.startswith(prefix) and r['eligible']]
        assert chosen[label] == min(candidates, key=lambda r: r['macro_mape'])['folder']


@needs_data
def test_self_check_matches_own_metrics_json(report_with_comparators):
    check = report_with_comparators['metrics_json_check']
    assert check['equal'], check
    saved = json.loads((SELF / 'metrics.json').read_text(encoding='utf-8'))['results']['policy']
    policy = report_with_comparators['overall']['policy']
    assert policy['macro_mape'] == saved['macro_mape']
    assert policy['series_wins'] == saved['series_wins']
    assert policy['bootstrap'] == saved['bootstrap']


@needs_data
def test_subsets_split_the_ten_series(report_with_comparators):
    r = report_with_comparators
    assert r['retail_only']['series_count'] == 5 and r['wholesale_only']['series_count'] == 5
    assert r['retail_only']['points'] + r['wholesale_only']['points'] == r['overall']['policy']['points']
    by_market = r['overall']['policy']['by_market']
    assert r['retail_only']['macro_mape'] == by_market['RETAIL']['macro_mape']
    assert r['wholesale_only']['macro_mape'] == by_market['WHOLESALE']['macro_mape']
    assert r['retail_only']['bootstrap']['blocks'] == 12 and r['retail_only']['bootstrap']['seed'] == 0
    assert r['preregistered_secondary']['defined_on'] and '사전 등록' in r['preregistered_secondary']['statement']
    assert len(r['per_series']) == 10 and set(r['by_season']) == {'spring', 'summer', 'autumn', 'winter'}
    assert sorted(r['by_horizon'], key=int) == [str(h) for h in range(1, 8)]


@needs_data
def test_comparator_rows_match_their_own_metrics_json(report_with_comparators):
    rows = report_with_comparators['comparison']['rows']
    assert report_with_comparators['comparison']['point_set_equal']
    assert len(rows) == len(compare.COMPARATORS) + 1
    for row, (label, folder, *_rest) in zip(rows[1:], compare.COMPARATORS):
        saved = json.loads((compare.ROOT / folder / 'metrics.json').read_text(encoding='utf-8'))['results']['policy']
        assert row['overall']['macro_mape'] == saved['macro_mape'], label
        assert row['overall']['series_wins'] == saved['series_wins'], label
        assert row['overall']['bootstrap']['ci_low'] == saved['bootstrap']['ci_low'], label
    # 대상 모델 자신과 같은 폴더의 비교 행은 같은 값
    assert rows[0]['overall'] == rows[1]['overall']
    assert rows[-1]['note'] == '참고: v2 특징 사용, 입력 조건 다름'


@needs_data
def test_outputs_are_written(report_with_comparators, tmp_path):
    json_path, md_path = compare.write_outputs(report_with_comparators, tmp_path)
    assert json.loads(json_path.read_text(encoding='utf-8'))['model']['evaluated_points'] == 11275
    text = md_path.read_text(encoding='utf-8')
    assert '사전 등록' in text and '소매 5계열' in text and '도매 5계열' in text and '일치' in text
