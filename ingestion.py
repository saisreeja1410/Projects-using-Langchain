from langchain_text_splitters import CharacterTextSplitter
from langchain_community.document_loaders import TextLoader
from langchain_pinecone import PineconeVectorStore
from langchain_huggingface import HuggingFaceEmbeddings
import os 
from dotenv import load_dotenv
load_dotenv()
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
PINECONE_REGION = os.getenv("PINECONE_REGION")

print(f"PINECONE_API_KEY: {PINECONE_API_KEY}")
print(f"PINECONE_REGION: {PINECONE_REGION}")

if __name__ == "__main__":
    
    print("ingestion started")
    loader = TextLoader("sampletext.txt")
    documents = loader.load()
    print(f"Loaded {len(documents)} documents")
    
    print("Splitting documents")
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    split_doc = text_splitter.split_documents(documents)
    print(f"Split {len(documents)} into {len(split_doc)} documents")
    
    print("Started embedding")
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    
    print("Inserting into Vector DB")
    vector_db = PineconeVectorStore.from_documents(split_doc, embeddings, index_name="sample")
    print(f"Inserted {len(split_doc)} documents")