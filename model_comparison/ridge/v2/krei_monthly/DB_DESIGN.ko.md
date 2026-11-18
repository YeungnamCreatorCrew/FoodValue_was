# KREI 월보 DB 적재 설계

이 문서는 설계만 기록한다. DB 연결, 테이블 생성, INSERT, 모델 학습은 구현하거나 실행하지 않았다.

| 논리 테이블 | 키와 주요 필드 | 보존 원칙 |
| --- | --- | --- |
| report_issue | issue_id, 발행 연월, 묶음 코드, 제목, 원본 XML SHA-256 | 발행 연월은 전망 대상 기간과 별도 |
| document_version | PDF SHA-256, issue_id, source_url, final_url, 파일 경로, 크기, 수집 시각, 등록·수정 원문 시각 | 동일 URL이라도 바이트가 달라지면 새 버전. 기존 버전 수정 금지 |
| document_item | PDF SHA-256, KREI 품목 코드, Ridge 품목명, 관계, 가공 형태·품종·시장 범위 | 묶음 PDF와 품목은 다대다. 마늘과 깐마늘은 동일 분류로 간주하지 않음 |
| extracted_page | PDF SHA-256, 페이지, 원문 텍스트, 줄·단어 좌표, native/OCR, 도구 버전, 품질 상태 | OCR 교정은 별도 버전에 저장. 원본 PDF 유지 |
| forecast_fact | record_id, 품목, metric/metric_candidate, 기준 종류, 값/하한/상한, 단위, 발행일, target_period/type, 근거 문장·페이지·좌표 | 불명확한 지표는 metric=NULL. 불명확한 일자·대상 기간도 NULL |
| review_decision | record_id, 검토자, 검토 일시, 판정, 확인한 페이지, 교정값, 사유 | 최초 추출 결과를 덮어쓰지 않는 추가 이력 |
| feature_materialization | snapshot_id, 예측 기준 시각, 승인된 fact IDs, 선택 정책 버전, 입력 SHA-256 | 과거 시점에 공개된 문서의 검증된 버전만 선택 |

값은 SQL DECIMAL/NUMERIC, 기간과 시각은 DATE 및 timezone-aware TIMESTAMP를 사용한다. 전년·평년·전월 기준을 별도 enum으로 저장하고, 증감률의 단위는 퍼센트 포인트가 아닌 `%`로 유지한다. 범위형 수치의 중앙값을 임의로 만들지 않는다. 원/10kg와 원/kg를 원본 필드에서 합치지 않으며, 단위 변환이 필요하면 변환식과 원본 record_id를 별도 파생 이력에 기록한다.

적재 전에는 `records.csv` 전체를 사용하지 않는다. 수동 검토와 시점 적합성 검증을 통과한 행만 staging에서 승인 테이블로 옮기는 작업을 별도로 승인·구현해야 한다. 현재 산출물의 `eligible_for_model`은 모두 false다.

자동화는 월보 XML을 현재 월과 최근 월에 대해 재조회하는 수집 작업, 원문 파일 버전 관리, 페이지 추출, 검토 큐, 승인된 특징 생성의 순서로 분리한다. `--refresh-known`은 같은 URL의 무통보 교체를 탐지할 때 사용한다. 평상시에는 등록·수정 시각이 같고 로컬 SHA-256이 일치하면 다운로드를 생략한다. 신규·수정 응답과 실행 결과를 매번 새 디렉터리에 남긴다. 재시도 후 실패한 URL만 별도 작업으로 재실행하며, 빈 API 응답을 네트워크 실패나 실제 미발행으로 단정하지 않는다.
