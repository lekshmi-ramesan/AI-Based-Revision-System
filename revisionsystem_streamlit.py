import streamlit as st
from revisionsystem_ai import (
    preprocess_text,
    get_top_sentences,
    generate_questions,
    evaluate_short_answer,
    generate_fill_blank,
    evaluate_fill_blank
)

st.set_page_config(page_title="AI Revision System", layout="wide")
st.title("AI Based Revision & Self-Assessment System")

if "questions" not in st.session_state:
    st.session_state.questions = []

text = st.text_area("Paste your study notes here", height=260)
qn_limit = st.slider("Number of Questions (max 10)", 1, 10, 5)
mode = st.selectbox("Answer Mode", ["Short Answer", "Fill in the Blank"])

if st.button("Generate Questions"):
    if not text.strip():
        st.warning("Please paste some study material.")
    else:
        sentences = preprocess_text(text)
        top_sentences = get_top_sentences(sentences)
        qs = generate_questions(top_sentences, qn_limit)

        if not qs:
            st.warning("No meaningful questions could be generated.")
            st.session_state.questions = []
        else:
            st.session_state.questions = qs
            if len(qs) < qn_limit:
                st.warning(f"Only {len(qs)} questions available.")
            else:
                st.success(f"Generated {len(qs)} questions.")



if st.session_state.questions:
    st.markdown("---")

    for idx, q in enumerate(st.session_state.questions):
        st.markdown(f"### Q{idx+1} ({q['type'].capitalize()})")

        
        if mode == "Short Answer":
            st.write(q["question"])
            user_ans = st.text_input("Your answer", key=f"sa_{idx}")

            col1, col2 = st.columns(2)
            if col1.button("Check", key=f"check_sa_{idx}"):
                score = evaluate_short_answer(user_ans, q["answer"])
                st.write(f"Understanding: **{int(score * 100)}%**")

            if col2.button("Show Answer", key=f"show_sa_{idx}"):
                st.info(q["answer"])

       
        else:
            masked, correct = generate_fill_blank(q["answer"])
            if not masked:
                st.info("Fill-in-the-blank not suitable for this sentence.")
                continue

            st.write(masked)
            user_ans = st.text_input("Your answer", key=f"fb_{idx}")

            col1, col2 = st.columns(2)
            if col1.button("Check", key=f"check_fb_{idx}"):
                if evaluate_fill_blank(user_ans, correct):
                    st.success("Correct ✅")
                else:
                    st.error("Incorrect ❌")

            if col2.button("Show Answer", key=f"show_fb_{idx}"):
                st.info(f"Answer: {correct}")
