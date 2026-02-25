# 🌍 Global ETF Intelligence Chatbot (RAG)

## 📌 Overview

The **Global ETF Intelligence Chatbot** is an end-to-end Retrieval-Augmented Generation (RAG) AI application that enables users to ask questions about Exchange Traded Funds (ETFs) and receive context-aware answers grounded in ETF documents.

The system retrieves relevant information from ETF PDFs and text files using a vector database and generates responses using an LLM.

⚠️ **Educational use only — no investment advice provided**

---

## 🎯 Problem Statement

ETF documentation is often lengthy and difficult for beginners to interpret.
Users need a way to quickly extract accurate information without manually reading multiple documents.

---

## ✅ Solution

This project builds a RAG chatbot that:

* Loads ETF knowledge from PDFs and text files
* Splits content into semantic chunks
* Converts text into embeddings
* Stores embeddings in a Chroma vector database
* Retrieves relevant content for user queries
* Generates answers using an LLM grounded in documents only

---

## 🧠 RAG Architecture (Simplified)

1. Document ingestion & chunking
2. Embedding generation
3. Vector storage (Chroma DB)
4. Retrieval of relevant context
5. LLM answer generation

---

## 🛠️ Tech Stack

* Python
* LangChain
* OpenAI API
* Chroma Vector Database
* Streamlit
* PyPDF Loader
* dotenv

---

## 📁 Project Structure

```
global-etf-chatbot/
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
├── .env
├── requirements.txt
└── README.md
```

---

## ⚙️ Setup & Installation

### 1️⃣ Clone repository

```bash
git clone https://github.com/SyedHussain23/global-etf-chatbot.git
cd global-etf-chatbot
```

---

### 2️⃣ Create virtual environment

```bash
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
```

---

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Add environment variables

Create `.env`

```
OPENAI_API_KEY=your_api_key_here
```

---

### 5️⃣ Ingest documents (run once)

```bash
python ingest.py
```

This creates the vector database.

---

### 6️⃣ Run chatbot

```bash
streamlit run app.py
```

---

## 💬 Example Queries

* What are ETFs?
* Difference between S&P 500 ETF and Nasdaq ETF
* Benefits and risks of ETFs
* How ETFs track indices

---

## 🔐 Safety & Guardrails

* Responses restricted to ETF documents
* No financial advice generated
* Explicit disclaimer included
* Document-grounded answers only

---

## 📊 Key Features

✅ RAG architecture
✅ Vector database retrieval
✅ Context-aware responses
✅ Document grounding
✅ Streamlit UI
✅ Modular ingestion pipeline
✅ Production-ready structure

---

## 🚀 Future Improvements

* Hybrid retrieval (BM25 + vector search)
* Metadata filtering
* Source citation in answers
* Streaming responses
* Multi-document ranking
* Deployment on cloud (Streamlit Cloud / AWS)
* Authentication layer
* Feedback loop for answer quality

---

## 📌 Author

**Syed Hussain Abdul Hakeem**
AI Engineer

GitHub: [https://github.com/SyedHussain23](https://github.com/SyedHussain23)

LinkedIn: https://www.linkedin.com/in/syed-hussain-abdul-hakeem

---

## ⭐ Support

If you found this project helpful, consider giving it a ⭐
