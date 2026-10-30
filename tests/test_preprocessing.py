from app.preprocessing import preprocess_text


def test_preprocessing_lowercases_and_removes_punctuation():
    assert preprocess_text("LIBRARY, Timings!") == "librari time"


def test_preprocessing_handles_empty_input():
    assert preprocess_text("") == ""


def test_preprocessing_handles_non_string():
    assert preprocess_text(None) == ""
