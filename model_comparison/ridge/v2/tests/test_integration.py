from datetime import date
import json
from types import SimpleNamespace
import numpy as np
import pytest
from model_comparison.ridge.v2 import audit as A, comparison as C, run as R
from model_comparison.ridge.v2.model import AUDIT_SINK, PooledRidgeV2
from model_comparison.v2 import run_pooled
from tools import evaluate, export_snapshot, loader, run_backtest, standard
from tests.test_snapshot_tools import fake_raw
from tests.test_v2 import write_extra


@pytest.fixture(scope='module')
def synthetic(tmp_path_factory):
    root=tmp_path_factory.mktemp('ridge-v2-synthetic')
    snapdir=root/'snap'
    export_snapshot.build(fake_raw(),snapdir,cutoff=standard.DATA_CUTOFF)
    extra=write_extra(root/'extra')
    return loader.Snapshot(snapdir),snapdir,extra


def setup_run(tmp_path,synthetic):
    snap,snapdir,extra=synthetic
    config=A.read(A.HERE/'configs/control.json')
    args=SimpleNamespace(origins='tune',month='2025-01',series='1',snapshot=snapdir,extra=extra)
    days=[d for d in snap.origins['tune'] if str(d).startswith('2025-01')][:2]
    attempt=A.Attempt(tmp_path/'experiments',['synthetic'])
    return config,args,snap,days,attempt


def test_common_runner_dynamic_loading_and_byte_identical_predictions_metrics(tmp_path,synthetic):
    config,args,snap,days,attempt=setup_run(tmp_path,synthetic)
    # Use two synthetic weekly origins in both runners.
    configpath=tmp_path/'c.json'; A.exclusive_json(configpath,config)
    original=snap.origins['tune']
    snap.origins['tune']=days
    # Common run loads its own snapshot, so select a month with matching weekly list through monkeypatch.
    from unittest.mock import patch
    with patch.object(run_pooled.loader,'Snapshot',return_value=snap):
        common=run_pooled.run(SimpleNamespace(config=configpath,origins='tune',month='2025-01',series='1',
                                             snapshot=args.snapshot,extra=args.extra,out=tmp_path/'common'))
    snap.origins['tune']=original
    assert R.train(config,snap,days,[1],args,attempt) in ('COMPLETED','PARTIAL')
    a,b=evaluate.read_predictions(common),evaluate.read_predictions(attempt.folder)
    for rows in (a,b):
        for r in rows: r.pop('experiment_id')
    assert a==b
    assert A.read(common/'metrics.json')==A.read(attempt.folder/'metrics.json')
    full=A.read(attempt.folder/'metrics_full_precision.json')
    assert full['policy']['overall']['rmse'] is not None
    assert AUDIT_SINK.get() is None
    assert 'FIT' in (attempt.folder/'events.jsonl').read_text(encoding='utf-8')


def test_failed_weekly_refit_never_reuses_previous_model_and_retains_partial(tmp_path,synthetic,monkeypatch):
    config,args,snap,days,attempt=setup_run(tmp_path,synthetic)
    old=run_pooled.Matrices.training
    def broken(self,sid,i,window):
        result=old(self,sid,i,window)
        if i==snap.series[sid].index(days[1]) and result is not None:
            x,y,h=result
            y=y.copy(); y[0]=np.inf
            return x,y,h
        return result
    monkeypatch.setattr(run_pooled.Matrices,'training',broken)
    assert R.train(config,snap,days,[1],args,attempt)=='PARTIAL'
    rows=evaluate.read_predictions(attempt.folder)
    assert any(r['status']=='OK' for r in rows[:7])
    assert all(r['status']=='FIT_FAILED' for r in rows[7:])
    assert A.read(attempt.folder/'metrics.json')['status_counts']['FIT_FAILED']==7
    assert 'Target prices' in (attempt.folder/'run.log').read_text(encoding='utf-8')


@pytest.mark.parametrize('error',[KeyboardInterrupt('stop'),MemoryError('OOM'),RuntimeError('prediction fail')])
def test_prediction_exceptions_preserve_flushed_rows_and_audit(tmp_path,synthetic,monkeypatch,error):
    config,args,snap,days,attempt=setup_run(tmp_path,synthetic)
    old=PooledRidgeV2.predict
    calls=0
    def fail(self,*a,**kw):
        nonlocal calls
        calls+=1
        if calls==2: raise error
        return old(self,*a,**kw)
    monkeypatch.setattr(PooledRidgeV2,'predict',fail)
    if isinstance(error,KeyboardInterrupt):
        with pytest.raises(KeyboardInterrupt): R.train(config,snap,days,[1],args,attempt)
        assert len(evaluate.read_predictions(attempt.folder))==7
    else:
        assert R.train(config,snap,days,[1],args,attempt)=='PARTIAL'
        assert len(evaluate.read_predictions(attempt.folder))==14
        assert all(r['status']=='PREDICT_FAILED' for r in evaluate.read_predictions(attempt.folder)[7:])
    assert AUDIT_SINK.get() is None


