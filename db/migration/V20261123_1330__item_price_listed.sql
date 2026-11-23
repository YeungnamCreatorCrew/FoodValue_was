-- 시세 목록에 보일 품목인지 구분한다.
-- 배추·무는 KAMIS가 작형(월동·봄·고랭지·가을)별 품종 코드로만 제공해서, 작형마다 원본 품목·계열을 따로 둔다(기준서 §2.1).
-- 그 원본 품목은 목록·검색에 나오지 않아야 하므로 FALSE로 두고, 이어 붙인 계열을 가진 배추·무가 목록에 나온다.
ALTER TABLE item ADD COLUMN is_price_listed BOOLEAN NOT NULL DEFAULT TRUE;
COMMENT ON COLUMN item.is_price_listed IS '시세 목록·검색 노출 여부. 작형별 원본 품목(예: 배추(월동))은 FALSE';
