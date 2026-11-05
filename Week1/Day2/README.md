# Day 2: Dynamic Prompt Templates & User Interaction

## 📌 Overview

On Day 2 of the 2-Week LangChain Mastery Journey, the primary focus was transitioning from static prompt strings to **dynamic prompt construction**. Utilizing `PromptTemplate` from `langchain-core`, we implemented runtime dynamic variable substitution and integrated user interactive inputs (`input()`) to construct reusable prompt workflows.

## 🎯 Key Learning Objectives

1. **Prompt Template Fundamentals:** Understand the role of `PromptTemplate` in creating modular, reusable, and maintainable prompt architectures.
2. **Modern Import Standards:** Standardize code implementations using the current `langchain_core.prompts` package instead of legacy import paths.
3. **Interactive Workflows:** Combine runtime user inputs (`topic`, `language`) with dynamic templates before executing requests to the Chat Model.

## 💡 Concepts & Terminology Covered

| Term / Concept | Description |
| :--- | :--- |
| **`PromptTemplate`** | A core LangChain class used to wrap raw text with parameterized variables `{variable}` for dynamic formatting. |
| **`input_variables`** | An array/list parameter specifying the variable placeholders expected inside the prompt template text. |
| **Runtime Interpolation (`format`)** | The mechanism of populating template variables with actual values (e.g., user inputs) before sending them to the LLM. |
| **`langchain-core`** | The underlying core package containing foundational abstractions, schemas, and components for the LangChain ecosystem. |

## 📄 Code Implementation (`app.py`)

Below is the verified interactive script created during Day 2:

```python
import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate

# 1. Load environment variables
load_dotenv()
api_key = os.environ.get("OPEN_API_SECRET_KEY")

# 2. Initialize LLM Model
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.7, api_key=api_key)

# 3. Define PromptTemplate with dynamic input variables
prompt_template = PromptTemplate(
    input_variables=["topic", "language"],
    template="Mujhe {topic} ke baray mein 2 lines mein batao, aur iska jawab {language} mein hona chahiye."
)

# 4. Interactive user input collection
topic = input("Enter topic: ")
language = input("Enter language: ")

# 5. Format prompt dynamically at runtime
final_prompt = prompt_template.format(
    topic=topic, 
    language=language
)

print("\n--- Generated Prompt ---")
print(final_prompt)
print("\n--- AI Response ---")

# 6. Invoke LLM and print response
response = llm.invoke(final_prompt)
print(response.content)
```

## 🧪 Execution & Verification

### Sample Interactive Output:
```text
Enter topic: Artificial Intelligence
Enter language: Roman Urdu

--- Generated Prompt ---
Mujhe Artificial Intelligence ke baray mein 2 lines mein batao, aur iska jawab Roman Urdu mein hona chahiye.

--- AI Response ---
Artificial Intelligence (AI) ek aisi technology hai jo machines ko insano ki tarah sochne aur masle hal karne ke kabil banati hai. Iska istemal smart assistants, self-driving cars aur automated software mein aam ho raha hai.
```

## ✅ Milestones Completed

- [x] Mastered `PromptTemplate` usage and dynamic variable substitution.
- [x] Resolved module pathing by adopting `langchain_core.prompts`.
- [x] Implemented runtime user interactive input feeding into LangChain pipelines.
- [x] Verified execution with `gpt-4o-mini`.