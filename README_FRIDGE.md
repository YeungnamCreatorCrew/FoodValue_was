# 냉장고 API 가이드

이 문서는 README의 일부이며 초기 참고 명세서보다 우선합니다.
백엔드 2명이 협업하며 우리 담당은 냉장고·시세예측입니다.

## 확정 기능

- 직접 입력·영수증 OCR 모두 사용자가 구입일을 선택합니다. 미래 구입일은 허용하지 않습니다.
- 소비기한 컬럼·추정·임박 표시를 제거합니다. 구입일 오래된 순으로 기본 정렬합니다.
- 품목 마스터에 없는 재료도 직접 이름을 입력해 등록할 수 있습니다.
- 원물/가공품은 RAW/PROCESSED, 보관 위치는 FRIDGE/FREEZER/ROOM입니다.
- USE는 부분 사용, FINISH는 잔량 전체 사용, DISCARD는 부분 또는 전체 폐기입니다.
- 삭제는 소프트 삭제로 사용 이력을 보존합니다. 잔량 0은 기본 목록에서 숨깁니다.
- 모든 API는 JWT 인증이 필요하고 다른 사용자의 재료·영수증은 404입니다.
- 수정·삭제·차감·영수증 확인은 행 잠금으로 동시 요청을 직렬화합니다.
- 상세의 itemId·priceAvailable로 시세 화면 연결을 준비합니다. 시세 API는 후속 작업입니다.
- 레시피 이동·요리 완료 연동은 레시피 담당자와 협의 후 구현합니다.
- 등록량·이력 보존을 위해 단위·수량·연결 품목은 수정하지 않습니다. 잘못 등록하면 삭제 후 재등록합니다.

## 단위

지원: g, kg, ml, L, 개, 단, 모, 팩, 봉, 송이, 구. 수량은 소수점 3자리까지 지원합니다.
Decimal 응답 값은 문자열입니다.

- g는 1g, kg는 1000g으로 고정합니다.
- 개수 단위는 gramsPerUnit(등록 단위 1개당 g)을 우선합니다. 없으면 품목 기본 단위와 같은 경우에만 마스터 값을 사용합니다.
- ml/L는 입력한 무게 또는 품목 density_g_per_ml로 환산합니다. 임의로 ml=g 처리하지 않습니다.
- 등록 시 환산값을 저장해 이후 마스터 변경에 영향을 받지 않습니다.
- 무게를 수정해도 과거 사용 기록의 gramsUsed는 유지됩니다.
- purchasePrice는 최초 등록량 전체의 구입 금액(원)입니다. 차감해도 바뀌지 않습니다.

## 영양 요약

현재 남은 재료 전체를 합산해 성인 1명·1일 기준과 비교합니다.
화면에 **냉장고 보유 재료 기준**으로 표시합니다. 실제 섭취량은 아닙니다.

item_nutrition.basis는 100G(가식부 100g) 또는 100ML(100ml)입니다.
100G: 잔량 × 단위당 무게 × 가식부 비율 / 100 / 100 × 영양성분.
100ML: ml 잔량 / 100 × 영양성분. 현재 ml/L로 등록한 재료만 지원합니다.
NULL은 데이터 없음, 0은 알려진 0입니다. 가식부 비율도 임의로 100%라고 가정하지 않습니다.

| 성분 | 일일 기준 | 판정 |
| --- | --- | --- |
| 탄수화물 | 324g | 미달 LOW, 부족량 표시 |
| 단백질 | 55g | 미달 LOW, 부족량 표시 |
| 지방 | 54g | 미달 LOW, 부족량 표시 |
| 나트륨 | 2000mg | 상한 비교, 부족 표시 없음 |
| 당류 | 100g | 상한 비교, 부족 표시 없음 |
| 콜레스테롤 | 300mg | 상한 비교, 부족 표시 없음 |

