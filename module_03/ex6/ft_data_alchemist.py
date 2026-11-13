#! /usr/bin/python3

import random


if __name__ == "__main__":
    print("=== Game Data Alchemist ===\n")

    players = ["Alice", "bob", "Charlie", "dylan", "Emma",
               "Gregory", "john", "kevin", "Liam"]
    print(f"Initial list of players: {players}\n")

    player_names_capitalized = [p.capitalize() for p in players]
    print(f"New list with all names capitalized: {player_names_capitalized}\n")

    capitalized_only = [p for p in players if p == p.capitalize()]
    print(f"New list of capitalized names only: {capitalized_only}\n")

    score_dict = {
        p: random.randint(50, 1000) for p in player_names_capitalized}
    print(f"Score dict: {score_dict}")

    score_average = round(sum(score_dict.values()) / len(score_dict), 2)
    print(f"\nScore average is {score_average}")

    high_scores = {
        p: score for p, score in score_dict.items() if score > score_average}
    print(f"\nHigh scores: {high_scores}")
