#! /usr/bin/python3

class GardenError(Exception):
    def __init__(self, message: str = "Unknown plant error") -> None:
        self.message = message
        super().__init__(self.message)


class PlantError(GardenError):
    def __init__(self, message: str = "Unknown plant error") -> None:
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message: str = "Unknown plant error") -> None:
        super().__init__(message)


if __name__ == "__main__":
    print("=== Custom Garden Errors Demo ===\n")

    try:
        print("Testing PlantError...")
        raise PlantError("The tomate plant is wilting!")
    except PlantError as e:
        print(f"Caught PlantError: {e}")

    print()

    try:
        print("Testing WaterError...")
        raise WaterError("Not enough water in the tank!")
    except WaterError as e:
        print(f"Caught WaterError: {e}")

    print()

    print("Testing an catching all garden errors...")
    try:
        raise PlantError("The tomate plant is wilting!")
    except PlantError as e:
        print(f"Caught PlantError: {e}")

    try:
        raise WaterError("Not enough water in the tank!")
    except WaterError as e:
        print(f"Caught WaterError: {e}")

    print("\nAll custom error types work correctly!")
