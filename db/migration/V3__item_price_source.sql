-- =====================================================================
-- FoodValue V3 : 품목별 시세 출처 (KAMIS 원물 / 참가격 가공품)
--
-- 품목 하나는 시세 출처를 하나만 가진다.
--   KAMIS  : 원물. price_code = 품목-품종-등급 조합 (형식은 팀 합의)
--   CHAMGA : 가공품. price_code = 대표 상품 1개의 코드 (예: 우유 → 서울우유 1L)
-- 둘 다 NULL 이면 시세 미제공.
-- =====================================================================

ALTER TABLE item ADD COLUMN price_source VARCHAR(10);
ALTER TABLE item RENAME COLUMN kamis_code TO price_code;
ALTER TABLE item ALTER COLUMN price_code TYPE VARCHAR(50);
ALTER TABLE item DROP CONSTRAINT uk_item_kamis_code;

-- 기존에 kamis_code 가 있던 품목은 KAMIS 로 표시
UPDATE item SET price_source = 'KAMIS' WHERE price_code IS NOT NULL;

ALTER TABLE item
    ADD CONSTRAINT ck_item_price_source CHECK (price_source IN ('KAMIS', 'CHAMGA')),
    -- 출처와 코드는 같이 채우거나 같이 비운다
    ADD CONSTRAINT ck_item_price_pair   CHECK ((price_source IS NULL) = (price_code IS NULL)),
    ADD CONSTRAINT uk_item_price_code   UNIQUE (price_source, price_code);

COMMENT ON COLUMN item.price_source IS '시세 출처: KAMIS 원물, CHAMGA 참가격 가공품. NULL 이면 시세 미제공';
COMMENT ON COLUMN item.price_code   IS '출처의 코드. KAMIS 는 품목-품종-등급, 참가격은 대표 상품 코드';
COMMENT ON COLUMN item.price_unit_label IS '시세 단위 표기. 예: 1단 · 800g, 서울우유 1L';
