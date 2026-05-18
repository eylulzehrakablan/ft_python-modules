#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self._name = name
        self._height = height
        self._age = age

    def show(self) -> None:
        print(f"{self._name}: {self._height:.1f}cm, {self._age} days old")

    def grow(self, growth: float, days: int) -> None:
        print(f"[make {(self._name).lower()} grow and age for {days} days]")
        for day in range(1, days + 1):
            self._height += growth
            self._age += 1

    def set_height(self, value: float) -> None:
        if (value < 0):
            print(f"{self._name}: Error, height can't be negative")
            print("Height update rejected")
        else:
            self._height = value
            print(f"Height updated: {round(self.get_height())}cm")

    def set_age(self, value: int) -> None:
        if (value < 0):
            print(f"{self._name}: Error, age can't be negative")
            print("Age update rejected")
        else:
            self._age = value
            print(f"Age updated: {self.get_age()} days")

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age


class Flower(Plant):
    def __init__(
        self,
        name: str,
        height: float,
        age: int,
        color: str
    ) -> None:
        super().__init__(name, height, age)
        self.color = color
        self.is_blooming = False

    def bloom(self) -> None:
        print(f"[asking the {(self._name).lower()} to bloom]")
        self.is_blooming = True

    def show(self) -> None:
        super().show()
        print(f" Color: {self.color}")
        if (self.is_blooming):
            print(f" {self._name} is blooming beautifully!")
        else:
            print(f" {self._name} has not bloomed yet")


class Tree(Plant):
    def __init__(
        self,
        name: str,
        height: float,
        age: int,
        trunk_diameter: float
    ) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        print(f"[asking the {(self._name).lower()} to produce shade]")
        print(f"Tree {self._name} now produces a shade of {self._height:.1f}")
        print(f"cm long and {self.trunk_diameter:.1f}cm wide")

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {self.trunk_diameter:.1f}cm")


class Vegetable(Plant):
    def __init__(
        self,
        name: str,
        height: float,
        age: int,
        harvest_season: str,
        nutritional_value: float
    ) -> None:
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value
        self.total_nutrition: float = 0

    def grow(self, growth: float, days: int) -> None:
        super().grow(growth, days)
        for day in range(1, days + 1):
            self.total_nutrition += self.nutritional_value

    def show(self) -> None:
        super().show()
        print(f" Harvest season: {self.harvest_season}")
        print(f" Nutritional value: {round(self.total_nutrition)}")


if __name__ == "__main__":
    print("=== Garden Plant Types ===")

    print("=== Flower")
    rose = Flower("Rose",  15, 10, "red")
    rose.show()
    rose.bloom()
    rose.show()
    print("\n=== Tree")
    oak = Tree("Oak", 200, 365, 30)
    oak.show()
    oak.produce_shade()
    print("\n=== Vegetable")
    tomato = Vegetable("Tomato", 5, 10, "April", 0.5)
    tomato.show()
    tomato.grow(1, 20)
    tomato.show()
