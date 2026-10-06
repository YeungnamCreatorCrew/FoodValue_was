import json

from starlette.types import ASGIApp, Message, Receive, Scope, Send

from app.core.constants import IMAGE_MAX_BYTES, IMAGE_REQUEST_OVERHEAD_BYTES, IMAGE_UPLOAD_PATH

_MAX_BODY = IMAGE_MAX_BYTES + IMAGE_REQUEST_OVERHEAD_BYTES
_DETAIL = f"이미지는 {IMAGE_MAX_BYTES // 1024 // 1024}MB 이하만 올릴 수 있습니다"


class ImageUploadSizeLimit:
    """업로드 경로의 요청 본문 크기를 받는 도중에 제한한다.

    멀티파트 본문은 라우터에 닿기 전에 파싱되어 임시 파일로 쌓이므로, 라우터의 크기 검사만으로는
    큰 파일이 디스크에 먼저 써지는 것을 막을 수 없다.
    Content-Length가 상한을 넘으면 읽지 않고 거절하고, 없거나 거짓이면(chunked) 받은 바이트를 세다 끊는다.
    """

    def __init__(self, app: ASGIApp) -> None:
        self.app = app

    async def __call__(self, scope: Scope, receive: Receive, send: Send) -> None:
        if scope["type"] != "http" or scope["method"] != "POST" or scope["path"] != IMAGE_UPLOAD_PATH:
            await self.app(scope, receive, send)
            return

        length = dict(scope["headers"]).get(b"content-length")
        if length is not None and length.isdigit() and int(length) > _MAX_BODY:
            await self._reject(send)
            return

        received = 0
        exceeded = False

        async def limited_receive() -> Message:
            nonlocal received, exceeded
            if exceeded:
                return {"type": "http.disconnect"}
            message = await receive()
            if message["type"] == "http.request":
                received += len(message.get("body", b""))
                if received > _MAX_BODY:
                    # 예외를 던지면 FastAPI가 400으로 바꿔버리므로, 연결이 끊긴 것처럼 읽기를 멈추고
                    # 앱이 무엇을 응답하든 아래에서 413으로 바꿔 보낸다
                    exceeded = True
                    return {"type": "http.disconnect"}
            return message

        replaced = False

        async def guarded_send(message: Message) -> None:
            nonlocal replaced
            if not exceeded:
                await send(message)
            elif not replaced:
                replaced = True
                await self._reject(send)

        await self.app(scope, limited_receive, guarded_send)

    @staticmethod
    async def _reject(send: Send) -> None:
        body = json.dumps({"detail": _DETAIL}, ensure_ascii=False).encode()
        await send({
            "type": "http.response.start",
            "status": 413,
            "headers": [(b"content-type", b"application/json"), (b"content-length", str(len(body)).encode()),
                        (b"connection", b"close")],
        })
        await send({"type": "http.response.body", "body": body})
