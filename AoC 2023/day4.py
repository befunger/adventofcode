with open("AoC 2023\inputs\day4.txt", "r") as file:
    # Remove linebreaks, remove 'Game X:' prefix, and split on pipe char
    inp = [line.strip("\n").split(": ")[1].split("|") for line in file.readlines()]

'''Part 1'''
points = 0
for line in inp:
    # Set of winning numbers (remove empty strings)
    win_set = set(line[0].split())
    # Amount of numbers on cards that are also in the win set
    num_matched = len([y for y in line[1].split() if y in win_set])
    if num_matched == 0:
        points += 2**(num_matched-1)
print("Part 1:", points)

'''Part 2'''
# Start out with 1 of each card
cards = [1]*len(inp)
for i, line in enumerate(inp):
    # Set of winning numbers (remove empty strings)
    win_set = set(line[0].split())
    # Amount of numbers on cards that are also in the win set
    num_matched = len([y for y in line[1].split() if y in win_set])
    # Increase number of the next [num_matched] scratch cards by 1 for each copy of this card
    # Scratch card X matches 3 numbers and has 5 copies => increase cards X+1, X+2, and X+3 by 5
    while num_matched:
        cards[i+num_matched] += cards[i]
        num_matched -= 1
# Answer is total number of cards of all types
print("Part 2:", sum(cards))
