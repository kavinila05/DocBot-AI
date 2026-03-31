import streamlit as st
from loaders import load_document
from utils.splitter import split_text
from vectorstore.chroma_db import create_vector_db
from llm.ollama_llm import load_llm
from langchain.chains import RetrievalQA

st.set_page_config(page_title="DocBot", layout="wide")
st.title("📄🤖 DocBot – Ask Your Document")

uploaded_file = st.file_uploader(
    "Upload a document",
    type=["pdf", "docx", "pptx", "xlsx", "txt"]
)

if uploaded_file:
    with st.spinner("Reading document..."):
        text = load_document(uploaded_file)

    with st.spinner("Splitting text..."):
        docs = split_text(text)

    with st.spinner("Creating vector database..."):
        vectordb = create_vector_db(docs)

    llm = load_llm()
    qa = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=vectordb.as_retriever()
    )

    st.success("✅ Document processed successfully!")

    query = st.text_input("Ask a question from the document:")

    if query:
        with st.spinner("Thinking..."):
            answer = qa.run(query)
        st.markdown(f"### 🧠 Answer:\n{answer}")
