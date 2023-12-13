#!/usr/bin/env python3
"""https://adventofcode.com/2022/day/11"""

from copy import deepcopy

REDUCE_WORRY = 1


class Monkey:
    def __init__(self):
        self.items = []
        self.op = ""
        self.op_value = 0
        self.test = 0
        self.test_true = 0
        self.test_false = 0
        self.total_inspect = 0

    def inspect(self, item, part_deux: bool = False) -> tuple:
        """
        Inspect the item and determine which monkey to throw to next
        :param item: item's priority
        :param part_deux: Whether to reduce worry by 1/3 (Part 1)
        :return: (item's new worry, monkey to throw to)
        """
        self.total_inspect += 1
        value = item if self.op_value == "old" else int(self.op_value)

        # Perform operation
        if self.op == "+":
            item = item + value
        elif self.op == "*":
            item = item * value

        if not part_deux:
            item /= 3
            item = int(item)

        # Reduce the worry so the code runs in a reasonable amount of time
        item = item % REDUCE_WORRY

        # Test
        test = item % self.test == 0
        return item, self.test_true if test else self.test_false


def run_round(monkeys: list, part_deux: bool = False) -> None:
    """
    Manage a single round of the Monkeys inspecting & throwing items
    :param monkeys: list of Monkey instances
    :param part_deux: Whether to reduce worry by 1/3 (Part 1)
    """
    for monkey in monkeys:
        # No items = no turn
        if not len(monkey.items):
            continue
        for _ in range(len(monkey.items)):
            item = monkey.items.pop(0)
            item, next_monkey = monkey.inspect(item, part_deux)
            monkeys[next_monkey].items.append(item)


def main() -> None:
    # Process the input and store each of them in a Monkey class
    monkeys = []
    with open("11.txt", "r") as f:
        monkey = Monkey()
        for line in f.readlines():
            line = line.rstrip()
            if line.startswith("Monkey"):
                monkey = Monkey()
            elif "Starting" in line:
                monkey.items = [int(x) for x in line.split(":")[1].split(", ")]
            elif "Operation" in line:
                monkey.op, monkey.op_value = line.split(" ")[-2:]
            elif "Test" in line:
                monkey.test = int(line.split(" ")[-1])
            elif "true" in line:
                monkey.test_true = int(line.split(" ")[-1])
            elif "false" in line:
                monkey.test_false = int(line.split(" ")[-1])
            else:
                monkeys.append(monkey)
        # Load the final monkey
        monkeys.append(monkey)
    # Make a copy for Part 2
    monkeys_pt2 = deepcopy(monkeys)

    # Get the product of all the tests, so we can reduce big number worries
    global REDUCE_WORRY
    for m in monkeys:
        REDUCE_WORRY *= m.test

    # Part 1
    for x in range(20):
        run_round(monkeys)
    part_1_sums = sorted([m.total_inspect for m in monkeys])
    part_1 = part_1_sums[-1] * part_1_sums[-2]

    # Part 2
    for x in range(10000):
        run_round(monkeys_pt2, True)
    part_2_sums = sorted([m.total_inspect for m in monkeys_pt2])
    part_2 = part_2_sums[-1] * part_2_sums[-2]

    print(f"Part 1: {part_1}")
    print(f"Part 2: {part_2}")


if __name__ == "__main__":
    main()