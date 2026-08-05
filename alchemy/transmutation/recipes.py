from ..potions import strenght_potion
from ..elements import create_air
from elements import create_fire


def lead_to_gold() -> str:
    return (f"Recipe transmuting Lead to Gold: brew '{create_air()}' "
            f"and {strenght_potion()} mixed with '{create_fire()}'")
