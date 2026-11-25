"""구조적 가격 전달 모델(struct) C5 보고용 비교표 생성기. 검증 전체 실행이 끝난 뒤에 쓴다.

    # struct 검증 결과 폴더 하나로 JSON + 마크다운 표(기본 출력 위치: 그 폴더. runs/struct 밖이면 --out-dir 필요)
    uv run --extra prices python -m model_comparison.structural.compare runs/struct/val-t13

    # 도구 자체 점검: 기존 검증 실험 하나를 '모델'처럼 넣는다(struct 검증 예측은 쓰지 않음)
    uv run --extra prices python -m model_comparison.structural.compare experiments/lgbm-p1-20261111-01 \\
        --out-dir <임시 폴더> --no-comparators

    # 비교 대상 후보 점검(기존 metrics.json만 읽음, 재실행 없음)
    uv run --extra prices python -m model_comparison.structural.compare --audit-comparators

지표 정의는 기준서 §8·score.py와 같다. tools.evaluate의 points_for·summarize·result·bootstrap을 읽기 전용으로 재사용한다.
- 주 결과는 policy(실패한 점은 naive로 대체). model_only, common_success(모델+비교 대상이 모두 성공한 점)도 함께 낸다.
- 소매 전용(계열 1·8·10·9001·9011)은 사전 등록(pre-registered) 보조 지표다. 검증 실행 전(2026-11-24, C4 확정 시점)에
  정의했으며 사후 선택이 아니다. 도매 전용(2·7·9·9002·9012)도 같은 방식으로 낸다. 주 지표는 전체 10계열 policy macro MAPE.
- 기존 모델 비교는 읽기 전용이다(예측 CSV와 config.json만 읽고 다시 돌리지 않는다). 모든 비교 대상을 struct와 같은 평가 점
  집합에서, 같은 policy로 다시 채점한다(기존 metrics.json 값과는 점 집합이 같으면 일치한다).
- model_comparison/llm_blind/points_*.csv는 읽지 않는다. experiments_v2는 앙상블 한 개의 예측을 사후에 읽을 뿐 입력이 아니다.
"""
import argparse
import json
import sys
from datetime import date
from pathlib import Path

from tools import evaluate, loader, standard

ROOT = Path(__file__).resolve().parents[2]
DEFAULT_SNAPSHOT = ROOT / 'data' / 'snapshots' / standard.DATA_VERSION
STRUCT_RUNS = ROOT / 'runs' / 'struct'
PREREGISTERED_ON = '2026-11-24'

RETAIL_IDS = (1, 8, 10, 9001, 9011)
WHOLESALE_IDS = (2, 7, 9, 9002, 9012)
ALL_IDS = tuple(sorted(RETAIL_IDS + WHOLESALE_IDS))
SEASON_ORDER = (('spring', '봄(3~5월)'), ('summer', '여름(6~8월)'), ('autumn', '가을(9~11월)'), ('winter', '겨울(12~2월)'))

# 비교 대상 대표 실험. 고른 방법은 README_MODEL.md "설정 확정 (C4)"와 audit_comparator_candidates()에 있다.
# (표시 이름, 폴더(ROOT 기준), 단계, 선택 이유, 참고 표시)
COMPARATORS = (
    ('LightGBM p1', 'experiments/lgbm-p1-20261111-01', 'p1', '모델당 p1 실험은 하나뿐', None),
    ('XGBoost p1', 'experiments/xgb-p1-20261110-01', 'p1', '모델당 p1 실험은 하나뿐', None),
    ('Ridge p1', 'experiments/ridge-p1-20261111-07', 'p1', '모델당 p1 실험은 하나뿐', None),
    ('AutoARIMA p1', 'experiments/arima-p1-20261112-01', 'p1', '모델당 p1 실험은 하나뿐', None),
    ('LightGBM p2', 'experiments/lgbm-p2-20261111-01', 'p2',
     '팀 표시: lightgbm/README_MODEL.md 결과표에서 +MARKET을 굵게 표시, 방향 적중 분석도 이 실험 기준', None),
    ('XGBoost p2', 'experiments/xgb-p2-20261111-06', 'p2',
     '팀 표시 없음: p2 중 검증 policy macro MAPE 최저(MARKET+NATIONAL_WEATHER+EVENT, 효과 있던 묶음 전체)', None),
    ('Ridge p2', 'experiments/ridge-p2-20261112-02', 'p2',
     '팀 표시 없음: p2 중 검증 policy macro MAPE 최저(+MARKET). 07(MARKET+PRODUCTION)과 0.002%p 차이', None),
    ('AutoARIMA p2', 'experiments/arima-p2-20261112-01', 'p2',
     'p2는 EVENT 하나뿐이며 v2/README.md가 현재 앙상블 구성원(AutoARIMA p2)으로 지정', None),
    ('앙상블 v2 기준(+ARIMA)', 'experiments_v2/ens-val-base-arima-validation-20261119-01', 'v2',
     'v2 앙상블(XGBoost robust + LightGBM + AutoARIMA p2) 검증 예측 한 개만 사후에 읽음',
     '참고: v2 특징 사용, 입력 조건 다름'),
)


