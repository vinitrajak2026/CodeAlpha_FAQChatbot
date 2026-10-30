# CodeAlpha Submission Pack

## 1. GitHub commands

Create a GitHub repository named `CodeAlpha_FAQChatbot`, then run:

```bash
git init
git add .
git commit -m "Build AskMate AI FAQ chatbot"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/CodeAlpha_FAQChatbot.git
git push -u origin main
```

Replace `YOUR_USERNAME` with your own GitHub username.

## 2. 3–5 minute demonstration script

**0:00–0:30 — Introduction**
“Hello, this is AskMate AI, an NLP-based FAQ chatbot developed for my CodeAlpha Artificial Intelligence Internship. It retrieves answers from a prepared FAQ knowledge base.”

**0:30–1:15 — User interface**
Show the home page, category filter and suggested questions.

**1:15–2:00 — Matching demonstration**
Ask “When does the library close?” Show the matched FAQ, answer and similarity score.

**2:00–2:40 — Fallback demonstration**
Ask an unrelated question and show that the chatbot does not invent an answer when the similarity is below the threshold.

**2:40–3:30 — Technical explanation**
Briefly show `preprocessing.py`, `matcher.py`, `chat_service.py` and `faqs.json`. Explain preprocessing, TF-IDF, cosine similarity and the threshold.

**3:30–4:00 — API and tests**
Show `/api/faqs`, `/api/categories` and the test command. Mention only tests that you actually ran.

**4:00–4:30 — Closing**
Summarize the project and show the GitHub repository.

## 3. LinkedIn post draft

I’m excited to share **AskMate AI**, an NLP-based FAQ Chatbot developed as part of my CodeAlpha Artificial Intelligence Internship.

The project uses Python, NLTK, Scikit-learn and Flask. It preprocesses user questions, represents FAQ text using TF-IDF, and uses cosine similarity to retrieve the closest matching answer. A configurable threshold helps the chatbot return a fallback response when no sufficiently relevant FAQ is found.

**Key features**
- NLP text preprocessing
- TF-IDF vectorization
- Cosine similarity-based FAQ retrieval
- Flask REST API
- Interactive web chat interface
- FAQ categories and feedback

GitHub: [Add your repository link]

#CodeAlpha #ArtificialIntelligence #NLP #Python #MachineLearning #Flask

## 4. Viva questions and answers

**Q1. What is the main purpose of AskMate AI?**  
It retrieves relevant prepared answers from an FAQ knowledge base based on a user's natural-language question.

**Q2. What is NLP?**  
Natural Language Processing is a field of AI that helps computers process human language.

**Q3. Why is preprocessing needed?**  
It reduces unnecessary differences in text so that matching can work more consistently.

**Q4. What is tokenization?**  
It is the process of splitting text into smaller units such as words.

**Q5. What is stemming?**  
It reduces related word forms to a common stem.

**Q6. What is TF-IDF?**  
It converts text into weighted numerical vectors based on term frequency and inverse document frequency.

**Q7. What is cosine similarity?**  
It measures similarity between vectors by comparing their direction.

**Q8. Why use cosine similarity?**  
It provides a simple way to rank FAQ questions by how closely their vector representations match the user's query.

**Q9. Why are FAQ variations used?**  
Different users can ask the same question in different words. Variations add alternate phrasings to the searchable knowledge base.

**Q10. What is a threshold?**  
It is the minimum similarity score required before the system returns a stored answer.

**Q11. Why use Flask?**  
Flask provides backend routes that receive frontend requests and return JSON responses.

**Q12. Is this a generative AI chatbot?**  
No. It is a retrieval-based NLP chatbot. It selects an answer already stored in the FAQ dataset rather than generating new answers.

## 5. Final checklist

- [ ] Run the application locally.
- [ ] Run `pytest -q` and record the actual result.
- [ ] Test a normal FAQ question.
- [ ] Test a differently phrased question.
- [ ] Test an unrelated question and verify fallback behaviour.
- [ ] Check the category filter and feedback buttons.
- [ ] Replace demo answers only with verified information if needed.
- [ ] Add genuine screenshots to the repository.
- [ ] Push source code to `CodeAlpha_FAQChatbot`.
- [ ] Record a 3–5 minute project video.
- [ ] Publish the LinkedIn post with the GitHub link and tag CodeAlpha.
- [ ] Submit through the official internship submission form.

Do not claim that tests passed, that the chatbot is deployed, or that information is official unless you have verified those statements yourself.
