"""TF-IDF and cosine-similarity FAQ matcher."""
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from app.preprocessing import preprocess_text


class FAQMatcher:
    def __init__(self, faqs):
        if not faqs:
            raise ValueError("FAQMatcher requires at least one FAQ.")
        self.faqs = faqs
        self.documents = []
        self.document_faq_indices = []
        for index, faq in enumerate(faqs):
            phrases = [faq["question"]] + faq.get("variations", [])
            for phrase in phrases:
                cleaned = preprocess_text(phrase)
                if cleaned:
                    self.documents.append(cleaned)
                    self.document_faq_indices.append(index)
        if not self.documents:
            raise ValueError("No usable FAQ questions were found.")
        # Character n-grams improve tolerance to small spelling differences.
        self.word_vectorizer = TfidfVectorizer(ngram_range=(1, 2), analyzer="word")
        self.char_vectorizer = TfidfVectorizer(
            analyzer="char_wb", ngram_range=(2, 5), min_df=1
        )
        self.word_matrix = self.word_vectorizer.fit_transform(self.documents)
        self.char_matrix = self.char_vectorizer.fit_transform(self.documents)

    def find_best_match(self, question):
        cleaned = preprocess_text(question)
        if not cleaned:
            return None
        word_query = self.word_vectorizer.transform([cleaned])
        char_query = self.char_vectorizer.transform([question.lower()])
        word_scores = cosine_similarity(word_query, self.word_matrix)[0]
        char_scores = cosine_similarity(char_query, self.char_matrix)[0]
        combined = (0.75 * word_scores) + (0.25 * char_scores)

        # Keep the highest-scoring phrase for each FAQ, so variations do not
        # cause duplicate FAQ results.
        best_by_faq = {}
        for phrase_index, score in enumerate(combined):
            faq_index = self.document_faq_indices[phrase_index]
            best_by_faq[faq_index] = max(best_by_faq.get(faq_index, 0.0), float(score))

        best_index = max(best_by_faq, key=best_by_faq.get)
        faq = self.faqs[best_index]
        return {
            "faq_id": faq["id"],
            "category": faq["category"],
            "matched_question": faq["question"],
            "answer": faq["answer"],
            "score": round(best_by_faq[best_index], 4),
        }
