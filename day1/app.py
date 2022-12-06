#!/usr/bin/env python3
"""https://adventofcode.com/2022/day/3"""


class Elf:
    def __init__(self) -> None:
        self.food = []

    def add_food(self, calories: int) -> None:
        self.food.append(calories)

    @property
    def total_calories(self) -> int:
        return sum(self.food)


def main():
    elves = []
    elf = Elf()
    with open("1.txt", "r") as f:
        for line in f.readlines():
            if line != "\n":
                elf.add_food(int(line.rstrip()))
            else:
                elves.append(elf)
                elf = Elf()
    # Add final elf
    elves.append(elf)

    # Sums of calories sorted largest first
    sums = sorted([e.total_calories for e in elves], reverse=True)

    print(f"Part 1: {sums[0]}")
    print(f"Part 2: {sum(sums[0:3])}")


if __name__ == "__main__":
    main()
