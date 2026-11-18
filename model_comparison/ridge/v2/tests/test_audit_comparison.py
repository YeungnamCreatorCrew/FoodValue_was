import copy
from datetime import date
import json
from pathlib import Path
from types import SimpleNamespace
import pytest
from model_comparison.ridge.v2 import audit as A, comparison as C, run as R


def test_unique_ids_exclusive_files_seal_recovery_and_lock(tmp_path):
    root=tmp_path/'experiments'
    with A.lock(root):
        one,two=A.Attempt(root,['same']),A.Attempt(root,['same'])
        assert one.folder!=two.folder
        A.exclusive_json(one.folder/'keep.json',{'keep':True})
        with pytest.raises(FileExistsError): A.exclusive_json(one.folder/'keep.json',{})
        one.finish('FAILED',previous_run_id=None)
        before=(one.folder/'artifacts_sha256.json').read_bytes()
        A.recover_incomplete(root)
        assert A.read(two.folder/'outcome.json')['status']=='ABANDONED'
        assert (one.folder/'artifacts_sha256.json').read_bytes()==before
        assert A.verify_seal(one.folder)
        with pytest.raises(RuntimeError):
            with A.lock(root): pass
    (one.folder/'keep.json').write_text('{}')
    with pytest.raises(ValueError): A.verify_seal(one.folder)


def test_manifest_hash_rows_and_path_escape(tmp_path):
    folder=tmp_path/'snap'; folder.mkdir()
    p=folder/'x.csv'; p.write_text('a\n1\n')
    manifest={'files':{'x.csv':{'sha256':A.sha(p),'rows':1}}}
    A.exclusive_json(folder/'manifest.json',manifest)
    digest=A.sha(folder/'manifest.json')
    assert A.verify_manifest(folder,digest)==manifest
    with pytest.raises(ValueError,match='Manifest SHA'): A.verify_manifest(folder,'bad')
    p.write_text('a\n2\n')
    with pytest.raises(ValueError,match='file SHA'): A.verify_manifest(folder,digest)


@pytest.mark.parametrize('metric,base,new,delta,pct,direction',[
    ('mape',5.,4.5,-.5,10.,'improved'),('mae',100.,120.,20.,-20.,'worsened'),
    ('rmse',10.,8.,-2.,20.,'improved'),('rmae',1.,1.,0.,0.,'same')])
def test_error_changes(metric,base,new,delta,pct,direction):
    r=C.change(base,new,metric)
    assert r['absolute_difference']==delta and r['relative_improvement_pct']==pytest.approx(pct)
    assert r['direction']==direction
    assert r['unit']==('%p' if metric=='mape' else 'ratio' if metric=='rmae' else 'price')


def test_zero_na_success_pp_and_no_rounding():
    assert C.change(0.,1.,'mape')['relative_improvement_pct'] is None
    assert C.change(None,1.,'rmse')['direction']=='unavailable'
    r=C.change(80.,90.,'success_rate_pct')
    assert r['absolute_difference']==10 and r['unit']=='%p' and r['relative_change_pct']==12.5
    assert r['relative_improvement_pct'] is None
    tiny=C.change(5.000000004,5.000000003,'mape')
    assert tiny['direction']=='improved' and tiny['absolute_difference']<0


def fixture_result(error=10.):
    points=[{'series_id':s,'origin':date(2025,1,6),'horizon':1,'y':100.,'naive':120.,'pred':100.+error,'ok':True}
            for s in range(1,11)]
    conditions={k:'same' for k in C.CONDITIONS}
    conditions.update(series_ids=list(range(1,11)),v1_id='fake',v1_sha='x')
    return {'id':str(error),'name':'synthetic','conditions':conditions,
            'grid':{C.key(p) for p in points},'policy':C.statistics(points,'policy',range(1,11)),
            'naive':C.statistics(points,'naive',range(1,11)), 'points':points,'precision':'synthetic unrounded',
            'source_sha256':{},'series_labels':{}}


