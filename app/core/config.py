import os
from functools import lru_cache

from dotenv import load_dotenv

from app.core.constants import CORS_DEFAULT_ORIGINS, JWT_SECRET_MIN_LENGTH

load_dotenv()


class Settings:
    def __init__(self) -> None:
        self.database_url = self._require("DATABASE_URL")
        self.jwt_secret_key = self._require("JWT_SECRET_KEY")
        if len(self.jwt_secret_key) < JWT_SECRET_MIN_LENGTH:
            raise RuntimeError(
                f"JWT_SECRET_KEY는 {JWT_SECRET_MIN_LENGTH}자 이상이어야 합니다"
            )
        # 선택값. 없으면 로컬 개발 주소만 허용한다 (운영은 반드시 지정)
        origins = os.getenv("CORS_ORIGINS", "")
        self.cors_origins = [o.strip().rstrip("/") for o in origins.split(",") if o.strip()] or CORS_DEFAULT_ORIGINS
        # 이미지 저장소 (S3 API). 로컬 MinIO / 운영 Supabase Storage 모두 같은 변수 이름을 쓴다
        self.s3_endpoint_url = self._require("S3_ENDPOINT_URL")
        self.s3_region = self._require("S3_REGION")
        self.s3_bucket = self._require("S3_BUCKET")
        self.s3_access_key = self._require("S3_ACCESS_KEY")
        self.s3_secret_key = self._require("S3_SECRET_KEY")
        self.s3_public_base_url = self._require("S3_PUBLIC_BASE_URL").rstrip("/")
        # Gemini (레시피 생성). 키와 모델명은 코드에 두지 않고 .env에서만 읽는다. 레시피 생성 시점에 require_gemini()로 검증한다
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
