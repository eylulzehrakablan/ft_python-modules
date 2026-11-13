def ft_count_harvest_recursive(current: int = 1, harvest_day: int = 0) -> None:
    if (harvest_day == 0):
        harvest_day = int(input("Days until harvest: ")) + 1
    print(f"Day {current}")
    if (current == harvest_day - 1):
        print("Harvest time!")
    else:
        ft_count_harvest_recursive(current + 1, harvest_day)
