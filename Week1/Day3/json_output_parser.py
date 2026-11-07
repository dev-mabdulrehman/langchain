import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser

load_dotenv()
api_key = os.environ.get("OPEN_API_SECRET_KEY")

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.7, api_key=api_key)

# 1. Parser initialize karna
parser = JsonOutputParser()

# 2. Prompt Template banana (Jisme parser ki instructions/format automatically add ho jata hai)
chat_template = ChatPromptTemplate.from_messages([
    (
        "system",
        "You are an expert fitness coach. Provide the workout and diet plan in valid JSON format "
        "with keys: 'goal', 'duration_days', 'workout_summary', and 'diet_summary'.\n"
        "{format_instructions}"
    ),
    (
        "human",
        "Goal: {goal}, Level: {fitness_level}, Diet: {diet_preferences}"
    )
])

prompt_with_instructions = chat_template.partial(
    format_instructions=parser.get_format_instructions()
)

chain = prompt_with_instructions | llm | parser

# User inputs
print("=== AI Fitness Coach (JSON Output Mode) ===")
goal = input("Your Goal (e.g., Weight Loss): ")
fitness_level = input("Your Fitness Level (e.g., Beginner): ")
diet_preferences = input("Your Diet Preference (e.g., Desi food): ")

print("\nGenerating structured JSON plan...")

# 5. Chain ko invoke karna (Ab humein seedha Python dictionary milegi!)
result = chain.invoke({
    "goal": goal,
    "fitness_level": fitness_level,
    "diet_preferences": diet_preferences
})

print("\n--- Parsed Python Dictionary Output ---")
print(type(result))  # Yeh batayega ke ab yeh string nahi balkay dictionary hai!
print(result)
