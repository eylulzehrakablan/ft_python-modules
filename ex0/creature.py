from abc import ABC, abstractmethod


class Creature(ABC):
    def __init__(self, name: str, creature_type: str) -> None:
        self.name = name
        self.type = creature_type

    @abstractmethod
    def attack(self) -> str:
        pass

    def describe(self) -> str:
        return f"{self.name} is a {self.type} type Creature"


class Flameling(Creature):
    def __init__(self) -> None:
        super().__init__(name="Flameling", creature_type="Fire")
        self.weapon: str = "Ember"

    def attack(self) -> str:
        return f"{self.name} uses {self.weapon}!"


class Pyrodon(Creature):
    def __init__(self) -> None:
        super().__init__(name="Pyrodon", creature_type="Fire/Flying")
        self.weapon: str = "Flamethrower"

    def attack(self) -> str:
        return f"{self.name} uses {self.weapon}!"


class Aquabub(Creature):
    def __init__(self) -> None:
        super().__init__(name="Aquabub", creature_type="Water")
        self.weapon: str = "Water Gun"

    def attack(self) -> str:
        return f"{self.name} uses {self.weapon}!"


class Torragon(Creature):
    def __init__(self) -> None:
        super().__init__(name="Torragon", creature_type="Water")
        self.weapon: str = "Hydro Pump"

    def attack(self) -> str:
        return f"{self.name} uses {self.weapon}!"


if __name__ == "__main__":
    print("")
