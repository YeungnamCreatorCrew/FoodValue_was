"""Batch orchestration only. Uses the existing runner without changing model/evaluation code."""
import csv
import json
import os
from pathlib import Path
import subprocess
import sys
import time
import traceback
from collections import Counter

ROOT = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT))
from model_comparison.ridge.v2 import audit as A, comparison as C, run as R
from tools import loader, standard

BATCH = A.EXPERIMENTS/'tune-features-20261117-batch01'
RUNS = BATCH/'runs'
CONTROL = A.EXPERIMENTS/'ridge-v2-20261117T060931078600Z-5aedd5a6c62a4e6cb409758eb5c3d60d'
REPORT = A.HERE/'verification/TUNE_FEATURE_COMPARISON_20261117.md'
FIXED = ('model','class','params','window_days','seed','refit','strategy','target_transform')
ORDER = ['market','national_weather','event','macro','production','garak','origin_weather',
         'weather_anom','cross_item','no_series_id','all','all_weather_anom','all_no_series_id',
         'no_market','no_national_weather','no_event','no_macro','no_production','no_garak',
         'no_origin_weather','no_cross_item']


def inventory():
    names = set(subprocess.check_output(['git','ls-files','-z'],cwd=ROOT).decode('utf-8').rstrip('\0').split('\0'))
    for dirname in ('model_comparison','experiments','data/snapshots','tools','tests','runs'):
        names.update(p.relative_to(ROOT).as_posix() for p in (ROOT/dirname).rglob('*')
                     if p.is_file() and '__pycache__' not in p.parts and BATCH not in p.parents)
    return {n:A.sha(ROOT/n) for n in sorted(names) if (ROOT/n).is_file() and BATCH not in (ROOT/n).parents}


def fingerprint(c):
    return A.object_sha({**{k:c[k] for k in FIXED},'bundles':sorted(c['bundles']),'blocks':sorted(c['blocks'])})


def prepare():
    assert A.git('branch','--show-current')=='feat/ridge-v2'
    assert not REPORT.exists(), 'Report exists: refusing overwrite'
    assert not BATCH.exists(), 'Batch exists: refusing overwrite'
    original=inventory()
    BATCH.mkdir(exist_ok=False)
    A.exclusive_json(BATCH/'preservation_before.json',original)
    snapshots=A.verify_data(ROOT/'data/snapshots'/standard.DATA_VERSION,ROOT/'data/snapshots'/A.EXTRA_ID)
    snap=loader.Snapshot(ROOT/'data/snapshots'/standard.DATA_VERSION)
    assert len(snap.origins['tune'])==53 and len(snap.series_ids)==10
    assert list(standard.HORIZONS)==list(range(1,8))
    result=C.load_result(CONTROL,snap)
    assert A.effective_outcome(CONTROL)['status']=='COMPLETED_WITH_MISSING'
    assert result['policy']['overall']['evaluated_points']==2498
    control=A.read(A.HERE/'configs/control.json')
    assert control['params']=={'alpha':10,'solver':'lsqr'} and control['window_days']==1825 and control['seed']==42
    configs=[]; skipped=[]; seen={fingerprint(control):'CONTROL reused'}
    for path in sorted((A.HERE/'configs').glob('*.json')):
        c=A.read(path); names=R.validate_config(c)
        assert all(c[k]==control[k] for k in FIXED),(path,'Fixed parameters differ')
        ident=fingerprint(c)
        entry={'name':c['name'],'config_path':str(path),'config_sha256':A.sha(path),
               'config_object_sha256':A.object_sha(c),'fingerprint':ident,'bundles':c['bundles'],
               'blocks':c['blocks'],'comparison':c.get('comparison'),'input_features':len(names)}
        if ident in seen:
            skipped.append({**entry,'reason':'duplicate','same_as':seen[ident]})
        else:
            seen[ident]=c['name']; configs.append(entry)
    assert len({e['name'] for e in configs})==len(configs)
    # Ordering does not create any experiments: unlisted existing configs still run.
    configs.sort(key=lambda e:(ORDER.index(e['name']) if e['name'] in ORDER else len(ORDER),e['name']))
    files={}
    for kind,folder in [('v1',snap.folder),('v2',ROOT/'data/snapshots'/A.EXTRA_ID)]:
        files[kind]={}
        for name,info in snapshots[kind]['manifest']['files'].items():
            with (folder/name).open(encoding='utf-8',newline='') as f:
                reader=csv.DictReader(f); first=next(reader,None)
            files[kind][name]={'rows':info['rows'],'columns':list(reader.fieldnames),'has_data':first is not None}
    assert all(v['has_data'] for fileset in files.values() for v in fileset.values())
    plan={'at':A.now(),'branch':A.git('branch','--show-current'),'git_sha':A.git('rev-parse','HEAD'),
          'control_id':CONTROL.name,'control_folder':str(CONTROL),'target_count':len(configs),
          'configs':configs,'skipped':skipped,'fixed':{k:control[k] for k in FIXED},
          'origins':[str(d) for d in snap.origins['tune']],'series_ids':snap.series_ids,
          'horizons':list(standard.HORIZONS),'expected_prediction_rows':3710,
          'comparison_conditions':result['conditions'],'snapshot_files':files,
          'snapshot_manifests':{k:v['manifest_sha256'] for k,v in snapshots.items()},
          'registry':str(RUNS),'report':str(REPORT),'orchestrator_sha256':A.sha(Path(__file__)),
          'policy':'Sequential existing configs only; no CONTROL refit; no Validation/Test; no retries; failures preserved',
          'aggregate_documents':'Dedicated new batch registry prevents modification of pre-existing aggregate logs/results'}
    A.exclusive_json(BATCH/'plan.json',plan)
    print(json.dumps({'batch':str(BATCH),'targets':len(configs),'names':[e['name'] for e in configs],
                      'skipped':[(e['name'],e['same_as']) for e in skipped],'protected_files':len(original)},ensure_ascii=False),flush=True)


