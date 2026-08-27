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
    pass


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    pass


def spell_sequence(spells: list[Callable]) -> Callable:
    pass


if __name__ == "__main__":

    def fireball(target: str, power: int) -> str:
        return f"Fireball hits {target} for {power} damage!"

    def heal(target: str, power: int) -> str:
        return f"Heal restores {target} for {power} HP."


    print("Testing spell combiner...")
    combined = spell_combiner(fireball, heal)
    res1, res2 = combined("Dragon", 10)
    print(f"Combined spell result: {res1}, {res2}")
