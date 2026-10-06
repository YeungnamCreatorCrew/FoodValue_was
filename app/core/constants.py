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
POST_IMAGE_URL_MAX_LENGTH = 500  # post_image.url VARCHAR(500)
POST_IMAGE_MAX_COUNT = 10
SEARCH_KEYWORD_MAX_LENGTH = 100
PAGE_DEFAULT_SIZE = 20
PAGE_MAX_SIZE = 50

# 이미지 업로드
IMAGE_MAX_BYTES = 5 * 1024 * 1024
IMAGE_UPLOAD_PATH = "/api/v1/images"
IMAGE_REQUEST_OVERHEAD_BYTES = 64 * 1024  # 멀티파트 경계·헤더 몫. 요청 본문 상한 = 이미지 상한 + 이 값
IMAGE_KEY_PREFIX = "posts"  # 저장 경로: posts/{user_id}/{uuid}.{확장자}
