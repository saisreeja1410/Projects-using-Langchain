from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
import os
from dotenv import load_dotenv

load_dotenv()

gemini_api_key = os.getenv("gemini_api_key") 
if __name__ == "__main__":

    llm = ChatGoogleGenerativeAI(
        model="gemini-1.5-flash-latest",
        api_key=gemini_api_key
    )

    sentence = input("Enter the sentence to translate: ")
    target_language = input("Enter the target language : ")

    prompt_template = "Translate the following sentence into {target_language}:\n'{sentence}'"
    prompt = PromptTemplate(template=prompt_template, input_variables=["sentence", "target_language"])

    chain = prompt | llm | StrOutputParser() 

    output = chain.invoke({"sentence": sentence, "target_language": target_language})
    print(output)
