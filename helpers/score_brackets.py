import json
import os

# Get the directory where the script is located
script_dir = os.path.dirname(__file__)
brackets_dir = os.path.abspath(os.path.join(script_dir, '..'))

def load_json(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def score_bracket(user_bracket, answer_key):
    score = 0
    points_per_round = {1: 1, 2: 2, 3: 4, 4: 8, 5: 16, 6: 32}  # Points for each round

    for round_num, round_name in enumerate(answer_key, start=1):
        for game_id, game in answer_key[round_name].items():
            if game_id in user_bracket[round_name]:
                # Compare the winners in the same game of both brackets
                if game["winner"] == user_bracket[round_name][game_id]["winner"]:
                    score += points_per_round[round_num]
    
    return score

def main():
    final_bracket = os.path.join(brackets_dir, 'final_bracket.json')
    answer_key = os.path.join(brackets_dir, 'answer_key.json')
    user_bracket = load_json(final_bracket)
    answer_key = load_json(answer_key)
    
    user_score = score_bracket(user_bracket, answer_key)
    print(f"User's Bracket Score: {user_score}")

if __name__ == "__main__":
    main()
