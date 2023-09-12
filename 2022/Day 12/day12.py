with open("2022\Day 12\input.txt", "r") as file:
    # map = [[char for char in line] for line in file.read().split('\n')]
    map = file.read().split('\n')

'''Checks if new point is eligible based on index, height, and newness constraints'''
def eligible_neighbour(x, y, i, j, visited):
    return not (x + i < 0 or x + i> 40 or y + j < 0 or y + j > 113 or               # Index constraints (Don't leave 40x114 grid)
                map[x][y] != 'S' and ord(map[x+i][y+j]) > ord(map[x][y]) + 1 or     # Height constraint (Can only climb to one higher order)
                (x+i, y+j) in visited)                                              # Newness constraint (Don't revisit same points in DFS)

# # Locate starting points
starts = [(i, j) for i, line in enumerate(map) for j, y in enumerate(line) if y=='a' or y=='S']

min_distance = 1e10
for start in starts:
    visited = {start : 0} # Dictionary with visited points as keys, and their step count as value
    node_queue = [(start)]

    while node_queue:
        curr = node_queue.pop(0)
        neighbours = [(curr[0]+i, curr[1]+j) for i,j in [[0, -1], [0, 1], [-1, 0], [1, 0]] if eligible_neighbour(curr[0], curr[1], i, j, visited)]
        for x,y in neighbours:
            if map[x][y] == 'E': # End found
                if map[start[0]][start[1]] == 'S': # Print length of S-E path for Part 1
                    print("Part 1:", visited[curr]+1)
                min_distance = min(visited[curr]+1, min_distance)
                node_queue = [] # Empty queue to immediately exit while-loop
            else:
                visited[(x,y)] = visited[curr]+1
                node_queue.append((x,y))

print("Part 2:", min_distance)
