"""Load and validate the FAQ knowledge base."""
import json


def load_faqs(path):
    try:
        with open(path, "r", encoding="utf-8") as file:
            payload = json.load(file)
    except FileNotFoundError as exc:
        raise RuntimeError(f"FAQ file not found: {path}") from exc
    except json.JSONDecodeError as exc:
        raise RuntimeError(f"FAQ file contains invalid JSON: {exc}") from exc

    faqs = payload.get("faqs") if isinstance(payload, dict) else None
    if not isinstance(faqs, list) or not faqs:
        raise ValueError("FAQ data must contain a non-empty 'faqs' list.")

    seen_ids = set()
    validated = []
    for item in faqs:
        if not isinstance(item, dict):
            raise ValueError("Each FAQ must be a JSON object.")
        required = ("id", "category", "question", "answer")
        if any(key not in item for key in required):
            raise ValueError(f"Each FAQ must contain: {', '.join(required)}.")
        if item["id"] in seen_ids:
            raise ValueError(f"Duplicate FAQ id: {item['id']}")
        if not all(isinstance(item[key], str) and item[key].strip()
                   for key in ("category", "question", "answer")):
            raise ValueError("FAQ category, question and answer must be non-empty strings.")
        variations = item.get("variations", [])
        if not isinstance(variations, list) or not all(
            isinstance(value, str) for value in variations
        ):
            raise ValueError("FAQ variations must be a list of strings.")
        seen_ids.add(item["id"])
        validated.append({
            "id": item["id"],
            "category": item["category"].strip(),
            "question": item["question"].strip(),
            "variations": [v.strip() for v in variations if v.strip()],
            "answer": item["answer"].strip(),
        })
    return validated
