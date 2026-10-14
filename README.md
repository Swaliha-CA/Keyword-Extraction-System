# 🔑 Keyword Extraction System

An NLP-based application that automatically extracts important keywords and phrases from text documents using **TF-IDF, RAKE-style phrase extraction, and Word Frequency** techniques.

## 📌 Project Overview

The Keyword Extraction System helps users identify the most important words and phrases from paragraphs, articles, research papers, and other text documents. It applies text preprocessing and keyword-ranking techniques to produce an easy-to-understand list of relevant terms.

The project is implemented using Python and can be executed in Google Colab or as a Flask web application.

## 🎯 Objectives

- Automatically extract meaningful keywords from text.
- Apply basic text preprocessing techniques.
- Implement and compare three keyword extraction methods.
- Rank keywords based on method-specific relevance scores.
- Display extracted keywords in a readable format.
- Allow users to download results as a CSV file in the Flask version.

## ✨ Features

- **User Input:** Enter a paragraph or text document.
- **Text Preprocessing:** Lowercase conversion, punctuation handling, and stop-word filtering.
- **TF-IDF:** Rank terms and two-word phrases using TF-IDF scores.
- **RAKE-style Extraction:** Identify and rank candidate keyword phrases.
- **Word Frequency:** Rank words based on their frequency.
- **Custom Keyword Count:** Select the number of keywords to display.
- **Ranked Results:** View keywords with their scores.
- **CSV Export:** Download results from the Flask web application.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Flask | Web application framework |
| scikit-learn | TF-IDF and stop-word processing |
| Pandas | Tabular result presentation in Colab |
| HTML | Web page structure |
| CSS | User interface styling |
| Google Colab | Cloud-based development and testing |
| GitHub | Source code management |

## ⚙️ Installation and Execution

### Option 1: Run in Google Colab

1. Open [Google Colab](https://colab.research.google.com/).
2. Create a new notebook.
3. Install the required libraries:

   ```python
   !pip install -q flask scikit-learn pandas
   ```

4. Copy the keyword extraction functions into a code cell.
5. Enter your text when prompted.
6. Select an extraction method:
   - `1` — TF-IDF
   - `2` — RAKE-style extraction
   - `3` — Word Frequency
7. Enter the number of keywords to extract.
8. View the ranked results and optionally download them as CSV.

### Option 2: Run the Flask Web Application

**Prerequisites:** Python 3.10 or newer and pip.

1. Clone the repository:

   ```bash
   git clone https://github.com/Swaliha-CA/Keyword-Extraction-System.git
   ```

2. Open the project directory:

   ```bash
   cd Keyword-Extraction-System
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Start the application:

   ```bash
   python app.py
   ```

5. Open the following URL in your browser:

   `http://127.0.0.1:5000`

6. Enter text, choose an extraction method, and click **Extract Keywords**.

## 🔄 System Workflow

1. **Text Input:** The user provides a paragraph or document.
2. **Preprocessing:** The system normalizes text and removes selected unwanted characters.
3. **Method Selection:** The user selects TF-IDF, RAKE-style extraction, or Word Frequency.
4. **Keyword Extraction:** The selected algorithm identifies and scores candidate terms.
5. **Ranking:** Keywords are sorted according to their scores.
6. **Output:** The ranked keywords are displayed to the user.
7. **Export:** The Flask application allows the user to download the results as a CSV file.

## 🧪 Example

**Input:**

> Machine learning is a branch of artificial intelligence. Natural language processing helps computers understand human language. Keyword extraction identifies important words from text documents.

**Possible extracted keywords:**

- Machine learning
- Artificial intelligence
- Natural language processing
- Human language
- Text documents

*The actual output and ranking depend on the selected algorithm and implementation.*

## 📊 Evaluation

The system can be evaluated using a collection of documents with manually identified reference keywords.

- **Precision@K:** Proportion of the top K extracted keywords that are relevant.
- **Recall@K:** Proportion of reference keywords found among the top K results.
- **F1-score:** Harmonic mean of precision and recall.
- **Processing Time:** Time required to extract and rank keywords.

Performance values should be reported only after running experiments on a labelled dataset.

## ⚠️ Limitations

- Primarily designed for English text.
- TF-IDF fitted to a single document provides limited corpus-level rarity information.
- The included RAKE-style method is a simplified educational implementation.
- Frequent words are not always the most meaningful keywords.
- PDF/DOCX upload and semantic embedding-based extraction are not included in the current starter implementation.

## 🚀 Future Enhancements

- Support PDF and DOCX document uploads.
- Implement corpus-level TF-IDF.
- Add TextRank and KeyBERT algorithms.
- Support Malayalam and other languages.
- Add automatic evaluation and performance comparison.
- Improve phrase extraction and keyword relevance.

## 👩‍💻 Author

**Swaliha C.A.**

GitHub: [@Swaliha-CA](https://github.com/Swaliha-CA)

## 🔗 Project Repository

[Keyword Extraction System](https://github.com/Swaliha-CA/Keyword-Extraction-System)

## 📄 License

This project is intended for educational and academic use. A formal open-source license can be added to the repository if you wish to permit reuse under specified terms.
