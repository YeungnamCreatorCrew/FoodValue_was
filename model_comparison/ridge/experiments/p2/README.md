# Ridge p2 실행 계획 — ridge-p2-v1

상태: **PLANNED**. 이번 준비 작업에서는 전체 p2 Validation과 공식 Test를 실행하지 않는다.
계획의 결과 수치는 `plan.json`에서 null이다. 자동화 테스트의 합성 데이터 결과는 연구 결과가 아니다.

공식 기준선은 `ridge-p1-20261111-07` 하나로 고정한다. policy Macro MAPE 5.060471%,
Naive 4.912547%, 상대 개선율 -3.011147%, macro rMAE 1.026703, Naive 승리 계열 2/10,
평가 대상 성공률 99.2018%, 관문 1X·2X·3X·4O·5X, 최종 Test 미실행.
`p1_reference.json`은 현재 체크아웃의 원본 파일 바이트 SHA-256을 고정하며 원본을 재작성하지 않는다.

## 변경과 고정 조건

기존 `ridge/model.py`는 그대로 보존한다. 새 `model_p2.py:RidgeP2Model`만 사용한다.
외부 특징과 결측 처리 외에는 p1의 StandardScaler → Ridge 파이프라인을 유지한다.
Alpha=10, solver=lsqr, raw_price, 계열별 direct_pooled(7 horizons를 한 회귀에 학습), seed=42,
최근 최대 1,825일, 주별 첫 기준일 재학습, 공통 Loader·정답·후처리·평가·분할은 동일하다.
요일 인코딩, 상호작용, 결측 표시 열, 특징 선택, 추가 튜닝은 도입하지 않는다.

`p2` 단계에서 `extra_features=[]`, `feature_set=base_v1`을 공통 검사기가 허용함을 확인했다.
따라서 CONTROL은 새 `ridge-p2-YYYYMMDD-NN` 실행으로 기록한다. p1 재실행이나 원본 덮어쓰기가 아니다.
CONTROL과 p1은 모델 클래스가 달라 config_id가 다르지만 유한한 기본 특징의 원시 예측은 같아야 한다.
단위 테스트는 합성 자료와 실제 스냅샷의 대파 소매·배추 소매, 한 기준일에서 이를 확인한다.

## 결측 및 비정상 데이터

매 `fit(history, 42)`에서 전달받은 **현재 학습 표본만으로** 특징별 유한 관측 중앙값을 구한다.
중앙값은 극단적인 가격 수준·변화율의 영향을 평균보다 적게 받는다. 대체 후 StandardScaler도 같은
학습 표본으로만 fit한다. 예측 입력·검증 정답·향후 주의 자료로 통계를 보정하지 않는다.
NaN이 없는 입력은 같은 수치 배열로 p1 파이프라인에 전달되어 학습 계산이 동일하다.

학습 표본에서 전부 NaN인 열은 차원을 유지하고 0으로 채운다. 그 열은 해당 모델의 예측에서도
관측값 유무와 관계없이 0으로 고정한다. 학습에서 관측하지 않은 분포를 임의로 반영하지 않으며,
StandardScaler의 분산=0, Ridge 계수=0이 된다. 다음 주 재학습 때 관측이 생기면 다시 중앙값을 학습한다.
전부 결측인 열을 자동 삭제하는 imputer의 라이브러리별 동작 차이도 피한다.

특징의 +∞·−∞는 NaN으로 간주하지 않고 오류로 거부한다. 타깃 NaN·∞·0 이하도 오류로 거부하며
타깃 대체·행 삭제·clip을 하지 않는다. 공통 실행기가 FIT_FAILED/PREDICT_FAILED를 기록한다.
예측 가격의 유효성 판정·반올림·실패 시 Naive 대체는 공통 도구에 맡긴다.
특징은 `history.feature_names`를 저장하고 예측 때 이름·순서·열 수 및 1~7 horizons를 검증한다.

