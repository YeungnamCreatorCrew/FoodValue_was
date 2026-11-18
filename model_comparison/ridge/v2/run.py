"""Audited Ridge-only loop built on the unmodified team pooled training primitives."""
import argparse
import csv
from collections import Counter
from datetime import timedelta
import json
from pathlib import Path
import sys
import time

from . import audit as A


def prediction_category(status, error, fit_state):
    """Audit classification only; common prediction statuses/evaluation stay intact."""
    if status == 'OK':
        return 'success'
    if status == 'NO_INPUT' or (status == 'FIT_FAILED' and fit_state == 'missing'):
        return 'expected_missing'
    if status == 'TIMEOUT' or (status == 'FIT_FAILED' and fit_state == 'timeout'):
        return 'timeout'
    if status == 'INVALID_VALUE' or (status == 'PREDICT_FAILED' and error == 'NONE'):
        return 'abnormal_prediction'
    return 'fit_failure' if status == 'FIT_FAILED' else 'predict_failure'


def health_summary(counts, events):
    categories = {k: counts[k] for k in ('success', 'expected_missing', 'fit_failure',
                                        'predict_failure', 'timeout', 'abnormal_prediction')}
    total = sum(categories.values())
    errors = total-categories['success']-categories['expected_missing']
    return {'denominator': 'all emitted prediction rows, including evaluation-ineligible rows',
            'prediction_rows': total, 'categories': categories,
            'prediction_success_rate': categories['success']/total if total else None,
            'missing_rate': categories['expected_missing']/total if total else None,
            'error_row_count': errors, 'error_event_counts': dict(events),
            'error_event_count': sum(events.values()),
            'has_model_errors': bool(errors or sum(events.values()))}


def exit_code(status):
    return 0 if status in ('PLANNED', 'COMPLETED', 'COMPLETED_WITH_MISSING', 'REPORTED', 'HELP') else 1


def validate_config(config):
    from tools import loader, standard
    from model_comparison.v2 import features as F
    from .model import PooledRidgeV2
    required = {'name','model','class','params','window_days','seed','bundles','blocks','strategy'}
    if required-set(config):
        raise ValueError(f'Missing configuration fields: {sorted(required-set(config))}')
    unknown=set(config)-(required|{'target_transform','refit','comparison','description'})
    if unknown:
        raise ValueError(f'Unknown configuration fields (scope belongs to CLI): {sorted(unknown)}')
    if config['class'] != 'model_comparison.ridge.v2.model:PooledRidgeV2' or config['model'] != 'Ridge':
        raise ValueError('Ridge v2 class/model required')
    if not isinstance(config['name'],str) or not config['name'].strip():
        raise ValueError('Experiment name is required')
    if config['strategy'] != 'direct_per_horizon' or config.get('target_transform') != 'change_ratio':
        raise ValueError('direct_per_horizon/change_ratio required')
    if config.get('refit') != standard.REFIT:
        raise ValueError('Weekly refit required')
    for group in ('bundles','blocks'):
        if not isinstance(config[group],list) or len(set(config[group])) != len(config[group]):
            raise ValueError('Feature groups must be unique lists')
    loader.check_bundles(config['bundles'])
    if set(config['blocks'])-set(F.V2_BLOCKS):
        raise ValueError('Unknown v2 feature block')
    if isinstance(config['window_days'],bool) or not isinstance(config['window_days'],int) or config['window_days'] < 400:
        raise ValueError('window_days must be an integer >=400')
    if isinstance(config['seed'],bool) or not isinstance(config['seed'],int) or config['seed'] < 0:
        raise ValueError('seed must be a nonnegative integer')
    if set(config['params'])-{'alpha','solver','strategy'}:
        raise ValueError('Unknown Ridge parameter')
    PooledRidgeV2(**config['params'])
    if config['params'].get('strategy',config['strategy']) != config['strategy']:
        raise ValueError('Inconsistent strategy')
    return F.feature_names(config['bundles'],config['blocks'])


