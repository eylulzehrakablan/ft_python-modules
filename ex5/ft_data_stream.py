#! /usr/bin/python3


import random
from typing import Generator

players = ["alice", "bob", "charlie", "dylan"]
actions = ["run", "eat", "sleep", "grab", "use",
           "move", "climb", "swim", "release"]


def gen_event() -> Generator[tuple[str, str], None, None]:
    while (True):
        yield (random.choice(players), random.choice(actions))


def consume_event(
        event_list: list[tuple[str, str]]) -> Generator[
            tuple[str, str], None, None]:
    while len(event_list) > 0:
        yield event_list.pop(random.randrange(len(event_list)))


if __name__ == "__main__":
    print("=== Game Data Stream Processor ===")

    g = gen_event()

    for i in range(1000):
        player, action = next(g)
        print(f"Event {i}: Player {player} did action {action}")

    event_list = []
    for i in range(10):
        event_list.append(next(g))
    print(f"Built list of 10 events: {event_list}")

    for event in consume_event(event_list):
        print(f"Got event from list: {event}")
        print(f"Remains in list: {event_list}")
