"""
https://adventofcode.com/2025/day/10
keiche
"""

from re import findall, match, search
from collections import deque


class Machine:
    def __init__(self, program: list[int]):
        # Reading input
        self.program = program
        self.end_lights = match(r"\[(.*?)\]", self.program).group(1)
        self.start_lights = "." * len(self.end_lights)
        self.buttons = [list(map(int, x.split(","))) for x in findall(r"\((.*?)\)", self.program)]
        self.joltage_requirements = tuple(map(int, search(r"\{(.*?)\}", self.program).group(1).split(",")))

    def print_machine(self):
        for k, v in self.__dict__.items():
            print(f"{k}: {v}")
        print()

    def min_presses_bfs(self) -> int:
        # Queue = {curr_state, num_presses}
        if self.start_lights == self.end_lights:
            return 0

        visited = {self.start_lights}
        queue = deque([(self.start_lights, 0)])

        # BFS
        while queue:
            lights, presses = queue.popleft()

            for button in self.buttons:
                # Convert to list to allow modification
                new_lights = list(lights)
                # Change the lights based on the button
                for button_num in button:
                    new_lights[button_num] = (
                        "#" if new_lights[button_num] == "." else "."
                    )
                # Convert back to string
                new_lights = "".join(new_lights)

                # End condition - check immediately after creating new state
                if new_lights == self.end_lights:
                    return presses + 1

                # Add the new state to the queue if not visited
                if new_lights not in visited:
                    visited.add(new_lights)
                    queue.append((new_lights, presses + 1))

        return -1


def main():
    part1_total = 0

    machines = []
    with open("input.txt", "r") as f:
        for line in f:
            machines.append(Machine(line.strip()))
    for m in machines:
        # m.print_machine()
        part1_total += m.min_presses_bfs()
    print(f"Part 1: {part1_total}")


if __name__ == "__main__":
    main()
