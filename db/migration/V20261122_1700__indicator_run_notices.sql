-- 지표 실행에서 카드를 만들지 않은 이유(예: 작형 전환 직후라 도매 흐름·변동폭을 잠시 비교하지 않음)를 화면에 알리려고 남긴다.
-- notices = [{"key": "WHOLESALE_LEAD", "reason": "KIND_SWITCH", "text": "..."}]
ALTER TABLE price_indicator_run ADD COLUMN notices JSONB NOT NULL DEFAULT '[]';
COMMENT ON COLUMN price_indicator_run.notices IS '카드를 만들지 않은 이유 목록. 카드 행이 없는 이유를 사용자에게 설명하는 용도(예측·검증 값이 아님)';
