-- 배추·무 이어 붙인 계열(기준서 §2.3)을 서비스 DB에 둔다.
-- KAMIS는 배추·무를 작형(월동·봄·고랭지·가을)별 품종 코드로만 준다. 작형별 원본 계열은 그대로 두고(source='KAMIS'),
-- 이어 붙인 계열은 source='MERGED'로 따로 만든다. 값은 app.merged_series가 작형별 price_daily로 다시 계산한다(원본 관측 없음).
-- MERGED 계열은 KAMIS 수집 대상이 아니다(collection_service·warehouse_service가 KAMIS 계열만 읽는다).
ALTER TABLE price_series DROP CONSTRAINT ck_price_series_source;
ALTER TABLE price_series ADD CONSTRAINT ck_price_series_source CHECK (source IN ('KAMIS', 'MERGED'));
COMMENT ON COLUMN price_series.source IS 'KAMIS: 원본 계열. MERGED: 작형별 KAMIS 계열을 이어 붙여 만든 계열(배추·무)';
