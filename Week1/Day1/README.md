# Day 1: Environment Setup, API Security & First LLM Call

## 📌 Overview
On Day 1 of the 2-Week LangChain Mastery Journey, the focus was on establishing a solid foundation for AI application development. This included setting up a dedicated virtual environment on Windows, understanding API key security best practices, learning core LangChain architecture concepts, and running the first functional Python script to interact with OpenAI's LLMs via LangChain.

---

## 🎯 Key Learning Objectives
1. **Understand LangChain Architecture:** Comprehend the distinction between raw LLMs and LangChain's orchestration capabilities.
2. **Environment & Security:** Isolate project dependencies using Python Virtual Environments (`venv`) and secure sensitive API keys using `.env` and `.gitignore`.
3. **First Integration:** Write and execute a Python script (`app.py`) to send prompts and receive responses using `ChatOpenAI`.

---

## 💡 Concepts & Terminology Covered

| Term / Concept | Description |
| :--- | :--- |
| **LLM (Large Language Model)** | Powerful pattern-recognition AI models (e.g., OpenAI's GPT-4o-mini) designed to process and generate text. |
| **LangChain** | An orchestration framework that connects LLMs with tools, external data, and memory to build complete applications. *(Analogy: LLM is the engine; LangChain is the entire car infrastructure).* |
| **Environment Variables (`.env`)** | Externalized configuration variables used to hide sensitive credentials like `OPENAI_API_KEY` from source code. |
| **`.gitignore`** | A configuration file instructing Git to omit secret files (`.env`) and large environments (`venv/`) from being pushed to public repositories. |
| **LangChain Modules** | Overview of Model I/O, Retrieval, Memory, Chains, and Agents. |

---

## 🛠️ Windows Environment Setup Guide

### 1. Create a Virtual Environment
```bash
python -m venv venv
```

### 2. Activate Virtual Environment (Windows)
```bash
venv\Scripts\activate
```
*(Verification: `(venv)` will appear at the start of the terminal prompt)*

### 3. Install Required Packages
```bash
pip install langchain langchain-openai python-dotenv
```

---

## 📄 Code Implementation (`app.py`)

```python
import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

# 1. Load environment variables from .env file
load_dotenv()

# 2. Access API Key safely from system environment
api_key = os.environ.get("OPEN_API_SECRET_KEY")

# 3. Initialize LangChain Chat Model
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.7, api_key=api_key)

# 4. Invoke LLM with a prompt
response = llm.invoke("LangChain kya hai aik line mein asan Urdu ya Roman Urdu mein batao.")

# 5. Output Response
print("AI Response:", response.content)
```

---

## ✅ Milestones Completed
- [x] Python Virtual Environment setup and verified.
- [x] Safe API configuration using `.env` and `.gitignore`.
- [x] Successfully invoked `gpt-4o-mini` using LangChain's `ChatOpenAI`.
- [x] Conceptual understanding verified via mini-quiz assessments.