# ---- 읽기·점검 -----------------------------------------------------------------------------------------------

def read_config(folder: Path) -> dict:
    return json.loads((Path(folder) / 'config.json').read_text(encoding='utf-8'))


def origin_list_of(config: dict):
    return config.get('origins') or config.get('origin_list')


def check_model_folder(folder: Path) -> dict:
    """채점 가능한 폴더인지: 줄인 실행(smoke) 거부, 시험 구간 거부(tune·validation만)."""
    config = read_config(folder)
    if config.get('kind') == 'smoke':
        raise ValueError(f'줄인 실행(smoke)은 채점하지 않음: {Path(folder).name}')
    origins = origin_list_of(config)
    if origins not in ('tune', 'validation'):
        raise ValueError(f'기준일 목록이 tune·validation이 아님({origins!r}): {Path(folder).name}')
    if config.get('month'):
        raise ValueError(f'--month로 줄인 실행은 채점하지 않음: {Path(folder).name}')
    return config


def check_comparator(folder: Path, snap=None) -> dict:
    """비교 대상 자격: 검증 구간 전체 기준일, 10계열 전부, 월 제한 없음. 이유 목록을 돌려준다(비면 자격 있음)."""
    reasons = []
    config = read_config(folder)
    if origin_list_of(config) != 'validation':
        reasons.append(f'기준일 목록이 validation이 아님({origin_list_of(config)!r})')
    if config.get('month'):
        reasons.append(f'month={config["month"]}')
    series = config.get('series')
    if series is not None and sorted(int(s) for s in series) != list(ALL_IDS):
        reasons.append(f'계열이 10개가 아님: {series}')
    return {'phase': config.get('phase'), 'origin_list': origin_list_of(config), 'month': config.get('month'),
            'series': series, 'experiment_id': config.get('experiment_id') or config.get('name'),
            'eligible': not reasons, 'reasons': reasons}


def audit_comparator_candidates(experiments_dir: Path = ROOT / 'experiments') -> list[dict]:
    """experiments/ 전체의 자격 점검과 기존 metrics.json 수치(읽기만). 대표 선택 근거를 남기는 용도."""
    out = []
    for config_path in sorted(Path(experiments_dir).glob('*/config.json')):
        folder = config_path.parent
        info = check_comparator(folder)
        metrics_path = folder / 'metrics.json'
        policy = {}
        if metrics_path.exists():
            policy = json.loads(metrics_path.read_text(encoding='utf-8'))['results']['policy']
        out.append({'folder': folder.name, 'phase': info['phase'], 'feature_set': read_config(folder).get('feature_set'),
                    'eligible': info['eligible'], 'reasons': info['reasons'],
                    'macro_mape': policy.get('macro_mape'), 'series_wins': policy.get('series_wins')})
    return out


# ---- 점수 계산 -----------------------------------------------------------------------------------------------

def policy_fn(p):
    return p['pred'] if p['ok'] else p['naive']


def model_only_fn(p):
    return p['pred'] if p['ok'] else None


def check_markets(points):
    """소매·도매 계열 목록이 실제 시장 구분과 같은지(사전 등록한 계열 목록이 어긋나면 중단)."""
    for p in points:
        expected = 'RETAIL' if p['series_id'] in RETAIL_IDS else 'WHOLESALE' if p['series_id'] in WHOLESALE_IDS else None
        if expected is None or p['market'] != expected:
            raise ValueError(f'계열 {p["series_id"]}의 시장 {p["market"]!r}이 사전 등록 목록과 다름')


def subset(points, ids):
    ids = set(ids)
    return [p for p in points if p['series_id'] in ids]


