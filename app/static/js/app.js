const form = document.getElementById("chatForm");
const input = document.getElementById("questionInput");
const messages = document.getElementById("messages");
const welcome = document.getElementById("welcome");
const sendButton = document.getElementById("sendButton");
const suggestions = document.getElementById("suggestions");
const categoryFilter = document.getElementById("categoryFilter");
const clearButton = document.getElementById("clearButton");

const suggestedQuestions = [
  "How can I apply for admission?",
  "When does the library close?",
  "How can I prepare for campus placements?",
  "Where can I check the examination timetable?"
];

function addMessage(text, role, meta = "") {
  welcome.hidden = true;
  const bubble = document.createElement("div");
  bubble.className = `message ${role}`;
  bubble.textContent = text;
  if (meta) {
    const details = document.createElement("span");
    details.className = "message-meta";
    details.textContent = meta;
    bubble.appendChild(details);
  }
  messages.appendChild(bubble);
  messages.scrollTop = messages.scrollHeight;
  return bubble;
}

function renderSuggestions() {
  suggestedQuestions.forEach((question) => {
    const button = document.createElement("button");
    button.type = "button";
    button.className = "suggestion";
    button.textContent = question;
    button.addEventListener("click", () => {
      input.value = question;
      form.requestSubmit();
    });
    suggestions.appendChild(button);
  });
}

async function loadCategories() {
  try {
    const response = await fetch("/api/categories");
    if (!response.ok) throw new Error("Could not load categories");
    const categories = await response.json();
    categories.forEach((category) => {
      const option = document.createElement("option");
      option.value = category;
      option.textContent = category;
      categoryFilter.appendChild(option);
    });
  } catch (error) {
    console.error(error);
  }
}

form.addEventListener("submit", async (event) => {
  event.preventDefault();
  const question = input.value.trim();
  if (!question) return;
  addMessage(question, "user");
  input.value = "";
  sendButton.disabled = true;
  const typing = addMessage("AskMate is finding the closest FAQ...", "bot");
  typing.classList.add("typing");
  try {
    const response = await fetch("/api/chat", {
      method: "POST",
      headers: {"Content-Type": "application/json"},
      body: JSON.stringify({question})
    });
    const data = await response.json();
    typing.remove();
    if (!response.ok) throw new Error(data.error || "Request failed");
    const meta = data.matched
      ? `Matched: ${data.matched_question} · Similarity: ${(data.score * 100).toFixed(1)}%`
      : `No confident FAQ match · Similarity: ${(data.score * 100).toFixed(1)}%`;
    const bubble = addMessage(data.answer, "bot", meta);
    if (data.matched && data.faq_id !== null) {
      const controls = document.createElement("div");
      controls.className = "feedback";
      [["up", "👍 Helpful"], ["down", "👎 Not helpful"]].forEach(([rating, label]) => {
        const button = document.createElement("button");
        button.type = "button";
        button.textContent = label;
        button.addEventListener("click", async () => {
          button.disabled = true;
          try {
            await fetch("/api/feedback", {
              method: "POST",
              headers: {"Content-Type": "application/json"},
              body: JSON.stringify({faq_id: data.faq_id, rating})
            });
            button.textContent = "Thanks!";
          } catch (error) {
            button.disabled = false;
            console.error(error);
          }
        });
        controls.appendChild(button);
      });
      bubble.appendChild(controls);
    }
  } catch (error) {
    typing.remove();
    addMessage(error.message || "Something went wrong. Please try again.", "bot");
  } finally {
    sendButton.disabled = false;
    input.focus();
  }
});

clearButton.addEventListener("click", () => {
  messages.replaceChildren();
  welcome.hidden = false;
  input.focus();
});

categoryFilter.addEventListener("change", async () => {
  const selected = categoryFilter.value;
  try {
    const response = await fetch("/api/faqs");
    const faqs = await response.json();
    const filtered = selected ? faqs.filter((faq) => faq.category === selected) : faqs;
    suggestions.replaceChildren();
    filtered.slice(0, 4).forEach((faq) => {
      const button = document.createElement("button");
      button.type = "button";
      button.className = "suggestion";
      button.textContent = faq.question;
      button.addEventListener("click", () => {
        input.value = faq.question;
        form.requestSubmit();
      });
      suggestions.appendChild(button);
    });
  } catch (error) {
    console.error(error);
  }
});

renderSuggestions();
loadCategories();
