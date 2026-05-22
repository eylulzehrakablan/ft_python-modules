#! /usr/bin/python3

def garden_operations(operation_number: int) -> None:
    try:
        match operation_number:
            case 0:
                input_value = "abc"
                int(input_value)
            case 1:
                42 / 0
            case 2:
                open("example.txt")
    except ValueError:
        print(f"Caught ValueError: invalid literal for int() with base 10: '{input_value}'")
    except ZeroDivisionError:
        print("Caught ZeroDivisionError: division by zero")
    except FileNotFoundError:
        print("FileNotFoundError: [Errno 2] No such file or directory: 'example.txt'")


if __name__ == "__main__":
    print("=== Garden Error Types Demo ===")
    for operation_number in range(0, 3):
        print()
        print(f"Testing operation {operation_number}...")
        garden_operations(operation_number)
