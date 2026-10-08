-- 앞 migration이 로컬 DB에 적용된 뒤 보완한 제약은 별도 파일로 관리한다.
ALTER TABLE price_model_run ADD CONSTRAINT ck_successful_price_run_metadata
    CHECK (status <> 'SUCCESS' OR (data_date IS NOT NULL AND model_name IS NOT NULL
        AND model_version IS NOT NULL AND quality IS NOT NULL AND metrics IS NOT NULL AND finished_at IS NOT NULL));
COMMENT ON COLUMN price_forecast.lower_price IS '예측 하한. 보정·평가 표본이 부족하면 NULL';
COMMENT ON COLUMN price_forecast.upper_price IS '예측 상한. 보정·평가 표본이 부족하면 NULL';
