"""
Basic example of using LangChain with ChatOpenAI.
Demonstrates a simple question-answer interaction with a chat model.
"""

from langchain_openai import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage
import os

def main():
    # Initialize the chat model with OpenAI API key
    chat = ChatOpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    # Define the conversation messages
    messages = [
        SystemMessage(content="You are a helpful assistant."),
        HumanMessage(content="What is the capital of France?"),
    ]

    # Get and print the response
    response = chat.invoke(messages)
    print(response)

if __name__ == "__main__":
    main()
