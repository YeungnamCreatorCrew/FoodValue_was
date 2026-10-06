import base64
import json
import uuid
from datetime import datetime, timedelta, timezone

import jwt
import pytest
from fastapi.testclient import TestClient
from sqlalchemy import text

from app.core.config import get_settings
from app.core.constants import ACCESS_TOKEN_EXPIRE_MINUTES, JWT_AUDIENCE, JWT_ISSUER
from app.core.db import get_engine
from app.core.security import create_access_token
from app.main import app

client = TestClient(app)
PREFIX = "pytest-auth-"


@pytest.fixture(autouse=True)
def cleanup():
    yield
    with get_engine().begin() as conn:
        conn.execute(text("DELETE FROM users WHERE email LIKE :p"), {"p": f"{PREFIX}%"})


def _signup(email=None, password="password123", nickname=None):
    uid = uuid.uuid4().hex[:8]
    body = {
        "email": email or f"{PREFIX}{uid}@example.com",
        "password": password,
        "nickname": nickname or f"t{uid}",
    }
    return body, client.post("/api/v1/auth/signup", json=body)


def _login(body):
    r = client.post("/api/v1/auth/login", json={"email": body["email"], "password": body["password"]})
    return r.json()


def _token(body):
    return _login(body)["accessToken"]


def _me(token=None, header=None):
    headers = {"Authorization": header} if header else (
        {"Authorization": f"Bearer {token}"} if token else {}
    )
    return client.get("/api/v1/users/me", headers=headers)


# ---------- 회원가입 ----------
def test_signup_ok_and_password_hashed():
    body, r = _signup()
    assert r.status_code == 201
    assert "password" not in r.json() and "password_hash" not in r.json()
    assert r.json()["email"] == body["email"]
    with get_engine().connect() as conn:
        h = conn.execute(text("SELECT password_hash FROM users WHERE email=:e"), {"e": body["email"]}).scalar()
    assert h != body["password"] and h.startswith("$argon2id$")


def test_signup_email_normalized():
    uid = uuid.uuid4().hex[:8]
    _, r = _signup(email=f"{PREFIX}{uid}@EXAMPLE.com", nickname=f"n{uid}")
    assert r.json()["email"] == f"{PREFIX}{uid}@example.com"


def test_signup_duplicate_email():
    body, _ = _signup()
    r = client.post("/api/v1/auth/signup", json={**body, "nickname": "other" + uuid.uuid4().hex[:6]})
    assert r.status_code == 409


def test_signup_duplicate_nickname():
    body, _ = _signup()
    _, r = _signup(nickname=body["nickname"])
    assert r.status_code == 409


@pytest.mark.parametrize(
    "patch",
    [{"password": "short"}, {"email": "not-an-email"}, {"nickname": "x"}, {"nickname": "n" * 21}],
)
def test_signup_invalid_input(patch):
    uid = uuid.uuid4().hex[:8]
    body = {"email": f"{PREFIX}{uid}@example.com", "password": "password123", "nickname": f"t{uid}", **patch}
    assert client.post("/api/v1/auth/signup", json=body).status_code == 422


# ---------- 로그인 ----------
def test_login_ok():
    body, _ = _signup()
    r = client.post("/api/v1/auth/login", json={"email": body["email"], "password": body["password"]})
    assert r.status_code == 200
    assert r.json()["accessToken"] and r.json()["tokenType"] == "Bearer"


def test_login_failures_same_response():
    body, _ = _signup()
    wrong = client.post("/api/v1/auth/login", json={"email": body["email"], "password": "wrongpass1"})
    nouser = client.post("/api/v1/auth/login", json={"email": f"{PREFIX}none@example.com", "password": "wrongpass1"})
    assert wrong.status_code == nouser.status_code == 401
    assert wrong.json() == nouser.json()


# ---------- 토큰 검증 ----------
def test_protected_ok():
    body, _ = _signup()
    r = _me(_token(body))
    assert r.status_code == 200 and r.json()["email"] == body["email"]


def test_protected_no_token():
    assert _me().status_code == 401


def test_protected_bad_scheme():
    body, _ = _signup()
    assert _me(header=f"Token {_token(body)}").status_code == 401
    assert _me(header=_token(body)).status_code == 401


def _claims(user_id, **over):
    now = datetime.now(timezone.utc)
    return {
        "sub": str(user_id), "iss": JWT_ISSUER, "aud": JWT_AUDIENCE,
        "iat": now, "exp": now + timedelta(minutes=5), **over,
    }


def _user_id(body):
    return jwt.decode(_token(body), options={"verify_signature": False})["sub"]


