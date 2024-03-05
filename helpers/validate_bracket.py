import json
import os
import sys

# Get the directory where the script is located
# script_dir = os.path.dirname(__file__)
# brackets_dir = os.path.abspath(os.path.join(script_dir, '..'))


def load_json(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)

def validate_structure(bracket, expected_rounds, expected_games):
    """
    Checks the basic structure of the user submission
    """
    # Check the number of rounds
    if len(bracket) != expected_rounds:
        return False, "Incorrect number of rounds."
    
    # Check number of games per round
    for round_name, games in bracket.items():
        actual_num_games = len(games)
        expected_num_games = expected_games[round_name]
        if not actual_num_games == expected_num_games:
            return False, f"Incorrect number of games in {round_name}."
        
        for game in games.values():
            if not all(key in game for key in ["team1", "team2", "winner"]):
                return False, "Missing keys in some games."
    
    return True, "Structure is correct."

def is_placeholder(team_name):
    """
    This identifies the first round matchups that aren't known 
    due to the play-in games
    """
    return team_name in ("TBD", "")

def validate_initial_matchups(user_bracket, initial_bracket):
    """
    Ensure that the initial matchups haven't been altered
    """
    for round_name in ["round0", "round1"]:
        for game_id, game in user_bracket[round_name].items():
            initial_game = initial_bracket[round_name].get(game_id, {})
            
            if not initial_game:
                return False, f"Game {game_id} is missing in the initial bracket for {round_name}."
            
            # Skip comparison for placeholders in initial games
            if not is_placeholder(initial_game["team1"]) and game["team1"] != initial_game["team1"]:
                return False, f"Team 1 in {game_id} for {round_name} has been altered."
            
            if not is_placeholder(initial_game["team2"]) and game["team2"] != initial_game["team2"]:
                return False, f"Team 2 in {game_id} for {round_name} has been altered."
    
    return True, "All matchups are valid."



def validate_content(bracket, initial_bracket):
    # Validate winners
    for round_name, games in bracket.items():
        for game_id, game in games.items():
            if game["winner"] not in [game["team1"], game["team2"]]:
                return False, f"Invalid winner in {game_id} of {round_name}."
    
    return True, "Content is valid."

def validate_progression(bracket):
    # make sure that the winner goes on to the appropriate game/round
    pass

def main(initial_path, user_path):
    initial_bracket = load_json(initial_path)
    user_bracket = load_json(user_path)
    
    # Define expected rounds and games for validation
    expected_rounds = 7
    expected_games = {"round0": 4, # for the play-in games
                      "round1": 32, 
                      "round2": 16, 
                      "round3": 8, 
                      "round4": 4,
                      "round5": 2,
                      "round6": 1}

    structure_valid, structure_message = validate_structure(user_bracket, expected_rounds, expected_games)
    if not structure_valid:
        print(structure_message)
        sys.exit(1)
    
    # Validate initial matchups
    matchups_valid, matchups_message = validate_initial_matchups(user_bracket, initial_bracket)
    if not matchups_valid:
        print(matchups_message)
        sys.exit(1)
    
    content_valid, content_message = validate_content(user_bracket, initial_bracket)
    if not content_valid:
        print(content_message)
        sys.exit(1)
    
    # Add call to validate_progression when implemented

    print("Bracket validation passed!")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python validate_bracket.py <path_to_initial_bracket.json> <path_to_user_bracket.json>")
        sys.exit(1)

    initial_path = sys.argv[1]
    user_path = sys.argv[2]
    
    main(initial_path, user_path)
