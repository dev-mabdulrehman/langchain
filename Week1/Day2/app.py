import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate

load_dotenv()
api_key = os.environ.get("OPEN_API_SECRET_KEY")

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.7, api_key=api_key)

prompt_template = PromptTemplate(
    input_variables=["topic", "language"],
    template="Mujhe {topic} ke baray mein 2 lines mein batao, aur iska jawab {language} mein hona chahiye."
)

topic = input("Enter topic:")
language = input("Enter language:")

final_prompt = prompt_template.format(
    topic=topic, language=language
)

print("\n--- Generated Prompt ---")
print(final_prompt)
print("\n--- AI Response ---")

response = llm.invoke(final_prompt)
print(response.content)
