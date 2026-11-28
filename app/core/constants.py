"""서비스 기준값. 임의로 흩어 쓰지 말고 이 파일 한 곳에서만 바꾼다."""

PAGE_MAX_SIZE = 50
ID_MAX = 2**63 - 1  # BIGINT 상한. 넘는 경로 ID는 DB 오류(500) 대신 입력 검증(400)으로 거른다

# CORS: 웹 프론트가 다른 origin에서 호출할 때 허용할 주소. 운영 값은 .env의 CORS_ORIGINS(쉼표 구분)
CORS_DEFAULT_ORIGINS = ["http://localhost:3000", "http://localhost:5173"]
GEMINI_TIMEOUT_SECONDS = 30

HEAT_MAX_TEMP = 33.0  # 폭염: 일 최고 33℃ 이상
HEAVY_RAIN_MM = 80.0  # 호우: 일 강수 80mm 이상
COLD_MIN_TEMP = -12.0  # 한파: 일 최저 -12℃ 이하

# 판단 보조 지표 (docs/INDICATORS_API_DESIGN.md, 초안: 임계값은 팀 합의 전)
LEAD_WHOLESALE_MOVE = 0.05  # 도매 2주 변화율이 ±5% 이상이면 '움직임'
LEAD_RETAIL_MOVE = 0.01  # 소매 2주 뒤 변화가 ±1% 넘어야 상승·하락으로 센다(그 안은 보합)
LEAD_LAG_WEEKS = 2  # 도매 변화를 보는 기간(주)
LEAD_AHEAD_WEEKS = 2  # 소매 결과를 보는 기간(주)
LEAD_MIN_WEEK_OBS = 2  # 주 평균을 만들 최소 관측일 수
LEAD_PLACEBO_P = 0.05  # 순환 이동 placebo p값이 이 이하여야 PASS
LEAD_SPLIT_DATE = '2023-01-01'  # 두 기간 일관성 확인 경계 (2016~22 / 2023~)

SEASONAL_NORMAL_YEARS = 5  # 평년 = 과거 5개 연도의 같은 구간 평균
SEASONAL_BAND = 0.10  # 평년 대비 ±10% 밖이면 싼 편·비싼 편 (초안)
SEASONAL_WINDOW_DAYS = 28  # 비교 구간: 기준일까지 최근 28일 vs 과거 연도의 같은 28일
SEASONAL_MIN_WINDOW_OBS = 10  # 구간의 관측일이 이보다 적으면 그 구간은 쓰지 않고, 이번 구간이면 방향을 말하지 않는다

INDICATOR_SPEC_VERSION = 'ind-v3'  # 지표 규칙·임계값이 바뀌면 올린다(과거 스냅샷은 그대로 둔다)
INDICATOR_REVALIDATE_DAYS = 31  # 마지막 검증의 data_end가 기준일보다 이만큼 오래되면 다시 검증한다
INDICATOR_STALE_DAYS = 7  # 지표 기준일이 오늘보다 이만큼 넘게 지났으면 STALE
INDICATOR_CHART_WEEKS = 26  # 도매·소매 지수 차트 길이

# 가격 지표(예측 모델·외부변수와 무관, 가격 이력만으로 만드는 사실 카드)
STATS_WINDOW_DAYS = 365  # 가격 위치·격차·변동성의 '평소'를 보는 기간
STATS_MIN_OBS = 120  # 위 기간에 관측이 이보다 적으면 카드를 만들지 않는다
POSITION_LOW = 0.25  # 1년 분포에서 이 아래면 싼 편
POSITION_HIGH = 0.75  # 이 위면 비싼 편
VOLATILITY_WINDOW_DAYS = 28  # 변동폭을 재는 구간(그 구간 최고-최저 ÷ 평균)
VOLATILITY_MIN_OBS = 10  # 구간 관측이 이보다 적으면 그 구간은 쓰지 않는다

# 수준 신호(배수·1년 위치) 검증: 기준일까지의 최근 52주 분포에서 하위/상위 25%를 신호로 본다(미래 분포 사용 금지)
LEVEL_WINDOW_WEEKS = 52
LEVEL_MIN_WEEKS = 40
LEVEL_LOW = 0.25
LEVEL_HIGH = 0.75
LEVEL_AHEAD_GRID = (1, 2, 3, 4)  # 결과를 보는 기간(주) 탐색 범위. placebo도 같은 탐색을 한다
LEVEL_MIN_VALIDATION_WEEKS = 156  # 수준 신호를 검증하려면 주 평균이 이만큼(3년) 필요
LEVEL_WEAK_RATIO = 0.5  # 한쪽 edge가 다른 쪽의 이 비율보다 작으면 그쪽은 '근거가 약함'
LEVEL_OVERLAP_CORR = 0.5  # 배수 백분위와 도매 2주 변화의 상관(절댓값)이 이 이상이면 도매 흐름과 겹친다고 표시

# DB 세션 타임존(app.core.db.make_engine이 접속마다 설정). 날짜 계산(app.core.dates.today)과 같은 기준
DB_TIMEZONE = 'Asia/Seoul'
# API 서버 DB 연결 풀. 공유 DB(Supabase) Session pooler는 프로젝트 전체 동시 접속을 15개로 제한한다(무료 기본값).
# 넘치면 접속 자체가 실패하므로 넘침(max_overflow) 없이 고정 크기로 두고, 몰린 요청은 풀에서 기다리게 한다.
DB_POOL_SIZE = 5
DB_POOL_TIMEOUT_SECONDS = 30
