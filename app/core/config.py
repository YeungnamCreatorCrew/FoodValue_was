import os
from functools import lru_cache

from dotenv import load_dotenv

from app.core.constants import JWT_SECRET_MIN_LENGTH

load_dotenv()


class Settings:
    def __init__(self) -> None:
        self.database_url = self._require("DATABASE_URL")
        self.jwt_secret_key = self._require("JWT_SECRET_KEY")
        if len(self.jwt_secret_key) < JWT_SECRET_MIN_LENGTH:
            raise RuntimeError(
                f"JWT_SECRET_KEY는 {JWT_SECRET_MIN_LENGTH}자 이상이어야 합니다"
            )

    @staticmethod
    def _require(name: str) -> str:
        value = os.getenv(name)
        if not value:
            raise RuntimeError(f"환경 변수 {name}가 설정되지 않았습니다 (.env 확인)")
        return value


@lru_cache
def get_settings() -> Settings:
    return Settings()
