# FoodValue DB 가이드

팀은 **공유 DB(Supabase)** 하나를 같이 봅니다(2026-11-28~). 로컬 Docker PostgreSQL은 테스트·실험용입니다. 공유 DB 운영 규칙은 아래 [공유 DB](#공유-dbsupabase) 절을 봅니다.
테이블은 `db/migration/` 의 SQL 파일로만 만들고 바꿉니다. `docker compose up` 하면 Flyway 컨테이너가 이 파일을 자동 실행합니다.

최신 스키마는 앱 테이블 26개이며 날짜 기반 migration도 포함합니다.
시세 조회·예측 배치는 [시세 가이드](README_PRICES.md)를 참고합니다.

## 예측 외부 원천 스키마 추가 (2026-11-03)

`V20261103_1611__external_prediction_sources.sql`에서 다음 3개 테이블을 추가했습니다.
기존 테이블·컬럼은 변경하지 않습니다.

| 테이블 | 용도 |
| --- | --- |
| `external_collection_run` | 기관·자료별 수집 성공/실패, 요청·수신·삽입 건수와 실행 시점 |
| `external_observation` | 지역·관측소별 원천 값, 단위, 대상 기간, 예보 발표·실제 공표·수집 시각과 수정 버전 |
| `item_weather_station` | 품목과 주산지 후보·관측소 연결, 검증 상태와 확인된 비중 |

동일 원천 키와 내용 해시는 중복 저장하지 않고, 내용이 달라지면 새 버전으로 보존합니다.
공표 시점을 확인하지 못한 자료는 `UNKNOWN`으로 보관합니다. 주산지 연결의 미확인 비중은 `NULL`입니다.
`item_id`는 기존 `item`을 참조하지만 특정 품목 ID나 실데이터를 migration에 넣지 않았습니다.

이 변경이 포함된 브랜치를 받은 뒤 다음 명령으로 기존 DB에 적용합니다. DB 초기화는 필요하지 않습니다.

```bash
docker compose up -d postgres
docker compose run --rm flyway
```

이 migration은 테이블 구조만 공유합니다. API 키, 수집 원본과 로컬 DB 데이터는 포함하지 않습니다.

## 처음 한 번

1. `.env` 파일을 프로젝트 루트에 둡니다. `.env`는 Git에 올리지 않고 팀원끼리 직접 전달합니다.
2. DB를 실행합니다.

```bash
docker compose up -d          # PostgreSQL 실행
```

`.env`에 들어가는 변수 이름은 아래와 같습니다. 값은 적지 않습니다.

- `DB_NAME`
- `DB_USER`
- `DB_PASSWORD`
- `DB_PORT`
- `DATABASE_URL`
- `SUPABASE_DATABASE_URL` (공유 DB, Session pooler 주소)

가격 예측 Open API 변수. 수집 파이프라인만 사용하며 API 서버는 읽지 않습니다. 자세한 내용은 [시세 가이드](README_PRICES.md#외부-원천-통합)를 참고합니다.

- `KAMIS_CERT_KEY`, `KAMIS_CERT_ID`
- `DATA_GO_KR_SERVICE_KEY`
- `KOSIS_API_KEY`
- `ECOS_API_KEY`
- `GARAK_API_ID`, `GARAK_API_PASSWORD` (가락시장 공공데이터 신청 시 받은 발급 ID와 신청 게시글 비밀번호)

앞으로 API 키 등이 추가되면 이 목록에 변수 이름을 더합니다.

`postgres`가 뜬 뒤 `flyway` 컨테이너가 테이블 26개(`flyway_schema_history` 제외)를 만들고 종료됩니다. 잘 됐는지는 로그로 확인합니다.

```bash
docker compose logs flyway    # 현재 SQL 파일 전체 적용 확인 (V1~V3 + 날짜 기반 V 파일)
```

새 V 파일이 추가되면 `docker compose run --rm flyway` 로 다시 실행하면 아직 안 돌린 파일만 적용됩니다.


DBeaver/DataGrip 접속 정보: host `localhost`, port `.env`의 DB_PORT, DB/계정/비밀번호는 `.env` 값.

## 스키마 규칙

1. 테이블 생성·변경은 `db/migration/` 의 SQL 파일로만 합니다. DB 툴이나 Supabase 화면에서 직접 바꾸지 않습니다.
2. 적용된 V 파일은 수정하지 않습니다 (V1~V3 포함). 변경은 새 V 파일을 추가합니다.
   - V4부터 파일 이름은 `V{YYYYMMDD}_{HHMM}__설명.sql` 입니다. 예: `V20261006_1430__add_price_indicator.sql`. 번호 충돌을 막기 위해서입니다.
   - 스키마를 바꾸는 PR은 dev를 먼저 pull 받은 뒤 만들고, 합친 뒤에는 `docker compose run --rm flyway` 로 적용합니다.
3. API 서버(SQLAlchemy)는 `Base.metadata.create_all()` 을 호출하지 않습니다. 모델 클래스는 이미 있는 테이블에 맞춰 작성만 하고, 컬럼을 바꿨으면 모델도 같이 고칩니다.
4. 배치·수집 파이프라인은 테이블을 만들거나 바꾸지 않습니다. 데이터 조회·적재 및 시세 예측 결과의 원자적 교체만 수행합니다.
5. DB 접속 주소는 코드에 쓰지 않고 `.env`의 `DATABASE_URL`에서 읽습니다.

### 스키마 바꾸는 순서

1. DBeaver나 psql에서 `ALTER`를 직접 쳐보며 실험해도 됩니다. 내 로컬 DB라 자유롭게 해도 됩니다.
2. 원하는 형태가 되면 성공한 SQL을 새 V 파일로 저장합니다.
3. `docker compose down -v && docker compose up -d` 로 DB를 초기화해서, 파일만으로 같은 결과가 나오는지 확인합니다.

3번을 안 하면 직접 만든 컬럼과 V 파일이 겹쳐서 Flyway가 오류를 냅니다.

## 팀 합의가 필요한 것

- (정함, `V20261106_1700`) KAMIS 코드는 `price_series`의 `item_code`·`kind_code`·`rank_code` 세 컬럼으로 나눠 저장합니다. 품목 × 시장(소매·도매)마다 계열 하나.
- (정함, `V20261106_1700`) 지역은 전국만 씁니다. `price_daily.region` 컬럼은 없앴습니다.
- 시세 적재 범위: 운영 DB(Supabase 무료 플랜)는 용량이 작으므로 지역 수와 기간을 먼저 정합니다.

## 공유 DB(Supabase)

2026-11-28에 로컬 기준 덤프(`foodvalue_base_20261128.dump`, 가격 11-27까지·예측 11-28 기준)를 복원해 시작했습니다. 서버는 배포하지 않고 각자 로컬에서 띄우되, DB만 같이 봅니다.

**접속**
- Supabase 대시보드 → Connect → Direct → **Session pooler**(포트 5432) 주소를 씁니다.
  - Transaction pooler(6543)는 쓰지 않습니다. 배치의 계열별 잠금(`pg_try_advisory_lock`)이 깨집니다.
  - Direct connection은 무료 플랜에서 IPv6 전용이라 붙지 않을 수 있습니다.
- `.env`에는 두 줄을 둡니다. 앞부분은 `postgresql+psycopg://`입니다(psycopg 3).
  - `SUPABASE_DATABASE_URL=postgresql+psycopg://postgres.<프로젝트>:<비밀번호>@<pooler 호스트>:5432/postgres`
  - `DATABASE_URL`: 서버를 공유 DB로 띄울 때는 위와 같은 값, 테스트를 돌릴 때는 로컬 DB
- 접속 정보는 `.env` 파일로 직접 전달합니다. 메신저·Git에 붙이지 않습니다.

**규칙**
1. **migration은 머지 후 담당자 1명만** 적용합니다. `scripts/flyway_shared.sh info`로 상태를 보고 `scripts/flyway_shared.sh migrate`로 적용합니다(`.env`의 `SUPABASE_DATABASE_URL`을 읽음).
2. **수집·예측 배치는 담당자 1명이 하루 1회** 공유 DB에 돌립니다.
   ```bash
   DATABASE_URL="$SUPABASE_DATABASE_URL" FOODVALUE_PRICE_MODEL=v2 uv run --extra prices python -m app.price_pipeline
   DATABASE_URL="$SUPABASE_DATABASE_URL" uv run python -m app.indicator_batch --item-id <품목>   # 대파·양파·깐마늘·배추·무
   ```
   여러 명이 돌려도 계열 잠금 때문에 깨지지는 않지만, 같은 날 실행이 중복으로 쌓입니다.
3. **테스트(`FOODVALUE_TEST_POSTGRES=1`)와 실험은 로컬 DB에서만** 합니다. 테스트는 `DATABASE_URL`에 행을 넣고 지웁니다.
4. 스키마는 공유 DB에서 직접 바꾸지 않습니다. 로컬에서 V 파일로 만들고 PR → 머지 → 1번 순서로 적용합니다.

**알아 둘 점**
- **타임존**: Session pooler는 DB·계정 기본값(`ALTER DATABASE/ROLE ... SET timezone`)과 접속 옵션을 무시하고 UTC로 접속합니다. 그래서 코드는 `app.core.db.make_engine`이 접속마다 `SET TIME ZONE 'Asia/Seoul'`을 실행합니다. DBeaver·psql로 직접 볼 때는 `now()`가 UTC로 나옵니다.
- **정렬**: 공유 DB는 로컬(en_US.utf8)과 정렬 규칙이 달라 한글 이름순이 가나다순으로 나옵니다.
- **용량**: 무료 플랜 500MB. 시작 시점 217MB이고 대부분 `external_observation`(원본 수집)입니다.
- **일시 정지**: 무료 프로젝트는 1주일 동안 접속이 없으면 멈춥니다. 대시보드에서 다시 켭니다.