def compact(res):
    """result()에서 보고에 쓰는 요약만."""
    if not res.get('points'):
        return {'points': 0, 'series_count': 0}
    boot = res.get('bootstrap') or {}
    return {'points': res['points'], 'series_count': res['series_count'], 'macro_mape': res['macro_mape'],
            'naive_macro_mape': res['naive_macro_mape'], 'relative_improvement_pct': res['relative_improvement_pct'],
            'macro_rmae': res['macro_rmae'], 'series_wins': res['series_wins'],
            'bootstrap': {k: boot.get(k) for k in ('delta', 'ci_low', 'ci_high', 'blocks', 'iterations', 'seed')} if boot else None}


def score_set(points, with_common=None):
    """한 점 집합의 전체 + 소매 전용 + 도매 전용(policy). with_common: common_success 점 키 집합."""
    pol = evaluate.result(points, policy_fn)
    out = {
        'success_rate': evaluate.r6(sum(p['ok'] for p in points) / len(points)) if points else 0.0,
        'policy': pol,
        'model_only': evaluate.result(points, model_only_fn, with_bootstrap=False),
        'retail_only': evaluate.result(subset(points, RETAIL_IDS), policy_fn),
        'wholesale_only': evaluate.result(subset(points, WHOLESALE_IDS), policy_fn),
    }
    if with_common is not None:
        out['common_success'] = evaluate.result([p for p in points if p['key'] in with_common], lambda p: p['pred'],
                                                with_bootstrap=False)
    return out


def load_points(folder: Path, snap):
    return evaluate.points_for(evaluate.read_predictions(Path(folder)), snap)


def comparator_entry(label, folder, phase, why, note, snap):
    folder = ROOT / folder
    check = check_comparator(folder)
    return {'label': label, 'folder': str(folder.relative_to(ROOT)), 'phase': phase, 'why_chosen': why, 'note': note,
            'config_check': check, 'points': {p['key']: p for p in load_points(folder, snap)}}


def build_report(folder: Path, snap, comparators=COMPARATORS, label=None):
    folder = Path(folder)
    config = check_model_folder(folder)
    points = load_points(folder, snap)
    if not points:
        raise ValueError(f'평가 점이 없음: {folder}')
    check_markets(points)
    keys = {p['key'] for p in points}
    entries = [comparator_entry(*c, snap) for c in comparators]
    bad = [e['folder'] for e in entries if not e['config_check']['eligible']]
    if bad:
        raise ValueError(f'자격 없는 비교 대상: {bad}')
    # 평가 점 집합 = 모델 점 ∩ 모든 비교 대상 점(같은 점에서 다시 채점). 보통 전부 같다.
    common_keys = set(keys)
    for e in entries:
        common_keys &= set(e['points'])
    by_key = {p['key']: p for p in points}
    models_ok = {k for k in common_keys if by_key[k]['ok'] and all(e['points'][k]['ok'] for e in entries)} if entries else None

    full = score_set(points)
    base_summary = {name: evaluate.summarize(points, fn) | {'series': None}
                    for name, fn in (('naive', lambda p: p['naive']), ('mean7', lambda p: p['mean7']))}
    per_series = []
    for sid, s in full['policy']['series'].items():
        per_series.append({'series_id': int(sid), 'item': snap.series[int(sid)].item, 'market': snap.series[int(sid)].market,
                           'points': s['points'], 'mape': s['mape'], 'naive_mape': s['naive_mape'],
                           'relative_improvement_pct': s['relative_improvement_pct'], 'rmae': s['rmae'], 'win': s['win']})
    report = {
        'tool': 'model_comparison/structural/compare.py',
        'preregistered_secondary': {
            'metric': '소매 전용(계열 1, 8, 10, 9001, 9011) macro MAPE·naive 대비·승/5·월 블록 부트스트랩 Δ',
            'defined_on': PREREGISTERED_ON,
            'statement': '검증 실행 전에 정의한 사전 등록 보조 지표이며 사후 선택이 아니다. 주 지표는 전체 10계열 policy macro MAPE.',
            'retail_series': list(RETAIL_IDS), 'wholesale_series': list(WHOLESALE_IDS)},
        'model': {'label': label or config.get('name') or folder.name, 'folder': str(folder), 'name': config.get('name'),
                  'experiment_id': config.get('experiment_id'), 'config_id': config.get('config_id'),
                  'kind': config.get('kind'), 'origins': origin_list_of(config), 'data_version': config.get('data_version'),
                  'evaluated_points': len(points), 'series_count': len({p['series_id'] for p in points})},
        'overall': {'success_rate': full['success_rate'], 'policy': full['policy'], 'model_only': full['model_only'],
                    'common_success': None, 'baselines': base_summary},
        'retail_only': full['retail_only'], 'wholesale_only': full['wholesale_only'],
        'per_series': per_series,
        'by_season': full['policy']['by_season'], 'by_horizon': full['policy']['by_horizon'],
        'by_kind_cross': full['policy']['by_kind_cross'],
    }
    comparison = {'point_set_equal': len(common_keys) == len(keys) and all(len(e['points']) == len(keys) for e in entries),
                  'model_points': len(keys), 'common_points': len(common_keys),
                  'common_success_points': None if models_ok is None else len(models_ok), 'rows': []}
    if entries:
        common_points = [p for p in points if p['key'] in common_keys]
        comparison['rows'].append({'label': report['model']['label'] + ' (대상 모델)', 'folder': str(folder), 'phase': None,
                                   'why_chosen': None, 'note': None, **summarize_scored(score_set(common_points, models_ok))})
        report['overall']['common_success'] = compact(evaluate.result(
            [p for p in common_points if p['key'] in models_ok], lambda p: p['pred'], with_bootstrap=False))
        for e in entries:
            pts = [e['points'][k] for k in sorted(common_keys)]
            comparison['rows'].append({'label': e['label'], 'folder': e['folder'], 'phase': e['phase'],
                                       'why_chosen': e['why_chosen'], 'note': e['note'], 'config_check': e['config_check'],
                                       **summarize_scored(score_set(pts, models_ok))})
    report['comparison'] = comparison
    report['metrics_json_check'] = crosscheck_metrics(folder, full)
    return report


