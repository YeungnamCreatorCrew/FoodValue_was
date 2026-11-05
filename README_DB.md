# FoodValue 로컬 DB 가이드

로컬은 Docker로 띄운 PostgreSQL을 각자 쓰고, 운영 DB(Supabase)는 나중에 연결 주소만 바꿔서 붙입니다.
테이블은 `db/migration/` 의 SQL 파일로만 만들고 바꿉니다. `docker compose up` 하면 Flyway 컨테이너가 이 파일을 자동 실행합니다.

냉장고 OCR 선택 환경 변수는 `CLOVA_OCR_RECEIPT_URL`, `CLOVA_OCR_SECRET`입니다.
최신 스키마는 앱 테이블 25개이며 날짜 기반 migration도 포함합니다.
시세 조회·예측 배치는 [시세 가이드](README_PRICES.md)를 참고합니다.
냉장고 동작과 설정은 [냉장고 API 가이드](README_FRIDGE.md)를 참고합니다.

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
- `JWT_SECRET_KEY` (32자 이상 무작위 문자열. 생성: `python -c "import secrets; print(secrets.token_urlsafe(48))"`)

이미지 저장소(S3 API) 변수. 로컬은 Docker MinIO, 운영은 Supabase Storage의 S3 연결 정보로 값만 바꿉니다.

- `S3_ENDPOINT_URL` (로컬 `http://localhost:9000`, Supabase `https://<프로젝트>.supabase.co/storage/v1/s3`)
- `S3_REGION` (로컬 `us-east-1`, Supabase는 프로젝트 리전)
- `S3_BUCKET`
- `S3_ACCESS_KEY`, `S3_SECRET_KEY` (로컬 MinIO 루트 계정을 겸함. 비밀번호는 8자 이상)
- `S3_PUBLIC_BASE_URL` (업로드한 파일을 읽는 공개 주소. 로컬 `http://localhost:9000/<버킷>`, Supabase `https://<프로젝트>.supabase.co/storage/v1/object/public/<버킷>`)

로컬 MinIO는 `docker compose up -d`로 함께 뜨고 버킷이 자동 생성됩니다(읽기 공개). 웹 콘솔은 http://localhost:9001 입니다.

가격 예측 Open API 변수. 수집 파이프라인만 사용하며 API 서버는 읽지 않습니다. 자세한 내용은 [시세 가이드](README_PRICES.md#외부-원천-통합)를 참고합니다.

- `KAMIS_CERT_KEY`, `KAMIS_CERT_ID`
- `DATA_GO_KR_SERVICE_KEY`

앞으로 API 키 등이 추가되면 이 목록에 변수 이름을 더합니다.

`postgres`가 뜬 뒤 `flyway` 컨테이너가 테이블 25개(`flyway_schema_history` 제외)를 만들고 종료됩니다. 잘 됐는지는 로그로 확인합니다.

```bash
docker compose logs flyway    # 현재 SQL 파일 전체 적용 확인 (V1~V3 + 날짜 기반 V 파일)
```

새 V 파일이 추가되면 `docker compose run --rm flyway` 로 다시 실행하면 아직 안 돌린 파일만 적용됩니다.


DBeaver/DataGrip 접속 정보: host `localhost`, port `.env`의 DB_PORT, DB/계정/비밀번호는 `.env` 값.

## 스키마 규칙

1. 테이블 생성·변경은 `db/migration/` 의 SQL 파일로만 합니다. DB 툴이나 Supabase 화면에서 직접 바꾸지 않습니다.
2. 적용된 V 파일은 수정하지 않습니다 (V1~V3 포함). 변경은 새 V 파일을 추가합니다.
   - V4부터 파일 이름은 `V{YYYYMMDD}_{HHMM}__설명.sql` 입니다. 예: `V20261006_1430__add_fridge_memo.sql`. 번호 충돌을 막기 위해서입니다.
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

- KAMIS price_code 형식(품목-품종-등급 조합): KAMIS는 품목·품종·등급 코드를 조합해야 특정 상품 시세가 나옵니다. 하나의 문자열로 어떻게 합칠지 정합니다 (예: `품목-품종-등급`).
- `price_daily.region` 값: KAMIS 지역 코드 → `NATIONAL`, `SEOUL`, `DAEGU` ... 대응표.
- 시세 적재 범위: 운영 DB(Supabase 무료 플랜)는 용량이 작으므로 지역 수와 기간을 먼저 정합니다.

## 운영 DB(Supabase)로 옮길 때

운영 서버의 `DATABASE_URL`을 Supabase 주소로 바꾸고, 같은 SQL 파일을 Flyway로 Supabase에 한 번 실행합니다.

```bash
docker run --rm -v ./db/migration:/flyway/sql:ro flyway/flyway:12-alpine \
  -url="jdbc:postgresql://<supabase-host>:5432/postgres" -user="<user>" -password="<password>" migrate
```
Direct connection이 안 붙으면 Supabase 대시보드 Connect 메뉴의 Session pooler 주소를 사용합니다.
