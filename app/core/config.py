import os
from functools import lru_cache

from dotenv import load_dotenv

from app.core.constants import CORS_DEFAULT_ORIGINS

load_dotenv()


class Settings:
    def __init__(self) -> None:
        self.database_url = self._require("DATABASE_URL")
        # 선택값. 없으면 로컬 개발 주소만 허용한다 (운영은 반드시 지정)
        origins = os.getenv("CORS_ORIGINS", "")
        self.cors_origins = [o.strip().rstrip("/") for o in origins.split(",") if o.strip()] or CORS_DEFAULT_ORIGINS
        self.gemini_api_key = os.getenv("GEMINI_API_KEY") or None
        self.gemini_model = os.getenv("GEMINI_MODEL") or None

    def require_gemini(self) -> tuple[str, str]:
        """(api_key, model)을 반환한다. 둘 중 하나라도 없으면 RuntimeError"""
        if not self.gemini_api_key:
            raise RuntimeError("환경 변수 GEMINI_API_KEY가 설정되지 않았습니다 (.env 확인)")
        if not self.gemini_model:
            raise RuntimeError("환경 변수 GEMINI_MODEL이 설정되지 않았습니다 (.env 확인)")
        return self.gemini_api_key, self.gemini_model

    @staticmethod
    def _require(name: str) -> str:
        value = os.getenv(name)
        if not value:
            raise RuntimeError(f"환경 변수 {name}가 설정되지 않았습니다 (.env 확인)")
        return value


@lru_cache
def get_settings() -> Settings:
    return Settings()
