#! /usr/bin/python3

import math


def distance_between_points(
        t1: tuple[float, float, float],
        t2: tuple[float, float, float]) -> float:
    return math.sqrt((t1[0]-t2[0])**2 + (t1[1]-t2[1])**2 + (t1[2]-t2[2])**2)


def get_player_pos() -> tuple[float, float, float]:
    while (True):
        user_input = input("Enter new coordinates as floats "
                           "in format 'x,y,z': ")
        try:
            splitted_input = user_input.split(',')

            if len(splitted_input) != 3:
                raise SyntaxError("Invalid syntax")

            coordinates = ["", "", ""]
            for i, value in enumerate(splitted_input):
                coordinates[i] = value.strip()

            x = float(coordinates[0])
            y = float(coordinates[1])
            z = float(coordinates[2])

            return (x, y, z)
        except ValueError as e:
            print(f"Error on parameter {e}")
        except SyntaxError as e:
            print(e)


if __name__ == "__main__":
    print("=== Game Coordinate System ===\n")

    print("Get a first set of coordinates")
    t1 = get_player_pos()
    print(f"Got a first tuple: {t1}")
    print(f"It includes: X={t1[0]}, Y={t1[1]}, Z={t1[2]}")
    print("Distance to center: "
          f"{round(distance_between_points(t1, (0.0, 0.0, 0.0)), 4)}")

    print("\nGot a second set of coordinates")
    t2 = get_player_pos()
    print("Distance between the 2 sets of coordinates: "
          f"{round(distance_between_points(t1, t2), 4)}")
