
import streamlit as st
from utils.file_loader import load_file
from utils.chunking import chunk_text
from utils.embedding import get_embeddings, model
from utils.faiss_handler import save_index, search_index

st.title("Upload File + Semantic Search with FAISS")

uploaded_file = st.file_uploader("Upload a PDF, TXT, or DOCX file", type=["pdf", "txt", "docx"])

if uploaded_file:
    text = load_file(uploaded_file)
    chunks = chunk_text(text)
    embeddings = get_embeddings(chunks)
    save_index(embeddings, chunks)
    st.success("File uploaded, chunked, and indexed successfully!")

st.divider()
query = st.text_input("🔍 Semantic Search in Document")

if query:
    results = search_index(query, model)
    st.markdown("### 🔎 Top Results:")
    for i, res in enumerate(results, 1):
        st.markdown(f"**Result {i}:** {res[:300]}...")  # limit length
    