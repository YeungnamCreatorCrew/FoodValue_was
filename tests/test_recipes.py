import json
import uuid

import httpx
import pytest
from fastapi.testclient import TestClient
from sqlalchemy import text

from app.core.db import get_engine
from app.main import app
from app.services import recipe_service

client = TestClient(app)
PREFIX = "pytest-rcp-"
API = "/api/v1"
GENERATE = f"{API}/recipes/generate"
SAVED = f"{API}/recipes/saved"

RECIPE = {
    "title": "김치볶음밥",
    "servings": 2,
    "ingredients": [{"name": "밥", "amount": "2공기"}],
    "seasonings": [{"name": "간장", "amount": "1큰술"}],
    "steps": ["김치를 볶는다", "밥을 넣고 볶는다"],
}
VALID = {"mainIngredients": ["김치", "밥"], "excludedIngredients": ["오이"], "requestNote": "2인분, 맵게"}


@pytest.fixture(autouse=True)
def cleanup():
    yield
    with get_engine().begin() as conn:
        conn.execute(
            text("DELETE FROM saved_recipe WHERE user_id IN (SELECT id FROM users WHERE email LIKE :p)"),
            {"p": f"{PREFIX}%"},
        )
        conn.execute(text("DELETE FROM users WHERE email LIKE :p"), {"p": f"{PREFIX}%"})


def _user():
    uid = uuid.uuid4().hex[:8]
    body = {"email": f"{PREFIX}{uid}@example.com", "password": "password123", "nickname": f"r{uid}"}
    assert client.post(f"{API}/auth/signup", json=body).status_code == 201
    token = client.post(f"{API}/auth/login", json=body).json()["accessToken"]
    return {"Authorization": f"Bearer {token}"}


@pytest.fixture
def gemini(monkeypatch):
    calls = []
    results = [json.dumps(RECIPE)]

    def fake(prompt):
        calls.append(prompt)
        r = results[min(len(calls), len(results)) - 1]
        if isinstance(r, Exception):
            raise r
        return r

    monkeypatch.setattr(recipe_service, "_call_gemini", fake)
    return calls, results


def test_requires_auth(gemini):
    assert client.post(GENERATE, json=VALID).status_code == 401
    assert gemini[0] == []


def test_generate_ok(gemini):
    r = client.post(GENERATE, json=VALID, headers=_user())
    assert r.status_code == 200
    assert r.json() == RECIPE
    prompt = gemini[0][0]
    assert "김치" in prompt and "오이" in prompt and "2인분, 맵게" in prompt


def test_generate_optional_fields(gemini):
    r = client.post(GENERATE, json={"mainIngredients": ["김치"]}, headers=_user())
    assert r.status_code == 200


@pytest.mark.parametrize(
    "body",
    [
        {"mainIngredients": []},
        {},
        {"mainIngredients": [f"재료{i}" for i in range(11)]},
        {"mainIngredients": ["가" * 31]},
        {"mainIngredients": [" "]},
        {"mainIngredients": ["김치"], "excludedIngredients": [f"재료{i}" for i in range(11)]},
        {"mainIngredients": ["김치"], "excludedIngredients": ["가" * 31]},
        {"mainIngredients": ["김치"], "requestNote": "가" * 201},
    ],
)
def test_generate_validation_422(gemini, body):
    r = client.post(GENERATE, json=body, headers=_user())
    assert r.status_code == 422
    assert gemini[0] == []


def test_generate_limit_boundaries_ok(gemini):
    body = {
        "mainIngredients": ["가" * 30] * 10,
        "excludedIngredients": ["나" * 30] * 10,
        "requestNote": "다" * 200,
    }
    assert client.post(GENERATE, json=body, headers=_user()).status_code == 200


def test_retry_then_success(gemini):
    calls, results = gemini
    results[:] = ["not json", json.dumps(RECIPE)]
    r = client.post(GENERATE, json=VALID, headers=_user())
    assert r.status_code == 200
    assert len(calls) == 2


