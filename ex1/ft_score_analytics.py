#! /usr/bin/python3

import sys


def py_atoi(tmp_str: str) -> int | None:
    try:
        return int(tmp_str)
    except ValueError:
        print(f"Invalid parameter: '{tmp_str}'")
        return None


def print_scores(scores: list[int]) -> None:
    print(f"Scores processed: {scores}")
    print(f"Total players: {len(sys.argv) - 1}")
    print(f"Total score: {sum(scores)}")
    print(f"Average score: {sum(scores) / (len(sys.argv) - 1)}")
    print(f"High score: {max(scores)}")
    print(f"Low score: {min(scores)}")
    print(f"Score range: {max(scores) - min(scores)}")


def ft_score_analytics() -> None:
    scores: list[str] = []

    for arg in sys.argv[1:]:
        value = py_atoi(arg)
        if value is not None:
            scores.append(value)

    if len(sys.argv) == 1 or not scores:
        print("No scores provided. Usage: python3", end="")
        print(f"{sys.argv[0]} <score1> <score2> ...")
    else:
        print_scores(scores)


if __name__ == "__main__":
    print("=== Player Score Analytics ===")
    ft_score_analytics()
