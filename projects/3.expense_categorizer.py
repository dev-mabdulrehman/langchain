import os
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from dotenv import load_dotenv

load_dotenv()


class ExpenseCategory(BaseModel):
    item_name: str = Field(description="Item Name")
    per_item_cost: float = Field(description="Item Cost")
    total_cost: float = Field(description="Total Expense cost")
    category: str = Field(description="Item Category")


api_key = os.environ.get("OPEN_API_SECRET_KEY")
llm = ChatOpenAI(api_key=api_key, temperature=0.7, model='gpt-4o-mini')
output_parser = PydanticOutputParser(pydantic_object=ExpenseCategory)

template = ChatPromptTemplate.from_messages([
    (
        "system",
        "Act as an expert senior finance manager. Your role is to categories given expense statement. "
        "You'll be given by the expense statement example: Bought 2 coffees for $10. "
        "You'll generate a proper given format \n"
        "{formatting_instruction}"
    ),
    (
        "human",
        "Expense statement is {statement}"
    )
])

template_with_instructions = template.partial(
    formatting_instruction=output_parser.get_format_instructions()
)

chain = template_with_instructions | llm | output_parser
statement = input("Statement: ")

response = chain.invoke({
    "statement": statement
})

for key, value in response.model_dump().items():
    formatted_key = key.replace("_", " ").title()
    print(f"{formatted_key}: {value}")
