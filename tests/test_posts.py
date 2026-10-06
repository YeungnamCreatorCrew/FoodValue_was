import uuid

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import text

from app.core.constants import PAGE_MAX_SIZE
from app.core.db import get_engine
from app.main import app

client = TestClient(app)
PREFIX = "pytest-post-"
API = "/api/v1"


@pytest.fixture(autouse=True)
def cleanup():
    yield
    with get_engine().begin() as conn:
        # post.user_id, comment.user_id 는 CASCADE가 아니라서 글·댓글부터 지운다
        sub = "(SELECT id FROM users WHERE email LIKE :p)"
        conn.execute(text(f"DELETE FROM comment WHERE user_id IN {sub}"), {"p": f"{PREFIX}%"})
        conn.execute(text(f"DELETE FROM post WHERE user_id IN {sub}"), {"p": f"{PREFIX}%"})
        conn.execute(text("DELETE FROM users WHERE email LIKE :p"), {"p": f"{PREFIX}%"})


def _user():
    """가입 후 Authorization 헤더를 돌려준다."""
    uid = uuid.uuid4().hex[:8]
    body = {"email": f"{PREFIX}{uid}@example.com", "password": "password123", "nickname": f"p{uid}"}
    assert client.post(f"{API}/auth/signup", json=body).status_code == 201
    token = client.post(f"{API}/auth/login", json=body).json()["accessToken"]
    return {"Authorization": f"Bearer {token}"}


def _post(h, **over):
    body = {"category": "RECIPE_SHARE", "title": "김치찌개", "content": "맛있게 끓이는 법", **over}
    return client.post(f"{API}/posts", json=body, headers=h)


def _total(h, **q):
    return client.get(f"{API}/posts", params=q, headers=h).json()["total"]


# ---------- 인증: 조회는 공개, 쓰기는 401 ----------
@pytest.mark.parametrize(
    "method,path",
    [("POST", "/posts"), ("PATCH", "/posts/1"), ("DELETE", "/posts/1"),
     ("POST", "/posts/1/comments"), ("PATCH", "/comments/1"), ("DELETE", "/comments/1")],
)
def test_write_requires_auth(method, path):
    assert client.request(method, f"{API}{path}", json={"content": "a"}).status_code == 401


def test_read_is_public():
    h = _user()
    tag = uuid.uuid4().hex[:10]
    pid = _post(h, title=tag).json()["id"]
    client.post(f"{API}/posts/{pid}/comments", json={"content": "댓글"}, headers=h)
    assert client.get(f"{API}/posts", params={"keyword": tag}).json()["total"] == 1
    d = client.get(f"{API}/posts/{pid}")
    assert d.status_code == 200 and d.json()["isMine"] is False  # 비로그인은 isMine=false
    c = client.get(f"{API}/posts/{pid}/comments")
    assert c.status_code == 200 and c.json()[0]["isMine"] is False


def test_invalid_token_on_public_read_is_401():
    assert client.get(f"{API}/posts", headers={"Authorization": "Bearer garbage"}).status_code == 401


# ---------- 게시글 CRUD ----------
def test_create_and_get():
    h = _user()
    r = _post(h, imageUrls=["https://img.example.com/a.jpg", "https://img.example.com/b.jpg"])
    assert r.status_code == 201
    d = r.json()
    assert d["category"] == "RECIPE_SHARE" and d["isMine"] is True
    assert d["imageUrls"] == ["https://img.example.com/a.jpg", "https://img.example.com/b.jpg"]
    got = client.get(f"{API}/posts/{d['id']}", headers=_user()).json()
    assert got["title"] == "김치찌개" and got["isMine"] is False
    assert got["author"]["nickname"] == d["author"]["nickname"]


def test_author_comes_from_token_not_body():
    a, b = _user(), _user()
    me = client.get(f"{API}/users/me", headers=a).json()
    r = _post(a, userId=999, author={"id": 999, "nickname": "x"})
    assert r.json()["author"]["id"] == me["id"]
    assert client.get(f"{API}/users/me", headers=b).json()["id"] != me["id"]


@pytest.mark.parametrize(
    "over",
    [{"category": "NOPE"}, {"title": ""}, {"title": "x" * 101}, {"title": "   "}, {"content": ""},
     {"content": "  \n "}, {"imageUrls": ["javascript:alert(1)"]}, {"imageUrls": ["https://a.com/x.jpg"] * 11}],
)
def test_create_invalid_400(over):
    assert _post(_user(), **over).status_code == 400


