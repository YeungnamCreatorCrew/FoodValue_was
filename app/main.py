from fastapi import FastAPI

from app.core.config import get_settings
from app.routers import auth, users

get_settings()  # 필수 환경 변수가 없으면 기동 단계에서 바로 실패

app = FastAPI(title="FoodValue")
app.include_router(auth.router, prefix="/api/v1")
app.include_router(users.router, prefix="/api/v1")