서비스 공통 [1일 영양성분 기준치](https://www.law.go.kr/LSW/flDownload.do?bylClsCd=110201&flSeq=147344939&gubun=)를 사용하며 개인별 권장량을 계산하지 않습니다.
정보가 누락되면 complete=false와 성분별 missingIngredientIds를 반환합니다.
누락이 있고 합계가 기준 미만이면 INCOMPLETE, shortfall=null입니다.
알려진 합계만으로 기준을 넘으면 누락이 있어도 SUFFICIENT/EXCESS를 반환할 수 있습니다.

## API

기본 경로 /api/v1/fridge. JSON은 camelCase, 목록 쿼리는 snake_case입니다.
page=1, size=20(최대 50). sort는 purchased(기본), name, newest입니다.

| 메서드 | 경로 | 기능 |
| --- | --- | --- |
| GET | /catalog?keyword=대파 | 품목 이름·별칭 검색 |
| GET | /items | 목록: storage, food_type, keyword, sort, include_empty |
| POST | /items | 직접 등록 |
| GET/PATCH/DELETE | /items/{id} | 상세·수정·삭제 |
| POST | /items/{id}/consume | 사용·다 먹음·폐기 |
| GET | /items/{id}/usage | 사용 이력, 페이지네이션 |
| GET | /summary | 보관 위치별 개수, 가장 오래된 구입일 |
| GET | /nutrition | 보유 재료 영양 요약 |
| POST | /receipts | 영수증 OCR 업로드 |
| GET | /receipts/{id} | OCR 후보 조회 |
| POST | /receipts/{id}/confirm | 확인한 재료 일괄 등록 |

직접 등록 예시:

```json
{
  "displayName": "두부", "quantity": "1", "unit": "모",
  "storage": "FRIDGE", "foodType": "PROCESSED", "purchasedAt": "2026-10-07",
  "gramsPerUnit": "300", "purchasePrice": 2500
}
```

영양 계산은 itemId로 연결한 품목의 영양정보가 필요합니다. 위 예시는 연결 없는 직접 등록입니다.
사용: {"reason":"USE","amount":"0.5","usedAt":"2026-10-07"}.
FINISH는 amount 생략, DISCARD도 생략하면 잔량 전체입니다.
PATCH 필드: displayName, storage, foodType, purchasedAt, gramsPerUnit, purchasePrice.
입력 오류 400, 미인증 401, 미존재/타인 소유 404, 영수증 중복 확인 409입니다.

## 영수증 OCR

초기 기술명세서의 CLOVA 영수증 OCR을 사용합니다.
[공식 요청·응답 문서](https://api.ncloud-docs.com/docs/en/ai-application-service-ocr-ocrdocumentocr-receipt).
환경 변수: CLOVA_OCR_RECEIPT_URL(HTTPS 영수증 전용 invoke URL), CLOVA_OCR_SECRET.
미설정 시 업로드만 503이며 직접 등록은 가능합니다.

1. POST /receipts: multipart file(PNG/JPEG, 5MB 이하), 선택 purchased_at.
2. 구입일: 사용자 입력 → 인식 날짜 → 서울 기준 오늘. 인식된 미래 날짜는 오늘로 대체합니다.
3. 이름·수량·금액·신뢰도와 정확히 일치하는 마스터/별칭을 반환합니다. 무게는 추정하지 않습니다.
4. 사용자가 비식품 행을 제외하고 단위·무게·구입일을 확인합니다. 모든 후보는 needsReview=true입니다.
5. confirm 요청은 {"items":[직접 등록 객체, ...]}입니다. 재료별 구입일을 개별 수정할 수 있습니다.
6. 최대 100개 재료를 한 트랜잭션으로 저장합니다. 중복 확인은 409입니다.

원본 이미지와 카드번호·결제정보 원문은 보관하지 않고 등록용 후보만 저장합니다.
API 키 발급과 실제 영수증 품질 검증은 실환경 설정 후 진행합니다.

## 스키마·검증

V20261007_1830__fridge_management.sql을 추가했습니다. 기존 V 파일은 수정하지 않습니다.
이 migration까지 fridge_receipt 포함 앱 테이블은 21개입니다. 이후 시세 migration까지의 최신 개수는 README_DB.md를 참고합니다.

```bash
docker compose run --rm flyway
uv run --group dev pytest tests/test_fridge.py
```

냉장고 테스트는 임시 SQLite와 대체 인증을 사용하며 실제 DB를 변경하지 않습니다.
PostgreSQL 검증은 별도 명령으로 실행합니다(로컬 DB 주소만 허용).

```powershell
$env:FOODVALUE_TEST_POSTGRES='1'
uv run --group dev pytest tests/test_fridge_postgres.py
```

실제 JWT 인증·CRUD·영양 합산·동시 차감·영수증 중복 확인을 검증합니다.
빈 임시 스키마에 전체 SQL을 적용하고 롤백해 재현성을 확인합니다.
생성한 테스트 사용자·재료·영수증만 정리하며 기존 데이터는 초기화하지 않습니다.
JWT/S3 설정이 없으면 테스트 프로세스에서만 임시 값을 사용합니다.
실제 API 서버 실행에는 `.env`의 JWT_SECRET_KEY와 S3 변수 설정이 필요합니다.
실제 OCR 서비스 호출은 CLOVA 설정 후 별도로 검증해야 합니다.
