import os
from dotenv import load_dotenv

load_dotenv()

from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
from langchain.chains import RetrievalQA


embeddings = OpenAIEmbeddings()

db = Chroma(
    persist_directory="chroma_db",
    embedding_function=embeddings
)

llm = ChatOpenAI(
    model="gpt-3.5-turbo",
    temperature=0
)

qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=db.as_retriever(search_kwargs={"k": 3}),
    chain_type="stuff"
)

def ask_question(question: str):
    safe_question = (
        "Answer using ETF documents only. "
        "Do not give investment advice.\n\n"
        f"Question: {question}"
    )
    return qa_chain.run(safe_question)