def summarize_scored(scored):
    return {'success_rate': scored['success_rate'], 'overall': compact(scored['policy']),
            'model_only_macro_mape': scored['model_only'].get('macro_mape'),
            'common_success_macro_mape': (scored.get('common_success') or {}).get('macro_mape'),
            'retail_only': compact(scored['retail_only']), 'wholesale_only': compact(scored['wholesale_only'])}


def crosscheck_metrics(folder: Path, full):
    """폴더에 metrics.json이 있으면 이 도구의 전체 policy 값과 맞는지 확인(도구 자체 점검)."""
    path = Path(folder) / 'metrics.json'
    if not path.exists():
        return None
    saved = json.loads(path.read_text(encoding='utf-8'))['results']['policy']
    mine = full['policy']
    pairs = {'macro_mape': (saved.get('macro_mape'), mine.get('macro_mape')),
             'naive_macro_mape': (saved.get('naive_macro_mape'), mine.get('naive_macro_mape')),
             'series_wins': (saved.get('series_wins'), mine.get('series_wins')),
             'macro_rmae': (saved.get('macro_rmae'), mine.get('macro_rmae')),
             'points': (saved.get('points'), mine.get('points')),
             'bootstrap_delta': ((saved.get('bootstrap') or {}).get('delta'), (mine.get('bootstrap') or {}).get('delta')),
             'bootstrap_ci_low': ((saved.get('bootstrap') or {}).get('ci_low'), (mine.get('bootstrap') or {}).get('ci_low')),
             'bootstrap_ci_high': ((saved.get('bootstrap') or {}).get('ci_high'), (mine.get('bootstrap') or {}).get('ci_high'))}
    return {'equal': all(a == b for a, b in pairs.values()),
            'fields': {k: {'metrics_json': a, 'compare': b, 'equal': a == b} for k, (a, b) in pairs.items()}}


# ---- 마크다운 --------------------------------------------------------------------------------------------------

def f(v, nd=3, sign=False):
    if v is None:
        return '-'
    return f'{v:+.{nd}f}' if sign else f'{v:.{nd}f}'


def boot_text(boot):
    if not boot or boot.get('ci_low') is None:
        return '-'
    return f'{f(boot["delta"], 3, True)} [{f(boot["ci_low"], 3, True)}, {f(boot["ci_high"], 3, True)}]'


