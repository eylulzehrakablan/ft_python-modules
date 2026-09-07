from collections.abc import Callable
from functools import wraps
from typing import Any
import time


def spell_timer(func: Callable[..., Any]) -> Callable[..., Any]:
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        print(f"Casting {func.__name__}...")
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Spell completed in {end_time - start_time:.3f} seconds")
        return result
    return wrapper


def power_validator(min_power: int) -> Callable[..., Any]:
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            power_level = kwargs.get('power')
            if power_level is None and args:
                power_level = args[-1]
            if power_level is not None and power_level >= min_power:
                return func(*args, **kwargs)
            return "Insufficient power for this spell"
        return wrapper
    return decorator


def retry_spell(max_attempts: int) -> Callable[..., Any]:
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    if attempt < max_attempts:
                        print(
                            f"Spell failed, retrying... "
                            f"(attempt {attempt}/{max_attempts})"
                        )
            return f"Spell casting failed after {max_attempts} attempts"
        return wrapper
    return decorator


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        if not isinstance(name, str) or len(name) < 3:
            return False

        cleaned = name.replace(" ", "")
        return len(cleaned) > 0 and cleaned.isalpha()

    @power_validator(min_power=10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with {power} power"


if __name__ == "__main__":
    print("\nCasting spell timer...")

    @spell_timer
    def fireball() -> str:
        time.sleep(0.101)
        return "Fireball cast!"
    print(F"Result: {fireball()}")

    print("\nTesting standalone power_validator...")

    @power_validator(min_power=50)
    def ultimate_attack(target: str, power: int) -> str:
        return f"Ultimate attack hit {target} with {power} power!"
    print(ultimate_attack("Dragon", 60))
    print(ultimate_attack("Dragon", 20))
    print(ultimate_attack("Dragon", power=100))
    print(ultimate_attack("Dragon", power=10))

    print("\nTesting retrying spell...")

    @retry_spell(max_attempts=3)
    def failing_spell() -> str:
        raise ValueError("Boom!")

    @retry_spell(max_attempts=3)
    def orc_spell() -> str:
        return "Waaaaaaagh spelled !"
    print(failing_spell())
    print(orc_spell())

    print("\nTesting MageGuild...")
    guild = MageGuild()
    print(guild.validate_mage_name("Gandalf"))
    print(guild.validate_mage_name("Jo"))
    print(guild.cast_spell("Lightning", 15))
    print(guild.cast_spell("Fireball", 5))
