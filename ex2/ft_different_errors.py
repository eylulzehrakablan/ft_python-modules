#! /usr/bin/python3

def garden_operations(operation_number: int) -> None:
    match operation_number:
        case 0:
            int("abc")
        case 1:
            1 / 0
        case 2:
            open("/non/existent/file")
        case 3:
            "1" + 1
        case _:
            return None


def test_error_types() -> None:
    operation_numbers = [0, 1, 2, 3, 4]
    for number in operation_numbers:
        print(f"Testing operation {number}...")
        try:
            garden_operations(number)
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

    print("\nAll error types tested successfully!")


if __name__ == "__main__":
    print("=== Garden Error Types Demo ===")
    test_error_types()
