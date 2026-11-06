-- 가격 예측 중심 스키마 4: 실제 동작과 달랐던 주석을 바로잡는다.

COMMENT ON TABLE exchange_rate_daily IS
    '일별 환율(ECOS 731Y001 매매기준율). 예측 모델 MACRO 묶음의 FX 특징(원/미국달러 7·28일 변화율)으로 쓴다';
COMMENT ON COLUMN calendar_day.is_market_closed IS
    'KAMIS 가격 미조사일(토·일·모든 공휴일). 이날 가격 결측은 정상. 실제 도매시장 휴장일과는 다를 수 있다';
COMMENT ON COLUMN calendar_day.day_of_week IS 'ISO 요일: 1 월 ~ 7 일 (Python date.isoweekday)';
COMMENT ON TABLE weather_daily IS
    '전국 날씨: ACTUAL은 ASOS 전국 관측소(app/collectors/data_go_kr.py NATIONAL_STATIONS) 단순 평균, '
    'FORECAST는 단기예보 17개 시·도 대표 격자 평균(최신 발표로 덮어씀). 극한 기상 기준값은 app/core/constants.py';
COMMENT ON TABLE external_observation IS
    '기관별 원천 관측·예보·통계와 수정 이력. 같은 원천 키의 여러 버전 중 최신 수집본을 쓴다. '
    '공표 시각을 주지 않는 원천(publication_status=UNKNOWN)은 app/services/exogenous.py의 공개지연 규칙으로 과거 시점을 재현한다';
COMMENT ON COLUMN price_model_run.quality IS
    'VALIDATED: 선택 구간에서 뽑힌 학습 모델이 최종 평가 구간에서도 기준 모델(LAST_PRICE·MEAN_7)을 이김, BASELINE: 기준 모델 사용. UNVALIDATED는 현재 코드에서 쓰지 않음';
