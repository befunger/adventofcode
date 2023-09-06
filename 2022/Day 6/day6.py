with open("2022\Day 6\input.txt", "r") as file:
    inp = file.read()

# Part 1
for i in range(4, len(inp)+1):
    if len(set((inp[i-4:i])))==4:
        print(i)
        break

# Part 2
for i in range(14, len(inp)+1):
    if len(set((inp[i-14:i])))==14:
        print(i)
        break
