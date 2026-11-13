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

    def show(self) -> None:
        print(f"{self._name.capitalize()}: "
              f"{(self.get_height()):.1f}cm, "
              f"{self.get_age()} days old")

    def set_height(self, height: float) -> None:
        if height < 0:
            print(f"{self._name.capitalize()}: "
                  "Error, height can't be negative")
            print("Height update rejected")
        else:
            self._height = height
            print(f"Height updated: {round(self.get_height())}cm")

    def get_height(self) -> float:
        return self._height

    def set_age(self, age: int) -> None:
        if age < 0:
            print(f"{self._name.capitalize()}: Error, age can't be negative")
            print("Age update rejected")
        else:
            self._age_in_days = age
            print(f"Age updated: {self.get_age()} days")

    def get_age(self) -> int:
        return self._age_in_days


if __name__ == "__main__":
    print("=== Garden Security System ===")
    plant = Plant("rose", 15, 10)
    print("Plant created: ", end="")
    plant.show()
    print()
    plant.set_height(25)
    plant.set_age(30)
    print()
    plant.set_height(-25)
    plant.set_age(-5)
    print()
    print("Current state: ", end="")
    plant.show()
