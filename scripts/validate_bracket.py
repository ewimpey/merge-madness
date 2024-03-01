import json
import os

# Change the current working directory to the script's directory
script_dir = os.path.dirname(__file__)  # Get the directory where the script is located
os.chdir(script_dir)  # Change the working directory


def load_json(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)

def validate_structure(bracket, expected_rounds, expected_games):
    # Check number of rounds
    if len(bracket) != expected_rounds:
        return False, "Incorrect number of rounds."
    
    # Check number of games per round
    for round_name, games in bracket.items():
        if not len(games) in expected_games.values():
            return False, f"Incorrect number of games in {round_name}."
        
        for game in games.values():
            if not all(key in game for key in ["team1", "team2", "winner"]):
                return False, "Missing keys in some games."
    
    return True, "Structure is correct."

def validate_initial_matchups(user_bracket, initial_bracket):
    # Check only the matchups in the initial round
    for game_id, game in user_bracket["round1"].items():
        initial_game = initial_bracket["round1"].get(game_id, {})
        if not initial_game:
            return False, f"Game {game_id} is missing in the initial bracket."
        # Compare team1 and team2 for each game in round 1
        if game["team1"] != initial_game["team1"] or game["team2"] != initial_game["team2"]:
            return False, f"Matchup in game {game_id} has been altered."
    
    return True, "Initial matchups are valid."


def validate_content(bracket, initial_bracket):
    # Validate winners
    for round_name, games in bracket.items():
        for game_id, game in games.items():
            if game["winner"] not in [game["team1"], game["team2"]]:
                return False, f"Invalid winner in {game_id} of {round_name}."
    
    return True, "Content is valid."

def validate_progression(bracket):
    # Implement progression validation logic here
    # This involves checking each winner advances to the correct next game
    pass

def main():
    initial_bracket = load_json('initial_bracket.json')
    user_bracket = load_json('final_bracket.json')
    
    # Define expected rounds and games for validation
    expected_rounds = 6
    expected_games = {"round1": 32, 
                      "round2": 16, 
                      "round3": 8, 
                      "round4": 4,
                      "round5": 2,
                      "round6": 1}

    structure_valid, structure_message = validate_structure(user_bracket, expected_rounds, expected_games)
    if not structure_valid:
        print(structure_message)
        return
    
    # Validate initial matchups
    matchups_valid, matchups_message = validate_initial_matchups(user_bracket, initial_bracket)
    if not matchups_valid:
        print(matchups_message)
        return
    
    content_valid, content_message = validate_content(user_bracket, initial_bracket)
    if not content_valid:
        print(content_message)
        return
    
    # Add call to validate_progression when implemented

    print("Bracket validation passed!")

if __name__ == "__main__":
    main()
