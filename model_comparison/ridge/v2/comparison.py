"""Read-only historical adapters, full precision v2 metrics, conservative comparisons."""
from collections import Counter
from datetime import date, timedelta
import math
from pathlib import Path
from .audit import HERE, ROOT, effective_outcome, object_sha, read, sha, verify_seal

ERRORS = ('mape', 'mae', 'rmse', 'rmae')
METRICS = (*ERRORS, 'success_rate_pct', 'valid_predictions', 'failed_predictions')
CONDITIONS = ('v1_id', 'v1_sha', 'v2_id', 'v2_sha', 'data_period', 'origin_list', 'origins',
              'series_ids', 'horizons', 'evaluation_rule', 'evaluation_source_sha', 'eligible_keys_sha')
RULE = 'tools.evaluate:observed_target_and_naive;policy_naive_fallback;round_half_up_6raw:v1'


def change(base, new, metric):
    unit = '%p' if metric in ('mape', 'success_rate_pct') else 'price' if metric in ('mae', 'rmse') else 'ratio' if metric == 'rmae' else 'count'
    base = base if base is None or math.isfinite(base) else None
    new = new if new is None or math.isfinite(new) else None
    if base is None or new is None:
        return {'baseline': base, 'new': new, 'absolute_difference': None, 'unit': unit,
                'relative_improvement_pct': None, 'relative_change_pct': None, 'direction': 'unavailable'}
    difference = new-base
    error = metric in ERRORS
    signed = -difference if error else difference
    return {'baseline': base, 'new': new, 'absolute_difference': difference, 'unit': unit,
            'relative_improvement_pct': (base-new)/base*100 if error and base != 0 else None,
            'relative_change_pct': difference/base*100 if not error and base != 0 else None,
            'direction': ('improved' if signed > 0 else 'worsened' if signed < 0 else 'same')
                         if metric not in ('valid_predictions', 'failed_predictions') else 'count_change'}


def comparability(a, b):
    reasons = []
    for key in CONDITIONS:
        if key not in a or key not in b or a[key] is None or b[key] is None:
            reasons.append(f'unknown:{key}')
        elif a[key] != b[key]:
            reasons.append(f'different:{key}')
    return {'label': 'direct' if not reasons else 'reference', 'reasons': reasons}


def statistics(points, mode, series_ids):
    """Float64 source point errors; no display rounding. Macro = mean of series values."""
    by = {}
    for sid in series_ids:
        pp = [p for p in points if p['series_id'] == int(sid)]
        usable = [p for p in pp if mode != 'model_only' or p['ok']]
        pairs = [(p, p['naive'] if mode == 'naive' or not p['ok'] else p['pred']) for p in usable]
        ae = [abs(p['y']-v) for p,v in pairs]
        nae = [abs(p['y']-p['naive']) for p,v in pairs]
        mae = math.fsum(ae)/len(ae) if ae else None
        naive_mae = math.fsum(nae)/len(nae) if nae else None
        ok = sum(p['ok'] for p in pp)
        by[str(sid)] = {'mape': math.fsum(abs(p['y']-v)/p['y']*100 for p,v in pairs)/len(pairs) if pairs else None,
                        'mae': mae, 'rmse': math.sqrt(math.fsum(e*e for e in ae)/len(ae)) if ae else None,
                        'rmae': mae/naive_mae if naive_mae else None,
                        'evaluated_points': len(pp), 'error_points': len(pairs),
                        'valid_predictions': len(pp) if mode == 'naive' else ok,
                        'failed_predictions': 0 if mode == 'naive' else len(pp)-ok,
                        'success_rate_pct': (100. if mode == 'naive' else ok/len(pp)*100) if pp else None}
    overall = {}
    for metric in ERRORS:
        values = [s[metric] for s in by.values() if s[metric] is not None]
        overall[metric] = math.fsum(values)/len(values) if values else None
    for metric in ('evaluated_points', 'error_points', 'valid_predictions', 'failed_predictions'):
        overall[metric] = sum(s[metric] for s in by.values())
    overall['success_rate_pct'] = overall['valid_predictions']/overall['evaluated_points']*100 if overall['evaluated_points'] else None
    overall['metric_series_counts'] = {m: sum(s[m] is not None for s in by.values()) for m in ERRORS}
    return {'overall': overall, 'series': by}


def key(p):
    return f'{p["series_id"]}|{p["origin"]}|{p["horizon"]}'


def extended(points, series_ids):
    return {'precision': 'unrounded errors from common final integer predictions',
            'policy': statistics(points, 'policy', series_ids),
            'model_only': statistics(points, 'model_only', series_ids),
            'naive': statistics(points, 'naive', series_ids)}


