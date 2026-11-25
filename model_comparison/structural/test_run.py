"""자체 실행기(run.py)·채점기(score.py) 규칙 테스트: 시험 기준일 거부, 시도 40회 상한, 검증 1회, 폴더 덮어쓰기 거부.

    uv run --extra prices python -m pytest model_comparison/structural/test_run.py
"""
import csv
import json
from datetime import date
from pathlib import Path

import pytest

from model_comparison.structural import run, score
from tools import standard

CONFIG = Path(run.ROOT) / 'model_comparison' / 'structural' / 'config.json'
HAS_SNAPSHOT = (run.DEFAULT_SNAPSHOT / 'manifest.json').exists()


def args_for(out, *extra, origins='tune', name='x'):
    return ['--config', str(CONFIG), '--name', name, '--origins', origins, '--out', str(out),
            '--snapshot', str(out / 'no-snapshot'), *extra]


def write_trials(out, count):
    out.mkdir(parents=True, exist_ok=True)
    with open(out / run.TUNING_LOG, 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f, lineterminator='\n')
        writer.writerow(run.TUNING_COLUMNS)
        for i in range(count):
            writer.writerow([i + 1, f't{i + 1}', '{}', '4.5', '1.0', 'OK'])


# ---- 시험 기준일 거부 ---------------------------------------------------------------------------------------

@pytest.mark.parametrize('day', [date(2025, 11, 1), date(2025, 11, 9), date(2025, 11, 10), date(2026, 3, 2)])
def test_origins_after_validation_are_refused(day):
    with pytest.raises(run.RunError):
        run.check_origins([date(2025, 1, 6), day])


def test_validation_origins_are_accepted():
    days = [date(2024, 11, 1), date(2025, 1, 6), date(2025, 10, 31)]
    assert run.check_origins(days) == days


def test_origins_before_validation_are_refused():
    with pytest.raises(run.RunError):
        run.check_origins([date(2024, 10, 31)])


@pytest.mark.skipif(not HAS_SNAPSHOT, reason='스냅샷 없음')
def test_runner_origin_lists_never_contain_test_days():
    from tools import loader
    snap = loader.Snapshot(run.DEFAULT_SNAPSHOT)
    for name in ('tune', 'validation'):
        assert run.check_origins(snap.origins[name])
        assert max(snap.origins[name]) <= standard.VALIDATION[1]


# ---- 시도 40회 상한 -----------------------------------------------------------------------------------------

def test_trial_budget_refuses_41st(tmp_path):
    out = tmp_path / 'struct'
    write_trials(out, 39)
    assert run.check_trial_budget(out) == 39  # 40번째는 허용
    write_trials(out, 40)
    with pytest.raises(run.RunError):
        run.check_trial_budget(out)


def test_main_refuses_when_budget_used_up(tmp_path, capsys):
    out = tmp_path / 'struct'
    write_trials(out, 40)
    assert run.main(args_for(out, '--record-trial')) == 1
    assert '상한' in capsys.readouterr().err
    assert not (out / 'x').exists()  # 폴더도 만들지 않는다


def test_tune_full_run_requires_record_trial(tmp_path, capsys):
    assert run.main(args_for(tmp_path / 'struct')) == 1
    assert '--record-trial' in capsys.readouterr().err


def test_record_trial_only_for_tune_full_runs(tmp_path, capsys):
    out = tmp_path / 'struct'
    assert run.main(args_for(out, '--record-trial', '--month', '2025-01')) == 1
    assert run.main(args_for(out, '--record-trial', origins='validation')) == 1


# ---- 검증 1회 -----------------------------------------------------------------------------------------------

def make_run_folder(out, name, kind):
    folder = out / name
    folder.mkdir(parents=True)
    (folder / 'config.json').write_text(json.dumps({'name': name, 'kind': kind}), encoding='utf-8')


def test_second_validation_run_is_refused(tmp_path, capsys):
    out = tmp_path / 'struct'
    make_run_folder(out, 'final-validation', 'validation_full')
    assert run.main(args_for(out, origins='validation')) == 1
    assert '1회' in capsys.readouterr().err


