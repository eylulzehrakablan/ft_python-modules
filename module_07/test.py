from ex1.capabilities import TransformCapability
from ex0.creature import Creature
from ex0.factories import CreatureFactory


class FTCreatureFactory(CreatureFactory):
    def create_cadet(self) -> Creature:
        return CadetCreature()

    def create_transcender(self) -> Creature:
        return TranscenderCreature()


class CadetCreature(Creature):
    def __init__(self) -> None:
        super().__init__(name="Cadet", creature_type="Student")
        self.weapon: str = "Keyboard"

    def attack(self) -> str:
        return f"{self.name} uses {self.weapon}"


class TranscenderCreature(Creature, TransformCapability):
    def __init__(self) -> None:
        super().__init__(name="Cadet", creature_type="Student")
        # Creature.__init__(self, name="Cadet", creature_type="Student")
        # TransformCapability.__init__(self)
        self.weapon: str = "Keyboard"

    def attack(self) -> str:
        if self.is_transformed:
            return f"{self.name} performs a boosted strike!"
        return f"{self.name} attacks normally."

    def transform(self) -> str:
        self.is_transformed = True
        return f"{self.name} shifts into a sharper form!"

    def revert(self) -> str:
        self.is_transformed = False
        return f"{self.name} returns to normal."


if __name__ == "__main__":
    # print(creatures.Shiftling.__mro__)
    print(CadetCreature.__mro__)
    print(TranscenderCreature.__mro__)
    transcender = TranscenderCreature()
    print(transcender.attack())
