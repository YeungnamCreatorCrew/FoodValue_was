import math
from datetime import date, timedelta
from types import SimpleNamespace

import pytest

from app.services import price_prediction as model
from app.services.price_batch_service import guidance


def observations(count=480,constant=False):
    start=date(2024,1,1)
    return [(start+timedelta(days=i),1000 if constant else round(1000+100*math.sin(i/20))) for i in range(count)]


def test_features_and_training_have_no_future_labels():
    rows=observations()
    days,values,observed,ages=model.normalize(rows,rows[-1][0])
    before=model.features(days,values,ages,60,7)
    edited=values.copy()
    edited[61:]=[900000]*len(edited[61:])
    assert model.features(days,edited,ages,60,7)==before
    inputs,targets=model.training_data(days,values,observed,ages,80,7)
    assert targets[-1]==values[80]/values[73]-1  # 시작일 가격 대비 변화율
    assert inputs[-1][0]==values[73]


def test_missing_targets_never_become_training_truth():
    rows=observations()
    missing=rows[70][0]
    rows=[row for row in rows if row[0]!=missing]
    days,values,observed,ages=model.normalize(rows,rows[-1][0])
    assert observed[70] is False and values[70]==values[69]
    _,targets=model.training_data(days,values,observed,ages,70,1)
    assert len(targets)==69-28  # 28..69까지 원래 42개 중 결측 타깃 1개 제외


def test_long_gaps_are_not_silently_filled():
    rows=observations(100)
    rows=[row for index,row in enumerate(rows) if not 40<=index<=55]
    days,values,observed,ages=model.normalize(rows,rows[-1][0])
    assert values[47] is None
    assert model.features(days,values,ages,60,1) is None


def test_short_or_stale_history_fails():
    rows=observations(50)
    with pytest.raises(model.InsufficientDataError):
        model.predict(rows,rows[-1][0])
    with pytest.raises(model.InsufficientDataError):
        model.normalize(rows,rows[-1][0]+timedelta(days=8))


def test_future_observations_do_not_affect_inputs():
    rows=observations(100)
    result=model.normalize(rows,rows[70][0])
    assert result[0][-1]==rows[70][0] and len(result[0])==71


@pytest.fixture(scope='module')
def actual_prediction():
    pytest.importorskip('xgboost')
    rows=observations(constant=True)
    return model.predict(rows,rows[-1][0])


def test_real_xgboost_and_baseline_selection(actual_prediction):
    result=actual_prediction
    assert result.model=='LAST_PRICE' and result.quality=='BASELINE'
    assert result.prices==[1000]*7
    assert result.metrics['evaluation']['LAST_PRICE']['mape']==0
    assert all(x['calibrationSamples']>=30 for x in result.metrics['intervals'])
    assert result.lower==result.upper==[1000]*7
    assert all(x['coverage']==1 for x in result.metrics['intervals'])


def test_guidance_requires_validation():
    assert guidance([900]*7,1000,'BASELINE')==('HOLD',None,None)
    assert guidance([990,980,900,970,980,1000,1100],1000,'VALIDATED')==('BUY_LATER',3,100)
    assert guidance([1010,1020,1030,1040,1050,1060,1070],1000,'VALIDATED')==('BUY_NOW',None,0)
    assert guidance([1000]*7,1000,'VALIDATED')==('STABLE',None,0)


def test_invalid_prices_and_duplicates():
    day=date(2024,1,1)
    with pytest.raises(ValueError):
        model.normalize([(day,0)],day)
    with pytest.raises(model.InsufficientDataError):
        model.normalize([(day,1000),(day,2000)],day)


def test_native_library_failure_is_reported_with_hint(monkeypatch):
    import sys
    import types

    class Broken(types.ModuleType):
        def __getattr__(self, name):
            raise RuntimeError('libomp.dylib could not be loaded')
    monkeypatch.setitem(sys.modules, 'xgboost', Broken('xgboost'))
    with pytest.raises(model.ModelDependencyError, match='libomp'):
        model.check_dependencies()
