from langchain_openai import ChatOpenAI
import os

chat = ChatOpenAI(api_key=os.getenv("OPENAI_API_KEY"))
print(chat.invoke("What is the capital of France?"))