def validate_rows(rows, config):
    from tools import origins, standard
    seen = set()
    for r in rows:
        sid, d, h = int(r['series_id']), date.fromisoformat(r['origin_date']), int(r['horizon'])
        if (sid, d, h) in seen:
            raise ValueError('Duplicate prediction key')
        seen.add((sid,d,h))
        origins.guard('p2', [d])
        if h not in standard.HORIZONS or date.fromisoformat(r['target_date']) != d+timedelta(days=h):
            raise ValueError('Invalid target date or horizon')
        if r['status'] not in standard.STATUSES:
            raise ValueError('Unknown prediction status')
        if r['status'] == 'OK' and (not math.isfinite(float(r['predicted_price'])) or float(r['predicted_price']) <= 0):
            raise ValueError('Invalid successful prediction')
        if r['data_version'] != config.get('data_version'):
            raise ValueError('Prediction data version mismatch')
    if not rows:
        raise ValueError('Empty prediction grid')
    return seen


def load_result(folder, snap=None, *, allow_unsealed=False):
    """Never rewrite/recompute legacy official metrics; RMSE remains unavailable there."""
    from tools import evaluate
    folder = Path(folder).resolve()
    if (folder/'invocation.json').exists() or (folder/'outcome.json').exists():
        outcome = effective_outcome(folder)
        if outcome['status'] in ('INCOMPLETE', 'ABANDONED', 'INTERRUPTED', 'FAILED_PREFLIGHT', 'PLANNED', 'HELP'):
            if not (allow_unsealed and outcome['status']=='INCOMPLETE'
                    and not (folder/'outcome.json').exists() and not (folder/'recovery.json').exists()):
                raise ValueError('Incomplete/non-executed audit run cannot be used as a completed result')
    catalog=HERE/'historical_baselines.json'
    if catalog.exists():
        for entry in read(catalog)['records']:
            if folder == (ROOT/entry['path']).resolve():
                if any(sha(folder/name)!=expected for name,expected in entry['sha256'].items()):
                    raise ValueError(f'Pinned historical source changed: {folder.name}')
    config, metrics = read(folder/'config.json'), read(folder/'metrics.json')
    rows = evaluate.read_predictions(folder)
    grid = validate_rows(rows, config)
    scope = {'origin_list': config.get('origin_list', config.get('origins')),
             'origins': sorted({d.isoformat() for sid,d,h in grid}),
             'series_ids': sorted({sid for sid,d,h in grid}), 'horizons': sorted({h for sid,d,h in grid}),
             'v1_id': config.get('data_version'), 'evaluation_rule': RULE}
    provenance = folder/'provenance.json'
    if provenance.exists():
        p = read(provenance)
        scope.update(p['comparison_conditions'])
        if sorted(grid) != sorted((sid,date.fromisoformat(d),h) for sid in scope['series_ids']
                                  for d in scope['origins'] for h in scope['horizons']):
            raise ValueError('Grid differs from planned scope')
    original = {'config.json': sha(folder/'config.json'), 'metrics.json': sha(folder/'metrics.json'),
                'predictions.csv': sha(folder/'predictions.csv')}
    for name in ('metrics_full_precision.json','provenance.json'):
        if (folder/name).exists():
            original[name]=sha(folder/name)
    if (folder/'artifacts_sha256.json').exists():
        verify_seal(folder)
    if (folder/'metrics_full_precision.json').exists():
        precise = read(folder/'metrics_full_precision.json')
        precision = precise['precision']
        policy = precise['policy']
        naive = precise['naive']
    else:
        policy0 = metrics['results']['policy']
        by = {}
        for sid in scope['series_ids']:
            s = policy0.get('series', {}).get(str(sid), {})
            by[str(sid)] = {m: s.get(m) for m in ERRORS}
            by[str(sid)].update(success_rate_pct=None, valid_predictions=None, failed_predictions=None)
        policy = {'overall': {'mape': policy0.get('macro_mape'), 'mae': None, 'rmse': None,
                              'rmae': policy0.get('macro_rmae'),
                              'success_rate_pct': metrics.get('success_rate', 0)*100,
                              'valid_predictions': None, 'failed_predictions': None}, 'series': by}
        # Exact counts from source statuses, not approximated using rounded success_rate.
        # Without original snapshot, eligible counts by series are unknown.
        naive = {'overall': {m: metrics.get('baselines', {}).get('naive', {}).get('macro_'+m) for m in ERRORS},
                 'series': {sid: {'mape': policy0['series'].get(sid, {}).get('naive_mape'),
                                  'mae': policy0['series'].get(sid, {}).get('naive_mae'),
                                  'rmse': None, 'rmae': None} for sid in by}}
        naive['overall']['success_rate_pct'] = 100.
        precision = 'legacy original metrics.json; rounded by common evaluator; missing metrics N/A'
    model_only = precise['model_only'] if (folder/'metrics_full_precision.json').exists() else None
    points = None
    if snap is not None:
        # Pairing is a separately named analysis, never substituted for historical metrics.
        points = evaluate.points_for(rows, snap)
        actual_sha = object_sha(sorted(key(p) for p in points))
        if scope.get('v1_sha') and scope['v1_sha'] != sha(snap.folder/'manifest.json'):
            raise ValueError('Pairing snapshot differs from source provenance')
        if scope.get('eligible_keys_sha') and actual_sha != scope['eligible_keys_sha']:
            raise ValueError('Eligible point set differs from provenance')
        if config.get('data_version') != snap.manifest['snapshot_id']:
            raise ValueError('Pairing snapshot version mismatch')
        if not (folder/'metrics_full_precision.json').exists():
            for sid, entry in policy['series'].items():
                pp = [p for p in points if str(p['series_id']) == sid]
                ok = sum(p['ok'] for p in pp)
                entry.update(valid_predictions=ok, failed_predictions=len(pp)-ok,
                             success_rate_pct=ok/len(pp)*100 if pp else None)
            policy['overall'].update(valid_predictions=sum(p['ok'] for p in points),
                                      failed_predictions=sum(not p['ok'] for p in points))
    return {'id': config.get('experiment_id', folder.name), 'name': config.get('name', folder.name),
            'folder': str(folder), 'conditions': scope, 'grid': {f'{s}|{d}|{h}' for s,d,h in grid},
            'policy': policy, 'model_only': model_only, 'naive': naive, 'precision': precision, 'points': points,
            'source_sha256': original, 'series_labels': {str(s): {'item': snap.series[s].item, 'market': snap.series[s].market}
                                                       for s in scope['series_ids']} if snap else {},
            'source_status_counts': dict(Counter(r['status'] for r in rows))}