def preflight(args):
    from tools import loader, origins, standard
    from . import comparison as C
    if args.origins not in ('tune','validation'):
        raise ValueError('Final Test is forbidden: only tune/validation allowed')
    config = A.read(args.config)
    names = validate_config(config)
    data = A.verify_data(args.snapshot,args.extra)
    snap = loader.Snapshot(args.snapshot)
    if len(snap.series_ids) != standard.DEFAULT_SERIES_COUNT:
        raise ValueError('Training requires exactly 10 price series')
    days = list(snap.origins[args.origins])
    if args.month:
        # Parse exactly; malformed month cannot silently yield an empty experiment.
        import datetime
        datetime.datetime.strptime(args.month,'%Y-%m')
        days = [d for d in days if d.strftime('%Y-%m') == args.month]
    if not days or days != sorted(set(days)):
        raise ValueError('Origin list must be nonempty, unique and chronological')
    origins.guard('p2',days)
    ids = snap.series_ids if not args.series else [int(s) for s in args.series.split(',')]
    if not ids or len(set(ids)) != len(ids) or set(ids)-set(snap.series_ids):
        raise ValueError('Unknown, duplicate or empty evaluation series')
    # Eligible truth metadata is used for auditing/evaluation only, never passed to fit.
    dummy = [{'series_id':sid,'origin_date':str(d),'target_date':str(d+timedelta(days=h)),
              'horizon':h,'status':'FIT_FAILED'} for sid in ids for d in days for h in standard.HORIZONS]
    from tools import evaluate
    points = evaluate.points_for(dummy,snap)
    conditions = {'v1_id':data['v1']['id'],'v1_sha':data['v1']['manifest_sha256'],
                  'v2_id':data['v2']['id'],'v2_sha':data['v2']['manifest_sha256'],
                  'data_period': {'cutoff':data['v1']['manifest']['cutoff'],
                                  'series':data['v1']['manifest']['series']},
                  'origin_list':args.origins,'origins':[str(d) for d in days],
                  'series_ids':sorted(ids),'horizons':list(standard.HORIZONS),
                  'evaluation_rule':C.RULE,'evaluation_source_sha':A.sha(A.ROOT/'tools/evaluate.py'),
                  'eligible_keys_sha':A.object_sha(sorted(C.key(p) for p in points))}
    return config,snap,days,ids,{'data':data,'comparison_conditions':conditions,
           'training_series':snap.series_ids,'origin_count':len(days),'evaluation_series_count':len(ids),
           'feature_names':names,'input_feature_count':len(names),'model_feature_count':len(names)-1,
           'feature_changes':config.get('comparison',{}),
           'preprocessing':'Per horizon TRAIN median, all-NaN frozen zero, TRAIN StandardScaler',
           'target':'target/current-1; price=current*(1+prediction)',
           'data_visibility':'own price <=origin; external observed data <=origin-1; calendar known; production publication lag'}


