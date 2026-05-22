#! /usr/bin/python3

def input_temperature(temp_str: str) -> int | None:
    try:
        return int(temp_str)
    except ValueError:
        print("Caught input_temperature error: ", end="")
        print(f"invalid literal for int() with base 10: '{temp_str}'")
        return None
    except Exception:
        print("Caught an error")
        return None


def test_temperature(user_input: str) -> None:
    try:
        print(f"\nInput data is '{user_input}'")
        x = input_temperature(user_input)
        if (x):
            print(f"Temperature is now {user_input}°C")
        elif (x == 0):
            print(f"Temperature is now {user_input}°C")
    except NameError:
        print("Caught name error: function name couldn't be found")
    except TypeError:
        print("Caught type error: function ", end="")
        print("missing required positional argument(s)")
    except Exception:
        print("Caught an error")


if __name__ == "__main__":
    print("=== Garden Temperature ===")
    test_temperature("25")
    test_temperature("abc")

    print("\nAll tests completed - program didn't crash!")
