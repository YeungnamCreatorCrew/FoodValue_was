"""Read sealed outputs and create a separate, exhaustive batch report. Never fit models."""
import json
import math
import os
from pathlib import Path
import sys
from collections import Counter

ROOT=Path(__file__).resolve().parents[4]
sys.path.insert(0,str(ROOT))
from model_comparison.ridge.v2 import audit as A, comparison as C
from tools import loader,evaluate,standard

BATCH=A.EXPERIMENTS/'tune-features-20261117-batch01'
REPORT=A.HERE/'verification/TUNE_FEATURE_COMPARISON_20261117.md'
CONTROL=A.EXPERIMENTS/'ridge-v2-20261117T060931078600Z-5aedd5a6c62a4e6cb409758eb5c3d60d'
METRICS=C.ERRORS
GOOD={'COMPLETED','COMPLETED_WITH_MISSING'}


def fmt(value,digits=10):
    if value is None: return 'N/A'
    if isinstance(value,bool): return str(value)
    if isinstance(value,int): return str(value)
    if isinstance(value,float): return f'{value:.{digits}g}'
    return str(value).replace('|','\\|').replace('\n',' ')


def table(lines,headers,rows):
    lines.extend(['','| '+' | '.join(headers)+' |','| '+' | '.join('---' for _ in headers)+' |'])
    lines.extend('| '+' | '.join(fmt(v) for v in row)+' |' for row in rows)
    lines.append('')


def link(path):
    return os.path.relpath(path,REPORT.parent).replace('\\','/')


def changes(base,new):
    return {m:C.change(base.get(m),new.get(m),m) for m in METRICS}


def signed_pair(change):
    d,p=change['absolute_difference'],change['relative_improvement_pct']
    return f'{d:+.10g} / {p:+.10g}%' if d is not None and p is not None else f'{fmt(d)} / N/A'


def read_run(folder,name,snap):
    outcome=A.effective_outcome(folder)
    r={'name':name,'folder':str(folder),'run_id':folder.name,'outcome':outcome,'status':outcome['status'],
       'sealed':False,'validated':False,'issues':[]}
    r['sealed']=bool(A.verify_seal(folder))
    for key,filename in [('config','config.json'),('health','prediction_health.json'),('provenance','provenance.json')]:
        if (folder/filename).exists(): r[key]=A.read(folder/filename)
    events=[json.loads(line) for line in (folder/'events.jsonl').read_text(encoding='utf-8').splitlines()]
    r['event_counts']=dict(Counter(e['event'] for e in events))
    r['errors']=[e for e in events if e['event']=='ERROR']
    r['fit_count']=sum(e['event']=='FIT' for e in events)
    r['fit_usable_count']=sum(e['event']=='REFIT_FINISHED' and e['usable'] for e in events)
    r['logs_equal']=(folder/'events.jsonl').read_bytes()==(folder/'run.log').read_bytes()
    if not (folder/'metrics_full_precision.json').exists():
        r['issues'].append('No full precision metrics; no performance claim')
        return r,None
    result=C.load_result(folder,snap)
    r['metrics']=A.read(folder/'metrics_full_precision.json')
    rows=evaluate.read_predictions(folder); points=result['points']
    r['row_count']=len(rows); r['status_counts']=dict(Counter(row['status'] for row in rows))
    r['origins']=sorted({row['origin_date'] for row in rows})
    r['series_ids']=sorted({int(row['series_id']) for row in rows})
    r['horizons']=sorted({int(row['horizon']) for row in rows})
    r['excluded_points']=len(rows)-len(points)
    r['expected_grid']=len(rows)==3710 and len(result['grid'])==3710 and r['origins']==[str(d) for d in snap.origins['tune']] and r['series_ids']==snap.series_ids and r['horizons']==list(standard.HORIZONS)
    r['full_precision_matches']=r['metrics']==C.extended(points,snap.series_ids)
    r['official_metrics_matches']=A.read(folder/'metrics.json')==evaluate.evaluate(folder,snap)
    r['adoption']=A.read(folder/'metrics.json').get('adoption')
    sources=A.read(folder/'sources_sha256.json')
    r['source_hashes']=sources
    r['archived_sources_match']=all(A.sha(folder/'sources'/n)==h for n,h in sources.items())
    r['current_sources_match']=all(A.sha(ROOT/n)==h for n,h in sources.items())
    r['config_hash_matches']=r['config']['config_sha256']==A.object_sha(A.read(folder/'requested_config.json'))
    r['eligible_keys_sha']=A.object_sha(sorted(C.key(p) for p in points))
    r['eligible_sha_matches']=r['eligible_keys_sha']==result['conditions']['eligible_keys_sha']
    r['series_health']={str(s):Counter() for s in snap.series_ids}
    category_map={}
    for e in events:
        if e['event']=='PREDICTION_BATCH':
            for h,category in zip(standard.HORIZONS,e['categories']):
                category_map[(str(e['series_id']),e['origin'],str(h))]=category
    missing=[]
    for row in rows:
        category=category_map[(row['series_id'],row['origin_date'],row['horizon'])]
        r['series_health'][row['series_id']][category]+=1
        if category=='expected_missing': missing.append(f'{row["series_id"]}|{row["origin_date"]}|{row["horizon"]}')
    r['series_health']={s:dict(c) for s,c in r['series_health'].items()}
    actual=Counter(category_map.values())
    r['health_matches']=len(category_map)==len(rows) and all(actual[k]==n for k,n in r['health']['categories'].items())
    r['missing_keys']=sorted(missing)
    for field in ('logs_equal','expected_grid','full_precision_matches','official_metrics_matches',
                  'archived_sources_match','current_sources_match','config_hash_matches','eligible_sha_matches','health_matches'):
        if not r[field]: r['issues'].append('Verification failed: '+field)
    r['validated']=not r['issues']
    return r,result


