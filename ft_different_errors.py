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
            case 3:
                "abc" + 42
            case 4:
                42 + 42
    except ValueError:
        print(f"Caught ValueError: invalid literal for int() with base 10: '{input_value}'")
    except ZeroDivisionError:
        print("Caught ZeroDivisionError: division by zero")
    except FileNotFoundError:
        print("Caught FileNotFoundError: [Errno 2] No such file or directory: 'example.txt'")
    except TypeError:
        print('Caught TypeError: can only concatenate str (not "int") to str')
    else:
        print("Operation completed successfully")


if __name__ == "__main__":
    print("=== Garden Error Types Demo ===")
    for operation_number in range(0, 5):
        print(f"Testing operation {operation_number}...")
        garden_operations(operation_number)
    print("\nAll error types tested successfully!")
