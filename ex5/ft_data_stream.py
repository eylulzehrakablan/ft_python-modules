#! /usr/bin/python3


import random
from typing import Generator

players = ["alice", "bob", "charlie", "dylan"]
actions = ["run", "eat", "sleep", "grab", "use", "move", "climb", "swim", "release"]

def gen_event() -> Generator[tuple[str, str], None, None]:
    while (True):
        yield (random.choice(players), random.choice(actions))


if __name__ == "__main__":
    print("=== Game Data Stream Processor ===")
    
    g = gen_event()

    for i in range(1000):
        player, action = next(g)
        print(f"Event {i}: Player {player} did action {action}")