def scopes(result,control,snap):
    """Explicitly distinguish policy, each-run success sets, and the common success set."""
    new=result['points']; base=control['points']
    nk={C.key(p) for p in new}; bk={C.key(p) for p in base}
    ns={C.key(p) for p in new if p['ok']}; bs={C.key(p) for p in base if p['ok']}
    shared=ns&bs
    comp=C.compare(control,result)
    direct=comp['comparability']['label']=='direct'
    subsets={'policy':(base,new,'policy'),
             'model_only':(base,new,'model_only'),
             'common_success':([p for p in base if C.key(p) in shared],[p for p in new if C.key(p) in shared],'model_only')}
    modes={}
    for mode,(bp,np,pred) in subsets.items():
        used_new=np if mode!='model_only' else [p for p in np if p['ok']]
        n=C.statistics(np,pred,snap.series_ids); b=C.statistics(bp,pred,snap.series_ids)
        naive=C.statistics(used_new,'naive',snap.series_ids)
        label='direct' if direct and (mode!='model_only' or ns==bs) else 'reference'
        modes[mode]={'new':n,'control':b,'naive':naive,'control_label':label,
                     'naive_label':'direct','new_error_keys_sha':A.object_sha(sorted(C.key(p) for p in used_new)),
                     'overall_control_changes':changes(b['overall'],n['overall']),
                     'overall_naive_changes':changes(naive['overall'],n['overall'])}
    return modes,comp


def load_all():
    assert (BATCH/'execution_finished.json').exists(),'Batch still running'
    plan=A.read(BATCH/'plan.json')
    snap=loader.Snapshot(ROOT/'data/snapshots'/standard.DATA_VERSION)
    snapshots=A.verify_data(snap.folder,ROOT/'data/snapshots'/A.EXTRA_ID)
    control,control_result=read_run(CONTROL,'CONTROL',snap)
    control['modes'],control['control_comparison']=scopes(control_result,control_result,snap)
    records=[control]; raw={'CONTROL':control_result}
    journal=[json.loads(line) for line in (BATCH/'progress.jsonl').read_text(encoding='utf-8').splitlines()]
    byname={r['name']:r for r in journal}
    for entry in plan['configs']:
        execution=byname.get(entry['name'])
        if not execution or not execution.get('folder'):
            records.append({'name':entry['name'],'status':'NOT_RUN','issues':['No allocated run'],'entry':entry})
            continue
        folder=Path(execution['folder'])
        try:
            r,result=read_run(folder,entry['name'],snap)
            r['entry']=entry; r['execution']=execution
            r['requested_config_file_matches']=A.sha(entry['config_path'])==entry['config_sha256']
            if not r['requested_config_file_matches']: r['issues'].append('Original config changed')
            r['fixed_fields_match']=all(r.get('config',{}).get(k)==v for k,v in plan['fixed'].items())
            r['feature_groups_match']=all(r.get('config',{}).get(k)==entry[k] for k in ('bundles','blocks'))
            if not r['fixed_fields_match']:r['issues'].append('Fixed training parameters differ')
            if not r['feature_groups_match']:r['issues'].append('Feature groups differ from original config')
            if r['status'] in GOOD and (r['fit_count']!=53 or r['fit_usable_count']!=53):
                r['issues'].append('Completed run did not retain 53 usable weekly fits')
            if result is not None:
                r['modes'],r['control_comparison']=scopes(result,control_result,snap)
                saved=A.read(folder/'comparison.json')
                r['saved_control_matches']=saved['CONTROL']==r['control_comparison']
                r['saved_naive_matches']=saved['Naive']==C.naive_comparison(result)
                r['sources_match_control']=r['source_hashes']==control['source_hashes']
                for field in ('saved_control_matches','saved_naive_matches','sources_match_control'):
                    if not r[field]:r['issues'].append('Verification failed: '+field)
                r['missing_keys_same_as_control']=r['missing_keys']==control['missing_keys']
                raw[entry['name']]=result
            r['validated']=not r['issues']
            records.append(r)
        except Exception as e:
            records.append({'name':entry['name'],'run_id':folder.name,'folder':str(folder),
                            'status':execution.get('status','UNVERIFIED'),'validated':False,
                            'issues':[repr(e)],'entry':entry,'execution':execution})
    ablations=[]
    for r in records[1:]:
        reference=r.get('entry',{}).get('comparison',{}).get('reference')
        if reference=='all' and r['name'] in raw and 'all' in raw:
            comparison=C.compare(raw['all'],raw[r['name']])
            saved=A.read(Path(r['folder'])/'comparison.json')
            matched=saved.get('ALL')==comparison
            if not matched:
                r['issues'].append('Saved ALL comparison mismatch');r['validated']=False
            ablations.append({'name':r['name'],'reference':'all','comparison':comparison,'saved_all_matches':matched})
    old=A.read(BATCH/'preservation_before.json')
    changed=[n for n,h in old.items() if not (ROOT/n).is_file() or A.sha(ROOT/n)!=h]
    previous=[{'id':p.name,'status':A.effective_outcome(p)['status'],'seal_count':len(A.verify_seal(p))}
              for p in sorted(A.EXPERIMENTS.glob('ridge-v2-*')) if p.is_dir()]
    preservation={'existing_file_count':len(old),'changed_or_missing':changed,
                  'branch':A.git('branch','--show-current'),'tracked_diff':A.git('diff','HEAD','--'),
                  'initial_git_sha':plan['git_sha'],'final_git_sha':A.git('rev-parse','HEAD'),
                  'git_head_unchanged':plan['git_sha']==A.git('rev-parse','HEAD'),
                  'previous_runs':previous,'snapshot_manifests':{k:v['manifest_sha256'] for k,v in snapshots.items()},
                  'orchestrator_unchanged':A.sha(A.HERE/'verification/run_tune_feature_batch_20261117.py')==plan['orchestrator_sha256']}
    return plan,snap,records,ablations,preservation


