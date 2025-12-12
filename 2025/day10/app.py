"""
https://adventofcode.com/2025/day/10
keiche
"""
from re import findall, match, search
from collections import deque
from z3 import Int, Optimize, Sum, sat


class Machine:
    def __init__(self, program: list[int]):
        # Reading input
        self.program = program
        self.end_lights = match(r"\[(.*?)\]", self.program).group(1)
        self.start_lights = "." * len(self.end_lights)
        self.buttons = [list(map(int, x.split(","))) for x in findall(r"\((.*?)\)", self.program)]
        self.joltage_requirements = list(map(int, search(r"\{(.*?)\}", self.program).group(1).split(",")))

    def print_machine(self):
        for k, v in self.__dict__.items():
            print(f"{k}: {v}")
        print()

    def min_presses_bfs(self) -> int:
        """Part 1 - Min button presses to get to end lights"""
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
                    new_lights[button_num] = "#" if new_lights[button_num] == "." else "."
                # Convert back to string
                new_lights = "".join(new_lights)

                # End condition
                if new_lights == self.end_lights:
                    return presses + 1

                # Add the new state to the queue if not visited
                if new_lights not in visited:
                    visited.add(new_lights)
                    queue.append((new_lights, presses + 1))

        return -1

    def solve_with_z3(self) -> int:
        """
        Part 2 - Use Z3 to find minimum button presses satisfying:
        Total presses at each position equals joltage requirement
        Had to get help to get this working! Tricky!
        """
        num_buttons = len(self.buttons)
        num_lights = len(self.end_lights)

        # Create Z3 optimizer
        opt = Optimize()

        # Variables: how many times each button is pressed (non-negative integers)
        button_presses = [Int(f"b{i}") for i in range(num_buttons)]

        # Constraint: each button pressed >= 0 times
        for bp in button_presses:
            opt.add(bp >= 0)

        # For each light position, calculate total presses affecting it
        for pos in range(num_lights):
            # Find which buttons affect this position
            affecting_buttons = [i for i, btn in enumerate(self.buttons) if pos in btn]

            # Total times this position is toggled
            total_toggles = Sum([button_presses[i] for i in affecting_buttons]) if affecting_buttons else 0

            # Constraint: Joltage requirement - total toggles must equal required joltage
            opt.add(total_toggles == self.joltage_requirements[pos])

        # Objective: minimize total button presses
        total_presses = Sum(button_presses)
        opt.minimize(total_presses)

        # Solve
        if opt.check() == sat:
            model = opt.model()
            return sum(model[bp].as_long() for bp in button_presses)
        else:
            return -1  # No solution found


def main():
    part1_total = 0
    part2_total = 0

    machines = []
    with open("input.txt", "r") as f:
        for line in f:
            machines.append(Machine(line.strip()))
    for m in machines:
        m.print_machine()
        part1_total += m.min_presses_bfs()
        part2_total += m.solve_with_z3()
    print(f"Part 1: {part1_total}")
    print(f"Part 2: {part2_total}")


if __name__ == "__main__":
    main()
