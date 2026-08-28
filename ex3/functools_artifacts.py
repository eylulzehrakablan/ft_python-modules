from collections.abc import Callable
from typing import Any
import functools
import operator
from functools import lru_cache

# spell_powers = [29, 25, 26, 18, 34, 13]
# operations = ['add', 'multiply', 'max', 'min']
# fibonacci_tests = [9, 12, 11]

@lru_cache()
def square(n):
    print("Calculating...")
    return n * n
print(square.cache_info())
print(square(5))
print(square(5))
print(square(6))
print(square(7))
print(square.cache_info())


# # first call to square(5) executes the function and caches the result
# # second call to square(5) uses the cached result. Therefore "Calculating..." is printed for once.

# print(square(6))
# print(square(5))
# print(square(6))
# print(square(3))


# functools.reduce(function, iterable, initalizer)

def spell_reducer(spells: list[int], operation: str) -> int:
    if not spells:
        return 0
    
    # try:
    operations = {
        "add": operator.add,
        "multiply": operator.mul,
        "max": max,
        "min": min
    }

    if operation not in operations:
        raise KeyError(f"Unknown operation: {operation}")

    return functools.reduce(operations[operation], spells)


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    return {
        "sweeping_edge": functools.partial(base_enchantment, power=50, element="sweeping_edge"),
        "flame": functools.partial(base_enchantment, power=50, element="fire"),
        "frost": functools.partial(base_enchantment, power=50, element="ice")
    }


@functools.lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    if n < 0:
        raise TypeError("n cannot be negative")
    if n == 0:
        return 0
    if n == 1:
        return 1
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)
    

def spell_dispatcher() -> Callable[[Any], str]:
       
    @functools.singledispatch
    def dispatcher(spell: Any) -> str:
        return "Unknown spell type"
        
    @dispatcher.register(int)
    def _(spell: int) -> str:
        return f"Damage spell: {spell} damage"
        
    @dispatcher.register(str)
    def _(spell: str) -> str:
        return f"Enchantment: {spell}"
        
    @dispatcher.register(list)
    def _(spell: list) -> str:
        return f"Multi-cast: {len(spell)} spells"
        
    return dispatcher


if __name__ == "__main__":
    print("\nTesting spell reducer...")
    # spell_powers = [29, 25, 26, 18, 34, 13]
    spell_powers = [10, 20, 30, 40]
    empty_spell_list = []
    print(f"Sum: {spell_reducer(spell_powers, 'add')}")
    print(f"Product: {spell_reducer(spell_powers, 'multiply')}")
    print(f"Max: {spell_reducer(spell_powers, 'max')}")
    print(f"Min: {spell_reducer(spell_powers, 'min')}")
    # print(f"Min: {spell_reducer(spell_powers, 'mn')}") # KeyError
    print(f"Min: {spell_reducer(empty_spell_list, 'min')}") # return 0

    print("\nTesting partial enchanter...")
    def enchanter(power: int, element: str, target: str) -> str:
        return f"item {target} enchanted with {element} of {power} power."
    enchanters = partial_enchanter(enchanter)
    print(enchanters["flame"](target="Sword"))
    print(enchanters["frost"](target="Boots"))
    print(enchanters["sweeping_edge"](target="Sword"))

    print("\nTesting memoized fibonacci...")
    print(f"Fib(0): {memoized_fibonacci(0)}")
    print(f"Fib(1): {memoized_fibonacci(1)}")
    print(f"Fib(10): {memoized_fibonacci(10)}")
    print(f"Fib(15): {memoized_fibonacci(15)}")

    print("\nTesting spell dispatcher...")
    dispatch = spell_dispatcher()
    print(dispatch(42))
    print(dispatch("fireball"))
    print(dispatch([1, 2, 3]))
    print(dispatch(3.14))



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

