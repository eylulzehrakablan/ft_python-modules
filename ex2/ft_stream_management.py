#! /usr/bin/python3

import sys


def ft_stream_management() -> None:
    if not len(sys.argv) == 2:
        print("Usage: ft_archive_creation.py <file>")
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
    except (FileNotFoundError, PermissionError, IsADirectoryError, OSError) as e:
        print(f"[STDERR] Error opening file '{file_path}': {e}")
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
            print(f"[STDERR] Error opening file '{user_input}': {e}", file=sys.stderr)
            print("Data not saved.")
            return
    else:
        print("Not saving data.")

#     print(f"Accessing file '{sys.argv[1]}'")
#     f = open(f"{sys.argv[1]}", "r")
#     print("---\n")
#     print(f.read())
#     print("---")
#     f.close()
#     print(f"File '{sys.argv[1]}' closed")


# def ft_stream_management() -> None:
#     if not len(sys.argv) == 2:
#         print("Usage: ft_archive_creation.py <file>")
#         return

#     try:
#         ft_ancient_text()

#         f = open(f"{sys.argv[1]}", "r")
#         lines = f.readlines()
#         f.close()

#         new_content = ""
#         for line in lines:
#             new_line = line[:-1]
#             new_content += new_line + "#\n"

#         print("\nTransform data:\n---\n")
#         print(new_content)
#         print("---\n")

#         sys.stdout.write("Enter new file name (or empty): ")
#         sys.stdout.flush()
#         user_input = (sys.stdin.readline())[:-1]
#         if not user_input == "":
#             f = open(user_input, "w")
#             f.write(new_content)
#             f.close()
#             print(f"Saving data to '{user_input}'")
#             print(f"Data saved in file '{user_input}'.")
#         else:
#             print("Not saving data.")
#     except (FileNotFoundError, PermissionError, IsADirectoryError) as e:
#         print(f"[STDERR] Error opening a file '{sys.argv[1]}': {e}", file=sys.stderr)


if __name__ == "__main__":
    print("=== Cyber Archives Recovery & Preservation ===")
    ft_stream_management()
