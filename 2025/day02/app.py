#!/usr/local/env python3
"""
https://adventofcode.com/2025/day/2
keiche
"""


def check_repeating(str_i: str) -> bool:
    # Check different lengths of repeating patterns
    for i in range(1, len(str_i) // 2 + 1):
        split_seq = [str_i[x : x + i] for x in range(0, len(str_i), i)]
        if all(split_seq[0] == x for x in split_seq):
            return True
    return False


def main():
    part1_total = 0
    part2_total = 0
    with open("input.txt", "r") as f:
        for line in f:
            line = line.strip()
            for r in line.split(","):
                start, end = r.split("-")
                for i in range(int(start), int(end) + 1):
                    str_i = str(i)
                    # Skip odd length as they can't be split into two equal parts
                    if len(str_i) % 2 == 0:
                        half_len = int(len(str_i) / 2)
                        left, right = str_i[0:half_len], str_i[half_len:]
                        if left == right:
                            part1_total += i
                    if check_repeating(str_i):
                        part2_total += i

    print(f"Part 1: {part1_total}")
    print(f"Part 2: {part2_total}")


if __name__ == "__main__":
    main()
