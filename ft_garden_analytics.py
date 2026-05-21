#!/usr/bin/env python3

class Plant:
    class _Stats:
        def __init__(self) -> None:
            self._grow_calls: int = 0
            self._age_calls: int = 0
            self._show_calls: int = 0
            self._shade_calls: int = 0

        def display(self) -> None:
            print(f"Stats: {self._grow_calls} grow, ", end="")
            print(f"{self._age_calls} age, {self._show_calls} show")

    def __init__(self, name: str, height: float, age: int) -> None:
        self._name = name
        self._height = height
        self._age_in_days = age
        self._stats = self._Stats()

    @staticmethod
    def is_older_than_one_year(age: int) -> None:
        print(f"Is {age} days more than a year? ", end="")
        if (age > 365):
            print("-> True")
        else:
            print("-> False")

    @classmethod
    def create_anonymous_plant(cls) -> "Plant":
        return cls("Unknown plant", 0, 0)

    def grow(self, growth: float) -> None:
        self._height += growth
        self._stats._grow_calls += 1

    def age(self) -> None:
        self._age_in_days += 1
        self._stats._age_calls += 1

    def show(self) -> None:
        print(f"{self._name}: ", end="")
        print(f"{self._height:.1f}cm, {self._age_in_days} days old")
        self._stats._show_calls += 1

    def display_stats(self) -> None:
        display_stats(self)


def display_stats(plant: Plant) -> None:
    print(f"[statistics for {plant._name}]")
    plant._stats.display()


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
        print(f"[asking the {(self._name).lower()} to grow and bloom]")
        self.is_blooming = True
        self.grow(1)

    def show(self) -> None:
        super().show()
        print(f" Color: {self.color}")
        if (self.is_blooming):
            print(f" {self._name} is blooming beautifully!")
        else:
            print(f" {self._name} has not bloomed yet")

    def display_stats(self) -> None:
        display_stats(self)


class Seed(Flower):
    def __init__(
        self,
        name: str,
        height: float,
        age: int,
        color: str,
    ) -> None:
        super().__init__(name, height, age, color)
        self.seeds: int = 0

    def show(self) -> None:
        super().show()
        print(f" Seeds: {self.seeds}")

    def bloom(self) -> None:
        print(f"[make {self._name} grow, age and bloom]")
        self.is_blooming = True
        self.seeds += 42
        self.age()
        self.grow(1.5)

    def display_stats(self) -> None:
        display_stats(self)


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
        self.is_shading = True
        self._stats._shade_calls += 1
        print(f"[asking the {(self._name).lower()} to produce shade]")
        print(f"Tree {self._name} now produces a shade of ", end="")
        print(f"{self._height:.1f}", end="")
        print(f"cm long and {self.trunk_diameter:.1f}cm wide.")

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {self.trunk_diameter:.1f}cm")

    def display_stats(self) -> None:
        display_stats(self)
        print(f" {self._stats._shade_calls} shade")


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
        super().grow(growth)
        for day in range(1, days + 1):
            self.total_nutrition += self.nutritional_value

    def show(self) -> None:
        super().show()
        print(f" Harvest season: {self.harvest_season}")
        print(f" Nutritional value: {round(self.total_nutrition)}")

    def display_stats(self) -> None:
        display_stats(self)


if __name__ == "__main__":
    print("=== Garden statistics ===")
    print("=== Check year-old")
    Plant.is_older_than_one_year(30)
    Plant.is_older_than_one_year(400)

    print("\n=== Flower")
    rose = Flower("Rose",  15, 10, "red")
    rose.show()
    rose.display_stats()
    rose.bloom()
    rose.show()
    rose.display_stats()

    print("\n=== Tree")
    oak = Tree("Oak", 200, 365, 30)
    oak.show()
    oak.display_stats()
    oak.produce_shade()
    oak.display_stats()

    print("\n=== Seed")
    sunflower = Seed("Sunflower", 80, 45, "yellow")
    sunflower.show()
    sunflower.bloom()
    sunflower.show()
    sunflower.display_stats()

    print("\n=== Anonymous")
    p1 = Plant.create_anonymous_plant()
    p1.show()
    p1.display_stats()
