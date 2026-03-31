from langchain.vectorstores import Chroma
from langchain.embeddings import HuggingFaceEmbeddings

def create_vector_db(documents):
    embeddings = HuggingFaceEmbeddings(
        model_name="all-MiniLM-L6-v2"
    )
    return Chroma.from_documents(documents, embeddings)
