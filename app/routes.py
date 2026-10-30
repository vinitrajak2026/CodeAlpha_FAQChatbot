"""JSON API endpoints."""
import json
import os
from datetime import datetime, timezone
from flask import Blueprint, current_app, jsonify, request


def create_api_blueprint():
    api = Blueprint("api", __name__, url_prefix="/api")

    @api.post("/chat")
    def chat():
        payload = request.get_json(silent=True)
        if not isinstance(payload, dict):
            return jsonify({"error": "Request body must be valid JSON."}), 400
        question = payload.get("question")
        if not isinstance(question, str) or not question.strip():
            return jsonify({"error": "Please enter a question."}), 400
        max_length = current_app.config["MAX_QUESTION_LENGTH"]
        if len(question) > max_length:
            return jsonify({"error": f"Question must be {max_length} characters or fewer."}), 400
        result = current_app.extensions["chat_service"].answer(question.strip())
        return jsonify(result), 200

    @api.get("/faqs")
    def faqs():
        items = current_app.extensions["faq_items"]
        return jsonify([{
            "id": item["id"],
            "category": item["category"],
            "question": item["question"],
        } for item in items]), 200

    @api.get("/categories")
    def categories():
        items = current_app.extensions["faq_items"]
        names = sorted({item["category"] for item in items})
        return jsonify(names), 200

    @api.post("/feedback")
    def feedback():
        payload = request.get_json(silent=True)
        if not isinstance(payload, dict):
            return jsonify({"error": "Request body must be valid JSON."}), 400
        faq_id = payload.get("faq_id")
        rating = payload.get("rating")
        if faq_id is None or rating not in ("up", "down"):
            return jsonify({"error": "faq_id and rating ('up' or 'down') are required."}), 400
        path = current_app.config["FEEDBACK_FILE"]
        os.makedirs(os.path.dirname(path), exist_ok=True)
        record = {
            "faq_id": faq_id,
            "rating": rating,
            "created_at": datetime.now(timezone.utc).isoformat(),
        }
        with open(path, "a", encoding="utf-8") as file:
            file.write(json.dumps(record) + "\n")
        return jsonify({"message": "Thank you for your feedback."}), 201

    return api
