#! /usr/bin/python3

import sys


def ft_ancient_text() -> None:
    if not len(sys.argv) == 2:
        print("Usage: ft_ancient_fragment.py <file>")
        return

    file_path = sys.argv[1]

    try:
        print("=== Cyber Archives Recovery ===")
        print(f"Accessing file '{file_path}'")

        f = open(file_path, "r")
        print("---\n")
        print(f.read())
        print("---")
        f.close()
        print(f"File '{file_path}' closed")
    except (FileNotFoundError, PermissionError) as e:
        print(f"Error opening file '{file_path}': {e}")


if __name__ == "__main__":
    ft_ancient_text()