def make_report(plan,snap,records,ablations,preservation):
    lines=['# Ridge v2 전체 외부변수 Tune 실험 종합 분석 — 2026-11-17','',
           f'작성 시각(UTC): {A.now()}  ',f'배치 경로: `{BATCH.relative_to(ROOT).as_posix()}`  ',
           f'기존 CONTROL: `{CONTROL.name}` (재학습하지 않음)','',
           '기존 모델·공통 평가·설정·스냅샷 코드를 변경하지 않고 기존 실행기를 사용했다. '
           '새 배치 전용 registry를 사용해 기존 누적 EXPERIMENT_LOG.md와 RESULTS.md도 보존했다. '
           'Validation/Test는 실행하지 않았고 실패한 설정의 변경·재시도도 하지 않았다.','',
           '오차 절대 차이 Δ = 신규 − 기준. 상대 개선률 = (기준 − 신규)/기준 × 100. '
           'Δ는 음수, 상대 개선률은 양수일 때 오차 개선이다. MAPE 차이는 %p, 상대 개선률은 %. '
           'MAE/RMSE 차이는 각 계열 가격 단위, rMAE 차이는 비율 단위다. '
           '기준 0 또는 결측이면 상대 개선률은 N/A다. 모든 계산은 원본 정밀도로 수행하고 표시만 반올림했다.','',
           '전체 MAPE·MAE·RMSE·rMAE는 계열별 값의 단순평균(macro)이다. '
           '서로 다른 가격 규격의 MAE/RMSE 전체값은 기술적인 평균이므로 계열별 결과를 함께 확인해야 한다.','',
           'policy는 평가 가능한 모든 관측치에서 비성공 예측을 Naive로 대체한다. '
           'model_only는 각 모델의 성공 관측치만 사용하며, 이 모드의 Naive도 신규 모델과 동일 성공 관측치에서 계산한다. '
           'CONTROL model_only의 성공 집합이 신규 모델과 다르면 해당 비교는 reference다. '
           'common_success는 신규 모델과 CONTROL 양쪽이 모두 성공한 동일 관측치를 사용하며 Naive도 그 집합에 맞춘다. '
           'reference의 수치 변화는 기술적 차이이며 직접적인 개선 효과가 입증된 것으로 해석하지 않는다.','',
           '성공률은 별도 명시하지 않으면 평가 가능 관측치 기준이다. 예상 결측·오류 행 수는 전체 출력 행 기준이다. '
           '평가상의 failed_predictions에는 예상 결측이 포함되므로 실제 모델 오류 건수와 다르다.','',
           '## A. 실험 전체 현황','']
    active=records[1:]
    counts=Counter('완료' if r['status'] in GOOD and r.get('validated') else '부분 완료' if r['status']=='PARTIAL' else
                   '미실행' if r['status']=='NOT_RUN' else '실패/검증 미통과' for r in active)
    lines += [f'기존 설정 {len(plan["configs"])+len(plan["skipped"])}개를 조사했다. '
              f'기존 CONTROL 중복 {len(plan["skipped"])}개를 제외한 대상은 {plan["target_count"]}개다. '
              '정의되지 않은 설정은 만들지 않았다. 기존 no_series_id 및 all_no_series_id는 명시된 ablation으로만 실행했다.',
              f'집계: 완료 {counts["완료"]}, 부분 완료 {counts["부분 완료"]}, 실패/검증 미통과 {counts["실패/검증 미통과"]}, 미실행 {counts["미실행"]}. '
              'COMPLETED_WITH_MISSING은 정상 완료 집계에 포함하되 예상 결측을 별도 표시한다.']
    table(lines,['실험','활성 특징 그룹','입력 특징 수','실행 ID','시작 UTC / 종료 UTC','종료 상태','CONTROL 조건','검증'],
          [[r['name'],', '.join(r.get('config',r.get('entry',{})).get('bundles',[])+r.get('config',r.get('entry',{})).get('blocks',[])) or '기본 특징만',
            r.get('provenance',{}).get('input_feature_count',r.get('entry',{}).get('input_features')),
            r.get('run_id','N/A'),r.get('execution',{}).get('started_at','기존 실행')+' / '+r.get('outcome',{}).get('at','N/A'),
            r['status'],r.get('control_comparison',{}).get('comparability',{}).get('label','N/A'),r.get('validated',False)] for r in records])
    lines += ['고정 조건: Tune 전체 53개 기준일(2024-11-01~2025-10-27), 10개 계열, Horizon 1~7, '
              '학습 창 1,825일, weekly_first_origin, Ridge alpha=10/solver=lsqr/seed=42, '
              'direct_per_horizon/change_ratio. CONTROL의 SERIES_ID는 그대로 유지했다.',
              'Manifest SHA-256:']
    table(lines,['스냅샷','SHA-256'],[[k,h] for k,h in preservation['snapshot_manifests'].items()])
    lines += ['모든 실행은 시작 전 고정 manifest, 파일 해시·행 수와 공통 스냅샷 검사를 수행한다. '
              '외부 입력 파일의 열·행 존재 확인은 배치 plan.json에 기록했다. '
              '모델 내부 학습 결측 처리와 train-only 감사 정보는 각 원본 FIT 이벤트에 보존돼 있다.',
              f'[실행 계획]({link(BATCH/"plan.json")}), [원본 실행 목록]({link(BATCH/"progress.jsonl")}).','',
              '## B. 전체 모델 성능 비교','',
              '다음 주 표는 policy 지표다. CONTROL은 기존 결과를 재사용했고 Naive는 CONTROL의 동일 평가 집합을 기준으로 표시한다. '
              '각 실험의 Naive 대비 변화는 해당 실험의 실제 관측치 집합에서 별도로 계산했다.']
    b_rows=[]
    for r in records:
        o=r.get('metrics',{}).get('policy',{}).get('overall',{})
        mode=r.get('modes',{}).get('policy',{})
        cc=mode.get('overall_control_changes',{}).get('mape',{})
        nc=mode.get('overall_naive_changes',{}).get('mape',{})
        b_rows.append([r['name'],*[o.get(m) for m in METRICS],o.get('success_rate_pct'),cc.get('relative_improvement_pct'),
                       nc.get('relative_improvement_pct'),r.get('control_comparison',{}).get('series_counts',{}).get('improved'),r['status']])
    naive=records[0]['metrics']['naive']['overall']
    b_rows.append(['Naive',*[naive[m] for m in METRICS],100,None,0,None,'기준선'])
    table(lines,['실험','MAPE (%)','MAE','RMSE','rMAE','성공률 (%)','CONTROL MAPE 개선률 (%)','Naive MAPE 개선률 (%)','CONTROL 대비 개선 계열 수','종료 상태'],b_rows)
    lines += ['### 전체 지표의 모드별 절대 차이와 상대 개선률','',
              '각 행에서 신규 값과 두 기준의 원본 값을 제공한다. model_only의 CONTROL 비교가 reference이면 성공 관측치 집합 차이를 포함한다.']
    comp_rows=[]
    for r in records:
        for mode,data in r.get('modes',{}).items():
            for m in METRICS:
                cc=data['overall_control_changes'][m]; nc=data['overall_naive_changes'][m]
                comp_rows.append([r['name'],mode,m,data['new']['overall'][m],cc['baseline'],cc['absolute_difference'],
                                  cc['relative_improvement_pct'],data['control_label'],nc['baseline'],
                                  nc['absolute_difference'],nc['relative_improvement_pct'],cc['unit'],data['new']['overall']['error_points']])
    table(lines,['실험','모드','지표','신규','CONTROL','Δ CONTROL','CONTROL 개선률 (%)','CONTROL 판정','Naive','Δ Naive','Naive 개선률 (%)','Δ 단위','오차 계산 관측치'],comp_rows)
    lines += ['## C. 외부변수별 개선·악화 분석','']
    for r in active:
        entry=r.get('entry',{}); description=entry.get('comparison',{})
        lines += [f'### {r["name"]}', '',
                  f'기존 설정 `{entry.get("config_path","N/A")}`. 설정상 비교 기준 `{description.get("reference","N/A")}`; '
                  f'추가 `{", ".join(description.get("added",[])) or "없음"}`, 제거 `{", ".join(description.get("removed",[])) or "없음"}`.']
        if 'modes' not in r:
            lines += [f'종료 상태 {r["status"]}; 성능 판정 불가. 원인: {r.get("issues")}', '']; continue
        mode=r['modes']['policy']; delta=mode['overall_control_changes']
        improved=[m for m in METRICS if delta[m]['direction']=='improved']
        worsened=[m for m in METRICS if delta[m]['direction']=='worsened']
        series=r['control_comparison']['policy']['series']
        available=[(s,v['mape']['relative_improvement_pct']) for s,v in series.items() if v['mape']['relative_improvement_pct'] is not None]
        best=max(available,key=lambda kv:kv[1]); worst=min(available,key=lambda kv:kv[1])
        label=lambda sid:f'{snap.series[int(sid)].item}/{snap.series[int(sid)].market}({sid})'
        lines += [f'CONTROL 대비 policy ΔMAPE {fmt(delta["mape"]["absolute_difference"])} %p, '
                  f'상대 개선률 {fmt(delta["mape"]["relative_improvement_pct"])}%. '
                  f'개선 지표: {", ".join(improved) or "없음"}; 악화 지표: {", ".join(worsened) or "없음"}. '
                  f'네 지표 동시 개선: {all(delta[m]["direction"]=="improved" for m in METRICS)}.',
                  f'MAPE 변화가 가장 유리한 계열: {label(best[0])}, {fmt(best[1])}%; '
                  f'가장 불리한 계열: {label(worst[0])}, {fmt(worst[1])}%. '
                  '모두 양수이면 가장 불리한 계열도 개선이며, 모두 음수이면 가장 유리한 계열도 악화다.',
                  f'비교 지위: {mode["control_label"]}; 개선/악화/동일/불가 계열 수: {r["control_comparison"]["series_counts"]}. '
                  f'CONTROL과 예상 결측 키 동일: {r.get("missing_keys_same_as_control")}; '
                  f'전체 오류 행 {r["health"]["error_row_count"]}, 오류 이벤트 {r["health"]["error_event_count"]}.',
                  f'[원본 산출물]({link(Path(r["folder"])/"outcome.json")}), '
                  f'[CONTROL/Naive 비교]({link(Path(r["folder"])/"comparison.json")}).','']
    lines += ['## D. 10개 계열별 상세 비교','',
              '어떤 실험·계열·주요 오차 지표도 생략하지 않았다. 각 모드의 오차 계산 관측치 수는 표의 n으로 표시한다. '
              '평가 성공률·유효 예측·예상 결측·실제 오류는 원래 실행의 범위에 대한 별도 열이다. '
              'common_success에서 100%가 되는 부분집합 성공률을 원래 실행 성공률로 표시하지 않는다.']
    for sid in snap.series_ids:
        key=str(sid); s=snap.series[sid]
        lines += [f'### {sid}: {s.item} / {s.market}','']
        for mode in ('policy','model_only','common_success'):
            lines += [f'#### {mode}','']
            values=[]; deltas=[]
            for r in records:
                data=r.get('modes',{}).get(mode)
                if not data:
                    values.append([r['name'],None,*([None]*10),r['status']]); continue
                v=data['new']['series'][key]; c=data['control']['series'][key]; n=data['naive']['series'][key]
                health=r['series_health'][key]; error=sum(health.get(k,0) for k in ('fit_failure','predict_failure','timeout','abnormal_prediction'))
                original=r['metrics']['policy']['series'][key]
                values.append([r['name'],v['error_points'],*[v[m] for m in METRICS],original['success_rate_pct'],
                               original['valid_predictions'],original['failed_predictions'],health.get('success',0),
                               health.get('expected_missing',0),error,r['status']])
                for m in METRICS:
                    cc=C.change(c[m],v[m],m); nc=C.change(n[m],v[m],m)
                    deltas.append([r['name'],m,v[m],c[m],cc['absolute_difference'],cc['relative_improvement_pct'],
                                   data['control_label'],n[m],nc['absolute_difference'],nc['relative_improvement_pct'],cc['unit']])
            table(lines,['실험','n','MAPE (%)','MAE','RMSE','rMAE','원래 평가 성공률 (%)','평가 유효 예측','평가 비성공','전체 OK','전체 예상 결측','전체 실제 오류 행','상태'],values)
            table(lines,['실험','지표','신규','CONTROL','Δ CONTROL','CONTROL 개선률 (%)','CONTROL 판정','Naive','Δ Naive','Naive 개선률 (%)','Δ 단위'],deltas)
    lines += ['## E. ALL 및 Ablation 분석','',
              'ALL은 기존 all.json의 8개 외부 그룹 조합이다. WEATHER_ANOM은 기본 ALL에 없으며 '
              'all_weather_anom.json이 기존 ALL에 WEATHER_ANOM을 추가한 별도 설정이다. '
              '아래 차이는 각 ablation/조합 모델에서 ALL을 뺀 값이다. '
              '동시 특징 제거/추가에 따른 조건부 결과이며 단독 변수의 인과 효과로 일반화하지 않는다.']
    lookup={r['name']:r for r in records}
    all_valid='all' in lookup and lookup['all']['status'] in GOOD and lookup['all'].get('validated')
    ar=[]
    for a in ablations:
        r=lookup[a['name']]; ok=all_valid and r['status'] in GOOD and r.get('validated')
        comp=a['comparison']; ar.append([a['name'],ok,comp['comparability']['label'],
            *[signed_pair(comp['policy']['overall'][m]) for m in METRICS],comp['series_counts']])
    table(lines,['기존 설정','양쪽 정상 완료·검증','비교 지위','MAPE Δ %p / 개선률','MAE Δ / 개선률','RMSE Δ / 개선률','rMAE Δ / 개선률','계열 MAPE 변화'],ar)
    if all_valid:
        allo=lookup['all']['metrics']['policy']['overall']
        singles=[r for r in active if r.get('entry',{}).get('comparison',{}).get('reference')=='control'
                 and len(r['entry']['comparison'].get('added',[]))==1 and r['status'] in GOOD and r.get('validated')]
        for m in METRICS:
            better=[r['name'] for r in singles if r['metrics']['policy']['overall'][m]<allo[m]]
            lines.append(f'- {m}: ALL {fmt(allo[m])}; ALL보다 낮은 개별 변수 모델: {", ".join(better) or "없음"}.')
        rows=[]
        for a in ablations:
            r=lookup[a['name']]
            if not (r['status'] in GOOD and r.get('validated')): continue
            desc=r['entry']['comparison']; removed=desc.get('removed',[])
            single_name=removed[0].lower() if len(removed)==1 else None
            single=lookup.get(single_name)
            single_gain=single['modes']['policy']['overall_control_changes']['mape']['relative_improvement_pct'] if single and 'modes' in single else None
            rows.append([a['name'],', '.join(removed) or '+WEATHER_ANOM',single_gain,
                         a['comparison']['policy']['overall']['mape']['relative_improvement_pct'],
                         '양의 ablation 개선률은 제거 모델이 ALL보다 낮은 오차'])
        table(lines,['설정','제거/추가','단독 추가 대 CONTROL MAPE 개선률 (%)','ablation/추가 대 ALL 개선률 (%)','해석'],rows)
        removal_gain=[]; removal_all=[]; sign_changes=[]
        for a in ablations:
            r=lookup[a['name']]
            if not (r['status'] in GOOD and r.get('validated')): continue
            removed=r['entry']['comparison'].get('removed',[])
            if len(removed)!=1: continue
            change=a['comparison']['policy']['overall']
            if change['mape']['direction']=='improved':removal_gain.extend(removed)
            if all(change[m]['direction']=='improved' for m in METRICS):removal_all.extend(removed)
            single=lookup.get(removed[0].lower())
            if single and 'modes' in single:
                single_pct=single['modes']['policy']['overall_control_changes']['mape']['relative_improvement_pct']
                removal_pct=change['mape']['relative_improvement_pct']
                if single_pct is not None and removal_pct is not None and single_pct*removal_pct>0:
                    sign_changes.append(removed[0])
        lines += ['ALL 맥락에서 제거 시 MAPE가 낮아진 변수: '+(', '.join(removal_gain) or '없음')+'.',
                  '제거 시 네 macro 오차 지표가 모두 낮아진 변수: '+(', '.join(removal_all) or '없음')+'.',
                  '단독 추가 효과와 ALL 내 포함 효과의 MAPE 방향이 달라진 변수: '+(', '.join(sign_changes) or '없음')+'. '
                  '포함 효과는 제거 효과의 반대 방향으로 해석했으며, 조합의 조건부 효과를 보여줄 뿐 원인을 확정하지 않는다.']
    else: lines.append('ALL이 정상 완료·검증되지 않아 ALL/ablation 효과 결론을 내리지 않는다.')
    return lines,counts


