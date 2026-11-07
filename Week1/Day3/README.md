# Day 3: Output Parsers, LCEL Pipelines & Structured Data

## 📌 Overview

On Day 3 of the 2-Week LangChain Mastery Journey, the primary focus was transitioning from raw unstructured text strings to **reliable, structured data extraction**. Utilizing `JsonOutputParser` and `PydanticOutputParser` from `langchain-core`, alongside modern LangChain Expression Language (LCEL) pipe operators (`|`), we implemented type-safe, production-ready parsing pipelines.

## 🎯 Key Learning Objectives

1. **Output Parser Fundamentals:** Understand the role of output parsers in translating raw LLM responses into structured Python dictionaries and validated objects.
2. **LCEL & The Pipe Operator (`|`):** Build clean, declarative pipelines (`prompt | llm | parser`) for seamless data flow.
3. **Structured JSON Extraction:** Parse flexible JSON structures programmatically using `JsonOutputParser`.
4. **Type-Safe Validation with Pydantic:** Implement schema enforcement, type safety, and field validation via `PydanticOutputParser`.

## 💡 Concepts & Terminology Covered

| Term / Concept | Description |
| :--- | :--- |
| **`JsonOutputParser`** | A LangChain parser that instructs the LLM to return valid JSON and parses the raw text into a Python dictionary. |
| **`PydanticOutputParser`** | A robust parser that validates LLM output against a predefined Pydantic schema, guaranteeing correct data types (e.g., `int`, `str`). |
| **LCEL / Pipe Operator (`\|`)** | Modern LangChain Expression Language syntax used to chain prompts, LLMs, and output parsers sequentially. |
| **`format_instructions`** | Automatic prompt instructions injected by parsers to guide the LLM on formatting requirements. |

## 📄 Code Implementation

### 1. JSON Output Parsing (`json_output_parser.py`)

Below is the verified code implementation for flexible JSON dictionary parsing:

```python
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
```

---

### 2. Type-Safe Pydantic Output Parsing (`pydantic_output_parser.py`)

Below is the verified code implementation for type-safe schema validation:

```python
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
```

## 🧪 Execution & Verification

### Sample Interactive Output:
```text
=== AI Fitness Coach (Pydantic Type-Safe Mode) ===
Your Goal (e.g., Weight Loss): Weight Loss
Your Fitness Level (e.g., Beginner): Beginner
Your Diet Preference (e.g., Desi food): Desi food

Generating type-safe structured plan...

--- Parsed Pydantic Object Output ---
<class '__main__.FitnessPlan'>
goal='Weight Loss' duration_days=3 workout_summary='Full-body workouts combined with cardio sessions tailored for beginners.' daily_calories=1500

Accessing specific field:
Target Calories: 1500 <class 'int'>
```

## ✅ Milestones Completed

- [x] Mastered `JsonOutputParser` for clean JSON-based application data extraction.
- [x] Implemented `PydanticOutputParser` for strict type safety and schema validation.
- [x] Adopted modern LCEL pipeline syntax using the pipe operator (`|`).
- [x] Created modular scripts (`json_output_parser.py`, `pydantic_output_parser.py`) and recorded learning artifacts (`Day 3 Learning Record.pdf`).