def test_ten_series_comparability_paired_targets_and_counts():
    b,n=fixture_result(10),fixture_result(5)
    c=C.compare(b,n)
    assert c['comparability']['label']=='direct'
    assert c['series_counts']=={'improved':10,'worsened':0,'same':0,'unavailable':0}
    assert c['series_denominator']==10
    n['points'][0]['ok']=False
    n['policy']=C.statistics(n['points'],'policy',range(1,11))
    c=C.compare(b,n)
    assert c['point_sets']['common_success']==9
    assert c['policy']['series']['1']['valid_predictions']['absolute_difference']==-1
    assert c['policy']['series']['1']['success_rate_pct']['absolute_difference']==-100
    assert c['paired_analysis']['common_success']['changes']['overall']['mape']['relative_improvement_pct']==50
    n['conditions']['v2_sha']='different'
    assert C.compare(b,n)['comparability']['label']=='reference'
    assert C.compare(b,n)['series_counts']['unavailable']==10
    n['points'].pop()
    assert 'different:actual_eligible_keys' in C.compare(b,n)['comparability']['reasons']


@pytest.mark.parametrize('field',C.CONDITIONS)
def test_any_unknown_or_changed_condition_is_reference(field):
    a={k:'x' for k in C.CONDITIONS}; b=copy.deepcopy(a)
    assert C.comparability(a,b)['label']=='direct'
    b[field]='y'
    assert C.comparability(a,b)['label']=='reference'
    del b[field]
    assert C.comparability(a,b)['label']=='reference'


def test_rmse_definition_policy_and_model_only():
    pts=fixture_result()['points'][:2]
    pts[0]['pred']=103.; pts[1]['pred']=104.; pts[1]['ok']=False
    s=C.statistics(pts,'policy',[1,2])
    assert s['series']['1']['rmse']==3 and s['series']['2']['rmse']==20
    assert s['overall']['rmse']==11.5 # macro of series RMSE, not pooled RMSE
    assert s['overall']['failed_predictions']==1
    assert C.statistics(pts,'model_only',[1,2])['series']['2']['mape'] is None


def test_main_preflight_rejects_test_bad_json_invalid_args_retry_and_records(tmp_path,monkeypatch):
    root=tmp_path/'experiments'
    monkeypatch.setattr(A.Attempt,'capture',lambda self:None)
    monkeypatch.setattr(R,'train',lambda *a,**k:pytest.fail('No training'))
    for argv in [['--origins','test'],['--unknown'],['--config',str(tmp_path/'absent')],['--retry-of','../outside']]:
        assert R.main(argv,root=root)==1
    folders=sorted(root.glob('ridge-v2-*'))
    assert len(folders)==4
    for p in folders:
        assert A.read(p/'outcome.json')['status']=='FAILED_PREFLIGHT'
        assert 'ERROR' in (p/'events.jsonl').read_text()
        A.verify_seal(p)
    parent=folders[0].name
    def stop(args): raise KeyboardInterrupt('synthetic user stop')
    monkeypatch.setattr(R,'preflight',stop)
    with pytest.raises(KeyboardInterrupt):
        R.main(['--retry-of',parent,'--changes','fix','--reason','retry'],root=root)
    interrupted=[p for p in root.glob('ridge-v2-*') if A.read(p/'outcome.json')['status']=='INTERRUPTED']
    assert len(interrupted)==1 and parent in (interrupted[0]/'events.jsonl').read_text()