def test_schema_violation_retried_then_502(gemini):
    calls, results = gemini
    results[:] = [json.dumps({**RECIPE, "steps": []})]
    r = client.post(GENERATE, json=VALID, headers=_user())
    assert r.status_code == 502
    assert len(calls) == 2
    assert "title" not in r.json()


def test_call_failure_502(gemini):
    calls, results = gemini
    results[:] = [httpx.ConnectError("boom")]
    assert client.post(GENERATE, json=VALID, headers=_user()).status_code == 502
    assert len(calls) == 2


def test_timeout_504(gemini):
    calls, results = gemini
    results[:] = [httpx.ReadTimeout("slow")]
    assert client.post(GENERATE, json=VALID, headers=_user()).status_code == 504
    assert len(calls) == 2


# ---------- 저장 레시피 ----------
def test_saved_requires_auth():
    assert client.post(SAVED, json=RECIPE).status_code == 401
    assert client.get(SAVED).status_code == 401
    assert client.get(f"{SAVED}/1").status_code == 401
    assert client.delete(f"{SAVED}/1").status_code == 401


def test_save_get_list_delete():
    h = _user()
    r = client.post(SAVED, json=RECIPE, headers=h)
    assert r.status_code == 201
    saved = r.json()
    assert saved["title"] == RECIPE["title"] and saved["content"] == RECIPE

    d = client.get(f"{SAVED}/{saved['id']}", headers=h)
    assert d.status_code == 200 and d.json()["content"] == RECIPE

    lst = client.get(SAVED, headers=h).json()
    assert lst["total"] == 1
    assert set(lst["items"][0]) == {"id", "title", "createdAt"}

    assert client.delete(f"{SAVED}/{saved['id']}", headers=h).status_code == 204
    assert client.get(f"{SAVED}/{saved['id']}", headers=h).status_code == 404
    assert client.delete(f"{SAVED}/{saved['id']}", headers=h).status_code == 404


def test_duplicate_save_allowed_and_latest_first_paging():
    h = _user()
    ids = [client.post(SAVED, json={**RECIPE, "title": f"r{i}"}, headers=h).json()["id"] for i in range(3)]
    assert len(set(ids)) == 3
    page = client.get(SAVED, params={"size": 2}, headers=h).json()
    assert page["total"] == 3 and page["size"] == 2
    assert [i["id"] for i in page["items"]] == [ids[2], ids[1]]
    page2 = client.get(SAVED, params={"size": 2, "page": 2}, headers=h).json()
    assert [i["id"] for i in page2["items"]] == [ids[0]]
    assert client.get(SAVED, params={"size": 51}, headers=h).status_code == 422
    assert client.get(SAVED, headers=h).json()["size"] == 20


@pytest.mark.parametrize(
    "over",
    [
        {"title": "가" * 101},
        {"title": ""},
        {"servings": "많이"},
        {"steps": []},
        {"ingredients": [{"name": "밥"}]},
    ],
)
def test_save_schema_violation_422(over):
    assert client.post(SAVED, json={**RECIPE, **over}, headers=_user()).status_code == 422
    body = {k: v for k, v in RECIPE.items() if k != "seasonings"}
    assert client.post(SAVED, json=body, headers=_user()).status_code == 422


def test_save_title_100_ok():
    assert client.post(SAVED, json={**RECIPE, "title": "가" * 100}, headers=_user()).status_code == 201


def test_other_users_recipe_is_404():
    owner, other = _user(), _user()
    rid = client.post(SAVED, json=RECIPE, headers=owner).json()["id"]
    assert client.get(f"{SAVED}/{rid}", headers=other).status_code == 404
    assert client.delete(f"{SAVED}/{rid}", headers=other).status_code == 404
    assert client.get(SAVED, headers=other).json()["total"] == 0
    assert client.get(f"{SAVED}/{rid}", headers=owner).status_code == 200
