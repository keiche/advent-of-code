#!/usr/bin/env python3
"""https://adventofcode.com/2022/day/15"""

import re


def dist(a: tuple, b: tuple) -> int:
    """
    Manhattan distance
    :param a: coord a
    :param b: coord b
    :return: distance
    """
    return sum([abs(v1- v2) for v1, v2 in zip(a, b)])

def main() -> None:
    grid = {}
    sensors = []
    beacons = []
    xs = []
    ys = []

    re_xy = re.compile(r"x=([^,]+), y=([^,]+)")
    with open("15.txt", "r") as f:
        for line in f.readlines():
            if m := re_xy.search(line.rstrip().split(":")[0]):
                x = int(m.group(1))
                y = int(m.group(2))
                xs.append(x)
                ys.append(y)
                sensors.append((x, y))
            if m := re_xy.search(line.rstrip().split(":")[1]):
                x = int(m.group(1))
                y = int(m.group(2))
                xs.append(x)
                ys.append(y)
                beacons.append((x, y))

    distress_max = 4000000
    line_num = 2000000

    # Part 1
    part_1_set = set()
    for i, (sensor, beacon) in enumerate(zip(sensors, beacons)):
        beacon_dist = dist(sensor, beacon)
        for x in range(min(xs) - beacon_dist, max(xs) + beacon_dist + 1):
            check_coord = (x, line_num)
            if dist(sensor, check_coord) <= beacon_dist and check_coord not in beacons and check_coord not in sensors:
                part_1_set.add(check_coord)
        print(f"Complete input {i}. Current sum: {len(part_1_set)}")
    part_1 = len(part_1_set)

    # Part 2
    # print("grid2 started")
    # grid2 = set()
    # for y in range(distress_max):
    #     for x in range(distress_max):
    #         grid2.add((x, y))
    # print("grid2 built")

    # for i, (sensor, beacon) in enumerate(zip(sensors, beacons)):
    #     print(f"Starting sensor #{i} out of 23")
    #     beacon_dist = dist(sensor, beacon)
    #     for y in range(distress_max):
    #         for x in range(distress_max):
    #             check_coord = (x, y)
    #             if check_coord in grid2 and dist(sensor, check_coord) <= beacon_dist:
    #                 grid2.remove(check_coord)
    #     print(f"Complete sensor #{i} out of 23")
    # print(grid2)
    # part_2 = grid2.pop()

    print(f"Part 1: {part_1}")
    # print(f"Part 2: {part_2[0] * 4000000 + part_2[1]}")


if __name__ == "__main__":
    main()
