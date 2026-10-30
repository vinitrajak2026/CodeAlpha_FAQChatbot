"""Flask application factory."""
from flask import Flask, render_template
from config import Config
from app.faq_loader import load_faqs
from app.matcher import FAQMatcher
from app.chat_service import ChatService
from app.routes import create_api_blueprint


def create_app(test_config=None):
    app = Flask(__name__)
    app.config.from_object(Config)
    if test_config:
        app.config.update(test_config)

    faqs = load_faqs(app.config["FAQ_FILE"])
    matcher = FAQMatcher(faqs)
    chat_service = ChatService(
        matcher=matcher,
        threshold=app.config["SIMILARITY_THRESHOLD"],
        fallback_message=app.config["FALLBACK_MESSAGE"],
    )
    app.extensions["faq_items"] = faqs
    app.extensions["chat_service"] = chat_service

    @app.get("/")
    def home():
        return render_template("index.html")

    app.register_blueprint(create_api_blueprint())
    return app
