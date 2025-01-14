from typing import List

from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.prompts.chat import ChatPromptTemplate, SystemMessagePromptTemplate
from langchain_openai.chat_models import ChatOpenAI
from pydantic import BaseModel, Field
import os
from dotenv import load_dotenv


class BusinessName(BaseModel):
    """Model representing a single business name with its rating.

    Attributes:
        name: The generated business name
        rating_score: A score from 0-10 indicating the quality of the name
    """

    name: str = Field(description="The name of the business")
    rating_score: float = Field(
        description="The rating score of the business, 0 is the lowest, 10 is the highest",
        ge=0,
        le=10,
    )


class BusinessNames(BaseModel):
    """Model representing a collection of business names.

    Attributes:
        names: List of BusinessName objects containing generated names and their ratings
    """

    names: List[BusinessName] = Field(description="The list of business names")


# Business name generation configuration
TEMPERATURE: float = 0.0
MAX_NAME_LENGTH: int = 10

BUSINESS_NAME_PRINCIPLES: str = """
1. The name must be easy to remember
2. Consider the {industry} industry context to create an effective name
3. The name must be unique and not already in use
4. The name must be easy to pronounce
5. Return only the name without any other text or characters
6. Avoid special characters, numbers, or symbols
7. Maximum length is {max_length} characters
8. Must be a single word
"""

GENERATION_TEMPLATE: str = """You are a business name generator.

Your task is to generate 5 creative business names for a startup in the {industry} industry.

Follow these principles:
{principles}

You must return the names in this exact format:
{format_instructions}

Generate the names now:"""


def validate_industry(industry: str) -> str:
    """Validate the industry input.
    
    Args:
        industry: The industry to validate
        
    Returns:
        str: The validated industry name
        
    Raises:
        ValueError: If industry is empty or invalid
    """
    if not industry or not isinstance(industry, str):
        raise ValueError("Industry must be a non-empty string")
    return industry.lower().strip()


def setup_name_generator() -> tuple[ChatPromptTemplate, PydanticOutputParser]:
    """Initialize and configure the name generation components.

    Returns:
        tuple: Contains the configured chat prompt and output parser
    """
    # Initialize the output parser for structured results
    parser = PydanticOutputParser(pydantic_object=BusinessNames)

    # Setup the chat prompt template
    system_message = SystemMessagePromptTemplate.from_template(GENERATION_TEMPLATE)
    chat_prompt = ChatPromptTemplate.from_messages([system_message])

    return chat_prompt, parser


def generate_business_names(industry: str) -> BusinessNames:
    """Generate and rate business names for a given industry.

    Args:
        industry: The target industry for name generation

    Returns:
        BusinessNames: Object containing generated names and their ratings
        
    Raises:
        ValueError: If industry validation fails
    """
    # Load environment variables
    load_dotenv()

    # Validate input
    validated_industry = validate_industry(industry)

    # Initialize components
    chat_prompt, parser = setup_name_generator()
    model = ChatOpenAI(api_key=os.getenv("OPENAI_API_KEY"), temperature=TEMPERATURE)

    # Create the generation pipeline
    prompt_and_model = chat_prompt | model

    # Generate names
    result = prompt_and_model.invoke(
        {
            "industry": validated_industry,
            "principles": BUSINESS_NAME_PRINCIPLES.format(
                industry=validated_industry,
                max_length=MAX_NAME_LENGTH
            ),
            "format_instructions": parser.get_format_instructions(),
        }
    )

    return parser.parse(result.content)


def main() -> None:
    """Main entry point for the business name generator."""
    try:
        business_names = generate_business_names("technology")
        print(business_names)
    except ValueError as e:
        print(f"Invalid input: {str(e)}")
    except Exception as e:
        print(f"Error generating business names: {str(e)}")


if __name__ == "__main__":
    main() 
