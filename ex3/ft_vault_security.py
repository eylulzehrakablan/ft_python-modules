#! /usr/bin/python3


def secure_archive(
    file_name: str,
    action: str = "read",
    content: str = ""
) -> tuple[bool, str]:
    try:
        if action == "read":
            with open(file_name, "r") as f:
                return (True, f.read())
        elif action == "write":
            with open(file_name, "w") as f:
                f.write(content)
            return (True, "Content successfully written to file")
        else:
            return (False, "Invalid action")
    except Exception as e:
        return (False, str(e))


if __name__ == "__main__":
    print("=== Cyber Archives Security ===\n")

    print("Using 'secure_archive' to read from a nonexisting file:")
    print(secure_archive("/non/existing/file"), end="\n\n")

    print("Using 'secure_archive' to read from an inaccessible file:")
    print(secure_archive("/etc/sudoers"), end="\n\n")

    print("Using 'secure_archive' to read from a regular file:")
    print(secure_archive("ancient_fragment.txt"), end="\n\n")

    print("Using 'secure_archive' to write content to a new file:")
    print(
        secure_archive(
            "new.txt",
            "write",
            "[FRAGMENT 001] Digital preservation protocols established 2087\n"
            "[FRAGMENT 002] Knowledge must survive the entropy wars\n"
            "[FRAGMENT 003] Every byte saved is a victory against oblivion\n"
        ),
    )
