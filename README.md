# AI-Based Revision & Self-Assessment System

This project is an AI-based revision and self-assessment system designed to help students actively revise study material by automatically generating questions and evaluating their answers.

The main intention of this project is to move beyond passive reading and enable **active recall**, which is proven to improve learning and understanding.

---

## Motivation & Intention

Students often revise by re-reading notes, which is inefficient and does not test understanding.  
The goal of this project is to:

- Convert plain study material into **interactive revision questions**
- Help students **test their understanding**
- Provide **approximate, semantic-based evaluation** instead of strict memorization-based checking

This system is designed as a **learning aid**, not as a strict examination or grading system.

---

## How the System Works

1. The user pastes study material (any topic, any paragraph).
2. The system splits the text into sentences.
3. Important sentences are identified using **semantic similarity**.
4. Questions are generated using **NLP heuristics**:
   - Definition questions
   - Explanation questions
   - Application-based questions
5. The user answers the questions.
6. Answers are evaluated using **semantic similarity**, not exact matching.

---

## AI & NLP Techniques Used

- **Sentence Embeddings** (Sentence Transformers)
- **Cosine Similarity** for semantic comparison
- **spaCy Dependency Parsing** for concept extraction
- **Noun Phrase Chunking** to avoid meaningless questions
- **Pronoun Filtering** to prevent invalid questions
- **Heuristic-Based Question Generation**
- **Approximate Answer Evaluation**

This project focuses on **explainable AI logic**, not black-box generation.

---

## Features

- Generates questions automatically from any study text
- Supports:
  - Short Answer questions
  - Fill-in-the-Blank questions
- Semantic answer evaluation (flexible phrasing allowed)
- Avoids pronoun-based and meaningless questions
- Interactive Streamlit interface
- Handles edge cases like weak or unsuitable sentences

---

## Technologies Used

- Python
- Streamlit
- NLTK
- spaCy
- Sentence Transformers
- Scikit-learn
- NumPy

---

##  How to Run the Project

```bash
pip install -r requirements.txt
streamlit run app.py
