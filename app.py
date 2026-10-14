from flask import Flask, render_template, request, send_file
from sklearn.feature_extraction.text import TfidfVectorizer, ENGLISH_STOP_WORDS
from collections import Counter
import re
import io
import csv

app = Flask(__name__)

def clean_text(text):
    """Normalize text while retaining meaningful word boundaries."""
    text = text.lower()
    text = re.sub(r"https?://\S+|www\.\S+", " ", text)
    text = re.sub(r"[^a-z0-9\s-]", " ", text)
    return re.sub(r"\s+", " ", text).strip()

def extract_tfidf(text, top_n=10):
    cleaned = clean_text(text)
    if not cleaned:
        return []
    vectorizer = TfidfVectorizer(
        stop_words="english",
        ngram_range=(1, 2),
        token_pattern=r"(?u)\b[a-zA-Z][a-zA-Z0-9-]+\b"
    )
    try:
        matrix = vectorizer.fit_transform([cleaned])
        terms = vectorizer.get_feature_names_out()
        scores = matrix.toarray()[0]
        ranked = sorted(zip(terms, scores), key=lambda x: x[1], reverse=True)
        return [{"keyword": term, "score": round(float(score), 4)}
                for term, score in ranked if score > 0][:top_n]
    except ValueError:
        return []

def extract_frequency(text, top_n=10):
    cleaned = clean_text(text)
    words = re.findall(r"\b[a-z][a-z0-9-]*\b", cleaned)
    words = [w for w in words if w not in ENGLISH_STOP_WORDS and len(w) > 2]
    counts = Counter(words)
    total = max(1, sum(counts.values()))
    return [{"keyword": word, "score": round(count / total, 4)}
            for word, count in counts.most_common(top_n)]

def extract_rake(text, top_n=10):
    """A lightweight RAKE-style phrase ranker using stopwords as phrase boundaries."""
    cleaned = clean_text(text)
    words = re.findall(r"\b[a-z][a-z0-9-]*\b", cleaned)
    phrases, current = [], []
    for word in words:
        if word in ENGLISH_STOP_WORDS or len(word) < 2:
            if current:
                phrases.append(current)
                current = []
        else:
            current.append(word)
    if current:
        phrases.append(current)

    freq, degree = Counter(), Counter()
    for phrase in phrases:
        for word in phrase:
            freq[word] += 1
            degree[word] += len(phrase) - 1
    scores = {word: (degree[word] + freq[word]) / freq[word] for word in freq}
    phrase_scores = Counter()
    for phrase in phrases:
        phrase_text = " ".join(phrase)
        phrase_scores[phrase_text] += sum(scores[w] for w in phrase)
    ranked = phrase_scores.most_common(top_n)
    if not ranked:
        return []
    max_score = max(score for _, score in ranked) or 1
    return [{"keyword": phrase, "score": round(score / max_score, 4)}
            for phrase, score in ranked]

@app.route("/", methods=["GET", "POST"])
def index():
    text = ""
    method = "tfidf"
    top_n = 10
    results = []
    error = None
    if request.method == "POST":
        text = request.form.get("text", "").strip()
        method = request.form.get("method", "tfidf")
        try:
            top_n = max(3, min(25, int(request.form.get("top_n", 10))))
        except ValueError:
            top_n = 10
        if len(text.split()) < 3:
            error = "Please enter at least three words to extract useful keywords."
        else:
            if method == "rake":
                results = extract_rake(text, top_n)
            elif method == "frequency":
                results = extract_frequency(text, top_n)
            else:
                method = "tfidf"
                results = extract_tfidf(text, top_n)
            if not results:
                error = "No keywords found. Try entering a longer text."
    return render_template("index.html", text=text, method=method,
                           top_n=top_n, results=results, error=error)

@app.route("/download", methods=["POST"])
def download():
    rows = request.form.get("rows", "")
    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerow(["Keyword", "Relevance Score"])
    for line in rows.splitlines():
        if "\t" in line:
            keyword, score = line.split("\t", 1)
            writer.writerow([keyword, score])
    mem = io.BytesIO(output.getvalue().encode("utf-8-sig"))
    mem.seek(0)
    return send_file(mem, mimetype="text/csv", as_attachment=True,
                     download_name="extracted_keywords.csv")

if __name__ == "__main__":
    app.run(debug=True)