def test_common_matrices_future_price_targets_excluded(synthetic):
    snap,_,extra=synthetic
    from model_comparison.v2.features import V2Features
    d=date(2025,1,6)
    def training():
        mats=run_pooled.Matrices(snap,V2Features(snap,extra),[],['SERIES_ID'])
        return mats.training(1,snap.series[1].index(d),1825)
    a=training()
    s=snap.series[1]
    i=s.index(d)
    actual,filled=s.actual.copy(),s.filled.copy()
    try:
        s.actual[i+1:]=999999.
        s.filled[i+1:]=999999.
        b=training()
        for left,right in zip(a,b): np.testing.assert_array_equal(left,right)
    finally:
        s.actual[:]=actual
        s.filled[:]=filled


def test_default_plan_and_preflight_abort_never_construct_matrices(tmp_path,synthetic,monkeypatch):
    config,args,snap,days,attempt=setup_run(tmp_path,synthetic)
    monkeypatch.setattr(A.Attempt,'capture',lambda self:None)
    monkeypatch.setattr(R,'train',lambda *a:pytest.fail('Planning must not train'))
    monkeypatch.setattr(R,'preflight',lambda args:(config,snap,days,[1],{'feature_names':['current','horizon']}))
    assert R.main([],root=tmp_path/'plans')==0
    folder=next((tmp_path/'plans').glob('ridge-v2-*'))
    assert A.read(folder/'outcome.json')['status']=='PLANNED'
    def bad(args): raise ValueError('synthetic manifest error')
    monkeypatch.setattr(R,'preflight',bad)
    assert R.main(['--execute'],root=tmp_path/'plans')==1
    assert len(list((tmp_path/'plans').glob('ridge-v2-*')))==2


def test_actual_preflight_rejects_data_before_feature_construction(tmp_path,monkeypatch):
    args=R.parser().parse_args(['--execute'])
    def bad(*args): raise ValueError('Manifest SHA-256 mismatch')
    monkeypatch.setattr(A,'verify_data',bad)
    monkeypatch.setattr(loader,'Snapshot',lambda *args:pytest.fail('Invalid data must stop before loading'))
    with pytest.raises(ValueError,match='Manifest SHA'): R.preflight(args)
    args.origins='test'
    with pytest.raises(ValueError,match='Test'): R.preflight(args)


def test_full_wrapper_seals_comparison_retry_and_reports_without_overwrite(tmp_path,synthetic,monkeypatch):
    config,args,snap,days,_=setup_run(tmp_path,synthetic)
    from model_comparison.v2 import features as F
    dummy=[{'series_id':1,'origin_date':str(d),'target_date':str(d+__import__('datetime').timedelta(days=h)),
            'horizon':h,'status':'FIT_FAILED'} for d in days for h in standard.HORIZONS]
    points=evaluate.points_for(dummy,snap)
    conditions={k:'synthetic' for k in C.CONDITIONS}
    conditions.update(v1_id=standard.DATA_VERSION,v1_sha=A.sha(snap.folder/'manifest.json'),
                      origin_list='tune',origins=[str(d) for d in days],series_ids=[1],horizons=list(standard.HORIZONS),
                      eligible_keys_sha=A.object_sha(sorted(C.key(p) for p in points)))
    provenance={'comparison_conditions':conditions,'feature_names':F.feature_names([],['SERIES_ID'])}
    monkeypatch.setattr(R,'preflight',lambda args:(config,snap,days,[1],provenance))
    monkeypatch.setattr(A.Attempt,'capture',lambda self:None)
    root=tmp_path/'runs'
    argv=['--execute','--extra',str(args.extra)]
    assert R.main(argv,root=root)==0
    first=next(root.glob('ridge-v2-*'))
    originals={p.relative_to(first):p.read_bytes() for p in first.rglob('*') if p.is_file()}
    assert A.verify_seal(first)
    assert R.main([*argv,'--retry-of',first.name,'--changes','repeat','--reason','determinism',
                   '--baseline','CONTROL='+str(first)],root=root)==0
    second=next(p for p in root.glob('ridge-v2-*') if p!=first)
    comparison=A.read(second/'comparison.json')['CONTROL']
    assert comparison['comparability']['label']=='direct'
    assert comparison['policy']['overall']['mape']['absolute_difference']==0
    assert comparison['series_counts']['same']==1
    assert len(comparison['paired_analysis']['common_success']['changes']['series'])==1
    assert {p.relative_to(first):p.read_bytes() for p in first.rglob('*') if p.is_file()}==originals
    assert A.verify_seal(second)
    report=(second/'RESULTS.md').read_text(encoding='utf-8')
    assert all(m in report for m in C.METRICS)
    assert first.name in (tmp_path/'EXPERIMENT_LOG.md').read_text(encoding='utf-8')
