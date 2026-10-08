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
            text("DELETE FROM fridge_ingredient WHERE user_id IN (SELECT id FROM users WHERE email LIKE :p)"),
            {"p": f"{PREFIX}%"},
        )
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


# ---------- 냉장고 재료 선택 ----------
FRIDGE = f"{API}/fridge/items"


def _fridge(headers, name="대파", quantity="2"):
    body = {"displayName": name, "quantity": quantity, "unit": "개", "storage": "FRIDGE", "purchasedAt": "2026-01-01"}
    r = client.post(FRIDGE, json=body, headers=headers)
    assert r.status_code == 201, r.text
    return r.json()["id"]


def _payload(prompt):
    return json.loads(prompt.split("입력(JSON):\n", 1)[1])


def test_generate_with_fridge_ingredients_only(gemini):
    h = _user()
    ids = [_fridge(h, "대파"), _fridge(h, "두부")]
    r = client.post(GENERATE, json={"fridgeIngredientIds": ids}, headers=h)
    assert r.status_code == 200 and r.json() == RECIPE
    assert _payload(gemini[0][0])["mainIngredients"] == ["대파", "두부"]


def test_generate_merges_manual_and_fridge_dedup(gemini):
    h = _user()
    ids = [_fridge(h, "대파"), _fridge(h, "두부")]
    body = {"mainIngredients": ["김치", "대 파"], "fridgeIngredientIds": ids + ids[:1]}
    assert client.post(GENERATE, json=body, headers=h).status_code == 200
    assert _payload(gemini[0][0])["mainIngredients"] == ["김치", "대 파", "두부"]


def test_fridge_ingredient_of_other_user_404(gemini):
    other_id = _fridge(_user())
    r = client.post(GENERATE, json={"fridgeIngredientIds": [other_id]}, headers=_user())
    assert r.status_code == 404
    assert gemini[0] == []


def test_fridge_ingredient_unknown_deleted_or_empty_404(gemini):
    h = _user()
    deleted, empty, ok = _fridge(h, "삭제"), _fridge(h, "소진", "1"), _fridge(h, "대파")
    assert client.delete(f"{FRIDGE}/{deleted}", headers=h).status_code == 204
    body = {"reason": "FINISH", "usedAt": "2026-01-02"}
    assert client.post(f"{FRIDGE}/{empty}/consume", json=body, headers=h).status_code == 200
    for bad in (deleted, empty, 999_999_999):
        assert client.post(GENERATE, json={"fridgeIngredientIds": [ok, bad]}, headers=h).status_code == 404
    assert gemini[0] == []


def test_fridge_ingredient_excluded_conflict_422(gemini):
    h = _user()
    body = {"fridgeIngredientIds": [_fridge(h, "대파")], "excludedIngredients": ["대 파"]}
    assert client.post(GENERATE, json=body, headers=h).status_code == 422
    assert gemini[0] == []


def test_combined_ingredients_over_limit_422(gemini):
    h = _user()
    ids = [_fridge(h, f"냉{i}") for i in range(3)]
    body = {"mainIngredients": [f"재료{i}" for i in range(8)], "fridgeIngredientIds": ids}
    assert client.post(GENERATE, json=body, headers=h).status_code == 422
    assert gemini[0] == []


@pytest.mark.parametrize(
    "body",
    [
        {"fridgeIngredientIds": []},
        {"fridgeIngredientIds": [0]},
        {"fridgeIngredientIds": [-1]},
        {"fridgeIngredientIds": ["a"]},
        {"fridgeIngredientIds": [2**63]},
        {"fridgeIngredientIds": list(range(1, 12))},
    ],
)
def test_fridge_ids_validation_422(gemini, body):
    assert client.post(GENERATE, json=body, headers=_user()).status_code == 422
    assert gemini[0] == []


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
