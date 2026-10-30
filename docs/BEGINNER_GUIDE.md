# AskMate AI — Beginner Guide

## 1. What is NLP?

Natural Language Processing (NLP) is a field of AI that helps computers work with human language, such as written questions.

In this project, NLP is used to prepare a question so that it can be compared with stored FAQ questions.

## 2. What is tokenization?

Tokenization splits a sentence into smaller parts called tokens, usually words.

Example: `library timings today` becomes `["library", "timings", "today"]`.

## 3. What is text preprocessing?

Text preprocessing cleans text before it is given to the matching algorithm. This project lowercases text, removes punctuation, tokenizes it, removes common stop words and stems remaining tokens.

## 4. What are stop words?

Stop words are common words that often add little value to a search, such as “the”, “is” and “a”. Removing them can make important terms easier to compare.

## 5. What is stemming?

Stemming reduces related word forms to a shorter root-like form. For example, “closing” and “closed” may be reduced to related stems. A stem is not always a valid dictionary word.

## 6. What is TF-IDF?

TF-IDF stands for Term Frequency–Inverse Document Frequency. It converts text into numbers (vectors). Terms that are frequent in one text but less common across the collection can receive higher weight.

## 7. What is cosine similarity?

Cosine similarity compares two vectors by measuring the cosine of the angle between them. In simple terms, it estimates how similar their word-weight patterns are. A higher score indicates a closer match.

## 8. Library example, step by step

Stored FAQ:
- Question: `What are the library timings?`
- Variation: `When does the library close?`
- Answer: `For this demo knowledge base, the library is shown as open from 9 AM to 6 PM. These are sample timings, not official college timings.`

User asks:
`When does the library close?`

1. The browser sends the question to the Flask API.
2. The API checks that the question is valid.
3. Preprocessing lowercases and tokenizes it, removes common words and stems useful tokens.
4. The word TF-IDF vectorizer converts the cleaned question into a numeric vector.
5. A character n-gram vectorizer also represents the original text to help with small spelling differences.
6. Cosine similarity compares the query with all stored FAQ questions and variations.
7. The best phrase is associated with FAQ ID 7.
8. The chat service checks the score against the configured threshold.
9. If the score meets the threshold, the matching answer is returned. Otherwise the fallback message is returned.
10. JavaScript displays the answer in a chatbot message bubble.

The alternate phrase is important because “when does the library close” and “what are the library timings” do not share all the same words. Variations give the retriever another phrase to compare.

## 9. How does Flask connect frontend and backend?

JavaScript uses `fetch()` to send JSON to `/api/chat`. Flask receives the request, calls the chat service, and sends a JSON response. JavaScript reads that response and updates the page.

## 10. What is the fallback mechanism?

Sometimes the user's question is unrelated to all stored FAQs. The matcher still finds the highest score, but the chat service compares it with a minimum threshold. If it is too low, the bot says it could not find a relevant answer.

## 11. Important files

- `data/faqs.json`: all FAQ questions, variations and answers.
- `app/preprocessing.py`: text cleaning and stemming.
- `app/matcher.py`: TF-IDF and cosine similarity.
- `app/chat_service.py`: threshold and fallback logic.
- `app/routes.py`: Flask API endpoints.
- `app/static/js/app.js`: browser-side chat behaviour.
- `config.py`: application settings.