def worker(name):
    plan=A.read(BATCH/'plan.json'); entry=next(e for e in plan['configs'] if e['name']==name)
    assert A.sha(entry['config_path'])==entry['config_sha256']
    assert name!='control'
    argv=['--execute','--config',entry['config_path'],'--origins','tune',
          '--snapshot',str(ROOT/'data/snapshots'/standard.DATA_VERSION),
          '--extra',str(ROOT/'data/snapshots'/A.EXTRA_ID),
          '--purpose','Existing-config full Tune feature batch; no Validation/Test',
          '--changes',json.dumps({'config':entry['comparison'],'fixed':plan['fixed']},ensure_ascii=False),
          '--reason','Run every existing unique configuration once; isolate feature changes against sealed CONTROL',
          '--next-decision','Tune provisional candidate only; no retries; Validation/Test not authorized',
          '--baseline','CONTROL='+str(CONTROL)]
    if entry['comparison'].get('reference')=='all' and (BATCH/'completed_all.json').exists():
        all_run=A.read(BATCH/'completed_all.json')['folder']
        argv+=['--baseline','ALL='+all_run]
    return R.main(argv,root=RUNS)


def run_batch():
    plan=A.read(BATCH/'plan.json')
    RUNS.mkdir(exist_ok=False)
    (BATCH/'console').mkdir(exist_ok=False)
    (BATCH/'records').mkdir(exist_ok=False)
    env={**os.environ,**standard.THREAD_ENV,'PYTHONUTF8':'1','PYTHONDONTWRITEBYTECODE':'1','GIT_OPTIONAL_LOCKS':'0'}
    with A.lock(BATCH/'orchestration'):
        for index,entry in enumerate(plan['configs'],1):
            name=entry['name']; start=A.now(); before=set(RUNS.glob('ridge-v2-*'))
            cmd=[sys.executable,'-X','utf8','-B',str(Path(__file__).resolve()),'worker',name]
            A.exclusive_json(BATCH/'records'/f'{index:02d}-{name}-request.json',
                             {'at':start,'name':name,'command':cmd,'cwd':str(ROOT),'registry':str(RUNS),'config':entry})
            print(f'START {index}/{len(plan["configs"])} {name} {start}',flush=True)
            with (BATCH/'console'/f'{index:02d}-{name}.log').open('xb') as log:
                proc=subprocess.run(cmd,cwd=ROOT,env=env,stdout=log,stderr=subprocess.STDOUT)
            allocated=sorted(set(RUNS.glob('ridge-v2-*'))-before)
            record={'name':name,'started_at':start,'finished_at':A.now(),'returncode':proc.returncode,
                    'folders':[str(p) for p in allocated],'retry':False}
            try:
                assert len(allocated)==1, 'Expected exactly one audit folder'
                folder=allocated[0]; record['run_id']=folder.name; record['folder']=str(folder)
                outcome=A.effective_outcome(folder); record['status']=outcome['status']
                record['sealed']=outcome['status']!='INCOMPLETE'
                A.verify_seal(folder)
                if (folder/'metrics_full_precision.json').exists():
                    snap=loader.Snapshot(ROOT/'data/snapshots'/standard.DATA_VERSION)
                    r=C.load_result(folder,snap); comp=C.compare(C.load_result(CONTROL,snap),r)
                    record['comparability']=comp['comparability']
                    record['policy']=r['policy']['overall']; record['health']=A.read(folder/'prediction_health.json')
                    if name=='all' and record['status'] in ('COMPLETED','COMPLETED_WITH_MISSING'):
                        A.exclusive_json(BATCH/'completed_all.json',{'folder':str(folder),'run_id':folder.name})
            except Exception as error:
                record['verification_error']=repr(error); record['traceback']=traceback.format_exc()
                record.setdefault('status','UNVERIFIED')
            A.exclusive_json(BATCH/'records'/f'{index:02d}-{name}-result.json',record)
            A.append(BATCH/'progress.jsonl',json.dumps(record,ensure_ascii=False,allow_nan=False)+'\n')
            print('END '+json.dumps({k:record.get(k) for k in ('name','run_id','status','returncode','verification_error','policy')},ensure_ascii=False),flush=True)
    A.exclusive_json(BATCH/'execution_finished.json',{'at':A.now(),'count':len(plan['configs']),'retries':0})


if __name__=='__main__':
    if sys.argv[1]=='prepare': prepare()
    elif sys.argv[1]=='worker': sys.exit(worker(sys.argv[2]))
    elif sys.argv[1]=='run': run_batch()
    else: raise ValueError('Use prepare, worker NAME, or run')
