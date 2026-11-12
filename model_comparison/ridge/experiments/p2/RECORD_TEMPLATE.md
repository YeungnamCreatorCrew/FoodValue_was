# 개별 실험 기록 양식

상태: PLANNED. 실행 전 결과 값은 모두 null/미실행으로 유지한다.
실행 후 이 양식을 새 시도 폴더 또는 별도 리뷰 문서로 복사한다. 완료 감사 원본은 수정하지 않는다.

| 식별·재현성 | 값/증거 경로 |
|---|---|
| 계획 ID / 실험 ID / 시도 ID / 버전 | null / start.json |
| UTC 및 KST 실행 시작·종료 / 경과 초 | null / start, completion 또는 failure, result |
| 상태 / 이전 시도 / 재사용 여부 | PLANNED / null / null |
| Git commit / branch / 변경분 해시 | null / start.identity.lineage |
| 모델·설정 파일 및 정규 설정 SHA-256 | null / source_sha256, requested_config_file_sha256, config_sha256 |
| 스냅샷 ID / manifest 및 CSV SHA-256 | null / start.identity.lineage |
| Loader·평가기·standard 버전 및 소스 해시 | null / standard_version 및 source_sha256 |
| 정확한 명령 / Python / NumPy·SciPy·sklearn / 전체 설치 목록 | null / start.command, lineage, environment.txt |
| Seed / Alpha / Solver / Strategy / Target | 42 / 10 / lsqr / direct_pooled / raw_price |
| 실제 기준일·계열·horizon / 비교 가능 범위 | null / start.identity.scope |

## 변경과 고정

- 추가 묶음 / 선택 이유 / 검증할 가설: null (plan.json 참조)
- 실제 추가 특징 / 전체 특징 이름·순서·수: null (start.json 및 FIT diagnostics)
- 비교 기준 실험 / 변경 항목 / 고정 항목: null (README 고정 조건 참조)
- 전처리 버전·변경 이유·예상 영향: ridge-p2-median-v1 / 학습 중앙값 / 누락 입력 대응
- 누락률·전체 결측 열·학습 대체값·예측 대체 횟수·전체 결측 열 강제 0 횟수: null
- 입력의 공개시점 가정 / 검증 증거 / 확인되지 않은 한계: null
- 코드나 설정 변경 시 이전 버전·SHA 및 CHANGELOG 연결: null

## 공식 결과 및 비교

| 항목 | 값 |
|---|---|
| policy Macro/Micro MAPE / Naive MAPE / 상대 개선율 | null |
| Ridge p1 대비 MAPE 변화 %p / 상대 개선율 % | null |
| macro rMAE / rMAE 제외 계열 | null |
| Naive보다 개선 계열 / p1보다 개선·악화·동률 계열 수 | null |
| 10개 계열별 MAPE·Naive·rMAE·p1 변화 | null |
| 품목별 macro MAPE 및 p1 변화 / 소매·도매별 동일 비교 | null |
| model_only / common_success | null |
| 평가 대상 수·성공률 / 전체 예측 행 상태·오류코드별 개수 | null |
| 실행 시간 / 공통 run.log RESOURCES / 잠정 메모리 한계 | null |
| 공통 형식 검사 오류·경고 / 관문 1~5 / 종합 | null |
| 조합 여부·구성 / 대응 단독 실험 ID / 각각과 MAPE 차이 | null |

숫자의 원본은 metrics.json이다. 기록용 result.json은 공식 결과의 발췌 및 아래 명시된 차이 계산이다.
`official_comparison.json`은 p1과의 policy/model_only/common_success를 공통 evaluate.compare로 구한다.
부분 범위 실행에서는 p1 대비 수치와 조합 선정 값을 생성하지 않는다.

## Ridge 특성 해석 및 결정

- 스케일러 평균·scale와 표준화/원 단위 계수의 주별 변화: null
- 가격 특징과 외부변수 상관·조건수·계수 부호/규모 안정성: null
- 학습/예측 누락률에 따른 구간별 성능, 품목·시장·계절·시차 차이: null
- 선형 관계 한계 및 대안 가설 / 실제 검증한 증거 / 아직 검증하지 않은 주장: null
- 유지/제외/추가 검증 결정 및 이유: PENDING_REVIEW
- 검토자·검토 시각 / 최종 선정에 이용한 실행 ID와 비교 근거: null

## 감사 이력

- 모든 시작·성공·실패·중단은 execution/events.jsonl과 각 시도 start/terminal record를 연결한다.
- 실패 원인·수정 내용·수정 전후 테스트 결과·영향 범위: null
- 재실행은 새 시도·새 공식 ID로 기록하고 이전 산출물 경로와 해시를 남긴다.
- completion.json은 공통 산출물 및 진단·설정·소스 복사본의 SHA-256 봉인 목록이다.
- 실행 후 리뷰는 새 문서로 추가한다. 실패 실험이나 기존 결과·감사 기록을 삭제하지 않는다.
