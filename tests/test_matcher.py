import json
import os
from app.faq_loader import load_faqs
from app.matcher import FAQMatcher


def make_matcher():
    path = os.path.join(os.path.dirname(__file__), "..", "data", "faqs.json")
    faqs = load_faqs(os.path.abspath(path))
    return FAQMatcher(faqs)


def test_library_variation_matches_library_faq():
    result = make_matcher().find_best_match("When does the library close?")
    assert result is not None
    assert result["faq_id"] == 7


def test_admission_question_matches_admission_faq():
    result = make_matcher().find_best_match("How do I join the college?")
    assert result["faq_id"] == 1


def test_empty_query_has_no_match():
    assert make_matcher().find_best_match("   ") is None
