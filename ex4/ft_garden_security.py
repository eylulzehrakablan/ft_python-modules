#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.__name = name
        self.__height = height
        self.__age = age

    def show(self) -> None:
        print(f"{self.__name}: {self.__height:.1f}cm, {self.__age} days old")

    def set_height(self, value: float) -> None:
        if (value < 0):
            print(f"{self.__name}: Error, height can't be negative")
            print("Height update rejected")
        else:
            self.__height = value
            print(f"Height updated: {round(self.get_height())}cm")

    def set_age(self, value: int) -> None:
        if (value < 0):
            print(f"{self.__name}: Error, age can't be negative")
            print("Age update rejected")
        else:
            self.__age = value
            print(f"Age updated: {self.get_age()} days")

    def get_height(self) -> float:
        return self.__height

    def get_age(self) -> int:
        return self.__age


if __name__ == "__main__":
    print("=== Garden Security System ===")
    rose = Plant("Rose", 15, 10)
    print("Plant created: ", end="")
    rose.show()
    print()
    rose.set_height(25)
    rose.set_age(30)
    print()
    rose.set_height(-5)
    rose.set_age(-5)
    print()
    print("Current state: ", end="")
    rose.show()
