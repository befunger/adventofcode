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

# One-liners because Fuwante is rude
# for i in range(4, len(inp)+1): print(i) if len(set((inp[i-4:i])))==4 else None
# for i in range(14, len(inp)+1): print(i) if len(set((inp[i-14:i])))==14 else None

# Carols homecooking
d, inp = (0, open('day6.txt', 'r').read())
for i in range(len(inp)): d += d < 1 and i > 4 and len(set(inp[i-4:i])) == 4 and print(i) is None or d < 2 and i > 14 and len(set(inp[i-14:i])) == 14 and print(i) is None
# Explanation: 
# We only evaluate the Y in 'X and Y' if X already returns True.
# As long as the len(set()) returns False, nothing really happens, but once it is True we continue to the print, and also the full expression evaluates to True
# This means d += True, which is equivalent to d += 1, meaning the first clause prior to 'or' will no longer be evaluated
# Same logic loops through the second part until we find something that evaluates the len(set()) expression to True, prints the result, and then increments d to 2 which halts any future evaluation.
