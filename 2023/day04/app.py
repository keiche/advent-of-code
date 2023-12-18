#!/usr/local/env python3
"""
https://adventofcode.com/2023/day/4
keiche
"""

part1_total = 0
part2_total = 0
# New unprocessed cards
new_cards = []
# Track which cards you win with each card
winner_table = {}

with open("input.txt", "r") as f:
    for line in f.readlines():
        line = line.rstrip()

        # Parse
        card_no = int(line.split(":")[0].split()[1])
        win_list = line.split(" | ")[0].split(": ")[1].split()
        num_list = line.split(" | ")[1].split()

        # Part 1 - Inner join
        winners = list(set(win_list) & set(num_list))

        if winners:
            card_value = 2 ** (len(winners) - 1)
            part1_total += card_value

        # Part 2
        # Current card is processed
        part2_total += 1

        # New cards (winnings)
        winnings = list(range(card_no + 1, card_no + len(winners) + 1))
        new_cards.extend(winnings)

        # Save winnings for simple lookup later
        winner_table[card_no] = winnings

# Part 2 - process new cards
while len(new_cards) > 0:
    c = new_cards.pop(0)

    # Add to processed cards
    part2_total += 1

    # Add the number of cards for each matches it has to the queue
    for i in range(int(c) + 1, int(c) + len(winner_table[c]) + 1):
        c.append(new_cards)

print(f"Part 1: {part1_total}")
print(f"Part 2: {part2_total}")
