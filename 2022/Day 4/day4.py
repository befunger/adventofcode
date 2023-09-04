with open("2022\Day 4\input.txt", "r") as file:
    pairs = file.readlines()

nums = [[rng.split("-") for rng in line.strip("\n").split(",")] for line in pairs]

# Part 1
overlaps = sum([1 if 
                int(line[0][0]) <= int(line[1][0]) and int(line[0][1]) >= int(line[1][1]) or 
                int(line[0][0]) >= int(line[1][0]) and int(line[0][1]) <= int(line[1][1]) else 0 for line in nums])
print(overlaps)

# Part 2
overlaps = sum([1 if 
                int(line[0][0]) in range(int(line[1][0]), int(line[1][1])+1) or 
                int(line[0][1]) in range(int(line[1][0]), int(line[1][1])+1) or
                int(line[1][0]) in range(int(line[0][0]), int(line[0][1])+1) else 0 for line in nums])
print(overlaps)