def compare(base, new):
    eligible = comparability(base['conditions'], new['conditions'])
    bp, np = base.get('points'), new.get('points')
    point_info = {'baseline_grid_count': len(base['grid']), 'new_grid_count': len(new['grid']),
                  'baseline_only_grid': sorted(base['grid']-new['grid']), 'new_only_grid': sorted(new['grid']-base['grid'])}
    paired = None
    if base['grid'] != new['grid']:
        eligible = {'label': 'reference', 'reasons': [*eligible['reasons'], 'different:actual_grid']}
    if bp is not None and np is not None:
        bm, nm = {key(p):p for p in bp}, {key(p):p for p in np}
        common = set(bm)&set(nm)
        success = {k for k in common if bm[k]['ok'] and nm[k]['ok']}
        point_info.update(baseline_eligible=len(bm), new_eligible=len(nm), common_eligible=len(common),
                          common_success=len(success), baseline_only_eligible=sorted(set(bm)-set(nm)),
                          new_only_eligible=sorted(set(nm)-set(bm)),
                          baseline_only_success=sorted(k for k in common if bm[k]['ok'] and not nm[k]['ok']),
                          new_only_success=sorted(k for k in common if nm[k]['ok'] and not bm[k]['ok']))
        if any(bm[k]['y'] != nm[k]['y'] or bm[k]['naive'] != nm[k]['naive'] for k in common):
            raise ValueError('Paired truth or Naive mismatch')
        ids = sorted(set(base['conditions']['series_ids']) | set(new['conditions']['series_ids']))
        paired = {mode: {'baseline': statistics([bm[k] for k in sorted(keys)], pred, ids),
                         'new': statistics([nm[k] for k in sorted(keys)], pred, ids)}
                  for mode,keys,pred in [('common_eligible_policy',common,'policy'),
                                         ('common_success',success,'model_only')]}
        for pair in paired.values():
            pair['changes'] = metric_comparison(pair['baseline'], pair['new'], ids)
        if set(bm) != set(nm):
            eligible = {'label': 'reference', 'reasons': [*eligible['reasons'], 'different:actual_eligible_keys']}
    ids = sorted(set(base['policy']['series']) | set(new['policy']['series']), key=int)
    comparisons = metric_comparison(base['policy'], new['policy'], ids)
    model_comparisons = (metric_comparison(base['model_only'], new['model_only'], ids)
                         if base.get('model_only') is not None and new.get('model_only') is not None else None)
    counts = Counter()
    for sid, value in comparisons['series'].items():
        direction = value['mape']['direction']
        counts[direction if eligible['label']=='direct' else 'unavailable'] += 1
    return {'baseline_id': base['id'], 'new_id': new['id'], 'comparability': eligible,
            'precision': {'baseline': base['precision'], 'new': new['precision']},
            'source_sha256': {'baseline': base['source_sha256'], 'new': new['source_sha256']},
            'point_sets': point_info, 'policy': comparisons, 'model_only': model_comparisons, 'paired_analysis': paired,
            'series_labels': {**base.get('series_labels', {}), **new.get('series_labels', {})},
            'series_counts': {k: counts[k] for k in ('improved','worsened','same','unavailable')},
            'series_denominator': len(ids),
            'effect_attribution': 'not_established' if eligible['label']=='reference' else 'matched_evaluation_conditions',
            'note': ('REFERENCE ONLY: numerical changes are descriptive; direct improvement effect is NOT established.'
                     if eligible['label']=='reference' else
                     'Matched evaluation conditions; numerical improvements alone do not establish causality.'),
            'metric_scopes': {'policy': 'All eligible points, with Naive fallback on unsuccessful predictions',
                              'model_only': 'Each run successful predictions; success sets may differ',
                              'paired_analysis.common_success': 'Identical keys successful in both runs'}}


