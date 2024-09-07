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
        # Simulating user choice
        print("Choose a game title:")
        games = ["Ace Combat 04: Shattered Skies", "The Legend of Spyro: The Eternal Night", "Jak II"]
        for i, game in enumerate(games, 1):
            print(f"{i}. {game}")
        
        choice = int(input("Enter the number of your choice: "))
        selected_game = games[choice - 1]

        # Generate and display the summary
        summary = generate_summary(selected_game)
        print(f"\nSummary for {selected_game}:\n{summary}")
        print(f"Character count: {len(summary)} / 255\n")

        # Continue with the next set of game titles
        # (You would dynamically fetch or generate these in a real application)
        continue_choice = input("Would you like to continue? (y/n): ")
        if continue_choice.lower() != 'y':
            break

if __name__ == "__main__":
    main()
