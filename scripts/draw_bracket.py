import json
import matplotlib.pyplot as plt
import os

# Change the current working directory to the script's directory
script_dir = os.path.dirname(__file__)  # Get the directory where the script is located
os.chdir(script_dir)  # Change the working directory

import json
import matplotlib.pyplot as plt
import numpy as np

def draw_game(ax, round_num, game_num, team1, team2, winner, total_rounds, y_step):
    # Calculate positions
    x = round_num
    y1 = 16 - (game_num * y_step) + round_num**1.5
    y2 = y1 - y_step / 2
    
    # Adjust text alignment
    align = "left" #if round_num < total_rounds / 2 else "right"
    
    # Draw team names
    ax.text(x, y1, team1, ha=align, va="center", fontsize=9)
    ax.text(x, y2, team2, ha=align, va="center", fontsize=9)
    
    # Draw connecting lines for winners
    if winner:
        next_x = x + 1 #if align == "left" else x - 1
        next_y = (y1 + y2) / 2
        ax.plot([next_x, x+0.3], [next_y, y1], color="gray", lw=1)
        ax.plot([next_x, x+0.3], [next_y, y2], color="gray", lw=1)
        # Highlight winner
        if round_num==total_rounds:
            ax.text(next_x+1, (y1 + y2) / 2, winner, ha=align, va="center", fontsize=9, color="blue")

def draw_bracket(file_path):
    with open(file_path, 'r') as f:
        bracket = json.load(f)

    fig, ax = plt.subplots(figsize=(12, 8))
    ax.axis('off')  # Turn off the axis

    total_rounds = len(bracket)
    y_step = 1
    game_num = 1

    for round_num, (round_name, games) in enumerate(bracket.items()):
        for game_name, game_details in games.items():
            team1 = game_details.get('team1', '')
            team2 = game_details.get('team2', '')
            winner = game_details.get('winner', '')
            draw_game(ax, round_num, game_num, team1, team2, winner, total_rounds, y_step)
            game_num += 1
        game_num = 1  # Reset game number for next round
        y_step *= 2  # Double the step size to spread out the teams in the next round

    plt.title('Tournament Bracket')
    plt.show()

draw_bracket('final_bracket.json')
