import os
from dotenv import load_dotenv
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

load_dotenv()

api_key = os.environ.get("OPEN_API_SECRET_KEY")

llm = ChatOpenAI(api_key=api_key, temperature=0.7, model="gpt-4o-mini")
output_parser = JsonOutputParser()

prompt_template = ChatPromptTemplate.from_messages([
    (
        "system",
        "Tum esy act kro jesy tum ik senior or expert movie watcher ho jisko movies ky bary ma sb kuch pata ha "
        "Tumhary sath apna mood yh phir movie ka genre or language share kro ga or tumhne mujy best movie recommend krni ha JSON format ma "
        "Keys: (movie_title, director, release_year, synopsis, duration, language, actors, producer, lead_male_role, lead_female_role, genre)"
        "Agr mood dia ha toh phir mood ky hisab sy recommend krna "
        "Or agr genre share kia toh osky hisab sy "
        "agr dono share nhi krta to error ki bajye values empty return kr dena\n"
        "{format_instructions}"
    ),
    (
        "human",
        "Language:{language}, Mood:{mood}, Genre:{genre}"
    )
])

prompt_template_with_instruction = prompt_template.partial(
    format_instructions=output_parser.get_format_instructions()
)

chain = prompt_template_with_instruction | llm | output_parser


def display_menu():
    print("\n" + "=" * 45)
    print(" AI MOVIE RECOMMENDATION SYSTEM ")
    print("=" * 45)
    print(" (Aap kisi bhi field ko khali chodh sakte hain) ")


def get_user_inputs():
    display_menu()
    print('\n\n')
    mood = input("Enter Mood (e.g. Happy, Sad, Thrilled): ").strip()
    genre = input("Enter Genre (e.g. Action, Sci-Fi, Comedy): ").strip()
    lang_input = input("Enter Language [Press Enter for English]: ").strip()

    language = lang_input if lang_input else "English"

    return mood, genre, language


def main():
    while True:
        mood, genre, language = get_user_inputs()

        print("\nFinding the best recommendation for you...")
        try:
            response = chain.invoke(
                {"mood": mood, "genre": genre, "language": language}
            )

            print("\nTop Recommendation:")
            print("-" * 45)
            for key, value in response.items():
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


if __name__ == "__main__":
    main()
