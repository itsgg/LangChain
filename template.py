from langchain_openai import ChatOpenAI
from langchain.prompts.chat import SystemMessagePromptTemplate, ChatPromptTemplate

import os

model = ChatOpenAI(api_key=os.getenv("OPENAI_API_KEY"))

template = """
You are a creative consultant brainstorming names for businesses.

You must follow the following principles:
{principles}

Please generate a numerical list of five catchy names for a startup in {industry} industry that deals with {context}

You must return the names in the following format:
1. Name 1
2. Name 2
3. Name 3
4. Name 4
5. Name 5
"""
system_prompt = SystemMessagePromptTemplate.from_template(template)
chat_prompt = ChatPromptTemplate.from_messages([system_prompt])

chain = chat_prompt | model

def main():
    print(chain.invoke({"principles": "The names must be catchy and memorable", "industry": "technology", "context": "AI"}))

if __name__ == "__main__":
    main()
