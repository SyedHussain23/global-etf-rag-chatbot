# 🌍 Global ETF Intelligence Chatbot (RAG)

An end-to-end **Retrieval-Augmented Generation (RAG)** chatbot that answers ETF-related questions using document-grounded responses.

The system retrieves relevant information from ETF documents stored in a vector database and generates accurate answers using an LLM.

⚠️ This project is **educational and research focused** and does not provide financial advice.

---

## 🚀 Project Overview

ETF documents are often lengthy and difficult to navigate.

This project solves that problem by building an AI assistant that:

* Reads ETF PDFs and text documents
* Converts them into embeddings
* Stores them in a vector database
* Retrieves relevant context when a user asks questions
* Generates answers strictly based on documents

---

## 🎯 Key Features

✅ Document-grounded answers (no hallucination style responses)
✅ Vector database retrieval (Chroma)
✅ Streamlit chatbot UI
✅ LangChain RetrievalQA pipeline
✅ Secure environment variable usage
✅ Financial disclaimer enforcement
✅ Modular architecture (ingest → retrieve → chat)

---

## 🧠 RAG Pipeline (Simple)

1. Documents are loaded and chunked
2. Chunks are converted into embeddings
3. Embeddings stored in Chroma vector DB
4. User query retrieves relevant chunks
5. LLM generates contextual answer

---

## 🛠️ Tech Stack

* Python
* LangChain
* OpenAI API
* Chroma Vector Database
* Streamlit
* PyPDFLoader
* RecursiveCharacterTextSplitter
* dotenv

---

## 📁 Project Structure

```
global-etf-rag-chatbot/
│
├── data/
│   ├── etf_basics.pdf
│   ├── sp500_etf_overview.pdf
│   ├── nasdaq100_etf_overview.pdf
│   └── risk_disclaimer.txt
│
├── ingest.py
├── chat.py
├── app.py
├── chroma_db/
├── .env.example
├── requirements.txt
├── README.md
```

---

## ⚙️ Setup & Installation

### 1️⃣ Clone repository

```bash
git clone https://github.com/SyedHussain23/global-etf-rag-chatbot.git
cd global-etf-rag-chatbot
```

### 2️⃣ Create virtual environment

```bash
python -m venv venv
source venv/bin/activate
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔐 Environment Variables

Create `.env`

```
OPENAI_API_KEY=your_api_key_here
```

---

## 📦 Ingest Documents (run once)

```bash
python ingest.py
```

This step:

* Loads ETF documents
* Splits into chunks
* Creates embeddings
* Stores in Chroma DB

---

## 💬 Run Chatbot

```bash
streamlit run app.py
```

Then open browser → `http://localhost:8501`

---

## 📊 Example Use Cases

* ETF fundamentals Q&A
* Portfolio research assistant
* Educational ETF exploration
* Document-aware financial chatbot prototype

---

## ⚠️ Disclaimer

This project is intended for **educational and research purposes only**.

* No financial advice
* No investment recommendation
* Answers are document-grounded
* Users must conduct independent research

---

## 🔮 Future Improvements

* Hybrid search (BM25 + vector)
* Multi-document reasoning
* Guardrails for financial compliance
* Conversation memory
* Evaluation pipeline
* UI improvements
* Cloud deployment

---

## 👨‍💻 Author

**Syed Hussain Abdul Hakeem**

LinkedIn:
[https://www.linkedin.com/in/syed-hussain-abdul-hakeem](https://www.linkedin.com/in/syed-hussain-abdul-hakeem)

GitHub:
[https://github.com/SyedHussain23](https://github.com/SyedHussain23)

---

## ⭐ Support

If you found this project useful:

👉 Give the repository a star
👉 Share feedback
👉 Connect on LinkedIn