## 외부변수 계획

열 이름과 결합 순서는 `tools.loader.feature_names()`와 `check_bundles()`를 사용한다.
`plan.json`에는 전체 열 이름과 열 수를 기록했다. 실행 시에도 start.json 및 매 FIT 진단에 실제 열을 남긴다.

| 순서 | 묶음 | 추가/전체 열 수 | 가설 및 해석 시 확인할 점 |
|---|---|---|---|
| 0 | CONTROL | 0 / 15 | 전처리가 기존 기본 특징 결과를 바꾸는지 검증 |
| 1 | MARKET | 4 / 19 | 상대 시장 선행·동행 정보. 가격 lag와 중복 및 작형 불일치 비율 NaN 확인 |
| 2 | NATIONAL_WEATHER | 6 / 21 | 전국 기상과 가격의 선형 연관. 지역 평균·지연·비선형 효과 한계 확인 |
| 3 | EVENT | 4 / 19 | 명절 전후 수요 시점. 계절 특징과 중복 및 품목 차이 확인 |
| 4 | MACRO | 2 / 17 | 환율 변화의 선형 연관. 전달 시차와 단위·품목 차이 확인 |
| 5 | PRODUCTION | 1 / 16 | 공개된 연간 공급 변화. 느린 갱신·발표 지연·누락 확인 |
| 6 | COMBINATION | 조건부 | 5개 단독 완료 후 p1보다 policy Macro MAPE가 낮은 묶음이 2개 이상이면 그 묶음 전체 1회 |

상대 시장·기상·환율은 d−1까지, 자기 가격은 d까지, EVENT는 사전 확정된 목표일 달력,
생산량은 Loader의 `published_from`(Y+1년 6/30) 규칙을 따른다. 미래 실제 외부값은 사용하지 않는다.
공통 Loader의 학습 표본은 각 표본의 목표일≤현재 재학습일이다. 학습 중앙값은 그 재학습일에
알려진 학습 창 전체에서 산출한다. 과거 표본별로 중앙값을 다시 fit할 필요는 없다.
최신 수정본을 사용하는 회고 평가라는 데이터 한계와 MARKET의 작형 차이는 보고서에 명시한다.

## 실행 절차와 명령어

아래 학습 명령은 **다음 실행 단계용이며 이번 작업에서 실행하지 않는다**.
프로젝트 루트에서 실행한다. `p2.py`는 기본적으로 읽기 전용 계획을 출력하며 `--execute`가 있어야 학습한다.

```powershell
# 계획만 출력: 학습 없음
uv run --extra prices python -m model_comparison.ridge.p2

# 향후 학습 전 데이터 확인
uv run python -m tools.check_snapshot data/snapshots/fv-snap-20261031-v1

# 별도 base-only p2 대조 실행
uv run --extra prices python -m model_comparison.ridge.p2 --execute --control

# 단독 실험: 아래 순서로 하나씩. 같은 명령 재호출 시 검증된 완료 결과만 재사용
uv run --extra prices python -m model_comparison.ridge.p2 --execute --bundle MARKET
uv run --extra prices python -m model_comparison.ridge.p2 --execute --bundle NATIONAL_WEATHER
uv run --extra prices python -m model_comparison.ridge.p2 --execute --bundle EVENT
uv run --extra prices python -m model_comparison.ridge.p2 --execute --bundle MACRO
uv run --extra prices python -m model_comparison.ridge.p2 --execute --bundle PRODUCTION

# 5개 단독이 모두 완료된 뒤 유효한 개선 묶음 전체 조합
uv run --extra prices python -m model_comparison.ridge.p2 --execute --combine

# 향후 한 번에 진행할 때: 단독 5개 → 조건부 조합 (CONTROL은 별도)
uv run --extra prices python -m model_comparison.ridge.p2 --execute --all

# 향후 제한 점검 예시: 부분 범위는 p1과 비교·조합 선정에 사용하지 않음
uv run --extra prices python -m model_comparison.ridge.p2 --execute --bundle MARKET --month 2025-01 --series 1 --out runs/ridge-p2-diagnostics
```

