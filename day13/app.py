#!/usr/bin/env python3

import json
from copy import deepcopy
from itertools import zip_longest
from typing import Union


def compare_values(left: list, right: list) -> Union[bool, None]:
    """
    Compare inputs based on the special criteria
    :param left: left (first) input
    :param right: right (second) input
    :return: Whether this is in order (bool) or undetermined (None)
    """
    result = None

    for v1, v2 in zip_longest(left, right):
        v1_int = isinstance(v1, int)
        v2_int = isinstance(v2, int)

        # The left list is out of elements first - correct order
        if v1 is None:
            return True
        # The right list is out of elements first - wrong order
        if v2 is None:
            return False

        # Both ints
        if v1_int and v2_int:
            # Left integer is lower - correct order
            if v1 < v2:
                return True
            # Right integer is lower - wrong order
            if v1 > v2:
                return False
        # Left int, right list
        elif v1_int and not v2_int:
            result = compare_values([v1], v2)
        # Left list, right int
        elif not v1_int and v2_int:
            result = compare_values(v1, [v2])
        # Both lists
        elif not v1_int and not v2_int:
            result = compare_values(v1, v2)

        # Results found - don't continue looping
        if result is not None:
            return result

    # No determination made - continue
    return None


def main() -> None:
    data = []
    with open("13.txt", "r") as f:
        for line in f.readlines():
            if line.startswith("["):
                data.append(json.loads(line.rstrip()))

    # Divide into separate arrays
    left = data[0::2]
    right = data[1::2]

    # Part 1
    right_order = []
    for i in range(len(left)):
        if compare_values(left[i], right[i]):
            right_order.append(i + 1)
    part_1 = sum(right_order)

    # Part 2
    dividers = [[[2]], [[6]]]
    data.extend(dividers)
    sorted_packets = [data[0]]
    # Insertion sort
    for p in data[1:]:
        for idx, sp in enumerate(deepcopy(sorted_packets)):
            if compare_values(p, sp):
                # Empty inputs (ex. [[]]) get missed - add them to the end
                if idx == len(sorted_packets) - 1:
                    sorted_packets.append(p)
                continue
            sorted_packets.insert(idx, p)
            break

    # Reverse the ordering
    sorted_packets = list(reversed(sorted_packets))

    # Get the location of the divider packets then multiply for the decoder key
    div_idx = [sorted_packets.index(d) + 1 for d in dividers]
    part_2 = div_idx[0] * div_idx[1]

    print(f"Part 1: {part_1}")
    print(f"Part 2: {part_2}")


if __name__ == "__main__":
    main()