def finish_report(lines,plan,snap,records,ablations,preservation,counts):
    lines += ['## F. 오류·결측·실패 분석','',
              '기존 CONTROL의 예상 결측은 깐마늘 도매(9)의 2025-07-07/14/21/28, '
              '2025-08-04/11/18/25, 각 7개 Horizon으로 총 56행이다. '
              '2025-06-25~07-31 가격 장기 결측과 이후 28일 특징 창의 결측 잔존에 따른 NO_INPUT이다. '
              '이 중 평가 가능한 19행은 Naive로 대체되고 37행은 평가 대상에서 제외된다. '
              '아래에서 키 동일 여부로 각 실험의 결측이 이 기존 현상과 일치하는지 확인한다.']
    health_rows=[]
    for r in records:
        h=r.get('health',{}); c=h.get('categories',{}); ev=h.get('error_event_counts',{})
        o=r.get('metrics',{}).get('policy',{}).get('overall',{})
        health_rows.append([r['name'],r.get('row_count'),c.get('success'),
                           h.get('prediction_success_rate',0)*100 if h else None,o.get('success_rate_pct'),
                           c.get('expected_missing'),c.get('fit_failure'),c.get('predict_failure'),c.get('timeout'),
                           c.get('abnormal_prediction'),h.get('error_event_count'),r.get('fit_count'),
                           r.get('missing_keys_same_as_control',True if r['name']=='CONTROL' else None),r['status']])
    table(lines,['실험','전체 행','OK','출력 성공률 (%)','평가 성공률 (%)','예상 결측','학습 실패 행','예측 실패 행','시간 초과 행','비정상 값 행','오류 이벤트','FIT 횟수','CONTROL 결측 키 동일','상태'],health_rows)
    total_rows=sum(r.get('row_count',0) for r in records[1:])
    total_ok=sum(r.get('health',{}).get('categories',{}).get('success',0) for r in records[1:])
    total_missing=sum(r.get('health',{}).get('categories',{}).get('expected_missing',0) for r in records[1:])
    total_errors=sum(r.get('health',{}).get('error_row_count',0) for r in records[1:])
    lines.append(f'기존 CONTROL 재사용분을 제외한 신규 실행 합계: 출력 {total_rows:,}행, '
                 f'정상 {total_ok:,}행, 예상 결측 {total_missing:,}행, 실제 오류 {total_errors:,}행.')
    lines += ['오류 행 수는 영향받은 예측 수이며, 오류 이벤트 수는 포착된 예외/시간 초과 횟수다. '
              '단일 학습 오류가 여러 예측 행에 영향을 줄 수 있으므로 두 수를 합산하지 않는다. '
              '각 원본 outcome과 이벤트 기록을 보존했으며 자동 재시도는 0회다.']
    failures=[r for r in records[1:] if r['status'] not in GOOD or not r.get('validated')]
    if failures:
        for r in failures:
            lines += [f'- {r["name"]}: 상태 {r["status"]}; 검증 문제 {r.get("issues")}; '
                      f'실행 오류 {r.get("errors")}; returncode {r.get("execution",{}).get("returncode")}.']
    else:lines.append('실패·부분 완료·중단·미실행 및 검증 미통과 실험은 없다.')
    lines += ['','## G. 지표별 순위 및 잠정 후보','',
              '정상 완료(COMPLETED 또는 COMPLETED_WITH_MISSING)·봉인·검증을 모두 통과한 모델만 추천 후보에 포함한다. '
              '다음 지표별 순위는 policy 기준이며 CONTROL과 Naive 기준선도 포함한다. '
              '동일 점수의 정렬은 이름순일 뿐 우열을 뜻하지 않는다.']
    valid=[r for r in records if r['status'] in GOOD and r.get('validated') and 'metrics' in r]
    naive=records[0]['metrics']['naive']['overall']
    rankdata=[(r['name'],r['metrics']['policy']['overall']) for r in valid]+[('Naive',naive)]
    ranking={}
    for metric in METRICS:
        order=sorted(rankdata,key=lambda p:(p[1][metric],p[0]))
        ranking[metric]=[{'name':name,'value':vals[metric]} for name,vals in order]
        lines += [f'### {metric} 순위','']
        table(lines,['순위','모델',metric,'Naive 대비 개선률 (%)','CONTROL 대비 개선률 (%)'],
              [[i,name,vals[metric],C.change(naive[metric],vals[metric],metric)['relative_improvement_pct'],
                C.change(records[0]['metrics']['policy']['overall'][metric],vals[metric],metric)['relative_improvement_pct']]
               for i,(name,vals) in enumerate(order,1)])
    worst=lambda r:max([0.]+[-v['mape']['relative_improvement_pct'] for v in r['control_comparison']['policy']['series'].values()
                             if v['mape']['relative_improvement_pct'] is not None])
    stable=sorted(valid,key=lambda r:(r['health']['error_event_count'],r['health']['error_row_count'],
                  -r['metrics']['policy']['overall']['success_rate_pct'],worst(r),r['metrics']['policy']['overall']['mape']))
    lines += ['### 성공률·안정성 순위','',
              '정렬 기준: 실제 오류 이벤트 수 → 오류 행 수 → 평가 성공률 내림차순 → '
              'CONTROL 대비 최악 계열 MAPE 악화율 → 전체 MAPE. '
              '이는 이번 Tune 결과의 운영·계열 균형 지표이며 미래 데이터 안정성을 보증하지 않는다. '
              'Naive는 학습 모델이 아니므로 이 운영 순위에서 별도 기준선으로 취급한다.']
    reliability_groups=Counter((r['health']['error_event_count'],r['health']['error_row_count'],
                               r['metrics']['policy']['overall']['success_rate_pct']) for r in valid)
    if len(reliability_groups)==1:
        lines.append(f'정상 완료 모델 {len(valid)}개는 오류 수와 예측 성공률이 모두 같아 관측된 운영 안정성은 동률이다. '
                     '아래 순서는 계열별 악화 위험과 MAPE를 보조 기준으로 사용한 것이며 운영 안정성 차이를 입증하지 않는다.')
    table(lines,['순위','모델','오류 이벤트','오류 행','평가 성공률 (%)','CONTROL 대비 최악 계열 MAPE 악화율 (%)','MAPE (%)'],
          [[i,r['name'],r['health']['error_event_count'],r['health']['error_row_count'],
            r['metrics']['policy']['overall']['success_rate_pct'],worst(r),r['metrics']['policy']['overall']['mape']]
           for i,r in enumerate(stable,1)])
    control=records[0]['metrics']['policy']['overall']
    eligible=[r for r in valid if r['name']!='CONTROL' and not r['health']['has_model_errors']]
    both=[r for r in eligible if all(r['metrics']['policy']['overall'][m]<min(control[m],naive[m]) for m in METRICS)]
    balance=sorted(eligible,key=lambda r:(max(r['metrics']['policy']['overall'][m]/naive[m] for m in METRICS),worst(r)))
    recommendation=None
    if both:
        recommendation=min(both,key=lambda r:(worst(r),r['metrics']['policy']['overall']['mape']))
        lines += ['네 macro 오차 지표가 모두 CONTROL 및 Naive보다 낮은 모델: '+', '.join(r['name'] for r in both)+'.',
                  f'이 조건을 만족하는 후보 중 CONTROL 대비 최악 계열 MAPE 악화율이 가장 작은 모델은 **{recommendation["name"]}**다. '
                  '전체 지표의 동시 개선과 계열별 최대 악화를 함께 고려한 잠정 후보로 제시한다.']
    elif balance:
        recommendation=balance[0]
        lines += ['네 macro 오차 지표가 모두 CONTROL 및 Naive보다 낮은 모델은 없다. '
                  '따라서 전반적인 우월성을 입증한 최종 모델은 선정하지 않는다.',
                  f'Naive 대비 네 오차 비율 중 최댓값을 최소화한 균형 검토 후보는 **{recommendation["name"]}**다. '
                  '이 기준은 지표 간 상충을 드러내기 위한 검토 순서이며 성능 입증이나 자동 채택 규칙이 아니다.']
    if recommendation:
        r=recommendation
        bad=[]
        for sid,v in r['control_comparison']['policy']['series'].items():
            bad.append((v['mape']['relative_improvement_pct'],sid))
        bad=[p for p in bad if p[0] is not None]
        value,sid=min(bad)
        label=f'{snap.series[int(sid)].item}/{snap.series[int(sid)].market}({sid})'
        lines += [f'후보의 CONTROL 대비 가장 불리한 계열은 {label}, MAPE 상대 개선률 {fmt(value)}%다. '
                  'D절의 Naive 대비 값과 MAE/RMSE/rMAE도 함께 검토해야 하며, 특정 계열 악화를 전체 평균으로 상쇄해 채택해서는 안 된다.',
                  '모든 순위와 후보는 **Tune 잠정 결과**다. Validation 성능을 측정하거나 미리 주장하지 않았다. '
                  'Validation/Test 실행은 이번 작업에 포함하지 않는다.']
        mode=r['modes']['policy']
        against_naive=[(C.change(mode['naive']['series'][str(s)]['mape'],mode['new']['series'][str(s)]['mape'],'mape')['relative_improvement_pct'],s)
                       for s in snap.series_ids]
        against_naive=[pair for pair in against_naive if pair[0] is not None]
        value,sid=min(against_naive)
        label=f'{snap.series[sid].item}/{snap.series[sid].market}({sid})'
        lines.append(f'후보의 Naive 대비 가장 불리한 계열은 **{label}**, MAPE 상대 개선률 **{fmt(value)}%**, '
                     f'rMAE {fmt(mode["new"]["series"][str(sid)]["rmae"])}다. '
                     +('이 계열에서 Naive보다 악화되므로 전 계열에 대한 일괄 우월성이나 최종 채택을 주장하지 않는다.'
                       if value<0 else '이 결과도 Tune 관측 범위에 한정된다.'))
    lines += ['','## H. 무결성, 남은 위험 및 감사 자료','',
              f'실행 전 보호 대상 기존 파일 {preservation["existing_file_count"]}개를 SHA-256으로 기록했다. '
              f'변경·누락: {len(preservation["changed_or_missing"])}개. '
              f'브랜치: {preservation["branch"]}. Git 추적 파일 diff 비어 있음: {preservation["tracked_diff"]==""}. '
              f'Git HEAD 유지: {preservation.get("git_head_unchanged","N/A")}. '
              f'실행 orchestration 소스 보존: {preservation["orchestrator_unchanged"]}.',
              '기존 CONTROL·소규모 실행·PLANNED·p1·p2·과거 로그와 결과·snapshot·공통 v2 코드·모델 구현을 수정하지 않았다. '
              '새 실행, 배치 감사 자료, 새 분석 도구 및 요청 보고서만 추가했다. '
              '각 새 실행의 코드/설정 보관본과 정밀 지표/공통 지표를 검산했다. '
              '기존 누적 문서 대신 배치 전용 누적 문서를 사용하므로 기존 로그에 대한 append도 없다.']
    table(lines,['기존 실행','유효 상태','봉인 파일 수'],[[p['id'],p['status'],p['seal_count']] for p in preservation['previous_runs']])
    issues=[(r['name'],issue) for r in records for issue in r.get('issues',[])]
    lines += ['남은 한계: Tune에서 여러 설정을 비교했으므로 선택 편향이 있다. '
              '특징 조합·ablation 결과는 조건부 수치 비교이며 단독 변수의 인과 효과가 아니다. '
              '기존 시간 제한은 함수 반환 후 판정 방식이며 강제 중단 장치가 아니다. '
              '파일 SHA-256은 감사 무결성 검증이며 WORM 저장을 보장하지 않는다. '
              'Git 권한 경고가 console에 있으면 해당 실행의 환경 기록과 소스 보관 검증을 함께 확인해야 한다.',
              f'검증 문제 목록: {issues or "없음"}.',
              f'미실행 실험: {[r["name"] for r in records[1:] if r["status"]=="NOT_RUN"] or "없음"}.',
              f'[배치 원본 기록]({link(BATCH/"progress.jsonl")}), '
              f'[보호 파일 사전 해시]({link(BATCH/"preservation_before.json")}), '
              f'[종합 원본 정밀도 분석]({link(BATCH/"analysis_full_precision.json")}), '
              f'[최종 검증]({link(BATCH/"analysis_verification.json")}).']
    return ranking,recommendation['name'] if recommendation else None


