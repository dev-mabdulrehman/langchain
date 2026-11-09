import os
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from dotenv import load_dotenv


class CountryDetails(BaseModel):
    country_name: str = Field(description="Name of the country")
    capital: str = Field(description="Country's capital")
    official_language:  str = Field(description="Country's Official language")
    currency: str = Field(description="Country's Currency")
    population: str = Field(
        description="Approximate population of the country")
    region: str = Field(
        description="Continent or region where the country is located")
    national_dish: str = Field(
        description="National or most famous dish of the country")
    time_zone: str = Field(description="Primary time zone of the country")


load_dotenv()
api_key = os.environ.get("OPEN_API_SECRET_KEY")
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.7, api_key=api_key)
output_parser = PydanticOutputParser(pydantic_object=CountryDetails)

chat_prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        "Act as an expert world traveler, and you have traveled whole world and know all countries details "
        "You have to give details of the given country in a proper JSON format.\n"
        "{formatting_instructions}"
    ),
    (
        "human",
        "Country:{country}"
    )
])

chat_prompt_with_instruction = chat_prompt.partial(
    formatting_instructions=output_parser.get_format_instructions()
)


chain = chat_prompt_with_instruction | llm | output_parser


def display_menu():
    print("\n" + "=" * 45)
    print(" Country Info Extractor ")
    print("=" * 45)


def get_user_inputs():
    display_menu()
    print('\n')
    country = input("Enter Country name: ").strip()

    return country


if __name__ == "__main__":
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        country = get_user_inputs()
        print("\nFinding country details")
        try:
            response = chain.invoke({
                "country": country
            })
            print("Country Details:")
            print("-" * 45)
            for key, value in response.model_dump().items():
                formatted_key = key.replace("_", " ").title()
                print(f"{formatted_key}: {value}")
            print("-" * 45)
        except Exception as e:
            print(f"\nAn error occurred: {e}")
        choice = (
            input("\nDo you want another recommendation? (y/n): ")
            .strip()
            .lower()
        )
        if choice != "y":
            print("\nThank you for using Movie Recommender! Goodbye!\n")
            break
