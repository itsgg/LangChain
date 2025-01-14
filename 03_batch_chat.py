"""
Example of batch processing multiple chat requests concurrently.
Demonstrates how to efficiently process multiple similar requests in parallel.
"""

from langchain_openai import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage
from langchain.schema.runnable import RunnableConfig
import os

def main():
    # Initialize the chat model with OpenAI API key
    chat = ChatOpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    # Define the base conversation messages
    messages = [
        SystemMessage(content="You are a story teller."),
        HumanMessage(
            content="Write a story about a person who hit rock bottom and how they got out of it."
        ),
    ]

    # Configure batch processing with max concurrency of 2
    config = RunnableConfig(max_concurrency=2)
    
    # Process 4 identical requests in parallel
    print("Processing batch requests:\n")
    for i, result in enumerate(chat.batch([messages] * 4, config=config), 1):
        print(f"\nStory {i}:")
        print(result)

if __name__ == "__main__":
    main()
