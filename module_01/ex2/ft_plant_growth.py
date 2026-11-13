#! /usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self.height = height
        self.age_in_days = age

    def show(self) -> None:
        print(f"{self.name.capitalize()}: "
              f"{self.height:.1f}cm, "
              f"{self.age_in_days} days old")

    def grow(self, growth: float) -> None:
        self.height += growth
        self.age()

    def age(self) -> None:
        self.age_in_days += 1


if __name__ == "__main__":

    print("=== Garden Plant Growth ===")

    plant = Plant("rose", 25, 30)
    plant.show()
    initial_height = plant.height

    for day in range(1, 8):
        print(f"=== Day {day} ===")
        plant.grow(0.8)
        plant.show()

    print(f"Growth this week: {(plant.height - initial_height):.1f}cm")
