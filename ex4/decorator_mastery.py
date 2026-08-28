from collections.abc import Callable
from functools import wraps
from typing import Any
import time


def spell_timer(func: Callable) -> Callable:
    @wraps(spell_timer)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        print(f"Casting {func.__name__}...")
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Spell completed in {end_time - start_time:.3f} seconds")
        return result
    return wrapper

def power_validator(min_power: int) -> Callable:
    pass


def retry_spell(max_attempts: int) -> Callable:
    pass


class MageGuild:

    @staticmethod
    def validate_mage_name(name: str) -> bool:
        pass

    def cast_spell(self, spell_name: str, power: int) -> str:
        pass

if __name__ == "__main__":
    print("Casting spell timer...")

    @spell_timer
    def fireball() -> str:
        time.sleep(0.101)
        return "Fireball cast!"

    print(F"Result: {fireball()}")

    