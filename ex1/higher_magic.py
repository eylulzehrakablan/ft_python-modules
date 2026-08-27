# test_values = [18, 20, 5]
# test_targets = ['Dragon', 'Goblin', 'Wizard', 'Knight']

from collections.abc import Callable

# x = 42
# def f():
#     x = 5
# res = callable(f)
# print(res)
# print(callable(x))

# class Cadet:
#     def __init__(self, name):
#         self.name = name
#     def __call__(self):
#         print(f"hello, this is {self.name}")
# print(callable(Cadet))
# cadetObject = Cadet("Zehra")
# cadetObject()


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    def combined_spell(target: str, power: int) -> tuple[str, str]:
        return (spell1(target, power), spell2(target, power))
    return combined_spell


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    def amplified_spell(target: str, power: int) -> str:
        return base_spell(target, power * multiplier)
    return amplified_spell


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    def conditional_spell(target: str, power: int) -> str:
        if condition(target, power):
            return spell(target, power)
        return "Spell fizzled"
    return conditional_spell



def spell_sequence(spells: list[Callable]) -> Callable:
    pass


if __name__ == "__main__":

    def fireball(target: str, power: int) -> str:
        return f"Fireball hits {target} for {power} damage!"

    def heal(target: str, power: int) -> str:
        return f"Heal restores {target} for {power} HP."

    def is_powerful(target: str, power: str) -> bool:
        return power >= 50

    print("\nTesting spell combiner...")
    combined = spell_combiner(fireball, heal)
    res1, res2 = combined("Dragon", 10)
    print(f"Combined spell result: {res1}, {res2}")

    print("\nTesting power amplifier...")
    fireball_rain = power_amplifier(fireball, 3)
    base_power = 10
    print(f"Original: {base_power}, Amplified: {base_power * 3}")
    print(f"Result: {fireball_rain('Dragon', base_power)}")

    print("\nTesting conditional caster...")
    conditional_attack = conditional_caster(is_powerful, fireball)
    print(" Conditional Attack Attempt 1 (power 42):")
    print(conditional_attack('ekablan', 42))
    print(" Conditional Attack Attempt 2 (power 142):")
    print(conditional_attack('ekablan', 142))
