#! /usr/bin/python3

import sys


def ft_inventory_system() -> None:
    inventory: dict[str, int] = {}

    for arg in sys.argv[1:]:

        try:
            if ":" not in arg:
                raise ValueError(f"Error - invalid parameter '{arg}'")

            item, quantity = arg.split(":")

            if item in inventory:
                print(f"Reduntant item '{item}' - discarding")
                continue

            inventory[item] = int(quantity)
        except ValueError as e:
            print(e)
        except Exception as e:
            print(f"Quantity error for '{item}': {e}")

    item_list = list(inventory.keys())
    total_quantity = sum(inventory.values())

    print(f"Got inventory: {inventory}")
    print(f"Item list: {item_list}")
    print(f"Total quantity of the {len(item_list)} items: {total_quantity}")

    for item, quantity in inventory.items():
        percenage = round((quantity / total_quantity) * 100, 1)
        print(f"Item {item} represenets {percenage}%")

    highest_quantity = max(inventory.values())
    for item, quantity in inventory.items():
        if quantity == highest_quantity:
            print(f"Item most abundant: {item} with quantity {quantity}")
            break

    lowest_quantity = min(inventory.values())
    for item, quantity in inventory.items():
        if quantity == lowest_quantity:
            print(f"Item least abundant: {item} with quantity {quantity}")
            break

    inventory.update({"magic_item": 1})
    print(f"Updated inventory: {inventory}")


if __name__ == "__main__":
    print("=== Inventory System Analysis ===")
    ft_inventory_system()
