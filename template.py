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
    principles = """
1. Each name should be short and easy to remember
2. Each name should be unique and not similar to existing names
3. Each name should be relevant to the industry and context
4. Each name should be catchy and memorable
5. Each name should be one word
"""
    industry = "technology"
    context = "AI"

    print(
        chain.invoke(
            {"principles": principles, "industry": industry, "context": context}
        )
    )


if __name__ == "__main__":
    main()
