#! /usr/bin/python3

import sys


def ft_command_quest() -> None:
    print(f"Program name: {sys.argv[0]}")

    try:
        _ = sys.argv[1]

        print(f"Arguments received: {len(sys.argv) - 1}")
        i: int = 1
        for arg in sys.argv[1:]:
            print(f"Argument {i}: {arg}")
            i += 1
    except IndexError:
        print("No arguments provided!")


if __name__ == "__main__":
    print("=== Command Quest ===")
    ft_command_quest()
    print(f"Total arguments: {len(sys.argv)}")
