# AI-Based Revision & Self-Assessment System

This project is an AI-based revision and self-assessment system designed to help students actively revise study material by automatically generating questions and evaluating their answers.
The main intention of this project is to move beyond passive reading and enable **active recall**, which is proven to improve learning and understanding.

## Motivation & Intention

Students often revise by re-reading notes, which is inefficient and does not test understanding.  
The goal of this project is to:

- Convert plain study material into **interactive revision questions**
- Help students **test their understanding**
- Provide **approximate, semantic-based evaluation** instead of strict memorization-based checking

This system is designed as a **learning aid**, not as a strict examination or grading system.

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

## AI & NLP Techniques Used

- **Sentence Embeddings** (Sentence Transformers)
- **Cosine Similarity** for semantic comparison
- **spaCy Dependency Parsing** for concept extraction
- **Noun Phrase Chunking** to avoid meaningless questions
- **Pronoun Filtering** to prevent invalid questions
- **Heuristic-Based Question Generation**
- **Approximate Answer Evaluation**

## Features

- Generates questions automatically from any study text
- Supports:
  - Short Answer questions
  - Fill-in-the-Blank questions
- Semantic answer evaluation (flexible phrasing allowed)
- Avoids pronoun-based and meaningless questions
- Interactive Streamlit interface
- Handles edge cases like weak or unsuitable sentences

## Technologies Used

- Python
- Streamlit
- NLTK
- spaCy
- Sentence Transformers
- Scikit-learn
- NumPy

##  How to Run the Project

```bash
pip install -r requirements.txt
streamlit run revisionsystem_streamlit.py


## Limitation

- Question generation is heuristic-based and rule-driven using NLP patterns, so some edge-case sentences may not always convert into perfect questions.
- Short-answer evaluation is based on semantic similarity using sentence embeddings, which provides approximate understanding rather than strict correctness.
- Deep analytical, evaluative, or multi-step reasoning questions are not currently generated.
- Coreference resolution (handling references like “they”, “it”, “this”) is not fully implemented; such cases are intentionally skipped to avoid meaningless questions.
- Large NLP models (SentenceTransformer and spaCy) may increase startup time and memory usage on low-resource systems.
- User progress and learning history are not persisted across sessions.


## Future Enhancements

- Multiple Choice Question (MCQ) generation with intelligent distractors  
- Long-answer and descriptive question generation  
- Flashcard generation for spaced repetition learning  
- AI-powered revision chatbot for conversational explanations  
- Adaptive revision loop that revisits weak concepts automatically  
- Keyword-based scoring combined with embeddings for better answer evaluation  
- Difficulty-level tagging (easy, medium, hard) for personalized revision  
- User progress tracking and performance analytics  
- Coreference resolution to intelligently handle pronouns  
- LLM-based question refinement for higher-quality questions  
- Deployment-ready optimizations for scalable real-world use  


## Academic Relevance

This project demonstrates the practical application of:

- Natural Language Processing (NLP)  
- Semantic AI using sentence embeddings  
- Educational Technology  
- Human-centered AI design  

It serves as a functional academic prototype that bridges AI concepts with real-world learning applications.

## Conclusion

The AI-Based Revision & Self-Assessment System provides an interactive and intelligent way for students to revise study material using AI techniques.  
By transforming static notes into dynamic questions and enabling semantic answer evaluation, the system promotes active learning and conceptual understanding.
While it does not replace teachers or formal assessments, it effectively supports self-learning and serves as a strong foundation for building more advanced educational AI systems.

