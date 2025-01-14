from langchain_openai import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage
from langchain.schema.runnable import RunnableConfig

import os

chat = ChatOpenAI(api_key=os.getenv("OPENAI_API_KEY"))
messages = [
    SystemMessage(content="You are a story teller."),
    HumanMessage(
        content="Write a story about a person who hit rock bottom and how they got out of it."
    ),
]


def main():
    config = RunnableConfig(max_concurrency=2)
    for result in chat.batch([messages] * 4, config=config):
        print(result)


if __name__ == "__main__":
    main()
