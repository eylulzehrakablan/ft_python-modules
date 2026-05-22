#! /usr/bin/python3

def garden_operations(operation_number: int) -> None:
    match operation_number:
        case 0:               
            input_value = "abc"
            int(input_value)
        case 1:
            42 / 0
        case 2:               
            open("example.txt")
        case 3:
            "abc" + 42
        case 4:
            42 + 42


def test_error_types():
    for operation_number in range(5):
        print(f"Testing operation {operation_number}")
        try:
            garden_operations(operation_number)
        except ValueError as e:
            print(f"Caught ValueError: {e}")
        except ZeroDivisionError as e:
            print(f"Caught ZeroDivisionError: {e}")
        except FileNotFoundError as e:
            print(f"Caught FileNotFoundError: {e}")
        except TypeError as e:
            print(f"Caught TypeError: {e}")
        else:
            print("Operation completed successfully")


if __name__ == "__main__":
    print("=== Garden Error Types Demo ===")
    test_error_types()
print("\nAll error types tested successfully!")
