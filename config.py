"""Application configuration."""
import os
from dotenv import load_dotenv

load_dotenv()
BASE_DIR = os.path.abspath(os.path.dirname(__file__))


class Config:
    SIMILARITY_THRESHOLD = float(os.getenv("SIMILARITY_THRESHOLD", "0.20"))
    FAQ_FILE = os.path.join(BASE_DIR, os.getenv("FAQ_FILE", "data/faqs.json"))
    FEEDBACK_FILE = os.path.join(BASE_DIR, "data", "feedback.jsonl")
    MAX_QUESTION_LENGTH = int(os.getenv("MAX_QUESTION_LENGTH", "300"))
    DEBUG = os.getenv("FLASK_DEBUG", "0") == "1"
    FALLBACK_MESSAGE = (
        "Sorry, I couldn't find a sufficiently relevant answer. "
        "Try rephrasing your question or choose one of the suggested questions."
    )
