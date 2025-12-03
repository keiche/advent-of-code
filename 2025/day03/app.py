#!/usr/local/env python3
"""
https://adventofcode.com/2025/day/3
keiche
"""


def find_max_combo(line: str, combo_length: int) -> int:
    # Find largest number with combo length still remaining
    combo = []
    max_digit_index = 0
    abs_digit_index = 0
    for i in range(combo_length, 0, -1):
        # Get possible digits to use and then find the largest
        end_pos = len(line) - i + 1
        viable_digits = line[abs_digit_index:end_pos]
        max_digit = max(map(int, viable_digits))

        # Add the largest digit to the combo
        combo.append(str(max_digit))

        # Prepare for next iteration
        max_digit_index = viable_digits.index(str(max_digit))
        abs_digit_index += max_digit_index + 1
    return int("".join(combo))


def main():
    part1_total = 0
    part2_total = 0
    with open("input.txt", "r") as f:
        for line in f:
            line = line.strip()
            combos1 = find_max_combo(line, 2)
            part1_total += combos1
            combos2 = find_max_combo(line, 12)
            part2_total += combos2

    print(f"Part 1: {part1_total}")
    print(f"Part 2: {part2_total}")


if __name__ == "__main__":
    main()
