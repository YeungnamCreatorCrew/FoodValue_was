from fastapi import FastAPI, Request, status
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from app.core.config import get_settings
from app.core.limits import ImageUploadSizeLimit
from app.routers import auth, images, posts, recipes, users

RECIPES_PATH = "/api/v1/recipes"

settings = get_settings()  # 필수 환경 변수가 없으면 기동 단계에서 바로 실패

app = FastAPI(title="FoodValue")
app.add_middleware(ImageUploadSizeLimit)
# 가장 마지막에 추가해야 가장 바깥에서 동작해, 413 같은 거절 응답에도 CORS 헤더가 붙는다
# 인증은 쿠키가 아니라 Authorization 헤더라서 credentials는 허용하지 않는다
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins,
    allow_methods=["GET", "POST", "PATCH", "DELETE"],
    allow_headers=["Authorization", "Content-Type"],
)


@app.exception_handler(RequestValidationError)
async def validation_error_handler(request: Request, exc: RequestValidationError):
    """입력 검증 실패는 400. 어느 필드가 왜 틀렸는지만 알려주고 입력값은 되돌려 보내지 않는다."""
    errors = [
        {"field": ".".join(str(x) for x in e["loc"][1:]) or str(e["loc"][0]), "message": e["msg"]}
        for e in exc.errors()
    ]
    # 레시피 API는 명세상 입력 위반이 422, 나머지는 400
    code = (
        status.HTTP_422_UNPROCESSABLE_CONTENT
        if request.url.path.startswith(RECIPES_PATH)
        else status.HTTP_400_BAD_REQUEST
    )
    return JSONResponse(
        status_code=code,
        content={"detail": "입력값이 올바르지 않습니다", "errors": errors},
    )


app.include_router(auth.router, prefix="/api/v1")
app.include_router(users.router, prefix="/api/v1")
app.include_router(posts.router, prefix="/api/v1")
app.include_router(images.router, prefix="/api/v1")
app.include_router(recipes.router, prefix="/api/v1")
