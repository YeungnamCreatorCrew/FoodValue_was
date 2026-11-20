import pytest


@pytest.fixture(autouse=True)
def _no_price_summary_llm(monkeypatch):
    """테스트는 외부 LLM을 부르지 않는다. 가격 문장은 고정 문장으로 만들어진다(개별 테스트에서 다시 바꿀 수 있다)."""
    from app.services import price_summary

    def offline(prompt):
        raise ConnectionError('테스트에서는 Gemini를 호출하지 않습니다')
    monkeypatch.setattr(price_summary, '_call_gemini', offline)
