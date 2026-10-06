"""서비스 기준값. 임의로 흩어 쓰지 말고 이 파일 한 곳에서만 바꾼다."""

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
