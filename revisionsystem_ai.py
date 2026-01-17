import nltk
from nltk.tokenize import sent_tokenize
import numpy as np
import spacy
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import re


try:
    nltk.data.find("tokenizers/punkt")
except LookupError:
    nltk.download("punkt", quiet=True)


model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")
nlp = spacy.load("en_core_web_sm")

PRONOUNS = {
    "it", "they", "this", "these", "those", "them", "their", "its",
    "he", "she", "we", "i", "you", "there", "here", "that"
}



def preprocess_text(text):
    if not text or not text.strip():
        return []
    return sent_tokenize(text)

def get_top_sentences(sentences, top_k=10):
    if not sentences:
        return []

    embeddings = model.encode(sentences)
    doc_embedding = np.mean(embeddings, axis=0)

    scored = []
    for i, s in enumerate(sentences):
        score = cosine_similarity(
            embeddings[i].reshape(1, -1),
            doc_embedding.reshape(1, -1)
        )[0][0]
        scored.append((s, score))

    scored.sort(key=lambda x: x[1], reverse=True)
    return [s for s, _ in scored[:top_k]]



def clean_concept(text):
    return re.sub(r"^(the|a|an)\s+", "", text.strip(), flags=re.I)

def get_main_concept(sentence):
    doc = nlp(sentence)

    
    for chunk in doc.noun_chunks:
        if chunk.root.dep_ in {"nsubj", "nsubjpass"}:
            first = chunk.text.split()[0].lower()
            if first not in PRONOUNS:
                return clean_concept(chunk.text)

    
    candidates = [
        clean_concept(c.text)
        for c in doc.noun_chunks
        if c.text.split()[0].lower() not in PRONOUNS
    ]

    if candidates:
        return max(candidates, key=len)

    
    return None

def classify_sentence(sentence):
    doc = nlp(sentence)

    if any(tok.lemma_ == "be" and tok.dep_ == "ROOT" for tok in doc):
        return "definition"

    if any(tok.lemma_ in {"enable", "allow", "cause", "form", "flow"} for tok in doc):
        return "explanation"

    if any(tok.lemma_ in {"use", "apply", "harness"} for tok in doc):
        return "application"

    return "other"


def generate_questions(top_sentences, qn_limit):
    questions = []
    seen = set()

    for s in top_sentences:
        q_type = classify_sentence(s)
        concept = get_main_concept(s)

        if not concept:
            continue  

        base = re.sub(r"[^\w\s]", "", concept.lower())
        if base in seen:
            continue

        if q_type == "definition":
            if concept.lower().endswith("s"):
                q_text = f"What are {concept}?"
            else:
                q_text = f"What is {concept}?"

        elif q_type == "explanation":
            q_text = f"Explain {concept}."

        elif q_type == "application":
            q_text = f"Where is {concept} used?"

        else:
            continue  

        seen.add(base)
        questions.append({
            "type": q_type,
            "question": q_text,
            "answer": s
        })

        if len(questions) >= qn_limit:
            break

    return questions



def evaluate_short_answer(user_answer, reference_answer):
    if not user_answer or not user_answer.strip():
        return 0.0

    ref_emb = model.encode(reference_answer)
    user_emb = model.encode(user_answer)

    score = cosine_similarity(
        np.array(ref_emb).reshape(1, -1),
        np.array(user_emb).reshape(1, -1)
    )[0][0]

    score = (score + 1) / 2  
    return max(0.0, min(1.0, score))



def generate_fill_blank(answer_sentence):
    doc = nlp(answer_sentence)

    chunks = [
        c.text for c in doc.noun_chunks
        if c.text.split()[0].lower() not in PRONOUNS
    ]

    if not chunks:
        return None, None

    target = max(chunks, key=len)
    masked = re.sub(re.escape(target), "__________", answer_sentence, count=1, flags=re.I)
    return masked, target.lower()

def evaluate_fill_blank(user_answer, correct_answer):
    if not user_answer or not correct_answer:
        return False

    norm = lambda s: re.sub(r"\W+", "", s.lower())
    return norm(user_answer) == norm(correct_answer)