def metric_comparison(base, new, ids):
    return {'overall': {m: change(base['overall'].get(m), new['overall'].get(m), m) for m in METRICS},
            'series': {str(s): {m: change(base['series'].get(str(s),{}).get(m),
                                         new['series'].get(str(s),{}).get(m),m) for m in METRICS} for s in ids}}


def naive_comparison(result):
    naive = {**result, 'id': 'Naive@'+result['id'], 'policy': result['naive'], 'model_only': None}
    # The Naive is defined on this run's exact eligible points, not a copied historical number.
    naive['precision'] = result['precision'] + '; source baselines.naive / full_precision.naive'
    naive['points'] = None
    return compare(naive, result)


def fmt(v):
    return 'N/A' if v is None else f'{v:.8g}' if isinstance(v,(int,float)) else str(v)


def markdown(result, comparisons):
    o = result['policy']['overall']
    control = comparisons.get('CONTROL')
    nv = comparisons.get('Naive')
    def improvement(c):
        if c is None:
            return 'N/A'
        suffix = 'reference; descriptive only; improvement effect NOT established' if c['comparability']['label']=='reference' else 'direct'
        return fmt(c['policy']['overall']['mape']['relative_improvement_pct'])+' ('+suffix+')'
    counts = control['series_counts'] if control else None
    lines = [f'\n## {result["id"]}\n',
             '| 실행 ID | 실험 | MAPE (%) | MAE | RMSE | rMAE | CONTROL 대비 MAPE 개선률 (%) | Naive 대비 개선률 (%) | 개선 계열 수 |',
             '| --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- |',
             f'| {result["id"]} | {result["name"]} | '+ ' | '.join(fmt(o.get(m)) for m in ERRORS) +
             f' | {improvement(control)} | {improvement(nv)} | {fmt(counts["improved"]) if counts else "N/A"} |',
             f'\nPrecision: {result["precision"]}. All aggregate MAE/RMSE values are descriptive macro averages across price units.\n']
    for label,c in comparisons.items():
        lines += [f'\n### {label}: {c["comparability"]["label"]}\n',
                  c['note'],
                  'Metric scope: policy includes Naive fallback. model_only uses successful model predictions; '
                  'paired_analysis.common_success uses the identical successful observation set (comparison.json).',
                  'Reasons: '+(', '.join(c['comparability']['reasons']) or 'identical recorded evaluation conditions'),
                  '\n| 전체 지표 | 기준 | 신규 | 절대 차이 | 단위 | 상대 개선/변화 (%) | 판정 |',
                  '| --- | ---: | ---: | ---: | --- | ---: | --- |']
        for m,v in c['policy']['overall'].items():
            pct=v['relative_improvement_pct'] if m in ERRORS else v['relative_change_pct']
            lines.append(f'| {m} | '+' | '.join(fmt(x) for x in (v['baseline'],v['new'],v['absolute_difference'],v['unit'],pct,v['direction']))+' |')
        lines += [
                  '\n| 계열 | 품목/시장 | 지표 | 기준 | 신규 | 절대 차이 | 단위 | 상대 개선/변화 (%) | 판정 |',
                  '| --- | --- | --- | ---: | ---: | ---: | --- | ---: | --- |']
        for sid,metrics in c['policy']['series'].items():
            label_info=c['series_labels'].get(sid,{})
            for m,v in metrics.items():
                pct=v['relative_improvement_pct'] if m in ERRORS else v['relative_change_pct']
                lines.append(f'| {sid} | {label_info.get("item", "?")}/{label_info.get("market", "?")} | {m} | '+
                             ' | '.join(fmt(x) for x in (v['baseline'],v['new'],v['absolute_difference'],v['unit'],pct,v['direction']))+' |')
        lines += ['\nSeries counts: '+str(c['series_counts'])+'/'+str(c['series_denominator']),
                  '\nPoint set differences and paired policy/common-success metrics: see comparison.json.\n']
    return '\n'.join(lines)+'\n'
