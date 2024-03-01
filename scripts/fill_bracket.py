import os
import json

# Change the current working directory to the script's directory
script_dir = os.path.dirname(__file__)  # Get the directory where the script is located
os.chdir(script_dir)  # Change the working directory


def prompt_for_winner(team1, team2):
    print(f"\n{team1} vs {team2}. Click the team that you think will win:")
    while True:
        choice = input(f"Type 1 for {team1} or 2 for {team2}: ").strip()
        if choice in ['1', '2']:
            return team1 if choice == '1' else team2
        else:
            print("Invalid input. Please type 1 or 2.")

def update_matchups(bracket, round_num, game_num, winner):
    next_round_num = round_num + 1
    next_game_num = (game_num - 1) // 2 + 1
    if next_round_num > 6:
        return  # No next round after the championship
    next_round = f"round{next_round_num}"
    next_game = f"game{next_game_num}"
    position = "team1" if game_num % 2 != 0 else "team2"
    bracket[next_round][next_game][position] = winner

def fill_bracket(bracket):
    for round_num in range(1, 7):
        current_round = f"round{round_num}"
        games = list(bracket[current_round].keys())
        for game in games:
            details = bracket[current_round][game]
            if 'team1' in details and 'team2' in details:  # For all rounds
                team1, team2 = details['team1'], details['team2']
                winner = prompt_for_winner(team1, team2)
                bracket[current_round][game]['winner'] = winner
                game_num = int(game.replace('game', ''))
                update_matchups(bracket, round_num, game_num, winner)

    return bracket

def main():
    # Load the initial bracket
    with open('initial_bracket.json', 'r') as f:
        initial_bracket = json.load(f)

    # Fill the bracket based on user input
    final_bracket = fill_bracket(initial_bracket)

    # Save the filled bracket
    with open('final_bracket.json', 'w') as f:
        json.dump(final_bracket, f, indent=4)

    print("\nBracket filled and saved to final_bracket.json")

if __name__ == "__main__":
    main()
