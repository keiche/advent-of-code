"""
https://adventofcode.com/2025/day/6
keiche
"""

import numpy as np
from re import findall


def part1(file_path):
    all_rows = []

    with open(file_path, "r") as f:
        for line in f:
            line = line.strip()
            if m := findall(r"(\d+)", line):
                all_rows.append([int(x) for x in m])
            elif m := findall(r"[+\-*/]", line):
                all_rows.append([x for x in m])

    # Iterate and combine numbers and operators
    part1_total = 0
    for z in zip(*all_rows):
        z = list(z)
        operator = z.pop(-1)
        # Perform calculation on the row
        row_total = None
        for num in z:
            if operator == "+":
                if row_total is None:
                    row_total = 0
                row_total += num
            elif operator == "*":
                if row_total is None:
                    row_total = 1
                row_total *= num
        # Add the row totals
        part1_total += row_total
    return part1_total


def part2(file_path):
    all_rows = []
    part2_total = 0

    with open(file_path, "r") as f:
        for line in f:
            # Ensure the line is the same length
            if line[-1] == "\n":
                line = line[:-1]
            all_rows.append(list(line))

    # Reverse the rows then rotate the matrix for cephalopod math
    # Output will look like this:
    # ['1' ' ' ' ' '*']
    # ['2' '4' ' ' ' ']
    # ['3' '5' '6' ' ']
    # [' ' ' ' ' ' ' ']
    matrix = []
    for r in all_rows:
        matrix.append(list(reversed(r)))
    matrix = np.array(matrix)
    rotated_matrix = np.rot90(matrix, k=1)

    # Perform calculations
    operator = None
    number_queue = []
    rotated_matrix_list = rotated_matrix.tolist()
    for idx, r in enumerate(rotated_matrix_list):
        last_element = r.pop(-1)
        if last_element != " ":
            operator = last_element

        # Add the numbers to the queue
        clean_r = "".join(r).strip()
        if clean_r.isdigit():
            number_queue.append(int(clean_r))
        # Perform calculation on the empty rows or if it's the last row
        if not clean_r.isdigit() or idx == len(rotated_matrix_list) - 1:
            row_total = None
            for num in number_queue:
                if operator == "+":
                    if row_total is None:
                        row_total = 0
                    row_total += int(num)
                elif operator == "*":
                    if row_total is None:
                        row_total = 1
                    row_total *= int(num)
            # Add the row total to the total
            part2_total += row_total

            # Reset the queue and operator
            number_queue = []
            operator = None
    return part2_total


def main():
    file_path = "input.txt"
    print(f"Part 1: {part1(file_path)}")
    print(f"Part 2: {part2(file_path)}")


if __name__ == "__main__":
    main()