def test_invalid_config_and_full_all_equivalence():
    from model_comparison.v2 import features as F
    common=A.read(A.ROOT/'model_comparison/v2/configs/all.json')
    configs=list((A.HERE/'configs').glob('*.json'))
    assert len(configs)>=22
    for p in configs: R.validate_config(A.read(p))
    allc=A.read(A.HERE/'configs/all.json')
    assert allc['bundles']==common['bundles'] and allc['blocks']==common['blocks']
    assert 'WEATHER_ANOM' not in allc['blocks']
    assert 'WEATHER_ANOM' in A.read(A.HERE/'configs/all_weather_anom.json')['blocks']
    assert len(R.validate_config(allc))==188
    for field,value in [('seed',True),('blocks',['TYPO']),('window_days',1),('strategy','pooled_horizon')]:
        bad=copy.deepcopy(allc); bad[field]=value
        with pytest.raises((ValueError,TypeError)): R.validate_config(bad)


def test_raw_legacy_metrics_adapter_does_not_recompute_or_write(tmp_path,monkeypatch):
    import csv
    from tools import evaluate, standard
    folder=tmp_path/'old'; folder.mkdir()
    conf={'data_version':standard.DATA_VERSION,'experiment_id':'old','origin_list':'validation'}
    metrics={'results':{'policy':{'macro_mape':5.000001,'macro_rmae':1.2,
                                'series':{'1':{'mape':5.000001,'mae':9.,'rmae':1.2,'naive_mape':4.,'naive_mae':7.5}}}},
             'success_rate':1.,'baselines':{'naive':{'macro_mape':4.,'macro_rmae':1.}}}
    A.exclusive_json(folder/'config.json',conf); A.exclusive_json(folder/'metrics.json',metrics)
    with (folder/'predictions.csv').open('w',newline='') as f:
        w=csv.writer(f); w.writerow(standard.PREDICTION_COLUMNS)
        w.writerow(['old','Ridge','x',standard.DATA_VERSION,1,'item','RETAIL','2025-01-06','2025-01-07',1,'100','100','OK',''])
    before={p.name:p.read_bytes() for p in folder.iterdir()}
    monkeypatch.setattr(evaluate,'evaluate',lambda *a:pytest.fail('Never recalculate historical metrics'))
    r=C.load_result(folder)
    assert r['policy']['overall']['mape']==5.000001 and r['policy']['overall']['rmse'] is None
    assert r['naive']['overall']['mape']==4.
    assert {p.name:p.read_bytes() for p in folder.iterdir()}==before
    A.exclusive_json(tmp_path/'historical_baselines.json',{'records':[
        {'path':'old','sha256':{p.name:A.sha(p) for p in folder.iterdir()}}]})
    monkeypatch.setattr(C,'HERE',tmp_path)
    monkeypatch.setattr(C,'ROOT',tmp_path)
    assert C.load_result(folder)['policy']['overall']['mape']==5.000001
    (folder/'metrics.json').write_text('{}')
    with pytest.raises(ValueError,match='Pinned historical'): C.load_result(folder)


def test_p1_p2_source_and_artifact_readonly_inventory():
    # Compare protected tracked files to Git. Untracked historical audits are never written by v2.
    import subprocess
    paths=['model_comparison/ridge/model.py','model_comparison/ridge/model_p2.py',
           'model_comparison/ridge/p2.py','model_comparison/v2','tools',
           'experiments/ridge-p1-20261111-07',*[f'experiments/ridge-p2-20261112-0{i}' for i in range(1,8)]]
    diff=subprocess.check_output(['git','diff','HEAD','--',*paths],cwd=A.ROOT)
    assert diff==b''


def test_historical_catalog_matches_actual_originals():
    catalog=A.read(A.HERE/'historical_baselines.json')
    for r in catalog['records']:
        folder=A.ROOT/r['path']
        for name,digest in r['sha256'].items(): assert A.sha(folder/name)==digest
        metrics=A.read(folder/'metrics.json')
        assert r['original_policy_macro_mape']==metrics['results']['policy']['macro_mape']
        assert r['original_naive_macro_mape']==metrics['baselines']['naive']['macro_mape']


def test_memory_resource_is_measured_or_unknown():
    memory=A.peak_memory_mb()
    assert memory is None or memory>0
