#!/usr/bin/env python3

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


plants = [
    Plant("rose", 25, 30),
    Plant("oak", 200, 365),
    Plant("cactus", 5, 90),
    Plant("sunflower", 80, 45),
    Plant("fern", 15, 120)
]

if __name__ == "__main__":
    print("=== Plant Factory Output ===")
    for plant in plants:
        print("Created: ", end="")
        plant.show()