def summary_row(name, s, wins_of=None):
    if not s.get('points'):
        return f'| {name} | - | - | - | - | - | - |'
    wins = f'{s["series_wins"]}/{s["series_count"]}'
    return (f'| {name} | {f(s["macro_mape"])} | {f(s["naive_macro_mape"])} | {f(s["relative_improvement_pct"], 2, True)}% | '
            f'{f(s["macro_rmae"])} | {wins} | {boot_text(s.get("bootstrap"))} |')


def render_markdown(report) -> str:
    m, o = report['model'], report['overall']
    pre = report['preregistered_secondary']
    pol = compact(o['policy'])
    lines = [
        f'# struct 검증 결과 비교표 — {m["label"]}', '',
        f'> **사전 등록(pre-registered) 보조 지표**: {pre["metric"]}은 검증 실행 전({pre["defined_on"]})에 정의했다. '
        f'사후 선택이 아니다. 주 지표는 전체 10계열 policy macro MAPE다.', '',
        f'- 폴더 `{m["folder"]}`, 기준일 목록 {m["origins"]}, 평가 점 {m["evaluated_points"]}개, 계열 {m["series_count"]}개, '
        f'성공률 {o["success_rate"]:.2%}',
        '- policy = 실패한 점은 naive로 대체. 부트스트랩 = 기준일 월 블록 1,000회(시드 0), Δ = naive macro MAPE − 모델 macro MAPE(양수면 모델이 좋음). '
        '"naive 대비" = (naive − 모델)/naive.',
        '', '## 1. 전체 (10계열)', '',
        '| 구분 | macro MAPE % | naive % | naive 대비 | rMAE | 계열 승 | 부트스트랩 Δ [95%] |', '|---|---|---|---|---|---|---|',
        summary_row('policy (주 결과)', pol),
        summary_row('model_only (실패 점 제외)', compact(o['model_only'])),
    ]
    if o.get('common_success'):
        lines.append(summary_row('common_success (모델+비교 대상 모두 성공한 점)', o['common_success']))
    lines += [summary_row('naive (직전 가격 유지)', {**o['baselines']['naive'], 'bootstrap': None}),
              summary_row('mean7', {**o['baselines']['mean7'], 'bootstrap': None}), '',
              '## 2. 소매 전용(사전 등록 보조 지표)·도매 전용', '',
              '| 구분 | macro MAPE % | naive % | naive 대비 | rMAE | 계열 승 | 부트스트랩 Δ [95%] |', '|---|---|---|---|---|---|---|',
              summary_row('소매 5계열 (1, 8, 10, 9001, 9011) — 사전 등록', compact(report['retail_only'])),
              summary_row('도매 5계열 (2, 7, 9, 9002, 9012)', compact(report['wholesale_only'])), '',
              '## 3. 계열별 (policy)', '',
              '| 계열 | 품목 | 시장 | 점 | MAPE % | naive MAPE % | 개선 | 승 |', '|---|---|---|---|---|---|---|---|']
    for s in report['per_series']:
        lines.append(f'| {s["series_id"]} | {s["item"]} | {s["market"]} | {s["points"]} | {f(s["mape"])} | {f(s["naive_mape"])} | '
                     f'{f(s["relative_improvement_pct"], 2, True)}% | {"승" if s["win"] else "-"} |')
    lines += ['', '## 4. 계절·시점·작형 전환 (policy macro MAPE)', '',
              '| 구분 | 점 | macro MAPE % | naive % | naive 대비 |', '|---|---|---|---|---|']

    def break_row(name, b):
        return (f'| {name} | {b["points"]} | {f(b["macro_mape"])} | {f(b["naive_macro_mape"])} | '
                f'{f(b["relative_improvement_pct"], 2, True)}% |')
    for key, name in SEASON_ORDER:
        if key in report['by_season']:
            lines.append(break_row(f'목표월 {name}', report['by_season'][key]))
    for h in sorted(report['by_horizon'], key=int):
        lines.append(break_row(f'시점 h={h}', report['by_horizon'][h]))
    for k, name in (('0', '작형 전환 없음'), ('1', '기준일→목표일 작형 전환(배추·무)')):
        if k in report['by_kind_cross']:
            lines.append(break_row(name, report['by_kind_cross'][k]))
    if not report['by_kind_cross']:
        lines.append('| 작형 전환 | - | - | - | - |')
    cmp_ = report.get('comparison') or {}
    if cmp_.get('rows'):
        lines += ['', '## 5. 기존 검증 결과와 비교 (같은 평가 점 집합, policy로 다시 채점, 기존 실험은 재실행하지 않음)', '',
                  f'- 평가 점 {cmp_["common_points"]}개(대상 모델 {cmp_["model_points"]}개, 점 집합 동일: '
                  f'{"예" if cmp_["point_set_equal"] else "아니오"}), common_success 점 {cmp_["common_success_points"]}개',
                  '- 대표 선택: 팀이 README에 표시한 실험이 있으면 그것, 없으면 p2 중 검증 policy macro MAPE 최저(선택 편향은 비교 대상에 유리한 쪽)', '',
                  '| 모델 | macro MAPE % | naive 대비 | rMAE | 승/10 | 부트스트랩 Δ [95%] | 소매 MAPE % (승/5) | 도매 MAPE % (승/5) | 성공률 | 비고 |',
                  '|---|---|---|---|---|---|---|---|---|---|']
        for r in cmp_['rows']:
            o_, rt, wh = r['overall'], r['retail_only'], r['wholesale_only']
            note = ' / '.join(x for x in (r.get('note'), r.get('folder') and f'`{Path(r["folder"]).name}`') if x)
            lines.append(f'| {r["label"]} | {f(o_["macro_mape"])} | {f(o_["relative_improvement_pct"], 2, True)}% | '
                         f'{f(o_["macro_rmae"])} | {o_["series_wins"]}/{o_["series_count"]} | {boot_text(o_.get("bootstrap"))} | '
                         f'{f(rt.get("macro_mape"))} ({rt.get("series_wins", "-")}/{rt.get("series_count", "-")}) | '
                         f'{f(wh.get("macro_mape"))} ({wh.get("series_wins", "-")}/{wh.get("series_count", "-")}) | '
                         f'{r["success_rate"]:.2%} | {note} |')
    chk = report.get('metrics_json_check')
    if chk is not None:
        lines += ['', f'- 이 폴더의 metrics.json과 전체 policy 값 일치 여부: {"일치" if chk["equal"] else "불일치"}']
    return '\n'.join(lines) + '\n'


