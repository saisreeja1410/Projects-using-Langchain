import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_pinecone import PineconeVectorStore
from langchain.prompts import PromptTemplate
from langchain import hub
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_retrieval_chain
from langchain_huggingface import HuggingFaceEmbeddings

load_dotenv()
gemini_api_key = os.getenv("GEMINI_API_KEY") 

if __name__ == "__main__":
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash-latest", api_key=gemini_api_key)
    query = input("Enter the query: ")
    
    prompt_template = PromptTemplate(input_variables=["input"], template=query)
    
    vector_db = PineconeVectorStore(index_name="sample", embedding=embeddings)
    
    # prompt for retrieving 
    prompt = hub.pull("langchain-ai/retrieval-qa-chat")
    
    # create_stuff_documents_chain- This chain takes a query, passes it to the LLM, and then passes the LLM's response to the retriever
    combined_chain = create_stuff_documents_chain(llm, prompt)
    
    # create_retriever_chain- This chain takes a query, passes it to the retriever, retrieves a list of documents, and then passes
    retriever = create_retrieval_chain(retriever=vector_db.as_retriever(), combine_docs_chain=combined_chain)
    
    output = retriever.invoke({"input": query})
    
    print(output)