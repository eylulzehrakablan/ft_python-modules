def ft_count_harvest_recursive(current_day = 1, harvest_day = 0):
    if (harvest_day == 0):
        harvest_day = int(input("Days until harvest: ")) + 1
    print(f"Day {current_day}")
    if (current_day == harvest_day - 1):
        print("Harvest time!")
    else:
        ft_count_harvest_recursive(current_day + 1, harvest_day)