# Global ETF Intelligence Chatbot (RAG)

## 📌 Project Overview
This project is a beginner-friendly end-to-end AI application that demonstrates a
Retrieval-Augmented Generation (RAG) chatbot.

The chatbot answers questions about Exchange Traded Funds (ETFs) by retrieving
information from provided ETF documents and generating accurate, context-based responses.

This project is for **educational purposes only** and does not provide investment advice.

---

## 🎯 Problem Statement
ETF-related documents are often lengthy and difficult for beginners to understand.
Users may want quick answers without reading entire PDFs.

---

## ✅ Solution
This chatbot:
- Reads ETF documents (PDFs and text files)
- Stores the content in a vector database
- Retrieves relevant information when a user asks a question
- Uses an LLM to generate answers strictly based on the documents

---

## 🧠 How RAG Works (Simple Explanation)
1. ETF documents are loaded and split into small text chunks
2. Text chunks are converted into embeddings
3. Embeddings are stored in a vector database (Chroma)
4. User questions are matched with relevant document chunks
5. The AI generates answers using only retrieved content

---

## 🛠️ Technologies Used
- Python
- LangChain
- OpenAI API
- Chroma Vector Database
- Streamlit
- PDF Loader

---

## 📁 Project Structure
global-etf-chatbot/
│
├── data/
│ ├── etf_basics.pdf
│ ├── sp500_etf_overview.pdf
│ ├── nasdaq100_etf_overview.pdf
│ └── risk_disclaimer.txt
│
├── ingest.py
├── chat.py
├── app.py
├── README.md
├── .env
└── venv/


---

## How to Run

```bash
# Activate virtual environment
source venv/bin/activate

# Load environment variables
export $(cat .env)

# Ingest documents (run once)
python ingest.py

# Run the chatbot
streamlit run app.py

Disclaimer
This project is intended for educational and demonstration purposes only.
It does not provide financial or investment advice.

Author
Syed Hussain Abdul Hakeem
