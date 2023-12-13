with open("AoC 2023\inputs\day11.txt", "r") as file:
    # Split input into list of of list of characters
    lines = [[char for char in line.strip("\n")] for line in file.readlines()]


# Go through grid to note down all galaxy positions in a list, and which rows/cols have none
# After enumerating, row_empty/col_empty will be 1 on empty rows, and 0 on non-empty
galaxies = []
row_empty = [1]*len(lines)
col_empty = [1]*len(lines[0])

for i, row in enumerate(lines):
    for j, x in enumerate(row):
        if x == '#':
            # Save galaxy to list
            galaxies.append((i,j))
            # Update row/col to reflect that it is not empty
            row_empty[i] = 0
            col_empty[j] = 0

# Make two cum sums for horizontal/vertical expansion
# padx[j] - padx[i] = # of horizontal lines between i and j to expand
padx = [0]
for val in row_empty:
    padx.append(padx[-1]+val)

pady = [0]
for val in col_empty:
    pady.append(pady[-1]+val)

# Use manhattan distance between each pair of galaxies + padding factor with cum sums
# For part 2, just multiply the added padding
sum_of_distances = 0
sum_of_BIG_distances = 0
for i,galaxy in enumerate(galaxies):
    # Only compare galaxy to ones later in the list (ensures 1 comparison per pair)
    for j,other_galaxy in enumerate(galaxies[i+1:], start=i+1):
        # Manhattan distance
        base_dist = abs(other_galaxy[0] - galaxy[0]) + abs(other_galaxy[1] - galaxy[1])
        # Amount of lines to be expanded in x and y direction
        pad_dist = abs(padx[other_galaxy[0]]-padx[galaxy[0]]) + abs(pady[other_galaxy[1]]-pady[galaxy[1]])

        sum_of_distances += base_dist + pad_dist
        sum_of_BIG_distances += base_dist + 999999*pad_dist

print("Part 1:", sum_of_distances)
print("Part 2:", sum_of_BIG_distances)