`configs/p2/*.json` 6개는 검토·직접 공통 실행용 설정이다. 감사 자동화를 위해 위 wrapper 사용을 권장한다.
wrapper는 보존된 p1 설정에서 필요한 클래스·feature_set·extra_features만 바꿔 같은 설정을 생성한다.
CLI에는 Test 단계나 튜닝 옵션이 없다. p1 공식 기준선은 최신 폴더 검색으로 고르지 않는다.
Windows CLI는 공통 도구의 subprocess 기록을 위해 필요하면 Python UTF-8 모드로 자동 재진입한다.
Python API에서 직접 호출할 때와 pytest 실행은 `python -X utf8`을 사용한다.

## 중복·실패·재개와 보존

공통 산출물은 새로운 `experiments/ridge-p2-…/` 폴더의 config, metrics, predictions, environment,
run.log, tuning_log에 저장한다. 기존 폴더는 공통 실행기가 거부한다. 실행 ID는 실패 폴더까지 피해서 생성한다.
감사 기록은 `experiments/p2/execution/attempts/<UTC시각-UUID>/`이며 각 시도는 별개다.
OS 잠금은 같은 기록 경로의 동시 실행을 차단하고 프로세스가 종료되면 자동 해제된다.

완료 재사용 조건은 다음 모두다: 전체 설정 SHA-256, 코드·Loader·평가기·lock SHA-256, 데이터 manifest 및
파일 SHA-256, Python·주요 라이브러리 버전, Git SHA·브랜치, 날짜·계열 범위 일치; 공통 6개 산출물 및 감사
파일의 해시 일치; 공통 형식 검사 통과; 정확한 계열×기준일×horizon 격자; 공식 metrics 재계산 결과 일치.
8자리 config_id나 metrics.json의 존재만으로 재사용하지 않는다.

모델 FIT_FAILED·PREDICT_FAILED·INVALID_VALUE·TIMEOUT 또는 평가 성공점 0은 FAILED로 보존하고 재사용하지
않는다. Loader의 NO_INPUT은 공식 실패 상태를 보존한 정상 종료로 인정하되 성공률·관문에서 평가한다.
`COMPLETED`는 실행·감사 완료이며 **채택 관문 통과와 다르다**. 관문 미달도 연구 결과로 보존한다.
Ctrl+C는 INTERRUPTED로 기록한다. 강제 종료로 terminal record가 없으면 다음 재개에서 INTERRUPTED를
기록하고 새 시도로 실행한다. 부분 예측을 이어 붙이지 않고 해당 묶음을 처음부터 새 ID로 실행한다.
실패·미완료·변조 의심 결과는 삭제하거나 덮어쓰지 않는다. 소스나 전처리 변경은 새 identity가 된다.

## 실행 전 추가 확인

팀의 실행 기준 커밋·uv.lock 및 설치 패키지 일치, p2 코드 검토, CONTROL 동등성, 데이터 manifest
`3297209f59afbe96faa1e93d22f267fcc653d107cf42082f10018dee4eb81aa0`, 10계열·244기준일·7시점,
원천의 공개시점 가정과 생산량 매핑을 확인한다. p1 코드/데이터 버전을 바꿔 비교하지 않는다.
수정이 필요하면 CHANGELOG에 이유·영향을 남기고 새 전처리/실험 버전을 사용한다.
자원 관문 6은 지정 장비의 Docker Test 값으로만 확정하므로 로컬 값을 채택 근거로 단정하지 않는다.

기록 형식은 `RECORD_TEMPLATE.md`, 분석 절차는 `ANALYSIS.md`, 준비 검증은 `verification/`을 참조한다.
