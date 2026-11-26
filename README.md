# FoodValue

FoodValue는 식자재 시세, 7일 가격 예측, 구매 판단 지표를 제공합니다.

## 문서

- [시세·예측 API 가이드](README_PRICES.md): 예측 알고리즘·조회 API·배치 실행·검증 기준

- [외부변수 가중치 결정 기록](README_WEIGHTING.md): 가중치 결정 방식·실험 로그·근거

- [가격 예측 모델 변경 기록](model_comparison/xgboost/README_MODEL.md): 모델 버전별 변경 내용·실데이터 백테스트 결과
- [모델 비교 실험 기준서 v1](model_comparison/MODEL_TRAINING_STANDARD.md): 4개 모델 비교 실험의 고정 규칙. 공통 도구는 [tools](tools/README.md), 결과 형식은 [experiments](experiments/README.md)


- [DB 가이드](README_DB.md): 로컬 DB 실행, 스키마(Flyway) 변경 규칙

## 커밋 · PR 규칙

### 커밋 메시지

`타입 : 설명` 형식으로 작성합니다. 예: `feat : 냉장고 재료 등록 API 추가`, `docs : DB 협업 가이드 수정`

| 타입 | 설명 |
| --- | --- |
| feat | 새로운 기능 추가 및 기존 기능 수정 |
| fix | 버그 수정 |
| docs | 문서 및 주석 수정 |
| style | 코드 스타일 및 포맷팅 수정 |
| refact | 기능 변화 없는 코드 리팩터링 |
| test | 테스트 코드 추가/수정 |
| chore | 패키지 매니저 수정 및 기타 변경 (예: `.gitignore`) |
| merge | 브랜치 병합 |

### Pull Request

- 작업 브랜치는 `dev`에서 분기하고, PR의 대상(base)도 `dev`로 지정합니다.
- PR 제목은 커밋 메시지와 같은 `타입 : 설명` 형식으로 작성합니다. 예: `Docs : DB 협업 가이드 수정`
- PR 본문은 `.github/pull_request_template.md` 양식(PR 요약 / 변경 내용 / 관련 이슈)에 맞춰 작성합니다.
