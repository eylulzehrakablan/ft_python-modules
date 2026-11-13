#! /usr/bin/python3

import math


def distance_between_points(
        t1: tuple[float, float, float],
        t2: tuple[float, float, float]) -> float:
    return math.sqrt((t1[0]-t2[0])**2 + (t1[1]-t2[1])**2 + (t1[2]-t2[2])**2)


def get_player_pos() -> tuple[float, float, float]:
    while True:
        user_input = input("Enter new coordinates as floats "
                           "in format 'x,y,z': ")

        splitted_input = user_input.split(',')
        try:
            _, _, _ = splitted_input
        except ValueError:
            print("Invalid syntax")
            continue

        coordinates: tuple[float, ...] = ()
        for value in splitted_input:
            clean_input = value.strip()
            try:
                coordinates = coordinates + (float(clean_input),)
            except ValueError as e:
                print(f"Error on parameter '{clean_input}': {e}")
                break
        else:
            return (coordinates[0], coordinates[1], coordinates[2])


def ft_coordinate_system() -> None:
    print("Get a first set of coordinates")
    t1 = get_player_pos()
    print(f"Got a first tuple: {t1}")
    print(f"It includes: X={t1[0]}, Y={t1[1]}, Z={t1[2]}")
    print("Distance to center: "
          f"{round(distance_between_points(t1, (0.0, 0.0, 0.0)), 4)}")

    print("\nGet a second set of coordinates")
    t2 = get_player_pos()
    print("Distance between the 2 sets of coordinates: "
          f"{round(distance_between_points(t1, t2), 4)}")


if __name__ == "__main__":
    print("=== Game Coordinate System ===\n")
    ft_coordinate_system()
