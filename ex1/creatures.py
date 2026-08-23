from ex0.creature import Creature
from .capabilities import HealCapability

class Sproutling(Creature, HealCapability):
    def __init__(self) -> None:
        super().__init__(name="Sproutling", creature_type="Grass")
        self.weapon: str = "Vine Whip"
    
    def attack(self) -> str:
        return f"{self.name} uses {self.weapon}!"

    def heal(self) -> str:
        return f"{self.name} heals itself for a small amount"


class Bloomelle(Creature, HealCapability):
    def __init__(self) -> None:
        super().__init__(name="Bloomelle", creature_type="Grass/Fairy")
        self.weapon: str = "Petal Dance"
    
    def attack(self) -> str:
        return f"{self.name} uses {self.weapon}!"

    def heal(self) -> str:
        return f"{self.name} heals itself and others for a large amount"
