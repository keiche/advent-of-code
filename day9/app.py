#!/usr/bin/env python3
"""https://adventofcode.com/2022/day/9"""


def move_follower(leader: list, follower: list) -> list:
    """
    Move the follower (next knot) based on how the leader moved
    Follower must be touching the leader (diagonal included)
    When they are diagonally separated then the follower takes 2 moves to catch up
    :param leader: coordinates of leader
    :param follower: coordinates of follower
    :return: new coordinates for follower
    """
    new_x = follower[0]
    new_y = follower[1]

    # Allow 2 moves to be taken when diagonal and separated
    flag_do_both = False
    if (leader[0] != follower[0] and abs(leader[1] - follower[1]) > 1) or (
        leader[1] != follower[1] and abs(leader[0] - follower[0]) > 1
    ):
        flag_do_both = True

    # Above/Below
    if abs(leader[1] - follower[1]) > 1 or flag_do_both:
        # Leader is below
        if leader[1] < follower[1]:
            new_y -= 1
        # Leader is above
        elif leader[1] > follower[1]:
            new_y += 1
    # Left/Right
    if abs(leader[0] - follower[0]) > 1 or flag_do_both:
        # Leader is left
        if leader[0] < follower[0]:
            new_x -= 1
        elif leader[0] > follower[0]:
            new_x += 1

    return [new_x, new_y]


def print_board(knot_pos: list) -> None:
    """
    Print the board (debug purposes)
    :param knot_pos: positions of all the knots
    """
    board = []
    min_coord = -256
    max_coord = 256
    for x in range(min_coord, max_coord):
        row = ""
        for y in range(min_coord, max_coord):
            cell = "."
            for idx, k in enumerate(knot_pos):
                if x == k[1] and y == k[0]:
                    cell = str(idx)
                    break
            if x == 0 and y == 0:
                cell = "s"
            row += cell
        board.append(row)

    # Print board
    for row in reversed(board):
        print(row)
    print()


def run(instructions: list, knots: int) -> int:
    """
    Process the instructions
    :param instructions: input instructions
    :param knots: number of knots to track
    :return: unique number of positions the tail (final knot) has been in
    """
    # Initialize the knot positions
    knot_pos = [[0, 0] for _ in range(0, knots)]

    # Track the unique tail coordinates (answers)
    unique_tail_coord = set()
    unique_tail_coord.add(tuple(knot_pos[-1]))

    # Process each instruction
    for direction, spaces in instructions:
        # Make each individual move as it will affect the other knots
        for space in range(1, spaces + 1):
            if direction == "L":
                knot_pos[0][0] -= 1
            elif direction == "R":
                knot_pos[0][0] += 1
            elif direction == "U":
                knot_pos[0][1] += 1
            elif direction == "D":
                knot_pos[0][1] -= 1

            for idx, k in enumerate(knot_pos):
                # Head already moved
                if idx == 0:
                    continue
                knot_pos[idx] = move_follower(knot_pos[idx - 1], knot_pos[idx])

                # Debug output
                # print_board(knot_pos)
                # print(knot_pos)

            # Tail may have moved - add to unique position set
            unique_tail_coord.add(tuple(knot_pos[-1]))

    return len(unique_tail_coord)


def main() -> None:
    moves = []
    with open("9.txt", "r") as f:
        for line in f.readlines():
            direction, spaces = tuple(line.rstrip().split(" "))
            moves.append((direction, int(spaces)))

    part_1 = run(moves, 2)
    part_2 = run(moves, 10)

    print(f"Part 1: {part_1}")
    print(f"Part 2: {part_2}")


if __name__ == "__main__":
    main()
