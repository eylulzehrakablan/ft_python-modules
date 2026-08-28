from collections.abc import Callable
from typing import Any
import functools
import operator
from functools import lru_cache

# spell_powers = [29, 25, 26, 18, 34, 13]
# operations = ['add', 'multiply', 'max', 'min']
# fibonacci_tests = [9, 12, 11]

# @lru_cache()
# def square(n):
#     print("Calculating...")
#     return n * n

# print(square(5))
# print(square(5))

# # first call to square(5) executes the function and caches the result
# # second call to square(5) uses the cached result. Therefore "Calculating..." is printed for once.

# print(square(6))
# print(square(5))
# print(square(6))
# print(square(3))


# functools.reduce(function, iterable, initalizer)

def spell_reducer(spells: list[int], operation: str) -> int:
    operations = {
        "add": operator.add,
        "multiply": operator.mul,
        "max": max,
        "min": min
    }
    return functools.reduce(operations[operation], spells)


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    pass


def memoized_fibonacci(n: int) -> int:
    pass


def spell_dispatcher() -> Callable[[Any], str]:
    pass


if __name__ == "__main__":
    print("\nTesting spell reducer...")
    # spell_powers = [29, 25, 26, 18, 34, 13]
    spell_powers = [10, 20, 30, 40]
    print(f"Sum: {spell_reducer(spell_powers, 'add')}")
    print(f"Product: {spell_reducer(spell_powers, 'multiply')}")
    print(f"Max: {spell_reducer(spell_powers, 'max')}")
    print(f"Min: {spell_reducer(spell_powers, 'min')}")



# Testing spell reducer...
# Sum: 100
# Product: 240000
# Max: 40

# Testing memoized fibonacci...
# Fib(0): 0
# Fib(1): 1
# Fib(10): 55
# Fib(15): 610

# Testing spell dispatcher...
# Damage spell: 42 damage
# Enchantment: fireball
# Multi-cast: 3 spells
# Unknown spell type

# a = [2, 4, 7, 10]
# res = functools.reduce(lambda x, y: x + y, a)
# print(res)

# print(operator.add(21, 21))
# print(operator.mul(3, 14))

# abc = ['a', 'b', 'c']

# get_third = operator.itemgetter(2)
# print(get_third(abc))
# get_second = operator.itemgetter(1)
# print(get_second(abc))

