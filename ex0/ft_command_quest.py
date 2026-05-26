#! /usr/bin/python3

import sys


def ft_command_quest() -> None:
    print("=== Command Quest ===")
    print(f"Program name: {sys.argv[0]}")

    if len(sys.argv) == 1:
        print("No arguments provided!")
        return
    else:
        print(f"Arguments received: {len(sys.argv) - 1}")
        i: int = 1
        for arg in sys.argv:
            print(f"Argument {i}: {arg}")
            i += 1


if __name__ == "__main__":
    ft_command_quest()
    print(f"Total arguments: {len(sys.argv)}")
