-- 가격 예측 중심 스키마 2: 예측·가이드를 실행(price_model_run) 단위로 저장한다.
--
-- 이전에는 (품목, 기준일, 목표일)이 유일해서 같은 날 다시 실행하면 앞 실행의 예측을 지우고 덮어썼다.
-- 이제 실행마다 예측 7개와 가이드 1개가 따로 남고, 공개는 기존처럼 최신 성공 실행을 고른다.
-- 품목·기준일은 실행에서 읽으므로 price_forecast·price_insight에서 뺀다.
-- 소매·도매 계열을 모두 예측하므로 실행은 품목이 아니라 가격 계열(price_series)을 가리킨다.

ALTER TABLE price_model_run ADD COLUMN series_id BIGINT REFERENCES price_series (id);
UPDATE price_model_run r SET series_id = s.id FROM price_series s WHERE s.item_id = r.item_id AND s.market = 'RETAIL';
DELETE FROM price_forecast WHERE model_run_id IN (SELECT id FROM price_model_run WHERE series_id IS NULL);
DELETE FROM price_insight WHERE model_run_id IN (SELECT id FROM price_model_run WHERE series_id IS NULL);
DELETE FROM price_model_run WHERE series_id IS NULL;
ALTER TABLE price_model_run ALTER COLUMN series_id SET NOT NULL;
DROP INDEX IF EXISTS idx_price_model_run_item;
ALTER TABLE price_model_run DROP COLUMN item_id;
CREATE INDEX idx_price_model_run_series ON price_model_run (series_id, base_date DESC, id DESC);

DELETE FROM price_forecast WHERE model_run_id IS NULL;
DELETE FROM price_insight WHERE model_run_id IS NULL;

ALTER TABLE price_forecast DROP CONSTRAINT uk_price_forecast, DROP CONSTRAINT ck_forecast_horizon;
ALTER TABLE price_forecast ALTER COLUMN model_run_id SET NOT NULL;
ALTER TABLE price_forecast DROP COLUMN item_id, DROP COLUMN base_date;
ALTER TABLE price_forecast ADD CONSTRAINT uk_price_forecast UNIQUE (model_run_id, target_date);
COMMENT ON COLUMN price_forecast.lower_price IS
    '예측구간 하한. 보정 구간의 절대오차 분위수로 만든 구간이며 목표 포함률은 price_model_run.metrics.nominalCoverage(현재 0.95). 표본이 부족하면 NULL';
COMMENT ON COLUMN price_forecast.upper_price IS '예측구간 상한. lower_price 참고';

ALTER TABLE price_insight DROP CONSTRAINT uk_price_insight;
ALTER TABLE price_insight ALTER COLUMN model_run_id SET NOT NULL;
ALTER TABLE price_insight DROP COLUMN item_id, DROP COLUMN base_date;
ALTER TABLE price_insight ADD CONSTRAINT uk_price_insight UNIQUE (model_run_id);
COMMENT ON COLUMN price_insight.mape IS '선택된 모델의 내부 최종 평가 구간 MAPE(%). 7개 시점 전체 평균';

