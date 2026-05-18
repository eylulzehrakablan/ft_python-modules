#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age_in_days = age

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age_in_days} days old")


plants = (
    Plant("Rose", 25, 30),
    Plant("Sunflower", 80, 45),
    Plant("Cactus", 15, 120)
)


if __name__ == "__main__":
    print("=== Garden Plant Registry ===")
    for plant in plants:
        plant.show()
