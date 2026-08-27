"""
sorted(iterable, key, reverse) -> list:
    creates a completely new sorted list.
"""
# a = ("b", "g", "a", "d", "f", "c", "h", "e")
# x = sorted(a)
# print(x)

"""
filter(function, iterable) -> Filter object:
    evaluates each item through the function, only keeps items where the function evaluates to True
"""
# powers = [5, 12, 17, 18, 24, 32]
# def filter_f(x):
#     if x < 15:
#         return False
#     return True
# most_powerful_mages = filter(filter_f, powers)
# for mage in most_powerful_mages:
#     print(mage)

"""
map(function, iterable) -> Map object:
    applies the provided function (is going to be a lambda in this example) to every single item in the iterable
"""
# def map_f(a):
#     return len(a)
# x = map(map_f, ('apple', 'banana', 'cherry'))
# print(x)
# print(list(x))

"""
max(iterable (required), *iterables (opt), key=None (opt), default=obj (opt))
max() has two forms:
    max() function with objects
    max() function with iterable

iterable (Required): The sequence or collection containing the elements you want to evaluate.
*iterables (Optional): Additional iterables to compare against the first one.
key (Optional): A single-argument function used to customize the comparison logic (e.g.,key=len to evaluate by item length).
default (Optional): The fallback value returned if the provided iterable is completely empty. If omitted and the iterable is empty, a ValueError is thrown.    
"""
# var1 = "hello"
# var2 = "world!"
# var3 = "42"
# var_list = []
# var_list.append(var1)
# var_list.append(var2)
# var_list.append(var3)
# print(var_list)

# max_val = max(var_list, key=len)
# print(max_val)
# max_val = max(var1, var2, var3, key=len)
# print(max_val)
# max_val = max(var1, var3, key=len)
# print(max_val)


def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(artifacts, key=lambda artifact: artifact['power'], reverse=True)


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda mage: mage['power'] >= min_power, mages))


# without lambda:
# def get_power(artifact):
#     return artifact['power']

# def artfct_sorter(artifacts: list[dict]) -> list[dict]:
#     return sorted(artifacts, key=get_power, reverse=True)


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda spell: f"* {spell} *", spells))


def mage_stats(mages: list[dict]) -> dict:

    if not mages:
        return {'max_power': 0, 'min_power': 0, 'avg_power': 0.0}

    max_power = max(mages, key=lambda mage: mage['power'])['power']
    min_power = min(mages, key=lambda mage: mage['power'])['power']
    total_power = sum(map(lambda mage: mage['power'], mages))
    avg_power = round(total_power / len(mages), 2)

    return {
        'max_power': max_power,
        'min_power': min_power,
        'avg_power': avg_power
    }


# {’name’: str, ’power’: int, ’type’: str}
if __name__ == "__main__":
    # artifacts = [
    #     {'name': 'Crystal Orb', 'power': 85, 'type': 'orb'}
    #     {'name': 'Fire Staff', 'power': 92, 'type': 'staff'}
    #     {'name': 'Which orb', 'power': 3, 'type': 'orb'}
    # ]

    artifacts = [
        {'name': 'Earth Shield', 'power': 103, 'type': 'accessory'},
        {'name': 'Water Chalice', 'power': 108, 'type': 'weapon'},
        {'name': 'Water Chalice', 'power': 114, 'type': 'weapon'},
        {'name': 'Crystal Orb', 'power': 100, 'type': 'weapon'}
    ]

    mages = [
        {'name': 'Kai', 'power': 80, 'element': 'earth'},
        {'name': 'Zara', 'power': 95, 'element': 'lightning'},
        {'name': 'Storm', 'power': 50, 'element': 'shadow'},
        {'name': 'Phoenix', 'power': 73, 'element': 'water'}, 
        {'name': 'Riley', 'power': 85, 'element': 'lightning'}, 
        {'name': 'Nova', 'power': 81, 'element': 'water'}
    ]

    spells = ['tsunami', 'lightning', 'darkness', 'freeze']


    # print("=" * 12 + " without lambda " + "=" * 12)
    # sorted_artfcts = artfct_sorter(artifacts)
    # if len(sorted_artfcts) >= 2:
    #     if len(sorted_artfcts) >= 2:
    #         print(f"{sorted_artfcts[0]['name']} ({sorted_artfcts[0]['power']} power) "
    #               f"comes before {sorted_artfcts[1]['name']} ({sorted_artfcts[1]['power']} power)")
    # print("=" * 40)

    print("\nTesting artifact sorter...")
    sorted_artifacts = artifact_sorter(artifacts)
    if len(sorted_artifacts) >= 2:
        if len(sorted_artifacts) >= 2:
            print(f"{sorted_artifacts[0]['name']} ({sorted_artifacts[0]['power']} power) "
                  f"comes before {sorted_artifacts[1]['name']} ({sorted_artifacts[1]['power']} power)")

    print("\nTesting power filter (min 78)...")
    filtered_mages = power_filter(mages, 78)
    for mage in filtered_mages:
        print(f"{mage['name']} - Power: {mage['power']}")

    print("\nTesting spell transformer...")
    transformed_spells = spell_transformer(spells)
    print(" ".join(transformed_spells))

    print("\nTesting mage stats...")
    stats = mage_stats(mages)
    print(f"Stats: {stats}")

# lambda arguments : expression

# x = lambda a : a + 10
# print(x(5))

# x = lambda a, b, c : a + b * c
# print(x(5, 3, 2))

# def f(n):
#     return lambda a, b : a + b * n
# # doubler = f(3) 
# # anonymous lambda fonksyiyonnunu bir degiskende tutuyoruz 
# (first-class citizens which can be stored in a variable)

# print(doubler(11, 2))
