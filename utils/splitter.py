from langchain.text_splitter import CharacterTextSplitter

def split_text(text):
    splitter = CharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=100
    )
    return splitter.create_documents([text])
