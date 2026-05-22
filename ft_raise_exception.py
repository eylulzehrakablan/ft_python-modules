#! /usr/bin/python3

def input_temperature(temp_str: str) -> int | None:
    try:
        temp = int(temp_str)
        if temp >= 0 and temp <= 40:
            return temp
        elif temp < 0:
            raise Exception(f"{temp}°C is too cold for plants (min 0°C)")
        else:
            raise Exception(f"{temp}°C is too hot for plants (max 40°C)")
    except ValueError as e:
        print(f"Caught input_temperature error: {e}")
        return None


def test_temperature() -> None:
    test_cases = ["25", "abc", "100", "-50"]

    for case in test_cases:
        try:
            print(f"\nInput data is '{case}'")
            x = input_temperature(case)
            if (x):
                print(f"Temperature is now {case}°C")
            elif (x == 0):
                print(f"Temperature is now {case}°C")
        except NameError as e:
            print(f"Caught NameError: {e}")
        except TypeError as e:
            print(f"Caught TypeError: function {e}")
        except Exception as e:
            print(f"Caught input_temperature error: {e}")
    print("\nAll tests completed - program didn't crash!")


if __name__ == "__main__":
    print("=== Garden Temperature ===")
    test_temperature()
