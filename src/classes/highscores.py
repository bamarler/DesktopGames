# highscores.py

import os

HIGH_SCORE_FILE = "highscores.txt"

def save_high_score(game_name, high_score):
    high_scores = load_high_scores()
    high_scores[game_name] = high_score
    with open(HIGH_SCORE_FILE, "w") as file:
        for game, score in high_scores.items():
            file.write(f"{game}: {score}\n")

def load_high_scores():
    high_scores = {}
    if os.path.exists(HIGH_SCORE_FILE):
        with open(HIGH_SCORE_FILE, "r") as file:
            for line in file:
                game, score = line.strip().split(": ")
                high_scores[game] = int(score)
    return high_scores

def load_high_score(game_name):
    high_scores = load_high_scores()
    return high_scores.get(game_name, 0)