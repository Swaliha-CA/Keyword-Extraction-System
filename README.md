# Automatic Keyword Extraction from Text Documents Using NLP

A small course-project web application that extracts and ranks keywords from user-provided text using three approaches:
- **TF-IDF:** ranks informative words and two-word phrases within the supplied text.
- **RAKE-style extraction:** generates candidate phrases using stop-word boundaries and scores them from word frequency and degree.
- **Word frequency baseline:** ranks non-stop words by normalized frequency.

## Requirements
- Python 3.10 or newer
- pip

## Run locally
1. Extract the ZIP file.
2. Open a terminal in the `keyword_extraction_nlp` folder.
3. Create and activate a virtual environment (recommended):
   - Windows: `py -m venv .venv` then `.venv\\Scripts\\activate`
   - macOS/Linux: `python3 -m venv .venv` then `source .venv/bin/activate`
4. Install packages: `pip install -r requirements.txt`
5. Start the app: `python app.py`
6. Open `http://127.0.0.1:5000` in your browser.

## Example input
Natural language processing enables computers to analyze human language. Keyword extraction identifies important terms from documents and research papers. TF-IDF ranks terms based on their importance, while RAKE can identify meaningful multi-word phrases.

## Course-project modules
1. Text input
2. Text normalization
3. Keyword candidate generation
4. Keyword scoring and ranking
5. Results visualization
6. CSV export

## Evaluation plan
Prepare 20–50 sample documents and manually annotate the important keywords for each document. Compare the top-k system output against the annotated keywords using:
- Precision@K = relevant extracted keywords in top K / K
- Recall@K = relevant extracted keywords in top K / total relevant keywords
- F1 = 2 × Precision × Recall / (Precision + Recall)

Compare TF-IDF, RAKE-style extraction, and frequency baseline on the same documents. Report average Precision@5, Recall@5, and F1@5.

## Limitations
- TF-IDF is normally strongest when computed across a collection of documents. In this demo, it is fitted to the single input, so its IDF component is limited; treat it as a practical baseline, not a full corpus-level TF-IDF evaluation.
- The RAKE-style method is a lightweight educational implementation, not a complete external RAKE library.
- The system uses English stop words and is intended for English text.
- Scores from different methods are not directly comparable.

## Possible future enhancements
- PDF/DOCX upload
- Compare against KeyBERT or TextRank
- Corpus-level TF-IDF using a document collection
- Support Malayalam and other languages
- Add automatic evaluation on a labelled dataset
