#!/usr/local/env python3
"""
https://adventofcode.com/2024/day/17
keiche
"""


class Computer:
    def __init__(self, a: int, b: int, c: int, program: list[int]):
        self.a = a
        self.b = b
        self.c = c
        self.program = program

        self.pointer = 0
        self.opcode = None
        self.operand = None
        self.combo_operand = None
        self.jumped = False  # used by jnz
        self.output = []

        self.instructions = {
            0: self.adv,
            1: self.bxl,
            2: self.bst,
            3: self.jnz,
            4: self.bxc,
            5: self.out,
            6: self.bdv,
            7: self.cdv,
        }

    def set_combo_operand(self):
        if 0 <= self.operand <= 3:
            self.combo_operand = self.operand
        elif self.operand == 4:
            self.combo_operand = self.a
        elif self.operand == 5:
            self.combo_operand = self.b
        elif self.operand == 6:
            self.combo_operand = self.c

    def adv(self):
        self.a = int(self.a / 2**self.combo_operand)

    def bxl(self):
        self.b = self.b ^ self.operand

    def bst(self):
        self.b = self.combo_operand % 8

    def jnz(self):
        if not self.a == 0:
            self.pointer = self.operand
            self.jumped = True

    def bxc(self):
        self.b = self.b ^ self.c

    def out(self):
        self.output.append(self.combo_operand % 8)

    def bdv(self):
        self.b = int(self.a / 2**self.combo_operand)

    def cdv(self):
        self.c = int(self.a / 2**self.combo_operand)

    def run(self) -> list[int]:
        while self.pointer + 1 < len(self.program):
            # Get the next set of instructions
            self.opcode = self.program[self.pointer]
            self.operand = self.program[self.pointer + 1]
            self.set_combo_operand()

            # Run the instruction
            self.instructions[self.opcode]()

            # Increment pointer
            if not self.jumped:
                self.pointer += 2
            self.jumped = False
        return self.output


def parse_input(filename: str) -> tuple[int, int, int, list[int]]:
    reg_a = 0
    reg_b = 0
    reg_c = 0
    program = []
    with open(filename, "r") as f:
        for line in f:
            line = line.strip()
            if ":" not in line:
                continue
            value = line.split(": ")[1]
            if "Register A" in line:
                reg_a = int(value)
            elif "Register B" in line:
                reg_b = int(value)
            elif "Register C" in line:
                reg_c = int(value)
            elif "Program" in line:
                program = list(map(int, value.split(",")))
    return reg_a, reg_b, reg_c, program


def main():
    computer = Computer(*parse_input("input.txt"))
    output = computer.run()
    print(f"Part 1: {','.join(list(map(str, output)))}")


if __name__ == "__main__":
    main()
