import re

def parse_input():
    with open("2022\Day 5\input.txt", "r") as file:
        inp = file.readlines()

    # Parse starting stacks (Values on index 1, 5, 9, ..., 33)
    stacks = [[]]*9
    stack_inp = inp[:8]
    stack_inp.reverse()
    stacks = [[stack_inp[i][j] for i in range(8) if stack_inp[i][j] != " "] for j in range(1, 34, 4)]

    # Parse command list
    commands_inp = inp[10:]
    commands = [re.sub("[a-zA-Z]", "", line).split() for line in commands_inp] # Prune alphabetic chars
    return stacks, commands

# Part 1 + 2
stacks, commands = parse_input()
for command in commands:
    num = int(command[0])           # Amount to move
    start = int(command[1]) - 1     # Index of pickup
    end = int(command[2]) - 1       # Index of placement

    temp = stacks[start][-num:]
    stacks[end].extend(temp[::-1]) # For part 2, extend with temp instead of temp[::-1] 
    stacks[start] = stacks[start][:-num]

print(''.join([stack[-1] for stack in stacks]))