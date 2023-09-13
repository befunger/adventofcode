with open("2022\Day 14\input.txt", "r") as file:
    # inp = [(int(entry[0])), int(entry[1])) for entry in line.split(',') in file.read().split('\n') for entry in line.split(' -> ')]
    lines = [[(int(entry.split(',')[0]), int(entry.split(',')[1])) for entry in line.split(' -> ')] for line in file.read().split('\n')]


# Make a set of all the points spanned by the lines in the input
rocks = set(
    {(x, y) for line in lines
            for i, p in enumerate(line[:-1])
            for ep in [line[i+1]]
            for x in range(min(p[0], ep[0]), max(p[0], ep[0]) + 1)      # One of these ranges will always return a single number for cardinal lines
            for y in range(min(p[1], ep[1]), max(p[1], ep[1]) + 1)}     # This code would not work in case of diagonal lines!
)
# Get the lowest rock y coordinate (sand below this point never comes to rest)
bottom = max(rocks, key=lambda item: item[1])[1]

# Starting coordinates
x, y = 500, 0
restingSand = 0
while(y < bottom):
    if (x,y+1) not in rocks:
        y+=1
    elif (x-1,y+1) not in rocks:
        x-=1
        y+=1
    elif (x+1,y+1) not in rocks:
        x+=1
        y+=1
    else:  # All three below occupied, sand comes to rest
        rocks.add((x,y))
        x,y = 500, 0
        restingSand += 1

print("Part 1:", restingSand)

# Part 2 
real_bottom = bottom + 1
x, y = 500, 0
while(True):
    if y == real_bottom: # Rock bottom
        rocks.add((x,y))
        restingSand += 1
        x,y = 500, 0
    elif (x,y+1) not in rocks:
        y+=1
    elif (x-1,y+1) not in rocks:
        x-=1
        y+=1
    elif (x+1,y+1) not in rocks:
        x+=1
        y+=1
    else:   # All three below occupied, sand comes to rest
        rocks.add((x,y))
        restingSand += 1
        if (x,y) == (500, 0): # Stop if coming to rest at start point
            break
        x,y = 500, 0

print("Part 2:", restingSand)