def train(config,snap,days,ids,args,attempt,matrix_factory=None):
    """Incrementally persist every prediction; use common Matrices/load_class/postprocessing."""
    import numpy as np
    from model_comparison.v2 import features as F, run_pooled
    from tools import evaluate, run_backtest as B, standard
    from .model import AUDIT_SINK
    from . import comparison as C
    record={**config,'experiment_id':attempt.folder.name,'data_version':standard.DATA_VERSION,
            'phase':'v2','origin_list':args.origins,'month':args.month,'series':ids,
            'feature_count':len(F.feature_names(config['bundles'],config['blocks'])),
            'git_sha':A.git('rev-parse','HEAD'),'implementation_version':'ridge-v2.1'}
    record.update(extra_features=[*config['bundles'],*config['blocks']],
                  feature_set='v2:'+str(config['window_days']),config_sha256=A.object_sha(config))
    record['config_id']=B.config_id(record)
    A.exclusive_json(attempt.folder/'config.json',record)
    cls=B.load_class(config['class'])
    if matrix_factory is None:
        matrix_factory=run_pooled.Matrices
    mats=matrix_factory(snap,F.V2Features(snap,args.extra),config['bundles'],config['blocks'])
    model,week=None,None
    failures,success,fit_seconds=0,0,0.
    counts, error_events = Counter(), Counter()
    fit_state = 'failure'
    token=AUDIT_SINK.set(lambda event: attempt.event(event['event'],**{k:v for k,v in event.items() if k!='event'}))
    try:
        with (attempt.folder/'predictions.csv').open('x',encoding='utf-8',newline='') as f:
            writer=csv.writer(f,lineterminator='\n')
            writer.writerow(standard.PREDICTION_COLUMNS)
            for d in days:
                attempt.context={'origin':str(d)}
                if d.isocalendar()[:2] != week:
                    week=d.isocalendar()[:2]
                    model=None
                    fit_state='failure'
                    start=time.perf_counter()
                    try:
                        parts=[mats.training(sid,snap.series[sid].index(d),config['window_days']) for sid in snap.series_ids]
                        parts=[p for p in parts if p is not None and len(p[1])]
                        h=np.concatenate([p[2] for p in parts]) if parts else np.array([])
                        if h.ndim != 1 or not np.isin(h,standard.HORIZONS).all():
                            raise ValueError('Malformed training horizons')
                        if not parts or not set(standard.HORIZONS) <= set(h):
                            fit_state='missing'
                            attempt.event('FIT_UNAVAILABLE',reason='INSUFFICIENT_TRAINING_SAMPLES',
                                          available_horizons=sorted(map(int,set(h))))
                        else:
                            X,y=(np.concatenate([p[k] for p in parts]) for k in range(2))
                            attempt.event('FIT_STARTED',samples=len(y),training_series=snap.series_ids,
                                          horizon_samples={str(g):int((h==g).sum()) for g in standard.HORIZONS})
                            candidate=cls(**config['params'])
                            candidate.fit(X,y,h,mats.names,config['seed'])
                            model=candidate
                            fit_state='success'
                    except Exception as e:
                        attempt.error(e,'fit')
                        error_events['fit_failure']+=1
                        model=None
                    elapsed=time.perf_counter()-start
                    fit_seconds+=elapsed
                    if elapsed>standard.TIMEOUT_SECONDS['refit']:
                        attempt.event('FIT_TIMEOUT',seconds=elapsed)
                        error_events['fit_timeout']+=1
                        fit_state='timeout'
                        model=None
                    attempt.event('REFIT_FINISHED',seconds=elapsed,usable=model is not None)
                for sid in ids:
                    attempt.context={'origin':str(d),'series_id':sid}
                    start=time.perf_counter()
                    try:
                        x=mats.inputs(sid,snap.series[sid].index(d))
                        if model is None:
                            rows=B.prediction_rows(None,'FIT_FAILED','NOT_FITTED')
                        elif x is None:
                            rows=B.prediction_rows(None,'NO_INPUT','STALE_OR_GAP')
                        else:
                            values=model.predict(x,np.array(standard.HORIZONS))
                            rows=B.prediction_rows([None if np.isnan(v) else float(v) for v in values],'OK','')
                    except Exception as e:
                        attempt.error(e,'predict')
                        error_events['predict_failure']+=1
                        rows=B.prediction_rows(None,'PREDICT_FAILED',type(e).__name__)
                    elapsed=time.perf_counter()-start
                    if elapsed>standard.TIMEOUT_SECONDS['predict']:
                        error_events['predict_timeout']+=1
                        rows=B.prediction_rows(None,'TIMEOUT','PREDICT_TIMEOUT')
                    for h,(raw,price,status,error) in zip(standard.HORIZONS,rows):
                        s=snap.series[sid]
                        writer.writerow([attempt.folder.name,'Ridge',record['config_id'],standard.DATA_VERSION,
                                         sid,s.item,s.market,str(d),str(d+timedelta(days=h)),h,raw,price,status,error])
                        failures+=status!='OK'
                        success+=status=='OK'
                        counts[prediction_category(status,error,fit_state)]+=1
                    f.flush()
                    import os
                    os.fsync(f.fileno())
                    attempt.event('PREDICTION_BATCH',seconds=elapsed,statuses=[r[2] for r in rows],
                                  categories=[prediction_category(r[2],r[3],fit_state) for r in rows],
                                  fit_state=fit_state)
        attempt.context={}
        health=health_summary(counts,error_events)
        A.exclusive_json(attempt.folder/'prediction_health.json',health)
        metrics,digest=evaluate.write_metrics(attempt.folder,snap)
        points=evaluate.points_for(evaluate.read_predictions(attempt.folder),snap)
        A.exclusive_json(attempt.folder/'metrics_full_precision.json',C.extended(points,ids))
        if model is not None:
            A.exclusive_json(attempt.folder/'importance.json',model.importance())
        attempt.event('EVALUATED',metrics_sha256=digest,successful_rows=success,failed_rows=failures,fit_seconds=fit_seconds)
        if health['has_model_errors']:
            return 'PARTIAL' if success else 'FAILED'
        return 'COMPLETED_WITH_MISSING' if counts['expected_missing'] else 'COMPLETED'
    finally:
        AUDIT_SINK.reset(token)
        attempt.context={}


