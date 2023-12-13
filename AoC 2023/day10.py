with open("AoC 2023\inputs\day10.txt", "r") as file:
    # Split input into list of of list of characters
    lines = [[char for char in line.strip("\n")] for line in file.readlines()]

def find_adjacent(layout, indices, prev=None):
    '''Given an index tuple, return index tuple of adjacent pipe it connects to. If a prev argument is given, exclude it as option'''
    connects_to = {'north'  : {'S', '|', 'L', 'J'},
                   'south'  : {'S', '|', 'F', '7'}, 
                   'west'   : {'S', '-', 'J', '7'}, 
                   'east'   : {'S', '-', 'F', 'L'}}
    i, j = indices
    pipe_type = layout[i][j]
    if i > 0 and pipe_type in connects_to['north']:
        # Check north
        if layout[i-1][j] in connects_to['south'] and (i-1, j) != prev:
            return (i-1, j)

    if i < 139 and pipe_type in {'S', '|', 'F', '7'}:
        # Check south
        if layout[i+1][j] in connects_to['north'] and (i+1, j) != prev:
            return (i+1, j)

    if j > 0 and pipe_type in connects_to['west']:
        # Check west
        if layout[i][j-1] in connects_to['east'] and (i, j-1) != prev:
            return (i, j-1)

    if j < 139 and pipe_type in connects_to['east']:
        # Check east
        if layout[i][j+1] in connects_to['west'] and (i, j+1) != prev:
            return (i, j+1)

    print("SOMETHING WENT WRONG")
    return 0


# 140 x 140
# Find starting square
start = (0, 0)
for i, line in enumerate(lines):
    if 'S' in line:
        start = (i, line.index('S'))
        break

dist = 0
node = start
prev = None
# Iterate until we hit S node again
while lines[node[0]][node[1]] != 'S' or dist == 0:
    # Get next node that matches orientation of current
    next = find_adjacent(lines, node, prev)
    # Iterate nodes
    prev = node
    node = next
    # Iterate distance traveled
    dist += 1

print("Part 1:", dist//2)


# Part 2: Find number of tiles enclosed by the loop (similar to point inside polygon problem)
