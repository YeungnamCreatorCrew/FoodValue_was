# KREI 검증 V2 실행 및 산출물 안내

이 디렉터리는 이동 후 새로 추가한 검증 코드와 결과만 담는다. 이전 `REPORT.ko.md`, 원본 PDF, 추출·OCR 캐시, 감사 기록, 봉인 파일은 읽기만 한다. 이전 스크립트는 과거 경로·루트 계산을 포함하므로 그대로 재실행하지 않는다. 새 코드는 `.git`이 있는 상위 프로젝트를 찾고, 과거 절대 경로를 메모리에서만 현재 KREI 디렉터리로 해석한다. 파일 이동·삭제·덮어쓰기를 하지 않는다.

## 현재 결과

`CURRENT_RESULT.json`과 상위 `VERIFICATION_V2_REPORT.ko.md`가 최종 결과를 지정한다. `runs/`의 다른 디렉터리와 이전 `results_*`는 규칙 개선 과정의 감사 이력이며 현재 데이터와 합산하지 않는다. `run_registry.json`에 결과의 사용 상태를 기록한다. 모든 실행은 Python의 `-B` 옵션으로 기존 라이브러리·코드의 bytecode 캐시 변경을 막는다.

```powershell
python -B model_comparison/ridge/v2/krei_monthly/verification_v2/test_verification.py

# 로컬 PDF만 다시 읽으며 매번 새 runs 디렉터리를 만든다.
python -B model_comparison/ridge/v2/krei_monthly/verification_v2/extract_v2.py --workers 3

# 동일 PDF 해시의 이미 검출된 표 좌표를 재사용할 수 있다.
python -B model_comparison/ridge/v2/krei_monthly/verification_v2/extract_v2.py --workers 3 --reuse-tables model_comparison/ridge/v2/krei_monthly/verification_v2/runs/extract_20261117T134619171311Z
```

`finalize.py --extraction <실제 새 RUN>`은 이전 1,934행을 모두 유지하는 재검증 원장과 새로운 수치 근거를 별도로 기록한다. 무조건 이전 자동 상태를 승계하지 않는다. 값·단위·비교 기준·지표·페이지·좌표·품종/작형 범위가 일치하는 명확한 근거와 연결된 경우만 통과한다. 이전 `metric=NULL`을 확정하는 경우 교정 이력을 남긴다.

## 검증 구분

- `auto_validated`: 네이티브 원문의 명확한 지표·범위·수치·단위·기준·대상 기간을 구조적으로 검증한 숫자다.
- `manually_verified`: 이 세션에서 에이전트가 실제 PDF 렌더 이미지의 숫자·행·열·제목을 대조한 결과다. 사람의 최종 승인이나 원본 버전 증명은 아니다.
- `needs_review`: 해석이 모호하거나 OCR·단위·시나리오·과거 조사치 등을 더 확인해야 한다.
- `vintage_status=unverified`: 당시 공개된 PDF와 지금 보존한 바이트가 같은 버전이라는 공식 증거를 확보하지 못한 상태다. 현재 모든 행에 해당한다.

문서 표기의 발행일을 확인한 것과 실제 과거 공개 시점의 증명은 별개다. 2025년 5월 엽근채소는 표지 발행일이 4월 2일로 인쇄되어 있어 임의 수정하지 않고 충돌로 남겼다. OCR에는 엔진이 제공하지 않는 신뢰도 점수를 넣지 않았다. 지역·품종·작형·가공형태·시장·등급을 함부로 합치지 않는다.

표에서 `평년`의 절대량 행은 증감률이 아니다. `증감률` 구역의 전년·평년 행만 변화율로 읽는다. 본문에서 단위가 반복되는 `1,400원∼1,500원`도 범위이며, 첫 값이나 임의 평균을 단일 전망으로 저장하지 않는다. 표의 정확한 수치와 본문의 반올림 수치는 각자 근거를 유지한다.

## 학습 준비 상태

`KREI_OUTLOOK`은 신규 제안 그룹 이름이며 기존 Ridge 코드·설정에 연결하지 않았다. `feature_plan.json`과 `feature_missingness.csv`만 작성한다. 학습 승인 수치가 0개인 동안 실제 특징 행렬은 생성하지 않는다. 검증 상태를 소득·가격 등의 숫자 대용 0으로 채우지 않는다. 기존 `asof.py`를 수정하지 않고 동일 차단 함수를 호출하며, 날짜만 알려진 발표의 당일 사용과 이후 수정본의 과거 사용을 차단한다.

10개 가격 계열 매핑은 보존된 `price_series.csv`를 읽어 작성했다. 일반 마늘 공급 전망은 깐마늘 가격의 관련 외부변수 후보이며 동일 상품 가격이 아니다. 배추·무의 포기/개를 kg로 바꾸는 가중치는 만들지 않았다. 가격의 직접 병합은 모든 계열에서 아직 승인하지 않았다.

수집·다운로드·DB·Git 쓰기·Ridge 학습을 실행하지 않는 로컬 검증 작업이다. 공식 웹 자료는 과거 공개 버전 확인을 위한 읽기 전용 조사에만 사용했다.
