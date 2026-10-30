import os
import pytest
from app import create_app


@pytest.fixture()
def app(tmp_path):
    faq_file = os.path.join(os.path.dirname(__file__), "..", "data", "faqs.json")
    app = create_app({
        "TESTING": True,
        "FAQ_FILE": os.path.abspath(faq_file),
        "SIMILARITY_THRESHOLD": 0.15,
        "MAX_QUESTION_LENGTH": 300,
        "FEEDBACK_FILE": str(tmp_path / "feedback.jsonl"),
        "FALLBACK_MESSAGE": "No relevant answer found.",
    })
    return app


@pytest.fixture()
def client(app):
    return app.test_client()