def test_validation_error_does_not_echo_input():
    r = _post(_user(), title="")
    assert r.status_code == 400 and r.json()["errors"][0]["field"] == "title"
    assert "input" not in r.text


def test_missing_post_404():
    h = _user()
    assert client.get(f"{API}/posts/999999999", headers=h).status_code == 404
    assert client.patch(f"{API}/posts/999999999", json={"title": "a"}, headers=h).status_code == 404
    assert client.delete(f"{API}/posts/999999999", headers=h).status_code == 404


def test_update_by_author_only():
    h, other = _user(), _user()
    pid = _post(h, imageUrls=["https://a.com/1.jpg"]).json()["id"]
    assert client.patch(f"{API}/posts/{pid}", json={"title": "해킹"}, headers=other).status_code == 403
    r = client.patch(f"{API}/posts/{pid}", json={"title": "수정됨", "category": "SHOWOFF"}, headers=h)
    assert r.status_code == 200
    d = r.json()
    assert d["title"] == "수정됨" and d["category"] == "SHOWOFF"
    assert d["content"] == "맛있게 끓이는 법" and d["imageUrls"] == ["https://a.com/1.jpg"]  # 안 보낸 항목 유지
    assert d["updatedAt"] >= d["createdAt"]
    assert client.patch(f"{API}/posts/{pid}", json={"imageUrls": []}, headers=h).json()["imageUrls"] == []
    assert client.get(f"{API}/posts/{pid}", headers=other).json()["title"] == "수정됨"


@pytest.mark.parametrize("body", [{}, {"title": None}, {"category": "NOPE"}, {"content": " "}])
def test_update_invalid_400(body):
    h = _user()
    pid = _post(h).json()["id"]
    assert client.patch(f"{API}/posts/{pid}", json=body, headers=h).status_code == 400


def test_delete_by_author_only_cascades():
    h, other = _user(), _user()
    pid = _post(h, imageUrls=["https://a.com/1.jpg"]).json()["id"]
    client.post(f"{API}/posts/{pid}/comments", json={"content": "댓글"}, headers=other)
    assert client.delete(f"{API}/posts/{pid}", headers=other).status_code == 403
    assert client.delete(f"{API}/posts/{pid}", headers=h).status_code == 204
    assert client.get(f"{API}/posts/{pid}", headers=h).status_code == 404
    with get_engine().connect() as conn:
        n = conn.execute(text("SELECT (SELECT count(*) FROM comment WHERE post_id=:i) + "
                              "(SELECT count(*) FROM post_image WHERE post_id=:i)"), {"i": pid}).scalar()
    assert n == 0
    assert client.delete(f"{API}/posts/{pid}", headers=h).status_code == 404


# ---------- 목록: 필터·검색·페이징 ----------
def test_list_filter_search_paging():
    h = _user()
    tag = uuid.uuid4().hex[:10]
    a = _post(h, category="RECIPE_SHARE", title=f"{tag} 레시피", imageUrls=["https://a.com/t.jpg"]).json()["id"]
    b = _post(h, category="GROUP_BUY", title=f"{tag} 소분").json()["id"]
    c = _post(h, category="SHOWOFF", title="무관", content=f"본문에 {tag} 포함").json()["id"]

    def get(**q):
        r = client.get(f"{API}/posts", params=q, headers=h)
        assert r.status_code == 200
        return r.json()

    res = get(keyword=tag)
    assert [i["id"] for i in res["items"]] == [c, b, a]  # 최신순, 제목·본문 검색
    assert res["total"] == 3 and res["page"] == 1
    assert [i["id"] for i in get(keyword=tag, category="GROUP_BUY")["items"]] == [b]
    assert get(keyword=tag, size=2)["total"] == 3 and len(get(keyword=tag, size=2)["items"]) == 2
    assert [i["id"] for i in get(keyword=tag, size=2, page=2)["items"]] == [a]  # 마지막 페이지
    by_id = {i["id"]: i for i in res["items"]}
    assert by_id[a]["thumbnailUrl"] == "https://a.com/t.jpg" and by_id[b]["thumbnailUrl"] is None


