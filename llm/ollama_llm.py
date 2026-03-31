from langchain.llms import Ollama

def load_llm():
    return Ollama(model="mistral")