def reports(folder,snap,baselines,attempt):
    from . import comparison as C
    result=C.load_result(folder,snap,allow_unsealed=Path(folder).resolve()==attempt.folder.resolve())
    comparisons={'Naive':C.naive_comparison(result)}
    for spec in baselines:
        label,sep,path=spec.partition('=')
        if not sep or not label or label=='Naive':
            raise ValueError('Use --baseline LABEL=FOLDER (Naive is automatic)')
        if label in comparisons:
            raise ValueError('Duplicate baseline label')
        base=C.load_result(Path(path),snap)
        comparisons[label]=C.compare(base,result)
    A.exclusive_json(attempt.folder/'comparison.json',comparisons)
    text=C.markdown(result,comparisons)
    with (attempt.folder/'RESULTS.md').open('x',encoding='utf-8') as f:
        f.write(text)
    return text


def parser():
    p=argparse.ArgumentParser(description='Ridge v2: audited plan by default; Test forbidden')
    p.add_argument('--config',type=Path,default=A.HERE/'configs/control.json')
    p.add_argument('--origins',default='tune')
    p.add_argument('--month')
    p.add_argument('--series')
    p.add_argument('--snapshot',type=Path,default=A.ROOT/'data/snapshots/fv-snap-20261031-v1')
    p.add_argument('--extra',type=Path,default=A.ROOT/'data/snapshots'/A.EXTRA_ID)
    p.add_argument('--execute',action='store_true')
    p.add_argument('--retry-of')
    p.add_argument('--purpose',default='Pre-registered feature experiment')
    p.add_argument('--changes',default='As specified in experiment config')
    p.add_argument('--reason',default='Pre-registered isolated feature contribution comparison')
    p.add_argument('--next-decision',default='PENDING_REVIEW; no automatic favorable feature selection')
    p.add_argument('--baseline',action='append',default=[])
    p.add_argument('--compare-only',type=Path,help='Read existing result; produce new audited report, no fit')
    return p


