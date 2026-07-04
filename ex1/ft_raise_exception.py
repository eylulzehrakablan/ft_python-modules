#! /usr/bin/python3

def input_temperature(temp_str: str) -> int:
    temp = int(temp_str)

    if temp < 0:
        raise ValueError(f"{temp}°C is too cold for plants (min 0°C)")
    elif temp > 40:
        raise ValueError(f"{temp}°C is too hot for plants (max 40°C)")

    return temp


def test_temperature() -> None:
    inputs = ["25", "abc", "100", "-50"]

    for input_value in inputs:
        try:
            print(f"\nInput data is '{input_value}'")
            temp = input_temperature(input_value)
            print(f"Temperature is now {temp}°C")
        except TypeError as e:
            print(f"Caught TypeError: {e}")
        except NameError as e:
            print(f"Caught NameError: {e}")
        except ValueError as e:
            print(f"Caught input_temperature error: {e}")
        except AttributeError as e:
            print(f"Caught AttributeError: {e}")
    print("\nAll tests completed - program didn't crash!")


if __name__ == "__main__":
    print("=== Garden Temperature Checker ===")
    test_temperature()
