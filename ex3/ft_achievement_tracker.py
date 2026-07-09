#! /usr/bin/python3

import random


achievmnts = ("Untouchable", "Crafting Genius", "Strategist", "World Savior",
              "Speed Runner", "Survivor", "Master Explorer", "Treasure Hunter",
              "Unstoppable", "First Steps", "Collector Supreme", "Sharp Mind",
              "Boss Slayer", "Hidden Path Finder")


def gen_players_achievements() -> set[str]:
    return set(random.sample(achievmnts, k=random.randint(1, len(achievmnts))))


def ft_achievement_tracker() -> None:
    players = ["Alice", "Bob", "Charlie", "Dylan"]
    player_sets: list[set[str]] = []

    i = 0
    while i < len(players):
        current_set = gen_players_achievements()
        player_sets = player_sets + [current_set]
        print(f"Player {players[i]}: {current_set}")
        if not i == len(players) - 1:
            print("-"*60)
        else:
            print("\n" + "="*60)
        i += 1

    all_distinct_achievements = set().union(*player_sets)
    print(f"\nAll distinct achievements: {all_distinct_achievements}")

    common_achievements = all_distinct_achievements.intersection(*player_sets)
    print(f"\nCommon achievements: {common_achievements}")

    print("\n" + "="*60, sep="", end="\n\n")

    i = 0
    while i < len(players):
        other_players_union = set().union(
            *player_sets[:i],
            *player_sets[i+1:]
        )
        only_player_has = set(player_sets[i]).difference(other_players_union)
        print(f"Only {players[i]} has: {only_player_has}")
        i += 1

    print("\n" + "="*60, sep="", end="\n\n")

    i = 0
    while i < len(players):
        missing = set(achievmnts).difference(player_sets[i])
        print(f"{players[i]} is missing: {missing}")
        if not i == len(players) - 1:
            print("-"*60)
        i += 1


if __name__ == "__main__":
    print("=== Achievement Tracker System ===\n")
    ft_achievement_tracker()
