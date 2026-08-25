from abc import ABC, abstractmethod
from ex0.creature import Creature
import ex1
import typing


class InvalidStrategyError(Exception):
    def __init__(self, creature_name: str, strategy_name: str):
        message = f"Invalid Creature '{creature_name}' for this {strategy_name} strategy"
        super().__init__(message)


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
        if not self.is_valid(creature):
            raise InvalidStrategyError(creature.name, "normal")
        print(creature.attack())


class AggressiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, ex1.TransformCapability)

    def act(self, creature: Creature) -> None:
        if not self.is_valid(creature):
            raise InvalidStrategyError(creature.name, "aggressive")
        transformer = typing.cast(ex1.TransformCapability, creature)
        print(transformer.transform())
        print(creature.attack())
        print(transformer.revert())


class DefensiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, ex1.HealCapability)

    def act(self, creature: Creature) -> None:
        if not self.is_valid(creature):
            raise InvalidStrategyError(creature.name, "defensive")
        healer = typing.cast(ex1.HealCapability, creature)
        print(creature.attack())
        print(healer.heal())
