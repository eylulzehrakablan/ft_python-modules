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


if __name__ == "__main__":
    rose = Plant("Rose", 25, 30)
    initial_height = rose.height
    print("=== Garden Plant Growth ===")
    rose.show()
    for day in range(1, 8):
        print(f"=== Day {day} ===")
        rose.grow(0.8)
        rose.show()
    print(f"Growth this week: {(rose.height - initial_height):.1f}cm")
