from langchain.chains.conversation.memory import ConversationBufferWindowMemory
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains import ConversationChain
from dotenv import load_dotenv
import os
load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")

#Create a ConversationChain with a ConversationBufferMemory
memory = ConversationBufferWindowMemory(k=2)

#It will use the llm model to generate the response
llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash-latest", api_key=gemini_api_key)

#It will store the conversation history
conversation = ConversationChain(
    llm = llm,
    memory = memory
)

while True:
    #Take user input
    user_input = input("\n Sreeja: ")
    
    #Check if user wants to exit
    if user_input.lower() in {'bye', 'exit', 'quit'}:
        print("AI: Goodbye!")
        
        #Print the conversation history
        print(conversation.memory.buffer)
        
        break
    
    #Generate a response
    response = conversation.predict(input=user_input)
    print("\n AI: ", response)