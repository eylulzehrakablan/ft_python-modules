#! /usr/bin/python3

import sys


def ft_ancient_text() -> None:
    if not len(sys.argv) == 2:
        print("Usage: ft_ancient_fragment.py <file>")
    else:
        try:
            print(f"Accessing file '{sys.argv[1]}'")
            f = open(f"{sys.argv[1]}", "r")
            print("---\n")
            print(f.read())
            print("---")
            f.close()
            print(f"File '{sys.argv[1]}' closed")
        except Exception as e:
            print(f"Error opening a file '{sys.argv[1]}': {e}")


if __name__ == "__main__":
    print("=== Cyber Archives Recovery ===")
    ft_ancient_text()
