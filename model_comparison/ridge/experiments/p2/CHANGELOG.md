# Ridge p2 변경·실패 이력

## ridge-p2-v1 / ridge-p2-median-v1 — 2026-11-11 준비

- 기존 v1과 공통 도구를 보존하고 p2 클래스·6개 설정·명시적 실행 wrapper를 추가했다.
- 중앙값을 현재 학습 표본에서만 구하고 전체 결측 열을 다음 fit까지 0으로 고정한다.
- 실패한 refit 후 이전 모델이 남지 않도록 fit 시작 시 모델을 무효화한다.
- 공통 평가기 phase/config 규칙을 확인해 외부변수 없는 p2 CONTROL을 별도 ID로 준비했다.
- XGBoost p2 예제의 config_id/metrics 존재 검사보다 엄격한 전체 SHA·격자·공식 재평가 검증을 추가했다.
- 단독 5개가 모두 검증되기 전에는 조합을 고르지 않는다. 부분 범위 결과를 p1과 비교하지 않는다.
- 실행/실패/중단/재사용 기록과 실제 특징·중앙값·계수·상관 진단을 새 시도별로 보존한다.

## 준비 테스트 실행 1 — 환경 경로 오류

명령: `.venv\Scripts\python.exe -m pytest tests/test_ridge_p2.py -q --basetemp .tmp/ridge-p2-tests`

결과: **21 passed, 15 errors**. 15건은 `.tmp` 상위 경로가 없는 상태에서 pytest가 basetemp를 생성하려 하여
WinError 3을 낸 fixture 준비 오류다. 모델 assertion 실패는 없었다. 실제 p1 스냅샷의 한 기준일·두 계열
예측 일치성도 통과했다. 원본 파일이나 평가 규칙의 문제가 아니므로 이를 변경하지 않았다.
수정: 존재하는 OS 임시 디렉터리 아래 매 실행마다 새로운 basetemp를 사용한다.
후속 로그와 발견된 코드 수정은 verification 및 아래 후속 항목으로 기록한다.

## 준비 테스트 실행 2 — Windows 문자 인코딩 경고

결과: **36 passed, 7 warnings** (26.90초). 하위 프로세스의 UTF-8 출력 일부를 Windows 기본 CP949로
해석하는 subprocess reader thread에서 UnicodeDecodeError 경고가 발생했다. 공통 환경 기록과 Git
한글 diff 감사가 불완전해질 수 있으므로 경고를 숨기지 않고 처리했다.
수정: p2 CLI는 Windows에서 UTF-8 모드가 아니면 `python -X utf8 -m model_comparison.ridge.p2`로
즉시 재진입한다. p2 자체 Git 조회는 bytes를 받아 UTF-8로 명시적으로 해석한다. 공통 도구는 수정하지 않았다.
재현 테스트는 Python UTF-8 모드와 `-W error`로 실행한다. 로그: verification/test-attempt-02.log.

## 준비 테스트 실행 3·4 — 최종 회귀 확인

- 실행 3: Ridge 및 공통 Loader·평가기·스냅샷·기준서 검사 **77 passed**, 경고 없음 (50.44초).
- 추가 회귀: 5개 단독 후 유효 조합의 순서·단독 대비 차이, 완료 봉인의 필수 파일,
  한글 Git diff의 UTF-8 해석을 확인했다.
- 실행 4: **80 passed**, 실패·경고·skip 없음 (53.70초), `-W error` 사용.
- 공통 검사기가 완전한 날짜 한 묶음이 빠진 격자를 놓칠 수 있어 wrapper가 정확한 전체 격자를
  별도로 검증한다. 위조 metrics도 공식 재계산으로 거부하는 회귀 테스트가 통과했다.
- 공통 도구의 FIT_FAILED가 있어도 파일 형식상 실행은 끝날 수 있으므로 wrapper는 해당 실행을
  FAILED로 보존하고 재사용하지 않는다. 이 경로도 합성 데이터 테스트로 확인했다.
- 읽기 전용 사전 점검: 스냅샷 검사·공식 p1 형식 검사 통과, 10계열·244 Validation 기준일 확인.
- 원본 191개 파일 SHA-256 재검증: 변경·누락 0. 공식 실행 폴더 추가·학습·Git 게시 작업 없음.

## 기존 p1 해시의 줄바꿈 차이

v1 문서에 기록된 metrics SHA-256은 LF 기준 `9c3e399dc7dc882b1e1e051e7ddf4a608a928234de79ef1e4f1e4f4c24535902`다.
현재 Windows 체크아웃 파일의 실제 바이트 SHA-256은 `d50f1601e9d6b680fc0fa72b4725a2388d557d62b393f0c5001f959428be7775`다.
읽은 바이트를 메모리에서만 CRLF→LF로 정규화하면 문서의 해시와 일치한다. 원본 파일을 정규화하거나
재작성하지 않았다. 이번 보존 검사는 작업 전후 실제 바이트 해시를 사용한다.

## 이후 변경 기록 규칙

각 변경은 시각, 버전·SHA, 변경 이유, 예상 영향, 선행 실패·실행 ID, 수정 전후 테스트 결과를 적는다.
모델/전처리 변경 후 이전 완료 결과를 재사용하지 않는다. 원본 실패 시도와 로그를 삭제하지 않는다.
