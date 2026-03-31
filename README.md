# 📄 DocBot – Ask Questions from Your Documents

DocBot is a **local, cost-free AI tool** that allows users to upload documents and ask natural language questions about their content.  
The entire system runs **offline**, using open-source models and libraries.

---

## 🔍 What This Project Does

DocBot can:

- Read documents such as PDF, DOCX, PPTX, Excel, and TXT files  
- Convert document content into searchable knowledge  
- Answer user questions using a local AI model  
- Work without any paid APIs or internet connection after setup  

This project is suitable for:

- Academic document analysis  
- Research paper question answering  
- Resume and report understanding  
- Local AI experimentation  

---

## 🧠 System Architecture (High Level)

1. User uploads a document  
2. Document text is extracted  
3. Text is split into manageable chunks  
4. Chunks are embedded into vectors  
5. Relevant content is retrieved  
6. A local language model generates the final answer  

---

## 🧰 Technology Stack

- **Programming Language:** Python  
- **User Interface:** Streamlit  
- **Large Language Model:** Mistral (via Ollama)  
- **Framework:** LangChain  
- **Vector Database:** ChromaDB  
- **Embeddings Model:** all-MiniLM-L6-v2 (Hugging Face)  

---

## ⚙️ Setup Instructions

### Step 1: Install Python

Ensure **Python 3.9 or above** is installed on your system.

---

### Step 2: Install Ollama
  - Download and install Ollama from the official website: https://ollama.com
  - After installation, download the Mistral model (one-time setup): 
  
  `ollama pull mistral`
  
---

### Step 3: Install Python Dependencies

Navigate to the project directory and install dependencies:

`pip install -r requirements.txt`

---

### Step 4: Run the Application

Start the Streamlit application:

`streamlit run app.py`


A browser window will open automatically.

---

## 🧪 How to Use DocBot

1. Upload a document using the file uploader  
2. Wait for the document to process  
3. Enter a question related to the document  
4. Read the AI-generated response  

---

## 📑 Supported File Types

- PDF files (`.pdf`)  
- Word documents (`.docx`)  
- PowerPoint presentations (`.pptx`)  
- Excel files (`.xlsx`)  
- Text files (`.txt`)  

---

## 🚫 Limitations

- Very large documents may take longer to process  
- Image-only or scanned PDFs are not supported  
- Answer accuracy depends on document clarity and structure  

---

## 🔐 Privacy and Cost

- Runs **entirely on local machine**  
- No data leaves the system  
- No paid APIs or subscriptions required  

---

## 🚀 Future Improvements

- Source citation in answers  
- Chat history support  
- Multi-document querying  
- Docker-based deployment  

---

## 📜 License

This project is open-source and intended for **educational and research purposes**.

---

## 🙋 Author 

Kavinila_V

---

## Collaborator

Priyadharshini_V