def main(argv=None,*,root=None):
    argv=list(sys.argv[1:] if argv is None else argv)
    root=Path(root or A.EXPERIMENTS)
    # Lock/record allocation errors are printed to stderr. No data/config access or training precedes allocation.
    try:
        with A.lock(root):
            A.recover_incomplete(root)
            attempt=A.Attempt(root,argv)
            A.append(root.parent/'EXPERIMENT_LOG.md',f'\n- {A.now()} `{attempt.folder.name}` **STARTED**; '+
                     f'[invocation](experiments/{attempt.folder.name}/invocation.json)\n')
            status,stage='FAILED_PREFLIGHT','bootstrap'
            text=None
            interrupted=None
            args=None
            try:
                args=parser().parse_args(argv)
                from tools.runtime import apply_environment
                apply_environment()
                attempt.capture()
                if args.origins not in ('tune','validation'):
                    raise ValueError('Final Test is forbidden')
                if args.retry_of:
                    if Path(args.retry_of).name != args.retry_of or not (root/args.retry_of/'outcome.json').is_file():
                        raise ValueError('retry-of must identify a previous terminal run in this registry')
                    if '--changes' not in argv or '--reason' not in argv:
                        raise ValueError('Retries require explicit --changes and --reason')
                attempt.event('INTENT',purpose=args.purpose,changes=args.changes,reason=args.reason,
                              previous_run_id=args.retry_of,retry=bool(args.retry_of),next_decision=args.next_decision)
                stage='preflight'
                if args.compare_only:
                    if args.execute:
                        raise ValueError('compare-only cannot execute')
                    from tools import loader
                    A.verify_data(args.snapshot,args.extra)
                    snap=loader.Snapshot(args.snapshot)
                    stage='comparison'
                    text=reports(args.compare_only,snap,args.baseline,attempt)
                    status='REPORTED'
                else:
                    with (attempt.folder/'requested_config.raw').open('xb') as f:
                        f.write(args.config.read_bytes())
                    config,snap,days,ids,provenance=preflight(args)
                    A.exclusive_json(attempt.folder/'requested_config.json',config)
                    A.exclusive_json(attempt.folder/'provenance.json',provenance)
                    # Validate every requested comparison source before any training begins.
                    from . import comparison as C
                    baseline_labels=set()
                    for spec in args.baseline:
                        label,sep,path=spec.partition('=')
                        if not sep or not label or label=='Naive' or label in baseline_labels:
                            raise ValueError('Use --baseline LABEL=FOLDER')
                        baseline_labels.add(label)
                        C.load_result(Path(path),snap)
                    attempt.event('PREFLIGHT_PASSED',origin_count=len(days),training_series=snap.series_ids,
                                  evaluation_series=ids,feature_count=len(provenance['feature_names']))
                    if args.execute:
                        stage='training'
                        status=train(config,snap,days,ids,args,attempt)
                        stage='comparison'
                        text=reports(attempt.folder,snap,args.baseline,attempt)
                    else:
                        status='PLANNED'
                attempt.finish(status,stage=stage)
            except BaseException as e:
                # Never append errors or call finish twice after a terminal write/seal.
                if (attempt.folder/'outcome.json').exists() or (attempt.folder/'artifacts_sha256.json').exists():
                    raise RuntimeError('Audit finalization failed; inspect effective_outcome before counting this run') from e
                if isinstance(e,KeyboardInterrupt):
                    status='INTERRUPTED'
                elif isinstance(e,SystemExit) and e.code==0:
                    status='HELP'
                else:
                    status='FAILED_PREFLIGHT' if stage in ('bootstrap','preflight') else 'FAILED'
                attempt.error(e,stage)
                attempt.finish(status,stage=stage)
                if isinstance(e,KeyboardInterrupt):
                    interrupted=e
            # Aggregate documents append; independent originals and reports are sealed above.
            A.append(root.parent/'EXPERIMENT_LOG.md',f'\n- {A.now()} `{attempt.folder.name}` **{status}**; '+
                     f'command/intention/errors/retry/next decision: [{attempt.folder.name}](experiments/{attempt.folder.name}/events.jsonl)\n')
            if args is not None:
                A.append(root.parent/'EXPERIMENT_LOG.md',json.dumps({
                    'purpose':args.purpose,'changes':args.changes,'reason':args.reason,
                    'previous_run_id':args.retry_of,'retry':bool(args.retry_of),
                    'next_decision':args.next_decision,'result_status':status,
                    'summary_source':str(attempt.folder/'metrics.json') if (attempt.folder/'metrics.json').exists() else None,
                    'errors_source':str(attempt.folder/'events.jsonl')},ensure_ascii=False)+'\n')
            if text:
                A.append(root.parent/'RESULTS.md',text)
            print(json.dumps({'run_id':attempt.folder.name,'status':status,'folder':str(attempt.folder)},ensure_ascii=False))
            if interrupted is not None:
                raise interrupted
            return exit_code(status)
    except (OSError,RuntimeError) as e:
        print(f'Cannot allocate/complete audit record; training refused: {e}',file=sys.stderr)
        return 2


if __name__=='__main__':
    sys.exit(main())
