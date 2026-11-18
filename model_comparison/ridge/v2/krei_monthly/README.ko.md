# KREI 과거 월보 수집 및 추출

모든 실행 파일과 산출물은 이 디렉터리에 격리되어 있다. 기존 Ridge 코드·설정·스냅샷·실험 파일을 import하거나 수정하지 않는다. DB 작업, Git commit/push/PR, Tune/Validation/Test 학습은 수행하지 않는다.

## 실행 환경

Python 3.13, PyMuPDF 1.26.7, Windows PowerShell 5.1 및 설치된 한국어 Windows.Media.Ocr 인식기를 사용했다. 외부 OCR 서비스는 사용하지 않는다. PyMuPDF는 `_vendor/`에만 설치했다. 다른 환경에서 실행할 때 해당 환경에 맞는 PyMuPDF wheel이 필요하다. 기존 프로젝트의 requirements/pyproject/가상환경은 변경하지 않았다.

```powershell
# 새로운 환경에서만 실행. 기존 _vendor 파일은 덮어쓰지 말 것.
python -m pip install --target data/krei_monthly/_vendor PyMuPDF==1.26.7

python data/krei_monthly/collector.py probe
python data/krei_monthly/collector.py sample
python data/krei_monthly/collector.py bulk
python data/krei_monthly/collector.py verify-routes

# collector가 출력한 실제 RUN_DIR를 지정한다.
python data/krei_monthly/analyzer.py --collection data/krei_monthly/metadata/collect_20261117T125343564705Z --workers 3
python data/krei_monthly/test_pipeline.py
```

네트워크가 차단된 샌드박스에서는 수집 명령에 외부 HTTPS 권한이 필요하다. 추출 명령은 로컬 파일과 로컬 OCR만 사용한다. PyMuPDF는 thread-safe하지 않으므로 PDF 분석은 별도 프로세스 최대 3개로 실행한다. HTTP 요청은 최대 동시 3개이며, 일시적 오류는 최대 3회 재시도한다. 400/401/403/404/410은 반복하지 않고 기록한다.

`collector.py bulk --refresh-known`은 기존 URL을 다시 확인하되 기존 SHA 파일을 덮어쓰지 않는다. 기본 재실행은 등록·수정 시각과 로컬 해시가 같은 PDF를 재사용한다. URL별 메타데이터, 실제 리다이렉트 결과, 응답 SHA, 시각, HTTP 상태·오류 종류·재시도 내역을 실행별로 남긴다.

## 원문 규격

사용자가 제공한 `model_comparison/ridge/v2/농업관측본부_관측월보속보_연동_v1.0_20210924.doc`를 숨김 Word 인스턴스에서 읽기 전용으로 열었다. `metadata/specification/`의 텍스트·PDF·페이지 이미지는 확인용 파생물이다. 원본 `.doc` 읽기 전후 해시는 provenance.json에 기록되어 있다. 현재 Word 출력 사본은 6페이지이며, API·요청 인자·대상 코드는 3~4페이지, 월보 XML과 PDF 주소 필드는 5페이지에 있다. 요청한 7페이지는 이 출력에서 존재하지 않는다.

API 주소는 `https://aglook.krei.re.kr/main/api/montlyReport`다. `monthlyReport`로 철자를 바꾸지 않는다. `yyyy`, `mm`, `ovr_item_code`, `prt_ovr_item_code`는 모두 선택사항이며, 생략하면 현재 연월을 조회한다. 과거 조회에서는 연월을 명시하고 **응답의 연월과 코드를 검증**한다. `pdf_link` 값을 다운로드 주소로 사용한다. `reg_date`는 등록일시이고 `mod_date`는 수정일시이며, 발행일로 대체하지 않는다.

| 품목 | 개별 코드 | 실제 묶음 월보 코드 | Ridge 연결 |
| --- | --- | --- | --- |
| 대파 | OVR0000000004 | OVR0000000036 양념채소 | 대파, 품종·시장 별도 확인 |
| 양파 | OVR0000000028 | OVR0000000036 양념채소 | 양파, 조생·중만생 구분 필요 |
| 마늘 | OVR0000000027 | OVR0000000036 양념채소 | 깐마늘의 관련 공급 지표. 동일 분류 아님 |
| 배추 | OVR0000000026 | OVR0000000008 엽근채소 | 배추, 작형·계절 별도 확인 |
| 무 | OVR0000000025 | OVR0000000008 엽근채소 | 무, 작형·계절 별도 확인 |

실제 품목분류 API 응답에서 위 계층을 재확인했다. 2020년 3월의 개별 코드 조회는 빈 응답이고, 묶음 코드는 PDF를 반환하므로 2개 묶음 PDF를 한 번씩 수집하고 5개 품목과 연결한다. 개별 코드가 항상 미지원이라고 단정하지 않는다.

## 파일과 검증 상태

- `raw/<sha256>.pdf`: 서버가 반환한 원본 바이트. 수정·재저장·OCR 레이어 삽입 없음.
- `metadata/collect_*/`: 요청 연월·코드, 원본 XML, HTTP 감사 기록, PDF URL·SHA·경로 manifest.
- `extracted/pages_v1/<sha256>/`: 페이지별 원래 텍스트, OCR 결과, 단어 좌표, 이미지·추출 상태. 원본 내용과 OCR 문자를 임의 교정하지 않음.
- `structured/analysis_*/`: records CSV/JSON, documents, 미추출 문장 review_segments, 실패 목록, 실행·파서 SHA. **최종 보고서가 가리키는 실행만 현재 결과로 사용한다.** 이전 실행은 추출 규칙 보강 전의 감사 이력이다.
- `audit/`: 기존 파일 보존 해시, 테스트, 원본 대조·통계, 보고서, 소량 검증 이미지.

`auto_passed`는 명확한 네이티브 텍스트 문장의 수치·기준·단위·대상 기간 규칙을 통과했다는 뜻이다. 모든 내용의 정답이나 학습 허가를 의미하지 않는다. OCR 수치는 모두 `needs_review`다. 복수 지표·조건·품종·과거 조사치가 섞여 의미 연결이 불분명한 경우 `metric`은 비우고 `metric_candidate`와 사유를 남긴다. 값이 없는 전망은 0으로 바꾸지 않는다. 지원하지 않는 표·범위형 숫자도 원문을 보존해 검토한다. 추출 성공률은 전수 수치 재현율이 아니라, 해당 품목·호에서 적어도 한 개 수치 행을 얻었는지에 대한 비율이다.

발행일이 텍스트에 명확할 때만 `publication_date`를 확정한다. OCR에서 읽은 날짜는 후보에 보관하고 확정 날짜는 NULL이다. `target_period_type=crop_year`는 연산 전망이며 임의의 월을 부여하지 않는다. 명시된 월을 발행 연도와 결합한 경우 `target_resolution`에 남기며, 과거 월·연도 경계가 모호하면 NULL이다.

`asof.py`는 공개 시점과 개정 버전 검증을 통과한 행만 예측 기준 시각 이전에 사용할 수 있게 하는 독립 함수다. 날짜만 알려진 발표는 당일 종료 후부터 허용하는 보수적 경계를 사용한다. 이는 발표 시각을 채워 넣는 것이 아니다. 현재 다운로드한 파일이 과거 시점의 원본임을 입증하지 못했으므로 전체 행은 `vintage_status=unverified_current_download`, `eligible_for_model=false`다. 실제 모델 연결과 학습은 수행하지 않았다.

DB·자동화 설계는 `DB_DESIGN.ko.md`에 있다.