def test_expired_token():
    body, _ = _signup()
    uid = int(_user_id(body))
    past = datetime.now(timezone.utc) - timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES + 1)
    assert _me(create_access_token(uid, now=past)).status_code == 401


def test_tampered_payload():
    body, _ = _signup()
    h, p, s = _token(body).split(".")
    payload = json.loads(base64.urlsafe_b64decode(p + "=="))
    payload["sub"] = "999999999"
    p2 = base64.urlsafe_b64encode(json.dumps(payload).encode()).rstrip(b"=").decode()
    assert _me(f"{h}.{p2}.{s}").status_code == 401


def test_wrong_secret():
    body, _ = _signup()
    t = jwt.encode(_claims(_user_id(body)), "x" * 40, algorithm="HS256")
    assert _me(t).status_code == 401


def test_alg_none():
    body, _ = _signup()
    enc = lambda d: base64.urlsafe_b64encode(json.dumps(d).encode()).rstrip(b"=").decode()
    claims = _claims(_user_id(body))
    claims["iat"] = int(claims["iat"].timestamp())
    claims["exp"] = int(claims["exp"].timestamp())
    t = f"{enc({'alg': 'none', 'typ': 'JWT'})}.{enc(claims)}."
    assert _me(t).status_code == 401


def test_wrong_audience_or_issuer():
    body, _ = _signup()
    key = get_settings().jwt_secret_key
    uid = _user_id(body)
    assert _me(jwt.encode(_claims(uid, aud="other"), key, algorithm="HS256")).status_code == 401
    assert _me(jwt.encode(_claims(uid, iss="other"), key, algorithm="HS256")).status_code == 401


def test_token_for_deleted_user():
    body, _ = _signup()
    t = _token(body)
    with get_engine().begin() as conn:
        conn.execute(text("DELETE FROM users WHERE email=:e"), {"e": body["email"]})
    assert _me(t).status_code == 401


# ---------- 리프레시 / 로그아웃 ----------
def _refresh(rt):
    return client.post("/api/v1/auth/refresh", json={"refreshToken": rt})


def test_login_returns_refresh_token_stored_as_hash():
    body, _ = _signup()
    rt = _login(body)["refreshToken"]
    with get_engine().connect() as conn:
        rows = conn.execute(text(
            "SELECT token_hash FROM refresh_token r JOIN users u ON u.id=r.user_id WHERE u.email=:e"
        ), {"e": body["email"]}).scalars().all()
    assert len(rows) == 1 and rows[0] != rt and len(rows[0]) == 64


def test_refresh_rotates_tokens():
    body, _ = _signup()
    old = _login(body)
    r = _refresh(old["refreshToken"])
    assert r.status_code == 200
    new = r.json()
    assert new["refreshToken"] != old["refreshToken"]
    assert _me(new["accessToken"]).status_code == 200


def test_refresh_reuse_revokes_family():
    body, _ = _signup()
    old = _login(body)["refreshToken"]
    new = _refresh(old).json()["refreshToken"]
    assert _refresh(old).status_code == 401  # 폐기된 토큰 재사용
    assert _refresh(new).status_code == 401  # 계열 전체가 폐기됨


def test_refresh_expired():
    body, _ = _signup()
    rt = _login(body)["refreshToken"]
    with get_engine().begin() as conn:
        conn.execute(text(
            "UPDATE refresh_token SET expires_at = now() - interval '1 minute' "
            "WHERE user_id = (SELECT id FROM users WHERE email=:e)"
        ), {"e": body["email"]})
    assert _refresh(rt).status_code == 401


def test_refresh_unknown_and_access_token_rejected():
    body, _ = _signup()
    assert _refresh("nope").status_code == 401
    assert _refresh(_token(body)).status_code == 401  # 액세스 토큰은 리프레시로 못 씀


def test_refresh_token_not_usable_as_access():
    body, _ = _signup()
    assert _me(_login(body)["refreshToken"]).status_code == 401


def test_logout_revokes_refresh():
    body, _ = _signup()
    rt = _login(body)["refreshToken"]
    assert client.post("/api/v1/auth/logout", json={"refreshToken": rt}).status_code == 204
    assert _refresh(rt).status_code == 401


def test_logout_is_idempotent_and_scoped_to_session():
    body, _ = _signup()
    a, b = _login(body)["refreshToken"], _login(body)["refreshToken"]
    assert client.post("/api/v1/auth/logout", json={"refreshToken": a}).status_code == 204
    assert client.post("/api/v1/auth/logout", json={"refreshToken": a}).status_code == 204
    assert client.post("/api/v1/auth/logout", json={"refreshToken": "unknown"}).status_code == 204
    assert _refresh(b).status_code == 200  # 다른 기기 세션은 유지