def test_list_empty_and_out_of_range_page():
    h = _user()
    tag = uuid.uuid4().hex[:10]
    empty = client.get(f"{API}/posts", params={"keyword": tag}, headers=h).json()
    assert empty["items"] == [] and empty["total"] == 0
    _post(h, title=tag)
    far = client.get(f"{API}/posts", params={"keyword": tag, "page": 99}, headers=h).json()
    assert far["items"] == [] and far["total"] == 1


def test_list_keyword_wildcards_are_literal():
    h = _user()
    tag = uuid.uuid4().hex[:8]
    _post(h, title=f"{tag}_x")
    _post(h, title=f"{tag}1x")
    assert _total(h, keyword=f"{tag}_x") == 1  # _ 가 와일드카드면 2건이 된다
    assert _total(h, keyword=f"{tag}%") == 0  # % 도 문자 그대로 취급


def test_list_sql_injection_is_literal():
    h = _user()
    assert _total(h, keyword="'; DROP TABLE post; --") == 0
    assert _total(h) >= 0  # 테이블이 살아 있다


@pytest.mark.parametrize(
    "q",
    [{"category": "NOPE"}, {"page": 0}, {"size": 0}, {"size": PAGE_MAX_SIZE + 1}, {"keyword": "k" * 101}],
)
def test_list_invalid_params_400(q):
    assert client.get(f"{API}/posts", params=q, headers=_user()).status_code == 400


def test_list_query_count_does_not_grow_with_rows():
    """N+1 방지: 글 수가 늘어도 목록 쿼리 수는 같다."""
    from sqlalchemy import event

    h = _user()
    tag = uuid.uuid4().hex[:10]

    def count_queries():
        n = []
        eng = get_engine()
        fn = lambda *a, **k: n.append(1)
        event.listen(eng, "before_cursor_execute", fn)
        try:
            client.get(f"{API}/posts", params={"keyword": tag, "size": 50})
        finally:
            event.remove(eng, "before_cursor_execute", fn)
        return len(n)

    _post(h, title=tag, imageUrls=["https://a.com/1.jpg"])
    few = count_queries()
    for _ in range(6):
        _post(h, title=tag, imageUrls=["https://a.com/1.jpg"])
    assert count_queries() == few


# ---------- 댓글 ----------
def test_comment_crud_and_count():
    h, other = _user(), _user()
    tag = uuid.uuid4().hex[:10]
    pid = _post(h, title=tag).json()["id"]
    r = client.post(f"{API}/posts/{pid}/comments", json={"content": "첫 댓글"}, headers=other)
    assert r.status_code == 201 and r.json()["isMine"] is True
    cid = r.json()["id"]
    client.post(f"{API}/posts/{pid}/comments", json={"content": "둘째"}, headers=h)

    lst = client.get(f"{API}/posts/{pid}/comments", headers=h).json()
    assert [c["content"] for c in lst] == ["첫 댓글", "둘째"]
    assert [c["isMine"] for c in lst] == [False, True]
    item = client.get(f"{API}/posts", params={"keyword": tag}, headers=h).json()["items"][0]
    assert item["commentCount"] == 2

    assert client.patch(f"{API}/comments/{cid}", json={"content": "x"}, headers=h).status_code == 403
    r = client.patch(f"{API}/comments/{cid}", json={"content": "수정"}, headers=other)
    assert r.status_code == 200 and r.json()["content"] == "수정"
    assert client.delete(f"{API}/comments/{cid}", headers=h).status_code == 403
    assert client.delete(f"{API}/comments/{cid}", headers=other).status_code == 204
    assert client.delete(f"{API}/comments/{cid}", headers=other).status_code == 404
    assert len(client.get(f"{API}/posts/{pid}/comments", headers=h).json()) == 1


def test_comment_invalid_and_missing():
    h = _user()
    pid = _post(h).json()["id"]
    assert client.post(f"{API}/posts/{pid}/comments", json={"content": " "}, headers=h).status_code == 400
    assert client.post(f"{API}/posts/{pid}/comments", json={}, headers=h).status_code == 400
    assert client.post(f"{API}/posts/999999999/comments", json={"content": "a"}, headers=h).status_code == 404
    assert client.get(f"{API}/posts/999999999/comments").status_code == 404
    assert client.patch(f"{API}/comments/999999999", json={"content": "a"}, headers=h).status_code == 404
    assert client.delete(f"{API}/comments/999999999", headers=h).status_code == 404