def main():
    assert not REPORT.exists(),'Refusing report overwrite'
    plan,snap,records,ablations,preservation=load_all()
    lines,counts=make_report(plan,snap,records,ablations,preservation)
    ranking,recommendation=finish_report(lines,plan,snap,records,ablations,preservation,counts)
    verification={'at':A.now(),'counts':dict(counts),'preservation':preservation,
                  'all_completed_runs_validated':all(r.get('validated') for r in records if r['status'] in GOOD),
                  'run_count':len(records)-1,'new_run_ids_unique':len({r.get('run_id') for r in records[1:]})==len(records)-1,
                  'no_validation_test':all(r.get('config',{}).get('origin_list')=='tune' for r in records if 'config' in r),
                  'analysis_source_sha256':A.sha(Path(__file__))}
    A.exclusive_json(BATCH/'analysis_full_precision.json',{'plan':plan,'runs':records,'ablations':ablations,
                      'ranking':ranking,'provisional_recommendation':recommendation,'verification':verification})
    A.exclusive_json(BATCH/'analysis_verification.json',verification)
    with REPORT.open('x',encoding='utf-8',newline='\n') as f:f.write('\n'.join(lines)+'\n')
    A.exclusive_json(BATCH/'report_sha256.json',{'report':str(REPORT),'sha256':A.sha(REPORT),
                      'analysis_sha256':A.sha(BATCH/'analysis_full_precision.json'),
                      'verification_sha256':A.sha(BATCH/'analysis_verification.json')})
    print(json.dumps({'report':str(REPORT),'lines':len(lines),'bytes':REPORT.stat().st_size,
                      'counts':dict(counts),'recommendation':recommendation,
                      'ranking_best':{m:rows[0] for m,rows in ranking.items()},'verification':verification},ensure_ascii=False),flush=True)


if __name__=='__main__':main()
