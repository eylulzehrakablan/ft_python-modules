from typing import Any


def artifact_sorter(artifacts: list[dict[str, Any]]) -> list[dict[str, Any]]:
    return sorted(
        artifacts, key=lambda artifact: artifact['power'], reverse=True)


def power_filter(
    mages: list[dict[str, Any]], min_power: int
        ) -> list[dict[str, Any]]:
    return list(filter(lambda mage: mage['power'] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda spell: f"* {spell} *", spells))


def mage_stats(mages: list[dict[str, Any]]) -> dict[str, Any]:

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


if __name__ == "__main__":

    artifacts = [
        {'name': 'Earth Shield', 'power': 103, 'type': 'accessory'},
        {'name': 'Water Chalice', 'power': 108, 'type': 'weapon'},
        {'name': 'Fireball', 'power': 114, 'type': 'weapon'},
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

    print("\nTesting artifact sorter...")
    sorted_artifacts = artifact_sorter(artifacts)
    if len(sorted_artifacts) >= 2:
        print(f"{sorted_artifacts[0]['name']} ({sorted_artifacts[0]['power']}"
              f" power) comes before {sorted_artifacts[1]['name']}"
              f"({sorted_artifacts[1]['power']} power)")

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
