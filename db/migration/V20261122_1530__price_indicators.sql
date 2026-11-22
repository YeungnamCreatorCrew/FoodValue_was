-- 판단 보조 지표: 가격 예측과 별개로, 가격 이력에서 계산한 사실(fact)과 과거 관계 검증(evidence)을 실행 단위로 저장한다.
--
-- 지표 계열은 소매 계열(price_series.market = RETAIL) 기준이다. 도매→소매 시차 지표는 같은 품목의 도매 가격을 함께 읽는다.
-- 검증(price_indicator_validation)은 느리게 바뀌는 근거 통계, 실행(price_indicator_run)은 기준일별 카드 스냅샷이다.
-- 카드는 어떤 검증 결과를 근거로 만들었는지(validation_id)를 남긴다. 임계값이 바뀌면 spec_version을 올린다.

CREATE TABLE price_indicator_validation (
    id            BIGSERIAL PRIMARY KEY,
    series_id     BIGINT      NOT NULL REFERENCES price_series (id),
    spec_version  VARCHAR(20) NOT NULL,
    indicator_key VARCHAR(30) NOT NULL,
    verdict       VARCHAR(12) NOT NULL CHECK (verdict IN ('PASS', 'FAILED')),
    stats         JSONB       NOT NULL,
    data_start    DATE        NOT NULL,
    data_end      DATE        NOT NULL,
    validated_at  TIMESTAMP   NOT NULL DEFAULT now(),
    CONSTRAINT uk_price_indicator_validation UNIQUE (series_id, spec_version, indicator_key, data_end),
    CONSTRAINT ck_indicator_validation_range CHECK (data_start <= data_end)
);
COMMENT ON TABLE price_indicator_validation IS
    '지표 근거 검증 실행. data_end 이하의 가격만 썼다(재현성). stats = 신호 이후 비율·평소 비율·표본 수·placebo p값·기간별 일관성';

CREATE TABLE price_indicator_run (
    id           BIGSERIAL PRIMARY KEY,
    series_id    BIGINT      NOT NULL REFERENCES price_series (id),
    as_of_date   DATE        NOT NULL,
    data_date    DATE        NOT NULL,
    spec_version VARCHAR(20) NOT NULL,
    status       VARCHAR(20) NOT NULL CHECK (status IN ('SUCCESS', 'INSUFFICIENT_DATA')),
    summary      JSONB,
    created_at   TIMESTAMP   NOT NULL DEFAULT now(),
    CONSTRAINT uk_price_indicator_run UNIQUE (series_id, as_of_date, spec_version),
    CONSTRAINT ck_indicator_run_data_date CHECK (data_date <= as_of_date)
);
COMMENT ON COLUMN price_indicator_run.data_date IS '카드 계산에 쓴 마지막 관측일(as_of_date 이하)';
COMMENT ON COLUMN price_indicator_run.status IS 'INSUFFICIENT_DATA: 보여줄 카드가 없음(이력 부족). 카드 행이 없다';
CREATE INDEX idx_price_indicator_run_series ON price_indicator_run (series_id, as_of_date DESC);

CREATE TABLE price_indicator_card (
    id            BIGSERIAL PRIMARY KEY,
    run_id        BIGINT      NOT NULL REFERENCES price_indicator_run (id) ON DELETE CASCADE,
    indicator_key VARCHAR(30) NOT NULL,
    validation_id BIGINT REFERENCES price_indicator_validation (id),
    verdict       VARCHAR(12) NOT NULL CHECK (verdict IN ('FACT', 'PASS', 'CONDITIONAL')),
    state         VARCHAR(10) CHECK (state IN ('UP', 'NEUTRAL', 'DOWN')),
    fact          JSONB       NOT NULL,
    evidence      JSONB       NOT NULL DEFAULT '{}',
    chart         JSONB,
    created_at    TIMESTAMP   NOT NULL DEFAULT now(),
    CONSTRAINT uk_price_indicator_card UNIQUE (run_id, indicator_key)
);
COMMENT ON COLUMN price_indicator_card.verdict IS 'FACT 방향 주장 없는 사실, PASS 검증 통과, CONDITIONAL 조건부(추가 확인 필요)';
COMMENT ON COLUMN price_indicator_card.state IS 'UP 상승 압력·비싼 편, DOWN 하락 압력·싼 편, NEUTRAL, NULL 방향 없음';
