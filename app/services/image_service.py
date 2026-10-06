import uuid

from botocore.exceptions import BotoCoreError, ClientError

from app.core import storage
from app.core.constants import IMAGE_KEY_PREFIX, IMAGE_MAX_BYTES
from app.models.user import User


class UnsupportedImageError(Exception):
    pass


class ImageTooLargeError(Exception):
    pass


class StorageError(Exception):
    pass


def _detect(data: bytes) -> tuple[str, str] | None:
    """파일 내용(매직 바이트)으로 (content-type, 확장자)를 판별한다. 클라이언트가 보낸 타입은 믿지 않는다."""
    if data.startswith(b"\x89PNG\r\n\x1a\n"):
        return "image/png", "png"
    if data.startswith(b"\xff\xd8\xff"):
        return "image/jpeg", "jpg"
    if data.startswith((b"GIF87a", b"GIF89a")):
        return "image/gif", "gif"
    if data[:4] == b"RIFF" and data[8:12] == b"WEBP":
        return "image/webp", "webp"
    return None


def upload_image(user: User, data: bytes) -> str:
    if len(data) > IMAGE_MAX_BYTES:
        raise ImageTooLargeError
    kind = _detect(data)
    if kind is None:
        raise UnsupportedImageError
    content_type, ext = kind
    # 파일 이름은 사용자 입력을 쓰지 않고 서버가 정한다 (경로 조작 방지)
    key = f"{IMAGE_KEY_PREFIX}/{user.id}/{uuid.uuid4().hex}.{ext}"
    try:
        return storage.put_object(key, data, content_type)
    except (BotoCoreError, ClientError):
        raise StorageError from None
