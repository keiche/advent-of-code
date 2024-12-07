#!/usr/local/env python3
"""
https://adventofcode.com/2024/day/7
keiche
"""

from itertools import product


class Calibration:
    def __init__(self, line: str):
        self.test = int(line.split(":")[0])
        self.operators = list(map(int, line.split(": ")[1].split(" ")))

    def _operator_permutations(self, num_operators: int = 2) -> list[str]:
        """Create permutations of operators (0, 1, 2) represent (+, *, ||)"""
        return list(product(list(range(num_operators)), repeat=len(self.operators)))

    def test_permutations(self, num_operators: int = 2) -> int:
        for p in self._operator_permutations(num_operators):
            first_num = self.operators[0]
            total = first_num
            for num, op in zip(self.operators[1:], list(p)):
                # Operator is 0 (+)
                if op == 0:
                    total += num
                # Operator is 1 (*)
                elif op == 1:
                    total *= num
                # Operator is 2 (||)
                elif op == 2:
                    total = int(str(total) + str(num))
            if self.test == total:
                return self.test
        return 0


def main():
    part1_total = 0
    part2_total = 0
    with open("input.txt", "r") as f:
        for line in f:
            cal = Calibration(line.strip())
            # Part 1
            if result := cal.test_permutations():
                part1_total += result
            if result2 := cal.test_permutations(3):
                part2_total += result2

    print(f"Part 1: {part1_total}")
    print(f"Part 2: {part2_total}")


if __name__ == "__main__":
    main()
