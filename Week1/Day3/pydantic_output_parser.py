import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field

load_dotenv()
api_key = os.environ.get("OPEN_API_SECRET_KEY")

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.7, api_key=api_key)

# 1. Pydantic Model define karna (Schema & Data Types)


class FitnessPlan(BaseModel):
    goal: str = Field(description="The fitness goal of the user")
    duration_days: int = Field(
        description="Number of days for the plan, e.g. 3")
    workout_summary: str = Field(
        description="A brief description of the workout routine")
    daily_calories: int = Field(
        description="Recommended daily calorie intake as an integer")


# 2. Parser initialize karna pydantic class ke sath
parser = PydanticOutputParser(pydantic_object=FitnessPlan)

# 3. Prompt Template banana
chat_template = ChatPromptTemplate.from_messages([
    (
        "system",
        "You are an expert fitness coach. Provide the response strictly matching the following schema instructions.\n"
        "{format_instructions}"
    ),
    (
        "human",
        "Goal: {goal}, Level: {fitness_level}, Diet: {diet_preferences}"
    )
])

# 4. Format instructions ko partial karna
prompt_with_instructions = chat_template.partial(
    format_instructions=parser.get_format_instructions()
)

# 5. Pipe Operator (|) ke zariye Chain banana
chain = prompt_with_instructions | llm | parser

print("=== AI Fitness Coach (Pydantic Type-Safe Mode) ===")
goal = input("Your Goal (e.g., Weight Loss): ")
fitness_level = input("Your Fitness Level (e.g., Beginner): ")
diet_preferences = input("Your Diet Preference (e.g., Desi food): ")

print("\nGenerating type-safe structured plan...")

# 6. Chain invoke karna
result = chain.invoke({
    "goal": goal,
    "fitness_level": fitness_level,
    "diet_preferences": diet_preferences
})

print("\n--- Parsed Pydantic Object Output ---")
print(type(result))      # Yeh batayega ke yeh ek Python object hai!
print(result)            # Poora object print hoga
print("\nAccessing specific field:")
print("Target Calories:", result.daily_calories, type(result.daily_calories))
