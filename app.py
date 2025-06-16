import streamlit as st
from parser import extract_text
from llm_utils import generate_flashcards

st.title("📚 Flashcard Generator")

uploaded_file = st.file_uploader("Upload a file (.pdf, .txt)", type=["pdf", "txt"])
subject_type = st.selectbox("Select subject type", ["General", "Biology", "History", "Computer Science"])

text_input = st.text_area("Or paste your content here", height=300)
submit = st.button("Generate Flashcards")

if submit:
    content = extract_text(uploaded_file, text_input)
    flashcards = generate_flashcards(content, subject_type)
    for i, card in enumerate(flashcards, 1):
        st.markdown(f"**Q{i}:** {card['question']}")
        st.markdown(f"**A{i}:** {card['answer']}")
