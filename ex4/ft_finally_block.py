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


plants = ["Tomato", "lettuce", "carrots"]


def test_watering_system() -> None:
    print("Testing valid plants...")
    try:
        print("Opening watering system")
        for plant in plants:
            water_plant(plant.capitalize())
        print("Closing watering system\n")
        print("Opening watering system")
        print("Testing invalid plants...")
        for plant in plants:
            water_plant(plant)
    except PlantError as e:
        print(f"Caught PlantError: {e}")
        print(".. ending tests and returning to main")
        print("Closing watering system")
        return
    else:
        print("Closing watering system")
    finally:
        print("\nCleanup always happens, even with errors!")


if __name__ == "__main__":
    print("=== Garden Watering System ===\n")
    test_watering_system()
