from langchain.chains.conversation.memory import ConversationSummaryBufferMemory
from langchain.chains import ConversationChain
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os

load_dotenv()
gemini_api_key = os.getenv("GEMINI_API_KEY")

#Initialize the LLM model
llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash-latest", api_key=gemini_api_key)

#Initialize the conversation with summary memory that will store the conversation history
memory = ConversationSummaryBufferMemory(
    llm=llm, 
    max_token_limit=200
)

#Initialize the conversation chain with summary buffer memory 
conversation = ConversationChain(
    llm=llm,
    memory=memory,
    verbose=True
)

while True:
    #Take user input
    user_input = input("\n Sreeja: ")
    
    #Check if user wants to exit
    if user_input.lower() in {'bye', 'exit', 'quit'}:
        print("AI: Goodbye!")
        
        #Print the conversation history as a summary
        print("\n Conversation Summary: ")
        print(conversation.memory.buffer)
        break
     
    #get the response from the LLM   
    output = conversation.predict(input=user_input)
    print("\n AI: ", output)