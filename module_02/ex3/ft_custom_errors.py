#! /usr/bin/python3

class GardenError(Exception):
    def __init__(
            self,
            message: str = "Unknown garden error"
            ) -> None:
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message: str = "Unknown plant error") -> None:
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message: str = "Unknown water error") -> None:
        super().__init__(message)


class Garden():
    def __init__(
            self,
            plant_name: str,
            plant_water_level: int,
            water_tank_level: int
            ) -> None:
        self.plant_name = plant_name
        self.plant_water_level = plant_water_level
        self.water_tank_level = water_tank_level


def test_planterror() -> None:
    garden = Garden("tomato", 0, 0)

    if garden.plant_water_level <= 0:
        raise PlantError(f"The {garden.plant_name} plant is wilting!")
    else:
        print("PlantError test passed!")


def test_watererror() -> None:
    garden = Garden("tomato", 0, 0)

    if garden.water_tank_level <= 0:
        raise WaterError("Not enough water in the tank!")
    else:
        print("WaterError test passed!")


if __name__ == "__main__":
    print("=== Custom Garden Errors Demo ===")

    try:
        print("\nTesting PlantError...")
        test_planterror()
    except PlantError as e:
        print(f"Caught PlantError: {e}")

    try:
        print("\nTesting WaterError...")
        test_watererror()
    except WaterError as e:
        print(f"Caught WaterError: {e}")

    print("\nTesting catching all garden errors...")
    try:
        test_planterror()
    except GardenError as e:
        print(f"Caught GardenError: {e}")

    try:
        test_watererror()
    except GardenError as e:
        print(f"Caught GardenError: {e}")

    print("\nAll custom error types work correctly!")
