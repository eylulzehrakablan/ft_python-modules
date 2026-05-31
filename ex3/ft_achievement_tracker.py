#! /usr/bin/python3

import random


achievements = ("Untouchable", "Crafting Genius", "Strategist", "World Savior",
                "Speed Runner", "Survivor", "Master Explorer", "Treasure Hunter",
                "Unstoppable", "First Steps", "Collector Supreme", "Sharp Mind",
                "Boss Slayer", "Hidden Path Finder")


def gen_players_achievements() -> set[str]:
    return set(random.sample(achievements, k=random.randint(1, len(achievements))))


if __name__ == "__main__":
    print("=== Achievement Tracker System ===\n")

    players = ["Alice", "Bob", "Charlie", "Dylan"]
    distinct_achievements_sets = []

    for i, player in enumerate(players):
        player_achievements = gen_players_achievements()
        distinct_achievements_sets.append(player_achievements)
        print(f"Player {player}: {player_achievements}\n")
        i += 1

    distinct_achievements = set().union(*distinct_achievements_sets)
    print(f"All distinct achievements: {distinct_achievements}\n")

    common_achievements = set(distinct_achievements_sets[0]).intersection(*distinct_achievements_sets[1:])
    print(f"Common achievements: {common_achievements}\n")

    for i, player in enumerate(players):
        other_players_union = set().union(
            *distinct_achievements_sets[:i],
            *distinct_achievements_sets[i+1:]
        )
        only_player_has = set(distinct_achievements_sets[i]).difference(other_players_union)
        print(f"Only {player} has: {only_player_has}")
        i += 1
    print()
    for i, player in enumerate(players):
        print(f"{player} is missing: {set(achievements) - distinct_achievements_sets[i]}")
        i += 1
