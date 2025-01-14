"""
Example of streaming responses from ChatGPT.
Shows how to get real-time token-by-token output from the chat model.
"""

from langchain_openai import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage
import os

def main():
    # Initialize the chat model with OpenAI API key
    chat = ChatOpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    # Define the conversation messages
    messages = [
        SystemMessage(content="You are a story teller."),
        HumanMessage(
            content="Write a story about a person who hit rock bottom and how they got out of it."
        ),
    ]

    # Stream the response token by token
    print("Streaming response:\n")
    for chunk in chat.stream(messages):
        print(chunk.content, end="", flush=True)
    print("\n")

if __name__ == "__main__":
    main()
