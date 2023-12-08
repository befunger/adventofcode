import math
with open("AoC 2023\inputs\day8.txt", "r") as file:
    instruction, mapping = file.read().split('\n\n')

# Array of left/right instructions
instruction = list(instruction)

# Create dictionary where map[node] = [left_node, right_node]
map = dict()
for node in mapping.split("\n"):
    node, neighbours = node.split(" = ")
    # Strip parentheses and split
    map[node] = neighbours.strip("(").strip(")").split(", ")

# Part 1
node = 'AAA'
step = 0

while node != 'ZZZ':
    # Select instruction with modulo to restart from beginning when we have gone through all
    # L => direction = 0, R => direction = 1
    direction = int(instruction[step % len(instruction)] == "R")
    # Choose neighbour based on map instruction
    node = map[node][direction]
    step += 1

print("Part 1:", step)

# Part 2

# List of start nodes ending with A
nodes = [key for key in map if key[-1] == 'A']

steps = []
for i,node in enumerate(nodes):
    step = 0
    while node[-1] != 'Z':
        # Get direction
        direction = int(instruction[step % len(instruction)] == "R")
        node = map[node][direction]
        step += 1
    steps.append(step)

# Find Least Common Multiple of steps (when cycles line up and all hit goal simultaneously)
# We can calculate LCM sequentially: LCM(X,Y,Z) = LCM(LCM(X,Y), Z)
result = 1
for step in steps:
    result = math.lcm(result, step)
print("Part 2:", result)
