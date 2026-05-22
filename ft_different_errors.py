#! /usr/bin/python3

def garden_operations(operation_number: int) -> None:
    try:
        match operation_number:
            case 0:
                input_value = "abc"
                int(input_value)
    except ValueError:
        print(f"Caught ValueError: invalid literal for int() with base 10: '{input_value}'")


if __name__ == "__main__":
    print("=== Garden Error Types Demo ===")
    for operation_number in range(0, 1):
        print()
        print(f"Testing operation {operation_number}...")
        garden_operations(operation_number)
