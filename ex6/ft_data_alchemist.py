#! /usr/bin/python3

import random


def ft_data_alchemist() -> None:
    players = ["Alice", "bob", "Charlie", "dylan", "Emma",
               "Gregory", "john", "kevin", "Liam"]

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


if __name__ == "__main__":
    print("=== Game Data Alchemist ===\n")
    ft_data_alchemist()


# the basic formula
# [expression for item in iterable if condition]


# import random


# def ft_data_alchemist() -> None:
#     players = ["Alice", "bob", "Charlie", "dylan", "Emma",
#                "Gregory", "john", "kevin", "Liam"]
#     print(f"Initial list of players: {players}")
#     print()

#     player_names_capitalized = []
#     for p in players:
#         player_names_capitalized.append(p.capitalize())
#     print(f"New list with all names capitalized: {player_names_capitalized}")
#     print()

#     capitalized_only = []
#     for p in players:
#         if p == p.capitalize():
#             capitalized_only.append(p)
#     print(f"New list of capitalized names only: {capitalized_only}")
#     print()

#     score_dict = {}
#     for p in player_names_capitalized:
#         score_dict[p] = random.randint(50, 1000)
#     print(f"Score dict: {score_dict}")

#     score_average = (sum(score_dict.values()) / len(score_dict))
#     print(f"Score average is {round(score_average, 2)}")

#     high_scores = {}
#     for p in score_dict:
#         if score_dict[p] > score_average:
#             high_scores[p] = score_dict[p]
#     print(f"High scores: {high_scores}")


# if __name__ == "__main__":
#     print("=== Game Data Alchemist ===\n")
#     ft_data_alchemist()
