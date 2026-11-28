-- 같은 계열·기준일에 여러 예측 모델 트랙을 함께 저장한다(API ?model=ENSEMBLE|STRUCT).
-- ENSEMBLE: 기본 공개 트랙. v2 앙상블 실행과, v2 대상이 아닌 계열의 v5 실행(LAST_PRICE 포함)이 여기에 들어간다. 기존 실행도 모두 ENSEMBLE.
-- STRUCT: 구조적 가격 전달 모델(PR #71) 실행. v2 대상 계열(대파·양파·깐마늘·배추·무 소매·도매)에만 만든다.
ALTER TABLE price_model_run ADD COLUMN model_track VARCHAR(20) NOT NULL DEFAULT 'ENSEMBLE';
ALTER TABLE price_model_run ADD CONSTRAINT ck_price_model_run_track CHECK (model_track IN ('ENSEMBLE', 'STRUCT'));
DROP INDEX IF EXISTS idx_price_model_run_series;
CREATE INDEX idx_price_model_run_series ON price_model_run (series_id, model_track, base_date DESC, id DESC);
COMMENT ON COLUMN price_model_run.model_track IS '예측 모델 트랙. 공개 실행은 계열 × 트랙마다 최신 성공 실행';
