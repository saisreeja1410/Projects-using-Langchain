from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain.tools import tool
from langchain.tools.render import render_text_description
from dotenv import load_dotenv
import os

load_dotenv()
gemini_api_key = os.getenv("GEMINI_API_KEY")

# Define tools
@tool
def get_length_of_string(string: str) -> int:
    """Returns the length of a string"""
    print(f"Length of {string} is {len(string)}")
    text = string.strip("'\n'").strip('"')
    return len(text)

@tool
def multiply(a: int, b: int) -> int:
    """Multiply two integers."""
    print(f"{a} * {b} = {a * b}")
    return a * b

@tool
def frequency(string: str) -> str:
    """Returns the most frequent character in a string"""
    print(f"The most frequent character in {string} is {max(set(string), key=string.count)}")
    return max(set(string), key=string.count)

if __name__ == "__main__":
    # Initialize LLM
    llm = ChatGoogleGenerativeAI(
        model="gemini-1.5-flash-latest", 
        api_key=gemini_api_key,
        temperature=0,
        max_tokens=1024,
    )

    # Define tools and prompt
    tools = [get_length_of_string, multiply, frequency]
    template = """
    You are a helpful assistant that answers questions about strings.
    Use the following tools:
    {tools}
    Use the following format:
    Question: the input question you must answer
    Thought: you should always think about what to do
    Action: the action to take, should be one of [{tool_names}]
    Observation: the result of the action
    ... (this Thought/Action/ Observation can be repeated any number of times)
    Answer: the answer to the original input question. If you don't know the answer, just say that you don't know, don't try to make up an answer.
    Begin!
    Question: {input}
    Thought:
    """

    prompt = PromptTemplate.from_template(template=template).partial(
        tools=render_text_description(tools),
        tool_names=", ".join([tool.name for tool in tools])
    )

    # Create chain
    chain = prompt | llm

    # Define input questions
    input_questions = [
        "What is the length of 'Lang Chain'?",
        "What is 2 * 3?",
        "What is the most frequent character in 'Sai Sreejaaa'?"
    ]

    # Run chain for each input question
    for question in input_questions:
        res = chain.invoke({"input": question})
        print(f"Question: {question}")
        print(res)
        print()