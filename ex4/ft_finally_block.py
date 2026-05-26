#! /usr/bin/python3

class GardenError(Exception):
    def __init__(self, message: str = "Unknown plant error") -> None:
        self.message = message
        super().__init__(self.message)


class PlantError(GardenError):
    def __init__(self, message: str = "Unknown plant error") -> None:
        super().__init__(message)


def water_plant(plant_name: str) -> None:
    if plant_name == plant_name.capitalize():
        print(f"Watering {plant_name}: [OK]")
    else:
        raise PlantError(f"Invalid plant name to water: '{plant_name}'")


invalid_plants = ["tomato", "lettuce", "carrots"]
valid_plants = [plant.capitalize() for plant in invalid_plants]


def test_watering_system(message: str, plants: list[str]) -> None:
    print(message)

    try:
        print("Opening watering system")
        for plant in plants:
            water_plant(plant)
    except PlantError as e:
        print(f"Caught PlantError: {e}")
        print(".. ending tests and returning to main")
        return
    finally:
        print("Closing watering system\n")


if __name__ == "__main__":
    print("=== Garden Watering System ===\n")
    test_watering_system("Testing valid plants...", valid_plants)
    test_watering_system("Testing invalid plants...", invalid_plants)
    print("Cleanup always happens, even with errors!")