def write_outputs(report, out_dir: Path):
    out_dir = Path(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / 'compare.json').write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    (out_dir / 'compare.md').write_text(render_markdown(report), encoding='utf-8')
    return out_dir / 'compare.json', out_dir / 'compare.md'


def default_out_dir(folder: Path):
    folder = Path(folder).resolve()
    if STRUCT_RUNS in folder.parents:
        return folder
    return None


def main(argv=None):
    parser = argparse.ArgumentParser(description='struct C5 보고용 비교표(검증 실행 뒤에 사용)')
    parser.add_argument('folder', nargs='?', type=Path, help='결과 폴더(predictions.csv·config.json)')
    parser.add_argument('--out-dir', type=Path, help='compare.json·compare.md 저장 폴더. runs/struct 안의 폴더면 기본은 그 폴더')
    parser.add_argument('--label', help='표에 쓸 모델 이름')
    parser.add_argument('--no-comparators', action='store_true', help='기존 모델 비교 생략')
    parser.add_argument('--audit-comparators', action='store_true', help='experiments/ 비교 대상 후보 점검(metrics.json만 읽음)')
    parser.add_argument('--snapshot', type=Path, default=DEFAULT_SNAPSHOT)
    args = parser.parse_args(argv)
    if args.audit_comparators:
        for row in audit_comparator_candidates():
            print(f'{row["folder"]:24} {row["phase"]:3} {str(row["feature_set"]):42} 자격 {"O" if row["eligible"] else "X"} '
                  f'macro {row["macro_mape"]} 승 {row["series_wins"]} {row["reasons"] or ""}')
        return 0
    if not args.folder:
        parser.error('folder 또는 --audit-comparators가 필요')
    out_dir = args.out_dir or default_out_dir(args.folder)
    if out_dir is None:
        parser.error('runs/struct 밖의 폴더는 --out-dir이 필요(기존 실험 폴더에 쓰지 않기 위해)')
    snap = loader.Snapshot(args.snapshot)
    try:
        report = build_report(args.folder, snap, () if args.no_comparators else COMPARATORS, args.label)
    except ValueError as error:
        print(f'실패: {error}', file=sys.stderr)
        return 1
    json_path, md_path = write_outputs(report, out_dir)
    print(render_markdown(report))
    print(f'저장: {json_path}, {md_path}')
    return 0


if __name__ == '__main__':
    sys.exit(main())
