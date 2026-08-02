#! /usr/bin/python3

import sys


def ft_stream_management() -> None:
    if not len(sys.argv) == 2:
        print("Usage: ft_stream_management.py <file>")
        return

    file_path = sys.argv[1]

    try:
        print("=== Cyber Archives Recovery & Preservation ===")
        print(f"Accessing file '{file_path}'")

        f = open(file_path, "r")
        print("---\n")
        content = f.read()
        print(content, end="")
        if len(content) > 0 and not content[-1] == '\n':
            print()
        print("\n---")
        f.close()
        print(f"File '{file_path}' closed.")
    except (
        FileNotFoundError,
        PermissionError,
        IsADirectoryError,
        OSError
    ) as e:
        sys.stderr.write(f"[STDERR] Error opening file '{file_path}': {e}\n")
        return

    new_content = ""
    for char in content:
        if char == '\n':
            new_content += "#\n"
        else:
            new_content += char

    if len(content) > 0 and not content[-1] == '\n':
        new_content += "#"

    print("\nTransform data:\n---\n")
    print(new_content, end="")
    if len(new_content) > 0 and not new_content[-1] == '\n':
        print()
    print("\n---")

    sys.stdout.write("Enter new file name (or empty): ")
    sys.stdout.flush()
    raw_user_input = sys.stdin.readline()
    if len(raw_user_input) > 0 and raw_user_input[-1] == '\n':
        user_input = raw_user_input[:-1]
    else:
        user_input = raw_user_input

    if not user_input == "":
        try:
            f = open(user_input, "w")
            f.write(new_content)
            f.close()
            print(f"Saving data to '{user_input}'")
            print(f"Data saved in file '{user_input}'.")
        except (PermissionError, IsADirectoryError) as e:
            sys.stderr.write(f"[STDERR] Error opening file '{user_input}': {e}")
            sys.stderr.flush()
            sys.stdout.write("\n")
            print("Data not saved.")
            return
    else:
        print("Not saving data.")


if __name__ == "__main__":
    ft_stream_management()
