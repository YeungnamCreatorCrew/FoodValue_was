from fastapi import FastAPI, Request, status
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

from app.core.config import get_settings
from app.routers import auth, posts, users

get_settings()  # 필수 환경 변수가 없으면 기동 단계에서 바로 실패

app = FastAPI(title="FoodValue")


@app.exception_handler(RequestValidationError)
async def validation_error_handler(request: Request, exc: RequestValidationError):
    """입력 검증 실패는 400. 어느 필드가 왜 틀렸는지만 알려주고 입력값은 되돌려 보내지 않는다."""
    errors = [
        {"field": ".".join(str(x) for x in e["loc"][1:]) or str(e["loc"][0]), "message": e["msg"]}
        for e in exc.errors()
    ]
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content={"detail": "입력값이 올바르지 않습니다", "errors": errors},
    )


app.include_router(auth.router, prefix="/api/v1")
app.include_router(users.router, prefix="/api/v1")
app.include_router(posts.router, prefix="/api/v1")
