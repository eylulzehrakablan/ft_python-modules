#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self.height = height
        self.age_in_days = age

    def show(self) -> None:
        print(f"{self.name}: {self.height:.1f}cm, {self.age_in_days} days old")

    def grow(self, growth: float) -> None:
        self.height += growth
        Plant.age(self)

    def age(self) -> None:
        self.age_in_days += 1


plants = [
    Plant("Rose", 25, 30),
    Plant("Oak", 200, 365),
    Plant("Cactus", 5, 90),
    Plant("Sunflower", 80, 45),
    Plant("Fern", 15, 120)
]


if __name__ == "__main__":
    print("=== Plant Factory Output ===")
    for plant in plants:
        print("Created: ", end="")
        plant.show()

    # for day in range(1, 8):
    #     for plant in plants:
    #         match plant.name:
    #             case "Rose":
    #                 plant.grow(0.1)
    #             case "Oak":
    #                 plant.grow(1.5)
    #             case "Cactus":
    #                 plant.grow(1.2)
    #             case "Sunflower":
    #                 plant.grow(0.8)
    #             case "Fern":
    #                 plant.grow(0.2)
    #             case _:
    #                 print("No match")
    #     print(f"\n= Day {day} =")
    #     for plant in plants:
    #         plant.show()
    # print("\n=== After Growth ===")
    # for plant in plants:
    #     plant.show()
