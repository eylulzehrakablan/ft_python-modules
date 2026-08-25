from abc import ABC, abstractmethod
from ex0.creature import Creature
import ex1
import typing


class BattleStrategy(ABC):
    @abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        pass

    @abstractmethod
    def act(self, creature: Creature) -> None:
        pass


class NormalStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return True

    def act(self, creature: Creature) -> None:
        if self.is_valid(creature):
            print(creature.attack())


class AggressiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, ex1.TransformCapability)

    def act(self, creature: Creature) -> None:
        if self.is_valid(creature):
            transformer = typing.cast(ex1.TransformCapability, creature)
            print(transformer.transform())
            print(creature.attack())
            print(transformer.revert())

            # print("===")
            # print(creature is transformer)
            # print(transformer is creature)
            # print(id(transformer))
            # print(id(creature))
            # print("===")


class DefensiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, ex1.HealCapability)

    def act(self, creature: Creature) -> None:
        if self.is_valid(creature):
            healer = typing.cast(ex1.HealCapability, creature)
            print(creature.attack())
            print(healer.heal())

            # print("===")
            # print(creature is healer)
            # print(healer is creature)
            # print(id(healer))
            # print(id(creature))
            # print("===")
