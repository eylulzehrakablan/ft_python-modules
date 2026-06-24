#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self._name = name

        if height < 0:
            self._height = 0.0
            print(f"{self._name}: Error, height can't be negative")
        else:
            self._height = height
        if age < 0:
            self._age_in_days = 0
            print(f"{self._name}: Error, age can't be negative")
        else:
            self._age_in_days = age

    @classmethod
    def create_plant(cls):
        return cls("anonymous", 0.0, 0)

    @staticmethod
    def is_older_than_a_year(age):
        print(f"Is {age} days more than a year? -> {age > 365}")

    def show(self) -> None:
        print(f"{self._name.capitalize()}: "
              f"{(self.get_height()):.1f}cm, "
              f"{self.get_age()} days old")

    def set_height(self, height: float) -> None:
        if height < 0:
            print(f"{self._name}: Error, height can't be negative")
            print("Height update rejected")
        else:
            self._height = height
            print(f"Height updated: {round(self.get_height())}cm")

    def get_height(self) -> float:
        return self._height

    def set_age(self, age: int) -> None:
        if age < 0:
            print(f"{self._name}: Error, age can't be negative")
            print("Age update rejected")
        else:
            self._age_in_days = age
            print(f"Age updated: {self.get_age()} days")

    def get_age(self) -> int:
        return self._age_in_days

    def grow(self, growth: float, days: int) -> None:
        print(f"[make {self._name} grow and age for {days} days]")
        for _ in range(days):
            self._height += growth
            self.age()

    def age(self) -> None:
        self._age_in_days += 1


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
        if not self.is_blooming:
            print(f"[asking the {self._name} to grow and bloom]")
            self.is_blooming = True

    def show(self) -> None:
        super().show()
        print(f" Color: {self.color}")
        if self.is_blooming:
            print(f" {self._name.capitalize()} is blooming beautifully!")
        else:
            print(f" {self._name.capitalize()} has not bloomed yet")


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
        self.is_shading = False

    def produce_shade(self) -> None:
        if not self.is_shading:
            print(f"[asking the {self._name} to produce shade]")
            self.is_shading = True
            print(f"Tree {self._name.capitalize()} now produces a shade of "
                  f"{self.get_height():.1f}cm long and "
                  f"{self.trunk_diameter:.1f}cm wide.")

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {self.trunk_diameter:.1f}cm")


class Vegetable(Plant):
    def __init__(
            self,
            name: str,
            height: float,
            age: int,
            harvest_season: str
            ) -> None:
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = 0

    def show(self) -> None:
        super().show()
        print(f" Harvest season: {self.harvest_season.capitalize()}")
        print(f" Nutritional value: {self.nutritional_value}")

    def age(self) -> None:
        super().age()
        self.nutritional_value += 1



if __name__ == "__main__":
    print("=== Garden statistics ===")

    print("=== Check year-old")
    Plant.is_older_than_a_year(30)
    Plant.is_older_than_a_year(400)

    print()

    print("=== Flower")
    rose = Flower("rose", 15, 10, "red")
    rose.show()
    rose.bloom()