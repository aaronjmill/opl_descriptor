from dotenv import load_dotenv
import os
import openai

# Load environment variables from .env file
load_dotenv()

# Retrieve the API key from the environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_summary(game_title):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"Generate a 255-character description for the PS2 game '{game_title}'",
        max_tokens=60
    )
    summary = response.choices[0].text.strip()
    return summary

def main():
    while True:
        # Take user input for the game title
        game_title = input("Enter the PlayStation 2 game title: ")

        # Generate and display the summary
        summary = generate_summary(game_title)
        print(f"\nSummary for {game_title}:\n{summary}")
        print(f"Character count: {len(summary)} / 255\n")

        # Option to continue or exit
        continue_choice = input("Do you want to generate a description for another game? (yes/no): ").strip().lower()
        if continue_choice != 'yes':
            break

if __name__ == "__main__":
    main()
