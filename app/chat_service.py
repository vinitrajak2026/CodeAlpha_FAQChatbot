"""Business logic for selecting an FAQ answer or fallback."""
class ChatService:
    def __init__(self, matcher, threshold, fallback_message):
        self.matcher = matcher
        self.threshold = float(threshold)
        self.fallback_message = fallback_message

    def answer(self, question):
        result = self.matcher.find_best_match(question)
        if result is None:
            return {
                "matched": False,
                "answer": self.fallback_message,
                "score": 0.0,
                "category": None,
                "matched_question": None,
                "faq_id": None,
            }
        if result["score"] < self.threshold:
            return {
                "matched": False,
                "answer": self.fallback_message,
                "score": result["score"],
                "category": None,
                "matched_question": None,
                "faq_id": None,
            }
        return {
            "matched": True,
            "answer": result["answer"],
            "score": result["score"],
            "category": result["category"],
            "matched_question": result["matched_question"],
            "faq_id": result["faq_id"],
        }
