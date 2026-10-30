def test_home_page_loads(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"AskMate AI" in response.data


def test_chat_returns_matching_faq(client):
    response = client.post("/api/chat", json={"question": "When does the library close?"})
    assert response.status_code == 200
    data = response.get_json()
    assert data["matched"] is True
    assert data["faq_id"] == 7
    assert "sample timings" in data["answer"]


def test_chat_rejects_empty_question(client):
    response = client.post("/api/chat", json={"question": " "})
    assert response.status_code == 400


def test_chat_rejects_missing_json(client):
    response = client.post("/api/chat", data="not json", content_type="text/plain")
    assert response.status_code == 400


def test_chat_rejects_too_long_question(client):
    response = client.post("/api/chat", json={"question": "x" * 301})
    assert response.status_code == 400


def test_faq_endpoint(client):
    response = client.get("/api/faqs")
    assert response.status_code == 200
    assert len(response.get_json()) == 20


def test_categories_endpoint(client):
    response = client.get("/api/categories")
    assert response.status_code == 200
    assert "Library" in response.get_json()


def test_feedback_endpoint(client):
    response = client.post("/api/feedback", json={"faq_id": 7, "rating": "up"})
    assert response.status_code == 201


def test_feedback_validation(client):
    response = client.post("/api/feedback", json={"faq_id": 7, "rating": "maybe"})
    assert response.status_code == 400
