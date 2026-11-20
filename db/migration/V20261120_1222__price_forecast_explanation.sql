-- 가격 예측 설명: 7일 뒤 예측의 변수별 기여(TreeSHAP, 원 단위)와 화면 문장을 실행 단위로 저장한다.
--
-- 기여·특징값·추이는 배치가 예측에 쓴 모델과 입력을 그대로 기록한다(그 시점에 알 수 있던 값만).
-- 기준 모델(LAST_PRICE·MEAN_7)로 공개된 실행은 설명할 모델이 없어 행이 없다. 공개 조건(published_query)과는 무관하다.

CREATE TABLE price_forecast_explanation (
    model_run_id    BIGINT PRIMARY KEY REFERENCES price_model_run (id),
    horizon_days    SMALLINT       NOT NULL CHECK (horizon_days BETWEEN 1 AND 7),
    method          VARCHAR(30)    NOT NULL,
    current_price   NUMERIC(14, 2) NOT NULL CHECK (current_price > 0),
    damping         NUMERIC(8, 4)  NOT NULL,
    base_price      NUMERIC(14, 2) NOT NULL,
    predicted_price INTEGER        NOT NULL CHECK (predicted_price > 0),
    created_at      TIMESTAMP      NOT NULL DEFAULT now()
);
COMMENT ON TABLE price_forecast_explanation IS
    '예측 실행의 SHAP 설명 머리 정보. 원 단위 기여 = current_price × damping × 변화율 기여. '
    'base_price + Σ contribution ≈ predicted_price (반올림 차이 1원 미만)';
COMMENT ON COLUMN price_forecast_explanation.method IS 'XGBOOST_TREE_SHAP: XGBoost pred_contribs. 가중 결합 모델은 결합 가중치로 합침';
COMMENT ON COLUMN price_forecast_explanation.base_price IS '모델 기대값(bias)을 원으로 바꾼 값 = current_price × (1 + damping × bias)';

CREATE TABLE price_forecast_factor (
    id            BIGSERIAL PRIMARY KEY,
    model_run_id  BIGINT           NOT NULL REFERENCES price_forecast_explanation (model_run_id),
    feature       VARCHAR(40)      NOT NULL,
    feature_value DOUBLE PRECISION,
    contribution  NUMERIC(14, 4)   NOT NULL,
    history       JSONB            NOT NULL DEFAULT '[]',
    created_at    TIMESTAMP        NOT NULL DEFAULT now(),
    CONSTRAINT uk_price_forecast_factor UNIQUE (model_run_id, feature)
);
COMMENT ON TABLE price_forecast_factor IS '특징별 SHAP 기여. 특징 이름·화면 라벨·단위는 app/services/price_explanation.py FEATURES';
COMMENT ON COLUMN price_forecast_factor.feature_value IS '기준일에 모델이 받은 입력값(화면 단위 변환 전, 분율 그대로). NULL은 결측(XGBoost 결측 분기)';
COMMENT ON COLUMN price_forecast_factor.contribution IS '7일 뒤 예측가에 대한 기여(원). 인과적 영향이 아님';
COMMENT ON COLUMN price_forecast_factor.history IS '최근 90일 각 날짜를 기준일로 둔 같은 특징값 [{"date": "YYYY-MM-DD", "value": number|null}]. 7일 뒤 시점 기준으로 계산';

-- 화면 문장(요약·분류별 설명). 기준 모델 실행에도 만든다.
ALTER TABLE price_insight ADD COLUMN summary JSONB,
    ADD COLUMN summary_generator VARCHAR(20),
    ADD COLUMN summary_model VARCHAR(60),
    ADD COLUMN summary_prompt_version VARCHAR(20);
ALTER TABLE price_insight ADD CONSTRAINT ck_insight_summary_generator
    CHECK (summary_generator IS NULL OR summary_generator IN ('GEMINI', 'TEMPLATE'));
COMMENT ON COLUMN price_insight.summary IS
    '{"headline": 예측 요약 1문장, "detail": 요인 요약 1문장, "categories": {분류: 설명}}. 입력은 예측값·SHAP 분류 합계만';
COMMENT ON COLUMN price_insight.summary_generator IS 'GEMINI: LLM이 다듬음(숫자 검증 통과), TEMPLATE: 고정 문장(LLM 실패·키 없음 포함)';
