#! /usr/bin/python3

import sys


def ft_ancient_text() -> None:
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


def ft_archive_creation(new_content: str = "") -> None:
    if not len(sys.argv) == 2:
        print("Usage: ft_archive_creation.py <file>")
    else:
        ft_ancient_text()

        f = open(f"{sys.argv[1]}", "r")
        lines = f.readlines()
        f.close()

        for line in lines:
            new_line = line[:-1]
            new_content += new_line + "#\n"

        print("\nTransform data:\n---\n")
        print(new_content)
        print("---\n")

        user_input = input("Enter new file name (or empty): ")
        if not user_input == "":
            f = open(user_input, "w")
            f.write(new_content)
            f.close()
            print(f"Saving data to '{user_input}'")
            print(f"Data saved in file '{user_input}'.")
        else:
            print("Not saving data.")


if __name__ == "__main__":
    print("=== Cyber Archives Recovery & Preservation ===")
    ft_archive_creation()
