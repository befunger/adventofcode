import numpy as np

with open("2022\Day 8\input.txt", "r") as file:
    inp = [[int(i) for i in line.strip("\n")] for line in file.readlines()]

inp = np.array(inp)
n,m = inp.shape

# Part 1
tree_map = np.zeros([n, m])
tree_map[:,[0,-1]] = tree_map[[0,-1]] = 1 # Initialise as 0-matrix with 1 on edges
# Part 2
scenic_map = 1 - tree_map  # Initialise as 1-matrix with 0 on edges

for i in range(1,n-1):
    for j in range(1,m-1):
        up, down, left, right = inp[:i,j], inp[i+1:,j], inp[i,:j], inp[i,j+1:]
        
        #Part 1
        tree_map[i][j] = inp[i,j] > min(np.max(left), np.max(right), np.max(up), np.max(down))
        
        # Part 2
        for dir in [up[::-1], left[::-1], right, down]:
            scenic_map[i,j] *= np.min(np.append(np.where(dir>=inp[i,j])[0]+1,np.size(dir)))

# Part 1
print(np.sum(tree_map))
# Part 2
print(np.max(scenic_map))
