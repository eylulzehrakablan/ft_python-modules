def ft_count_harvest_iterative():
    harvest_day = int(input("Days until harvest: ")) + 1
    for i in range(1, harvest_day):
        print(f"Day {i}")
    print("Harvest time!")