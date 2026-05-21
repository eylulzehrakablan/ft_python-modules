#! /usr/bin/python3

def input_temperature(temp_str: str) -> int | None:
    try:
        temp = int(temp_str)
        if temp >= 0 and temp <= 40:
            return temp
        elif temp < 0:
            message1 = f"Caught input_temperature error: {temp}"
            message2 = "°C is too cold for plants (min 0°C)"
            raise Exception(message1 + message2)
        else:
            message1 = f"Caught input_temperature error: {temp}"
            message2 = "°C is too hot for plants (max 40°C)"
            raise Exception(message1 + message2)
    except ValueError:
        print("Caught input_temperature error: ", end="")
        print(f"invalid literal for int() with base 10: '{temp_str}'")
        return None


def test_temperature() -> None:
    test_cases = ["25", "abc", "0", "-50", "100"]

    for case in test_cases:
        try:
            print(f"\nInput data is '{case}'")
            x = input_temperature(case)
            if (x):
                print(f"Temperature is now {case}°C")
            elif (x == 0):
                print(f"Temperature is now {case}°C")
        except Exception as e:
            print(e)
        except NameError:
            print("Caught name error: function name couldn't be found")
        except TypeError:
            print("Caught type error: function ", end="")
            print("missing required positional argument(s)")

    print("\nAll tests completed - program didn't crash!")


if __name__ == "__main__":
    print("=== Garden Temperature ===")
    test_temperature()
