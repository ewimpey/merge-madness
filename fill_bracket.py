import os
import json

def prompt_for_winner(team1, team2):
    """
    Provide user prompt for two teams
    Returns the winning team
    """
    print(f"\n{team1} vs {team2}")
    while True:
        choice = input(f"Type 1 for {team1} or 2 for {team2}: ").strip()
        if choice in ['1', '2']:
            return team1 if choice == '1' else team2
        else:
            print("Invalid input. Please type 1 or 2.")

def update_matchups(bracket, round_num, game_num, winner):
    """
    Updates future rounds based on winners
    """
    next_round_num = round_num + 1
    next_game_num = (game_num - 1) // 2 + 1
    if next_round_num > 6:
        return  # Round 6 is championship
    next_round = f"round{next_round_num}"
    next_game = f"game{next_game_num}"
    position = "team1" if game_num % 2 != 0 else "team2"
    bracket[next_round][next_game][position] = winner

def update_round0_matchups(bracket, game, winner):
    """
    Helper function for mapping the play-in games
    """
    if game == "game1":
        bracket["round1"]["game1"]["team2"] = winner  # M16 winner
    elif game == "game2":
        bracket["round1"]["game5"]["team2"] = winner  # M11 winner
    elif game == "game3":
        bracket["round1"]["game9"]["team2"] = winner  # W16 winner
    elif game == "game4":
        bracket["round1"]["game13"]["team2"] = winner  # W11 winner

def fill_bracket(bracket):
    """
    Function to fill an initial bracket
    """
    # First handle the play-in games
    games = list(bracket["round0"].keys())
    for game in games:
        details = bracket["round0"][game]
        if 'team1' in details and 'team2' in details:  # Ensure both teams are present
            team1, team2 = details['team1'], details['team2']
            winner = prompt_for_winner(team1, team2)
            bracket["round0"][game]['winner'] = winner
            
            update_round0_matchups(bracket, game, winner)
    # Now the remaining rounds
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
