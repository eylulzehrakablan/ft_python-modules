#! /usr/bin/python3

import sys


def ft_inventory_system() -> None:
    inventory = {}

    for arg in sys.argv[1:]:

        if ":" not in arg:
            print(f"Error - invalid parameter '{arg}'")
            continue

        item, raw_quantity = arg.split(":")

        try:
            quantity = int(raw_quantity)

            if item in inventory:
                print(f"Redundant item '{item}' - discarding")
                continue

            inventory[item] = quantity
        except ValueError as e:
            print(f"Quantity error for '{item}': {e}")

    print(f"Got inventory: {inventory}")
    key_list = list(inventory.keys())
    print(f"Item list: {key_list}")
    total_quantity = sum(inventory.values())
    print(f"Total quantity of the {len(key_list)} items: {total_quantity}")

    if len(key_list) > 0:
        for item in inventory.keys():
            quantity = inventory[item]
            percentage = round((quantity / total_quantity) * 100, 1)
            print(f"Item {item} represents {percentage}%")

        most_abundant_item = key_list[0]
        least_abundant_item = key_list[0]
        for item in key_list:
            if inventory[item] > inventory[most_abundant_item]:
                most_abundant_item = item
            if inventory[item] < inventory[least_abundant_item]:
                least_abundant_item = item

        print(f"Item most abundant: {most_abundant_item} "
              f"with quantity {inventory[most_abundant_item]}")
        print(f"Item least abundant: {least_abundant_item} "
              f"with quantity {inventory[least_abundant_item]}")

    inventory.update({"magic_item": 1})
    print(f"Updated inventory: {inventory}")


if __name__ == "__main__":
    print("=== Inventory System Analysis ===")
    ft_inventory_system()
