import uuid

import httpx
import pytest
from fastapi.testclient import TestClient
from sqlalchemy import text

from app.core import storage
from app.core.config import get_settings
from app.core.constants import IMAGE_MAX_BYTES
from app.core.db import get_engine
from app.main import app

client = TestClient(app)
PREFIX = "pytest-img-"
API = "/api/v1"

PNG = b"\x89PNG\r\n\x1a\n" + b"\x00" * 32
JPEG = b"\xff\xd8\xff\xe0" + b"\x00" * 32
GIF = b"GIF89a" + b"\x00" * 32
WEBP = b"RIFF\x24\x00\x00\x00WEBPVP8 " + b"\x00" * 32

_uploaded: list[str] = []


@pytest.fixture(autouse=True)
def cleanup():
    yield
    base = get_settings().s3_public_base_url + "/"
    for url in _uploaded:
        storage.delete_object(url.removeprefix(base))
    _uploaded.clear()
    with get_engine().begin() as conn:
        conn.execute(text("DELETE FROM users WHERE email LIKE :p"), {"p": f"{PREFIX}%"})


def _user():
    uid = uuid.uuid4().hex[:8]
    body = {"email": f"{PREFIX}{uid}@example.com", "password": "password123", "nickname": f"i{uid}"}
    assert client.post(f"{API}/auth/signup", json=body).status_code == 201
    token = client.post(f"{API}/auth/login", json=body).json()["accessToken"]
    return {"Authorization": f"Bearer {token}"}


def _upload(h, data, filename="a.png", content_type="image/png"):
    r = client.post(f"{API}/images", files={"file": (filename, data, content_type)}, headers=h)
    if r.status_code == 201:
        _uploaded.append(r.json()["url"])
    return r


def test_requires_auth():
    r = client.post(f"{API}/images", files={"file": ("a.png", PNG, "image/png")})
    assert r.status_code == 401


@pytest.mark.parametrize(
    "data,ext,ctype",
    [(PNG, "png", "image/png"), (JPEG, "jpg", "image/jpeg"), (GIF, "gif", "image/gif"), (WEBP, "webp", "image/webp")],
)
def test_upload_and_public_read(data, ext, ctype):
    r = _upload(_user(), data, filename=f"x.{ext}")
    assert r.status_code == 201
    url = r.json()["url"]
    assert url.startswith(get_settings().s3_public_base_url) and url.endswith(f".{ext}")
    got = httpx.get(url)  # 로그인 없이 공개 URL로 읽힌다
    assert got.status_code == 200 and got.content == data
    assert got.headers["content-type"] == ctype


def test_filename_and_client_type_are_not_trusted():
    # 이름이 ../ 이고 content-type이 png라고 우겨도 내용이 텍스트면 거부
    r = _upload(_user(), b"<script>alert(1)</script>", filename="../../evil.png", content_type="image/png")
    assert r.status_code == 415
    # 내용이 PNG면 이름이 이상해도 서버가 정한 키로 저장된다
    r = _upload(_user(), PNG, filename="../../evil.html", content_type="text/html")
    assert r.status_code == 201 and "evil" not in r.json()["url"] and r.json()["url"].endswith(".png")


def test_empty_file_415():
    assert _upload(_user(), b"").status_code == 415


def test_too_large_413():
    r = _upload(_user(), PNG + b"\x00" * IMAGE_MAX_BYTES)
    assert r.status_code == 413


def test_missing_file_400():
    assert client.post(f"{API}/images", headers=_user()).status_code == 400


def test_each_upload_gets_unique_key():
    h = _user()
    assert _upload(h, PNG).json()["url"] != _upload(h, PNG).json()["url"]


def test_uploaded_url_usable_in_post():
    h = _user()
    url = _upload(h, PNG).json()["url"]
    body = {"category": "SHOWOFF", "title": "사진", "content": "자랑", "imageUrls": [url]}
    r = client.post(f"{API}/posts", json=body, headers=h)
    assert r.status_code == 201 and r.json()["imageUrls"] == [url]
    pid = r.json()["id"]
    with get_engine().begin() as conn:
        conn.execute(text("DELETE FROM post WHERE id=:i"), {"i": pid})


# ---------- 요청 본문 크기 제한 (라우터에 닿기 전) ----------
def test_huge_body_rejected_by_content_length_before_reading():
    h = _user()
    big = b"\x00" * (IMAGE_MAX_BYTES + 200 * 1024)
    r = client.post(f"{API}/images", files={"file": ("a.png", PNG + big, "image/png")}, headers=h)
    assert r.status_code == 413


def test_chunked_body_without_content_length_is_cut_off():
    h = _user()
    chunk = b"\x00" * (256 * 1024)

    def body():
        yield b"--b\r\nContent-Disposition: form-data; name=\"file\"; filename=\"a.png\"\r\n\r\n" + PNG
        for _ in range(40):  # 약 10MB, Content-Length 없이 전송
            yield chunk
        yield b"\r\n--b--\r\n"

    r = client.post(f"{API}/images", content=body(),
                    headers={**h, "Content-Type": "multipart/form-data; boundary=b"})
    assert r.status_code == 413


def test_limit_applies_only_to_upload_path():
    h = _user()
    body = {"category": "SHOWOFF", "title": "t", "content": "c" * (IMAGE_MAX_BYTES + 200 * 1024)}
    r = client.post(f"{API}/posts", json=body, headers=h)  # 본문이 커도 글 작성은 이 제한 대상이 아님
    assert r.status_code == 201
    with get_engine().begin() as conn:
        conn.execute(text("DELETE FROM post WHERE id=:i"), {"i": r.json()["id"]})
