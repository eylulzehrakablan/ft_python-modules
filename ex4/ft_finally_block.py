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


plants = ["tomato", "lettuce", "carrots"]


def test_watering_system(message, plants) -> None:
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
    test_watering_system("Testing valid plants...", [plant.capitalize() for plant in plants])
    test_watering_system("Testing invalid plants...", plants)
    print("Cleanup always happens, even with errors!")
