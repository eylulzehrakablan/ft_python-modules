#!/usr/bin/env python3

class Plant:
    class Stats:
        def __init__(self) -> None:
            self._grow_calls = 0
            self._age_calls = 0
            self._show_calls = 0

        def count_grow(self) -> None:
            self._grow_calls += 1

        def count_age(self) -> None:
            self._age_calls += 1

        def count_show(self) -> None:
            self._show_calls += 1

        def display(self) -> None:
            print(f"Stats: {self._grow_calls} grow, "
                  f"{self._age_calls} age, {self._show_calls} show")

    def __init__(self, name: str, height: float, age: int) -> None:
        self._name = name
        self.stats = self.Stats()

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
    def create_anonymous(cls) -> "Plant":
        return cls("Unknown plant", 0.0, 0)

    @staticmethod
    def is_older_than_year(age: int) -> bool:
        return age > 365

    def show(self) -> None:
        self.stats.count_show()
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

    def grow(self, growth: float) -> None:
        self.stats.count_grow()
        self._height += growth

    def age(self, days: int) -> None:
        self.stats.count_age()
        self._age_in_days += days


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
        self.is_blooming = True

    def show(self) -> None:
        super().show()
        print(f" Color: {self.color}")
        if self.is_blooming:
            print(f" {self._name.capitalize()} is blooming beautifully!")
        else:
            print(f" {self._name.capitalize()} has not bloomed yet")


class Tree(Plant):
    class Stats(Plant.Stats):
        def __init__(self) -> None:
            super().__init__()
            self._shade_calls = 0

        def count_shade(self) -> None:
            self._shade_calls += 1

        def display(self) -> None:
            super().display()
            print(f" {self._shade_calls} shade")

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
        self.stats: Tree.Stats = self.Stats()

    def produce_shade(self) -> None:
        self.stats.count_shade()
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

    def age(self, days: int) -> None:
        super().age(days)
        self.nutritional_value += 1


class Seed(Flower):
    def __init__(
            self,
            name: str,
            height: float,
            age: int,
            color: str
            ) -> None:
        super().__init__(name, height, age, color)
        self.seed_count = 0

    def bloom(self) -> None:
        super().bloom()
        self.seed_count = 42

    def show(self) -> None:
        super().show()
        print(f" Seeds: {self.seed_count}")


def display_statistics(plant: Plant) -> None:
    print(f"[statistics for {plant._name.capitalize()}]")
    plant.stats.display()


if __name__ == "__main__":
    print("=== Garden statistics ===")

    print("=== Check year-old")
    print(f"Is 30 days more than a year? -> {Plant.is_older_than_year(30)}")
    print(f"Is 400 days more than a year? -> {Plant.is_older_than_year(400)}")

    print()

    print("=== Flower")
    rose = Flower("rose", 15, 10, "red")
    rose.show()
    display_statistics(rose)
    print(f"[asking the {rose._name} to grow and bloom]")
    rose.grow(8)
    rose.bloom()
    rose.show()
    display_statistics(rose)

    print()

    print("=== Tree")
    oak = Tree("oak", 200, 365, 5)
    oak.show()
    display_statistics(oak)
    print(f"[asking the {oak._name} to produce shade]")
    oak.produce_shade()
    display_statistics(oak)

    print()

    print("=== Seed")
    sunflower = Seed("sunflower", 80, 45, "yellow")
    sunflower.show()
    print(f"[make {sunflower._name} grow, age and bloom]")
    sunflower.grow(30)
    sunflower.age(20)
    sunflower.bloom()
    sunflower.show()
    display_statistics(sunflower)

    print()

    print("=== Anonymous")
    anonymous_plant = Plant.create_anonymous()
    anonymous_plant.show()
    display_statistics(anonymous_plant)
