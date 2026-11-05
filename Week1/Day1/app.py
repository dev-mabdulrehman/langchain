import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

api_key = os.environ.get("OPEN_API_SECRET_KEY")

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.7, api_key=api_key)

response = llm.invoke(
    "LangChain kya hai aik line mein asan Urdu ya Roman Urdu mein batao.")

print("AI Response:", response.content)
