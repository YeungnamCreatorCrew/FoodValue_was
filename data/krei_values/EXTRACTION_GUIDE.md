# KREI 관측월보 추출 작업 안내 (인수인계용)

2021~2024년 80호와 2026-11호(2개 묶음)는 추출·적재가 끝났다. 남은 호는 [TODO.md](TODO.md)에 있다.
추출 규칙은 [README.md](README.md)가 최우선이다(특히 "표준 결정" 절). 이 문서는 작업 순서만 적는다.

## 0. 처음 한 번: 로컬 DB 준비
```bash
git pull                                   # 이 브랜치(또는 dev에 합쳐진 뒤 dev)
docker compose up -d
docker compose run --rm flyway             # V20261117_1722__krei_report_value 적용
uv run python -m app.krei_monthly --start-year 2021   # 월보 목록·PDF·발행일 수집 (인증키 불필요, pdftotext 필요: brew install poppler)
uv run python -m app.krei_values data/krei_values/*/*.json   # 이미 추출된 83개 파일 적재 → 모두 SUCCESS 여야 함
```
- 2016-12호(4605)·2017-05호(4771)는 KREI 서버가 빈 응답을 줘서 수집이 PARTIAL로 끝날 수 있다. 2021년 이후만 받으면 상관없다.
- 적재 명령은 JSON의 `pdf_sha256`과 같은 PDF의 원본 호에만 붙는다. KREI가 PDF를 고쳐 올렸으면 "같은 PDF의 원본 호 없음"이 뜬다 → 그 호는 새 PDF로 다시 추출.

## 1. 호마다 할 일
1. PDF의 **모든 쪽을 이미지로** 읽는다(텍스트 PDF여도. pdftotext는 2단 레이아웃에서 표 칸 순서가 밀린다).
2. 실험 품목만 뽑는다.
   - 양념채소(OVR0000000036): `대파`, `양파`, `마늘` (건고추·쪽파 제외)
   - 엽근채소(OVR0000000008): `배추`, `무` (양배추·당근 제외)
3. README 규칙대로 값을 만든다. 자주 틀리는 것:
   - 문서에 적힌 숫자만. 계산 금지. 감소·하락은 음수.
   - 비교 기준(PREV_YEAR/NORMAL/PREV_MONTH) 행은 `direction`을 **문장 기준**으로 반드시 적는다("비슷"·"보합"=FLAT, 약보합=DOWN, 강보합=UP).
   - 지난달 도매가격은 **본문 문장 값**(시계열 표 값 아님).
   - 작형은 README의 **표준 표기 목록**만. 출하 경로(산지/저장) 칸은 `unmapped`.
   - "N월"의 연도는 호의 발행 연월 기준(2025-03호의 "2월 가격" → 2025-02, 2025-01호의 "12월" → 2024-12).
4. 스키마에 없는 데이터는 `unmapped`에 짧게(`item_name`, `what`, `evidence`).
5. 요약 표(마지막 쪽·2쪽·표지)의 가격 전망·면적·생산 전망 값이 본문에서 뽑은 값과 같은지 검산. 다르면 본문 우선, evidence에 요약 표기.
6. 저장: `data/krei_values/{묶음코드}/{pdf_id}.json`
   - 최상위: `source_record_key`, `pdf_sha256`(TODO.md 값), `extractor`(쓴 모델 ID, 예: `claude-opus-5-5`), `extractor_version`: `"v1"`, `values`, `unmapped`
   - UTF-8, `ensure_ascii=False`
7. 적재·검증: `uv run python -m app.krei_values data/krei_values/{묶음코드}/{pdf_id}.json` → `"status": "SUCCESS"`가 나올 때까지 JSON을 고친다(실패 메시지가 어떤 값이 왜 거부됐는지 알려준다).

형식·세밀도 예시: `OVR0000000036/8780.json`(양념채소), `OVR0000000008/8786.json`(엽근채소), 2024년 호들(`8483`, `8485` 등).

## 2. 다 끝난 뒤 확인
```bash
uv run pytest -q tests/test_krei_values.py      # 커밋된 JSON 형식 검사 포함
```
- 규칙이 애매했던 사례는 임의로 새 규칙을 만들지 말고 가장 가까운 규칙을 적용한 뒤 PR 설명에 적는다.
- Claude 등 LLM 에이전트에게 맡길 때는 이 문서와 README를 그대로 지시서로 주면 된다. 여러 에이전트를 동시에 돌릴 때는 임시 파일 폴더를 에이전트마다 분리하고, 4개 정도씩 나눠 돌린다(동시에 16개를 돌리다 사용량 한도에 걸린 적 있음).

## 3. 알려진 표기 차이 (추출 후 일괄 정리 예정, 새로 추출할 때는 README 표준대로)
- 양파 월말 재고 작형: 일부 파일 `중만생종` → 표준은 `null`
- 양파·마늘 입고(계획)량: 호마다 `STOCK` 또는 `unmapped`로 갈림
- 같은 작기 이름이 연도별로 다름: 무 `가을`/`가을일반`, 배추·무 `고랭지`/`여름` → 로더에서 연결
- 일부 준고랭지2기작 값이 `unmapped`에 있음(규칙 보강 전 추출)
- 8452: 마늘 전체 생산량(284.5천 톤)이 `난지형`으로 분류된 것으로 보임
