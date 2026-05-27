#! /usr/bin/python3

import sys


def ft_ancient_text() -> None:
    print(f"Accessing file '{sys.argv[1]}'")
    f = open(f"{sys.argv[1]}", "r")
    print("---\n")
    print(f.read())
    print("---")
    f.close()
    print(f"File '{sys.argv[1]}' closed")


def ft_archive_creation() -> None:
    if not len(sys.argv) == 2:
        print("Usage: ft_archive_creation.py <file>")
        return

    try:
        ft_ancient_text()

        f = open(f"{sys.argv[1]}", "r")
        lines = f.readlines()
        f.close()

        new_content = ""
        for line in lines:
            new_line = line[:-1]
            new_content += new_line + "#\n"

        print("\nTransform data:\n---\n")
        print(new_content)
        print("---\n")

        sys.stdout.write("Enter new file name (or empty): ")
        sys.stdout.flush()
        user_input = (sys.stdin.readline())[:-1]
        if not user_input == "":
            f = open(user_input, "w")
            f.write(new_content)
            f.close()
            print(f"Saving data to '{user_input}'")
            print(f"Data saved in file '{user_input}'.")
        else:
            print("Not saving data.")
    except Exception as e:
        print(f"[STDERR] Error opening a file '{sys.argv[1]}': {e}", file=sys.stderr)


if __name__ == "__main__":
    print("=== Cyber Archives Recovery & Preservation ===")
    ft_archive_creation()