def test_validation_smoke_and_tune_runs_do_not_count_as_validation(tmp_path):
    out = tmp_path / 'struct'
    make_run_folder(out, 'smoke', 'smoke')
    make_run_folder(out, 't01', 'tune_trial')
    run.check_validation_once(out)  # 예외 없음


def test_validation_with_series_but_no_month_is_refused(tmp_path):
    out = tmp_path / 'struct'
    assert run.main(args_for(out, '--series', '1', origins='validation')) == 1


def test_run_kind():
    assert run.run_kind('tune', None, None) == 'tune_trial'
    assert run.run_kind('validation', None, None) == 'validation_full'
    assert run.run_kind('validation', '2025-01', None) == 'smoke'
    assert run.run_kind('tune', None, '1,2') == 'smoke'


def test_existing_result_folder_is_refused(tmp_path, capsys):
    out = tmp_path / 'struct'
    make_run_folder(out, 'x', 'smoke')
    assert run.main(args_for(out, '--month', '2025-01')) == 1
    assert '이미 있는 결과 폴더' in capsys.readouterr().err


# ---- 실행기 후처리·채점 --------------------------------------------------------------------------------------

def test_prediction_rows_postprocessing():
    rows = run.prediction_rows([100.4, 100.5, None, float('nan'), -1.0, 0.2, 99.999999], 'OK', '')
    assert rows[0][1] == '100' and rows[1][1] == '101'  # 0.5는 올림
    assert rows[2][2:] == ('PREDICT_FAILED', 'NONE')
    assert rows[3][2:] == ('INVALID_VALUE', 'NOT_FINITE')
    assert rows[4][2:] == ('INVALID_VALUE', 'NON_POSITIVE')
    assert rows[5][1] == '1'  # 반올림 결과 0이면 1
    assert len(run.prediction_rows(None, 'NO_INPUT', 'STALE_OR_GAP')) == 7
    assert run.prediction_rows([1.0] * 6, 'OK', '')[0][2:] == ('PREDICT_FAILED', 'BAD_LENGTH')


@pytest.mark.skipif(not HAS_SNAPSHOT, reason='스냅샷 없음')
def test_score_naive_on_tune_list_matches_prd_value():
    """naive 자신을 채점하면 튜닝 목록 10계열 macro MAPE가 PRD 값 4.607%다(모델 없이 naive만 계산)."""
    from tools import loader
    snap = loader.Snapshot(score.DEFAULT_SNAPSHOT)
    metrics = score.evaluate_rows(score.naive_rows(snap, snap.origins['tune']), snap)
    assert metrics['series_count'] == 10
    assert metrics['baselines']['naive']['macro_mape'] == pytest.approx(4.607089, abs=1e-6)
    assert metrics['results']['policy']['macro_mape'] == metrics['baselines']['naive']['macro_mape']
    assert metrics['results']['policy']['relative_improvement_pct'] == 0


# ---- 줄인 실행은 정확도 지표를 내지 않는다(예산 우회 방지) ---------------------------------------------------------

ACCURACY_WORDS = ('mape', 'rmae', 'naive', 'improvement', 'macro')


def make_predictions(folder):
    with open(folder / 'predictions.csv', 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f, lineterminator='\n')
        writer.writerow(run.PREDICTION_COLUMNS)
        for status in ('OK', 'OK', 'NO_INPUT', 'FIT_FAILED', 'TIMEOUT'):
            writer.writerow(['x', 1, 'a', 'RETAIL', '2025-01-06', '2025-01-07', 1, '1.0', '1', status, ''])


