from langchain_core.prompts import PromptTemplate
from langchain.prompts.chat import (
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
    ChatPromptTemplate,
)
from langchain_openai.chat_models import ChatOpenAI

prompt = PromptTemplate(
    template="""You are a helpful assistant that translates {input_language} to {output_language}.""",
    input_variables=["input_language", "output_language"],
)
system_message_prompt = SystemMessagePromptTemplate(prompt=prompt)

human_template = "Translate this text: {text}"
human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)

chat_prompt = ChatPromptTemplate.from_messages(
    [system_message_prompt, human_message_prompt]
)

def main():
    chat = ChatOpenAI()
    response = chat.invoke(
        chat_prompt.format_messages(
            input_language="English", output_language="Tamil", text="Hello, how are you?"
        )
    )
    print(response)

if __name__ == "__main__":
    main()
