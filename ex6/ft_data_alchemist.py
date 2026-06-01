#! /usr/bin/python3

import random


players = ["Alice", "bob", "Charlie", "dylan", "Emma",
           "Gregory", "john", "kevin", "Liam"]


if __name__ == "__main__":
    print("=== Game Data Alchemist ===\n")
    print(f"Initial list of players: {players}")

    player_names_capitalized = [p.capitalize() for p in players]
    print(f"New list with all names capitalized: {player_names_capitalized}")

    print("New list of capitalized names only: "
          f"{[p for p in players if p == p.capitalize()]}\n")

    score_dict = {
        p: random.randint(50, 1000) for p in player_names_capitalized}
    print(f"Score dict: {score_dict}")

    average_score = (sum(score_dict.values()) / len(score_dict))
    print(f"Score average is {round(average_score, 2)}")

    high_scores = {
        p: score for p, score in score_dict.items() if score > average_score}
    print(f"High scores: {high_scores}")
