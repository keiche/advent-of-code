#!/usr/local/env python3
"""
https://adventofcode.com/2024/day/13
keiche
"""

from re import compile


class ClawMachine:
    def __init__(self, a: tuple[int, int], b: tuple[int, int], prize: tuple[int, int]) -> None:
        self.a = a
        self.b = b
        self.prize = prize

    def solve_equation(self) -> tuple[int, int]:
        """Original brute force"""
        max_presses = 100
        ax, ay = self.a
        bx, by = self.b
        px, py = self.prize

        # Max of 100 times the buttons can be pressed
        for i in range(max_presses):
            for j in range(max_presses):
                if (i * ax) + (j * bx) == px and (i * ay) + (j * by) == py:
                    return i, j
        return 0, 0

    def cramers_rule(self, part2: bool = False) -> tuple[int, int]:
        """https://en.wikipedia.org/wiki/Cramer%27s_rule#Applications"""
        ax, ay = self.a
        bx, by = self.b
        px, py = self.prize
        if part2:
            px += 10000000000000
            py += 10000000000000

        a_presses = ((px * by) - (bx * py)) / ((ax * by) - (bx * ay))
        b_presses = ((ax * py) - (px * ay)) / ((ax * by) - (bx * ay))

        machine_total_x = (int(a_presses) * ax) + (int(b_presses) * bx)
        machine_total_y = (int(a_presses) * ay) + (int(b_presses) * by)
        if machine_total_x == px and machine_total_y == py:
            return int(a_presses), int(b_presses)
        return 0, 0


def parse_input(filename: str) -> list[ClawMachine]:
    machines = []
    re_button = compile(r"Button (?P<button>[AB]): X\+(?P<x>\d+), Y\+(?P<y>\d+)")
    re_prize = compile(r"Prize: X=(?P<x>\d+), Y=(?P<y>\d+)")
    with open(filename, "r") as f:
        button_a = None
        button_b = None
        for line in f:
            line = line.strip()
            if m := re_button.match(line):
                if m.group("button") == "A":
                    button_a = (int(m.group("x")), int(m.group("y")))
                elif m.group("button") == "B":
                    button_b = (int(m.group("x")), int(m.group("y")))
            elif m := re_prize.match(line):
                prize = (int(m.group("x")), int(m.group("y")))
                machines.append(ClawMachine(button_a, button_b, prize))
                # Reset for next input
                button_a = None
                button_b = None

    return machines


def main():
    machines = parse_input("input.txt")

    part1_total = 0
    part2_total = 0
    for m in machines:
        a, b = m.cramers_rule()
        part1_total += (a * 3) + b
        a2, b2 = m.cramers_rule(part2=True)
        part2_total += (a2 * 3) + b2

    print(f"Part 1: {part1_total}")
    print(f"Part 2: {part2_total}")


if __name__ == "__main__":
    main()
