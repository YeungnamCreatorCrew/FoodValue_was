from fastapi import APIRouter, Depends, HTTPException, UploadFile, status

from app.core.constants import IMAGE_MAX_BYTES
from app.core.deps import get_current_user
from app.models.user import User
from app.schemas.image import ImageResponse
from app.services import image_service

router = APIRouter(tags=["images"])


@router.post("/images", response_model=ImageResponse, status_code=status.HTTP_201_CREATED)
async def upload_image(file: UploadFile, user: User = Depends(get_current_user)):
    # 상한보다 1바이트만 더 읽어 크기를 초과했는지만 확인한다 (큰 파일 전체를 메모리에 올리지 않음)
    data = await file.read(IMAGE_MAX_BYTES + 1)
    try:
        url = image_service.upload_image(user, data)
    except image_service.ImageTooLargeError:
        raise HTTPException(
            status.HTTP_413_CONTENT_TOO_LARGE,
            f"이미지는 {IMAGE_MAX_BYTES // 1024 // 1024}MB 이하만 올릴 수 있습니다",
        ) from None
    except image_service.UnsupportedImageError:
        raise HTTPException(
            status.HTTP_415_UNSUPPORTED_MEDIA_TYPE, "PNG, JPEG, GIF, WEBP 이미지만 올릴 수 있습니다"
        ) from None
    except image_service.StorageError:
        raise HTTPException(status.HTTP_502_BAD_GATEWAY, "이미지 저장소에 연결할 수 없습니다") from None
    return ImageResponse(url=url)
