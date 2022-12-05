#!/usr/bin/env python3

def winner(theirs, mine):
    # Tie
    if theirs == mine:
        return 3
    # Win
    if (theirs == "rock" and mine == "paper") or (theirs == "paper" and mine == "scissors") or (theirs == "scissors" and mine == "rock"):
        return 6
    # Loss
    return 0


def results2shape(theirs, result):
    if (theirs == "rock" and result == "lose") or (theirs == "paper" and result == "win") or (theirs == "scissors" and result == "tie"):
        return "scissors"
    if (theirs == "rock" and result == "tie") or (theirs == "paper" and result == "lose") or (theirs == "scissors" and result == "win"):
        return "rock"
    if (theirs == "rock" and result == "win") or (theirs == "paper" and result == "tie") or (theirs == "scissors" and result == "lose"):
        return "paper"


shape_translate = {"A": "rock", "B": "paper", "C": "scissors", "X": "rock", "Y": "paper", "Z": "scissors"}
results_translate = {"X": "lose", "Y": "tie", "Z": "win"}
shape_pts = {"rock": 1, "paper": 2, "scissors": 3}

total_pt1 = 0
total_pt2 = 0
with open("2.txt", "r") as f:
    for line in f.readlines():
        first, second = line.rstrip().split(" ")
        theirs = shape_translate[first]

        # Part 1
        mine = shape_translate[second]
        total_pt1 += winner(theirs, mine) + shape_pts[mine]

        # Part 2
        result = results_translate[second]
        mine = results2shape(theirs, result)
        total_pt2 += winner(theirs, mine) + shape_pts[mine]

print(f"Part 1: {total_pt1}")
print(f"Part 2: {total_pt2}")