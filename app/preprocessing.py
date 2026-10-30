"""Text preprocessing utilities for FAQ matching."""
import re
import string
from nltk.stem import PorterStemmer
from nltk.tokenize import RegexpTokenizer

_TOKENIZER = RegexpTokenizer(r"[a-zA-Z0-9]+")
_STEMMER = PorterStemmer()
# Built-in fallback keeps the application usable without downloading NLTK corpora.
_FALLBACK_STOP_WORDS = {
    "a", "an", "the", "is", "are", "was", "were", "be", "been", "being",
    "do", "does", "did", "can", "could", "would", "should", "will", "shall",
    "i", "me", "my", "we", "our", "you", "your", "he", "she", "it", "they",
    "to", "of", "in", "on", "at", "for", "from", "with", "and", "or", "but",
    "what", "when", "where", "who", "why", "how", "please", "tell", "about",
}


def preprocess_text(text):
    """Normalize, tokenize, remove common stop words, and stem tokens."""
    if not isinstance(text, str):
        return ""
    normalized = text.lower().translate(str.maketrans("", "", string.punctuation))
    tokens = _TOKENIZER.tokenize(normalized)
    useful_tokens = [token for token in tokens if token not in _FALLBACK_STOP_WORDS]
    # Retain original tokens if stop-word removal would erase the whole query.
    if not useful_tokens:
        useful_tokens = tokens
    return " ".join(_STEMMER.stem(token) for token in useful_tokens)
