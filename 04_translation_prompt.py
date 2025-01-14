"""
Example of using prompt templates for language translation.
Shows how to create and combine different types of message templates
to create a translation chat prompt.
"""

from langchain_core.prompts import PromptTemplate
from langchain.prompts.chat import (
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
    ChatPromptTemplate,
)
from langchain_openai import ChatOpenAI
import os

def create_translation_prompt():
    # Create system message template for translation setup
    system_template = """You are a helpful assistant that translates {input_language} to {output_language}."""
    system_prompt = PromptTemplate(
        template=system_template,
        input_variables=["input_language", "output_language"],
    )
    system_message_prompt = SystemMessagePromptTemplate(prompt=system_prompt)

    # Create human message template for the text to translate
    human_template = "Translate this text: {text}"
    human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)

    # Combine both templates into a chat prompt
    return ChatPromptTemplate.from_messages(
        [system_message_prompt, human_message_prompt]
    )

def main():
    # Initialize the chat model
    chat = ChatOpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    
    # Create the translation prompt
    chat_prompt = create_translation_prompt()

    # Format the messages with specific languages and text
    messages = chat_prompt.format_messages(
        input_language="English",
        output_language="Tamil",
        text="Hello, how are you?"
    )

    # Get and print the translation
    response = chat.invoke(messages)
    print("\nTranslation:")
    print(response)

if __name__ == "__main__":
    main()
