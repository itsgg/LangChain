from langchain_openai import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage

import os

chat = ChatOpenAI(api_key=os.getenv("OPENAI_API_KEY"))
messages = [
    SystemMessage(content="You are a helpful assistant."),
    HumanMessage(content="What is the capital of France?"),
]

def main():
    print(chat.invoke(messages))


if __name__ == "__main__":
    main()
