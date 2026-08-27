# """

# sorted(iterable, key, reverse) -> list: creates a completely new sorted list.
# filter(function, iterable) -> Filter object: evaluates each item through the function, only keeps items where the function evaluates to True
# map(function, iterable) -> Map object: applies the provided function (is going to be a lambda in this example) to every single item in the iterable


# """

def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    print("Testing artifact sorter...")
    return sorted(artifacts, key=lambda artifact: artifact['power'], reverse=True)



def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    pass


def spell_transformer(spells: list[str]) -> list[str]:
    pass


def mage_stats(mages: list[dict]) -> dict:
    pass


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

    sorted_artifacts = artifact_sorter(artifacts)
    if len(sorted_artifacts) >= 2:
        if len(sorted_artifacts) >= 2:
            print(f"{sorted_artifacts[0]['name']} ({sorted_artifacts[0]['power']} power) "
                  f"comes before {sorted_artifacts[1]['name']} ({sorted_artifacts[1]['power']} power)")


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
