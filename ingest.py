from langchain_community.document_loaders import PyPDFLoader, TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma

# Load documents
loaders = [
    PyPDFLoader("data/etf_basics.pdf"),
    PyPDFLoader("data/sp500_etf_overview.pdf"),
    PyPDFLoader("data/nasdaq100_etf_overview.pdf"),
    TextLoader("data/risk_disclaimer.txt")
]

documents = []
for loader in loaders:
    documents.extend(loader.load())

# Split text into chunks
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=100
)
chunks = text_splitter.split_documents(documents)

# Create embeddings
embeddings = OpenAIEmbeddings()

# Store in Chroma DB
db = Chroma.from_documents(
    chunks,
    embeddings,
    persist_directory="chroma_db"
)

db.persist()
print("Documents stored successfully")
