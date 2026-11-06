"""서비스 기준값. 임의로 흩어 쓰지 말고 이 파일 한 곳에서만 바꾼다."""

from enum import StrEnum

# 인증 (액세스 JWT + 불투명 리프레시 토큰)
JWT_ALGORITHM = "HS256"
JWT_ISSUER = "foodvalue"
JWT_AUDIENCE = "foodvalue-app"
ACCESS_TOKEN_EXPIRE_MINUTES = 60
JWT_SECRET_MIN_LENGTH = 32
REFRESH_TOKEN_EXPIRE_DAYS = 14

# 가입 입력 규칙
PASSWORD_MIN_LENGTH = 8
PASSWORD_MAX_LENGTH = 72  # argon2는 제한이 없지만 과도한 입력 방어용
NICKNAME_MIN_LENGTH = 2
NICKNAME_MAX_LENGTH = 20  # users.nickname VARCHAR(20)


# 커뮤니티 게시판
class PostCategory(StrEnum):
    """post.category CHECK 제약과 같은 값"""

    RECIPE_SHARE = "RECIPE_SHARE"  # 레시피 공유
    GROUP_BUY = "GROUP_BUY"  # 소분 모집
    SHOWOFF = "SHOWOFF"  # 요리 자랑


POST_TITLE_MAX_LENGTH = 100  # post.title VARCHAR(100)
POST_CONTENT_MAX_LENGTH = 10_000  # post.content는 TEXT라 DB 제한이 없어 서버에서 막는다
COMMENT_MAX_LENGTH = 1_000
POST_IMAGE_URL_MAX_LENGTH = 500  # post_image.url VARCHAR(500)
POST_IMAGE_MAX_COUNT = 10
SEARCH_KEYWORD_MAX_LENGTH = 100
PAGE_DEFAULT_SIZE = 20
PAGE_MAX_SIZE = 50
ID_MAX = 2**63 - 1  # BIGINT 상한. 넘는 경로 ID는 DB 오류(500) 대신 입력 검증(400)으로 거른다

# CORS: 웹 프론트가 다른 origin에서 호출할 때 허용할 주소. 운영 값은 .env의 CORS_ORIGINS(쉼표 구분)
CORS_DEFAULT_ORIGINS = ["http://localhost:3000", "http://localhost:5173"]  # 로컬 개발(React/Vite 기본 포트)

# 이미지 업로드
IMAGE_MAX_BYTES = 5 * 1024 * 1024
IMAGE_UPLOAD_PATH = "/api/v1/images"
IMAGE_REQUEST_OVERHEAD_BYTES = 64 * 1024  # 멀티파트 경계·헤더 몫. 요청 본문 상한 = 이미지 상한 + 이 값
IMAGE_KEY_PREFIX = "posts"  # 저장 경로: posts/{user_id}/{uuid}.{확장자}

# 레시피 생성 (Gemini)
RECIPE_MAIN_INGREDIENTS_MIN = 1
RECIPE_MAIN_INGREDIENTS_MAX = 10
RECIPE_EXCLUDED_INGREDIENTS_MAX = 10
RECIPE_FRIDGE_INGREDIENTS_MAX = 10  # 냉장고에서 고르는 재료. 직접 입력과 합쳐도 주재료 최대 개수를 넘을 수 없다
RECIPE_INGREDIENT_NAME_MAX_LENGTH = 30
RECIPE_REQUEST_NOTE_MAX_LENGTH = 200
RECIPE_TITLE_MAX_LENGTH = 100  # saved_recipe.title VARCHAR(100)
RECIPE_ITEM_NAME_MAX_LENGTH = 100  # 응답의 재료·양념 이름과 분량
RECIPE_STEP_MAX_LENGTH = 1_000
RECIPE_STEPS_MAX_COUNT = 30
RECIPE_LIST_MAX_COUNT = 50  # 응답의 재료·양념 개수 상한
RECIPE_SERVINGS_MAX = 100
GEMINI_TIMEOUT_SECONDS = 30  # 호출 1회당 제한. 넘으면 504
GEMINI_MAX_RETRIES = 1  # 호출 실패·JSON 검증 실패 시 추가 시도 횟수. 그래도 실패하면 502

# 가격 예측 외부 수집 기준값 (weather_daily 극한 기상 관측소 비율)
HEAT_MAX_TEMP = 33.0  # 폭염: 일 최고 33℃ 이상
HEAVY_RAIN_MM = 80.0  # 호우: 일 강수 80mm 이상
COLD_MIN_TEMP = -12.0  # 한파: 일 최저 -12℃ 이하
