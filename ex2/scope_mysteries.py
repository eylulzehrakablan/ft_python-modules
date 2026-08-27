from collections.abc import Callable

# def mage_counter():
#     count = 0
#     def counter():
#         nonlocal count
#         count += 1
#         return count
#     return counter

# my_func = mage_counter()
# print(my_func.__closure__[0].cell_contents)


def mage_counter() -> Callable:
    count = 0
    def counter() -> int:
        nonlocal count
        count += 1
        return count
    return counter


def spell_accumulator(initial_power: int) -> Callable:
    total_power = initial_power
    def accumulate(amount: int) -> int:
        nonlocal total_power
        total_power += amount
        return total_power
    return accumulate


def enchantment_factory(enchantment_type: str) -> Callable:
    pass


def memory_vault() -> dict[str, Callable]:
    pass


if __name__ == "__main__":
    print("\nTesting mage counter...")
    counter_a = mage_counter()
    counter_b = mage_counter()

    print(f"Counter_a call 1: {counter_a()}")
    print(f"Counter_a call 2: {counter_a()}")
    print(f"Counter_a call 1: {counter_b()}")

    # print(counter_a.__closure__)
    # print(counter_a.__closure__[0].cell_contents)
    # print(counter_b.__closure__)
    # print(counter_b.__closure__[0].cell_contents)

    print("\nTesting spell accumulator...")
    accumulator = spell_accumulator(100)
    print(f"Base 100, add 20: {accumulator(20)}")
    print(f"Base 100, add 30: {accumulator(30)}")
    # accumulator2 = spell_accumulator(0)
    # number = accumulator2(20)
    # print(number)
    # accumulator2(2)
    # print(number)
    # number = accumulator2(3)
    # print(number)


# def func1():
#     name = "Zehra"
#     def func2():
#         nonlocal name
#         name = "Eylul"
#     func2()
#     return name

# print(func1())