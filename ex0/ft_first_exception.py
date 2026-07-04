#! /usr/bin/python3

def input_temperature(temp_str: str) -> int:
    return int(temp_str)


def test_temperature() -> None:
    inputs = ["25", "abc"]

    for input_value in inputs:
        try:
            print(f"\nInput data is '{input_value}'")
            input_temperature(input_value)
            print(f"Temperature is now {input_value}°C")

        except ValueError as e:
            print(f"Caught input_temperature error: {e}")

    print("\nAll tests completed - program didn't crash")


if __name__ == "__main__":
    print("=== Garden Temperature ===")
    test_temperature()
