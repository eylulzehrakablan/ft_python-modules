from collections.abc import Callable


def mage_counter() -> Callable:
    count = 0

    def counter() -> int:
        nonlocal count
        count += 1
        return count
    return counter



def spell_accumulator(initial_power: int) -> Callable:
    pass


def enchantment_factory(enchantment_type: str) -> Callable:
    pass


def memory_vault() -> dict[str, Callable]:
    pass


if __name__ == "__main__":
    print("Testing mage counter...")
    counter_a = mage_counter()
    counter_b = mage_counter()

    print(f"Counter_a call 1: {counter_a()}")
    print(f"Counter_a call 2: {counter_a()}")
    print(f"Counter_a call 1: {counter_b()}")



# def func1():
#     name = "Zehra"
#     def func2():
#         nonlocal name
#         name = "Eylul"
#     func2()
#     return name

# print(func1())