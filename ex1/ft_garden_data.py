#! /usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def show(self) -> None:
        print(f"{self.name.capitalize()}: "
              f"{self.height}cm, "
              f"{self.age} days old")


plants = [
    Plant("rose", 25, 30),
    Plant("sunflower", 80, 45),
    Plant("cactus", 15, 120)
]


if __name__ == "__main__":
    print("=== Garden Plant Registry ===")
    for plant in plants:
        plant.show()
