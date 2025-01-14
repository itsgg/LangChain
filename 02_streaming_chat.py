from langchain_openai import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage

import os

chat = ChatOpenAI(api_key=os.getenv("OPENAI_API_KEY"))
messages = [
    SystemMessage(content="You are a story teller."),
    HumanMessage(
        content="Write a story about a person who hit rock bottom and how they got out of it."
    ),
]


def main():
    for chunk in chat.stream(messages):
        print(chunk.content, end="", flush=True)


if __name__ == "__main__":
    main()
