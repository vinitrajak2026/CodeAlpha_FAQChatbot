# AskMate AI — CodeAlpha FAQ Chatbot

A student-support FAQ chatbot built for the **CodeAlpha Artificial Intelligence Internship — Task 2: Chatbot for FAQs**.

> **Important:** The included college FAQs and answers are sample/demo data. They are not official policies or verified information for any real institution.

## 1. Problem statement

Students often need to search through notices or contact offices to find routine information. AskMate AI demonstrates how an NLP-based FAQ system can retrieve a relevant prepared answer from a small knowledge base.

## 2. Objectives

- Store questions and answers in a separate FAQ dataset.
- Preprocess text using NLP techniques.
- Represent FAQ questions using TF-IDF.
- Compare a user's question with FAQ phrases using cosine similarity.
- Return the best answer only when its score meets a configurable threshold.
- Provide a simple web chat interface.

## 3. Features

- Natural-language FAQ matching.
- NLTK tokenization and stemming, with a built-in stop-word list.
- TF-IDF word n-grams and cosine similarity.
- Character n-gram similarity blended into the score to help with small spelling differences.
- Alternate FAQ phrasings (`variations`) to improve recall.
- Configurable fallback threshold.
- Flask JSON API.
- Category filter, suggested questions, chat clear, and feedback buttons.
- Responsive dark interface.

## 4. Technology stack

| Area | Technology |
|---|---|
| Language | Python |
| NLP | NLTK |
| Vectorization | Scikit-learn TF-IDF |
| Similarity | Cosine similarity |
| Backend | Flask |
| Frontend | HTML, CSS, JavaScript |
| Tests | pytest |

## 5. Architecture

1. Browser sends a question to `POST /api/chat`.
2. Flask validates the JSON input and length.
3. `ChatService` calls `FAQMatcher`.
4. Preprocessing normalizes and stems the question.
5. TF-IDF word and character vectors are compared against FAQ question/variation vectors using cosine similarity.
6. The highest-scoring phrase selects its parent FAQ.
7. If the score meets the configured threshold, its answer is returned; otherwise the fallback message is returned.

The matcher is fitted once when the Flask app starts, not on every request.

## 6. Folder structure

```text
CodeAlpha_FAQChatbot/
├── app/
│   ├── __init__.py
│   ├── routes.py
│   ├── chat_service.py
│   ├── matcher.py
│   ├── preprocessing.py
│   ├── faq_loader.py
│   ├── templates/index.html
│   └── static/
│       ├── css/style.css
│       └── js/app.js
├── data/faqs.json
├── tests/
├── docs/
├── config.py
├── run.py
├── requirements.txt
├── .env.example
└── README.md
```

## 7. Installation

Python 3.10 or newer is recommended.

### Windows PowerShell

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
Copy-Item .env.example .env
pip install -r requirements.txt
```

If PowerShell blocks activation, run the commands in Command Prompt:

```bat
venv\Scripts\activate
```

### macOS / Linux

```bash
python3 -m venv venv
source venv/bin/activate
cp .env.example .env
pip install -r requirements.txt
```

## 8. Run the application

```bash
python run.py
```

Open `http://127.0.0.1:5000` in your browser.

## 9. API documentation

### `POST /api/chat`

Request:

```json
{"question": "When does the library close?"}
```

Successful response shape:

```json
{
  "matched": true,
  "answer": "For this demo knowledge base, the library is shown as open from 9 AM to 6 PM. These are sample timings, not official college timings.",
  "score": 0.0,
  "category": "Library",
  "matched_question": "What are the library timings?",
  "faq_id": 7
}
```

The score shown above is illustrative; the actual score is calculated by the installed scikit-learn version and dataset.

### `GET /api/faqs`

Returns FAQ IDs, categories and canonical questions.

### `GET /api/categories`

Returns the available category names.

### `POST /api/feedback`

Request:

```json
{"faq_id": 7, "rating": "up"}
```

Feedback is appended to `data/feedback.jsonl`, which is ignored by Git.

## 10. NLP workflow explained

### Preprocessing

The question is lowercased, punctuation is removed, tokens are extracted, common stop words are removed, and remaining words are stemmed.

Example:

`"When does the library close?"` becomes a normalized token representation similar to `librari close`.

### TF-IDF

TF-IDF means Term Frequency–Inverse Document Frequency. It gives higher weight to terms that are useful for distinguishing one document from others.

### Cosine similarity

Cosine similarity compares two vectors. A larger score means the vectors point in a more similar direction. It is used to rank FAQ phrases against the user's question.

### FAQ variations

A canonical FAQ can include alternate phrasings. For example, the library FAQ includes “when does the library close”. These variations are stored in JSON and vectorized with the canonical question. This is still retrieval-based NLP; it is not a generative AI model.

### Threshold and fallback

`SIMILARITY_THRESHOLD` controls the minimum score needed to return an FAQ answer. If the best score is below the threshold, the bot responds with a fallback instead of confidently returning an unrelated answer. The threshold should be tuned against a representative test set.

## 11. Sample test questions

- How can I apply for admission?
- When does the library close?
- How do I borrow a book?
- How can I prepare for campus placements?
- Where can I check the examination timetable?
- What is the weather on Mars? (should normally trigger fallback)

A retrieval score is not a calibrated probability. A score of 70% should not be described as 70% certainty.

## 12. Testing

Run:

```bash
pytest -q
```

The repository includes unit and API tests. Run them in the same virtual environment after installing requirements. Record your actual local test result here before submission; do not claim tests passed unless you ran them.

## 13. Limitations

- It can only answer questions represented in its FAQ knowledge base.
- TF-IDF and cosine similarity do not understand meaning as deeply as modern language models.
- Alternate phrasings improve matching but need thoughtful maintenance.
- Demo answers must be replaced with verified institution-specific information before real use.
- Similarity scores are ranking signals, not calibrated confidence probabilities.

## 14. Future improvements

- Add a larger reviewed FAQ knowledge base.
- Add multilingual question support.
- Evaluate precision, recall and fallback behaviour on a labelled test set.
- Add an admin interface to manage FAQs.
- Add persistent user sessions and analytics.
- Explore sentence embeddings while retaining a transparent fallback mechanism.

## 15. CodeAlpha submission

- Repository name: `CodeAlpha_FAQChatbot`
- Upload the complete source code and README to GitHub.
- Add genuine screenshots after running the application locally.
- Record a short demonstration video and post it on LinkedIn with the repository link.
- Submit using the official CodeAlpha submission form shared with interns.

## 16. Demo data notice

All FAQs in `data/faqs.json` are fictional sample content for demonstrating the project. Replace them with verified information only if you have permission and authoritative sources.
