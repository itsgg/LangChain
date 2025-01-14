"""
Advanced example of using templates for business name generation.
Demonstrates how to create a specialized system prompt template
and chain it with a chat model for creative business name generation.
"""

from langchain_openai import ChatOpenAI
from langchain_core.prompts.chat import SystemMessagePromptTemplate, ChatPromptTemplate
import os

def create_business_name_prompt():
    # Define the system template with specific business naming principles
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
    
    # Create system prompt template
    system_prompt = SystemMessagePromptTemplate.from_template(template)
    return ChatPromptTemplate.from_messages([system_prompt])

def main():
    # Initialize the chat model
    model = ChatOpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    # Create the prompt template
    chat_prompt = create_business_name_prompt()

    # Define naming principles and business context
    principles = """
    1. Each name should be short and easy to remember
    2. Each name should be unique and not similar to existing names
    3. Each name should be relevant to the industry and context
    4. Each name should be catchy and memorable
    5. Each name should be one word
    """
    
    # Set the industry and context for name generation
    params = {
        "principles": principles,
        "industry": "technology",
        "context": "AI"
    }

    # Create the chain and generate names
    chain = chat_prompt | model
    print("\nGenerated Business Names:")
    print(chain.invoke(params))

if __name__ == "__main__":
    main()
