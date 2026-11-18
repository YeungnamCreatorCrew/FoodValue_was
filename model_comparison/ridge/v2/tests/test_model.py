import copy
import numpy as np
import pytest
from sklearn.linear_model import Ridge
from sklearn.preprocessing import StandardScaler
from model_comparison.v2.models import relative
from model_comparison.ridge.v2.model import AUDIT_SINK, PooledRidgeV2


def data():
    # 10 series, 7 horizons, 5 synthetic origins each.
    names=['current','lag7','horizon','external','empty','is_series']
    h=np.tile(np.repeat(np.arange(1,8),5),10)
    sid=np.repeat(np.arange(10),35)
    rng=np.random.default_rng(42)
    current=100+sid*100+rng.uniform(1,10,len(h))
    x=np.column_stack([current,current*.95,h,rng.normal(size=len(h)),np.full(len(h),np.nan),sid])
    x[::4,3]=np.nan
    y=current*(1+h*.01)
    return x,y,h,names


def test_interface_ten_pooled_series_seven_models_relative_manual_reference():
    x,y,h,names=data()
    before=x.copy()
    model=PooledRidgeV2().fit(x,y,h,names,42)
    assert set(model.models)==set(range(1,8))
    assert [d['samples'] for d in model.diagnostics_]==[50]*7
    rel,current=relative(x,names)
    j=1
    train=rel[h==j][:,[0,1,3,4,5]]
    median=np.array([np.nanmedian(train[:,i]) if i!=3 else 0. for i in range(5)])
    clean=np.where(np.isnan(train),median,train)
    scaler=StandardScaler().fit(clean)
    ref=Ridge(alpha=10,solver='lsqr',random_state=42).fit(scaler.transform(clean),y[h==j]/current[h==j]-1)
    expected=current[h==j]*(1+ref.predict(scaler.transform(clean)))
    np.testing.assert_allclose(model.predict(x[h==j],h[h==j]),expected)
    np.testing.assert_array_equal(x,before)
    np.testing.assert_allclose(model.predict(x,h),y,rtol=1e-10)
    assert 'horizon' not in model.importance()


def test_training_only_per_horizon_medians_scaling_freeze_and_no_mutation():
    x,y,h,names=data()
    x[h==1,3]=np.nan
    x[h==2,3]=123.
    m=PooledRidgeV2().fit(x,y,h,names,42)
    assert m.models[1]['all_missing'][2]
    assert m.models[2]['median'][2]==123
    state=copy.deepcopy(m.diagnostics_)
    p=x[:7].copy()
    p[:,3:5]=1e12
    p[:,2]=np.arange(1,8)
    original=p.copy()
    a=m.predict(p,np.arange(1,8))
    p[:,4]=np.nan
    np.testing.assert_array_equal(a,m.predict(p,np.arange(1,8)))
    assert m.diagnostics_==state
    np.testing.assert_array_equal(original[:,3:5],1e12)


@pytest.mark.parametrize('defect', ['inf','bad_current','nan_current','zero_current','bad_target','nan_target',
                                  'dimensions','names','horizons','missing_horizon','target_shape','horizon_column'])
def test_reject_malformed_and_invalidate_refit(defect):
    x,y,h,names=data()
    m=PooledRidgeV2().fit(x,y,h,names,42)
    if defect=='inf': x[0,4]=np.inf
    if defect=='bad_current': x[0,0]=-1
    if defect=='nan_current': x[0,0]=np.nan
    if defect=='zero_current': x[0,0]=0
    if defect=='bad_target': y[0]=-1
    if defect=='nan_target': y[0]=np.nan
    if defect=='dimensions': x=x[:,0]
    if defect=='names': names[-1]=names[0]
    if defect=='horizons': h=h[:,None]
    if defect=='missing_horizon': x,y,h=x[h!=7],y[h!=7],h[h!=7]
    if defect=='target_shape': y=y[:,None]
    if defect=='horizon_column': x[0,2]=7
    with pytest.raises(ValueError): m.fit(x,y,h,names,42)
    assert m.models=={} and not m.fitted_
    with pytest.raises(RuntimeError): m.predict(*data()[::2][:2])


def test_bad_predict_inputs_determinism_and_nonpositive_output():
    x,y,h,names=data()
    a=PooledRidgeV2().fit(x,y,h,names,42)
    b=PooledRidgeV2().fit(x,y,h,names,42)
    np.testing.assert_array_equal(a.predict(x,h),b.predict(x,h))
    before=x.copy()
    a.predict(x,h)
    np.testing.assert_array_equal(before,x)
    for col,value in [(0,0),(0,np.nan),(4,np.inf)]:
        bad=x.copy(); bad[0,col]=value
        with pytest.raises(ValueError): a.predict(bad,h)
    a.models[1]['ridge'].coef_[:]=0
    a.models[1]['ridge'].intercept_=-2
    assert np.isnan(a.predict(x[h==1],h[h==1])).all()


def test_fit_failure_midway_leaves_no_models_and_audits(monkeypatch):
    x,y,h,names=data()
    events=[]
    token=AUDIT_SINK.set(events.append)
    old=Ridge.fit
    count=0
    def fail(self,*args,**kwargs):
        nonlocal count
        count+=1
        if count==3: raise MemoryError('synthetic OOM')
        return old(self,*args,**kwargs)
    monkeypatch.setattr(Ridge,'fit',fail)
    m=PooledRidgeV2()
    try:
        with pytest.raises(MemoryError): m.fit(x,y,h,names,42)
    finally: AUDIT_SINK.reset(token)
    assert not m.models
    assert events[-1]['error_type']=='MemoryError'


def test_diagnostics_json_finite_and_no_svd(monkeypatch):
    import json
    monkeypatch.setattr(np.linalg,'svd',lambda *a,**k: pytest.fail('No SVD'))
    events=[]
    token=AUDIT_SINK.set(events.append)
    try:
        PooledRidgeV2().fit(*data(),42)
    finally: AUDIT_SINK.reset(token)
    json.dumps(events,allow_nan=False)
    feature=events[0]['horizons'][0]['features']['empty']
    assert feature['all_missing'] and feature['median']==0 and feature['missing_rate']==1