def test_status_summary_has_counts_and_no_accuracy_fields(tmp_path):
    make_predictions(tmp_path)
    summary = run.write_status_summary(tmp_path, 12.34)
    assert summary == {'status_counts': {'FIT_FAILED': 1, 'NO_INPUT': 1, 'OK': 2, 'TIMEOUT': 1},
                       'prediction_rows': 5, 'seconds': 12.3}
    assert json.loads((tmp_path / run.STATUS_SUMMARY).read_text(encoding='utf-8')) == summary
    assert not (tmp_path / 'metrics.json').exists()
    text = (tmp_path / run.STATUS_SUMMARY).read_text(encoding='utf-8').lower()
    assert not any(word in text for word in ACCURACY_WORDS)


def test_score_refuses_smoke_folder(tmp_path):
    folder = tmp_path / 'smoke'
    folder.mkdir()
    (folder / 'config.json').write_text(json.dumps({'name': 'smoke', 'kind': 'smoke'}), encoding='utf-8')
    make_predictions(folder)
    with pytest.raises(ValueError):
        score.write_metrics(folder, snap=None)
    assert not (folder / 'metrics.json').exists()


@pytest.mark.skipif(not HAS_SNAPSHOT, reason='스냅샷 없음')
@pytest.mark.parametrize('origins,extra', [('tune', ('--month', '2025-01', '--series', '1')),
                                           ('validation', ('--month', '2025-01', '--series', '1')),
                                           ('validation', ('--month', '2025-01')),
                                           ('tune', ('--series', '1,2'))])
def test_reduced_run_writes_no_accuracy(tmp_path, capsys, origins, extra):
    out = tmp_path / 'struct'
    argv = ['--config', str(CONFIG), '--name', 'r', '--origins', origins, '--out', str(out), *extra]
    if '--series' not in extra:
        argv += ['--series', '1']
    assert run.main(argv) == 0
    folder = out / 'r'
    assert (folder / 'predictions.csv').exists() and (folder / 'run.log').exists()
    assert not (folder / 'metrics.json').exists()
    summary = json.loads((folder / run.STATUS_SUMMARY).read_text(encoding='utf-8'))
    assert set(summary) == {'status_counts', 'prediction_rows', 'seconds'}
    assert summary['status_counts'].get('OK', 0) > 0
    assert not (out / run.TUNING_LOG).exists()  # 줄인 실행은 시도로 세지 않는다
    printed = (capsys.readouterr().out + (folder / 'run.log').read_text(encoding='utf-8')).lower()
    assert '%' not in printed.replace('100%', '')  # 수치 비율 출력 없음
    assert not any(word in printed for word in ('macro', 'rmae', 'mape', '개선', '계열 승'))


# ---- 골든값: retail_k_grid 패치 뒤에도 t01·t04의 튜닝 예측이 그대로(옛 코드로 만든 runs/struct 결과와 비교) ---------------

@pytest.mark.skipif(not HAS_SNAPSHOT, reason='스냅샷 없음')
@pytest.mark.parametrize('trial', ['t01_v0', 't04_noratio', 't18_retail_t01'])
def test_golden_tune_predictions_unchanged(trial):
    from tools import loader
    saved = Path(run.DEFAULT_OUT) / trial / 'predictions.csv'
    if not saved.exists():
        pytest.skip('저장된 결과 없음')
    user = json.loads((Path(run.ROOT) / 'model_comparison' / 'structural' / 'configs' / f'{trial}.json').read_text(encoding='utf-8'))
    snap = loader.Snapshot(run.DEFAULT_SNAPSHOT)
    bundles = loader.check_bundles(user['extra_features'])
    cls = run.load_class(user['class'])
    with open(saved, encoding='utf-8', newline='') as f:
        old = {(int(r['series_id']), r['origin_date'], int(r['horizon'])): (r['predicted_price_raw'], r['status'])
               for r in csv.DictReader(f)}
    for sid in (1, 2, 9001, 9002, 9011):  # 소매 3 + 도매 2
        results, _ = run.run_series(cls, user['params'], user['seed'], snap, sid, snap.origins['tune'], lambda m: None, bundles)
        for d, rows in results:
            for h, (raw, price, status, _error) in zip(standard.HORIZONS, rows):
                assert old[(sid, d.isoformat(), h)] == (raw, status), (trial, sid, d, h)
