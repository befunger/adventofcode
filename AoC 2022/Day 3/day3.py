with open("2022\Day 3\input.txt", "r") as file:
    sacks = file.readlines()
sacks = [sack.strip('\n') for sack in sacks]

# Get priority of an item (a-z => 1 - 26, A-Z => 27 - 52)
def prio(item):
    return ord(item) - 96 if ord(item) > 96 else ord(item) - 38

# Part 1
priority_sum = 0
for ruck in sacks:
    l = len(ruck)//2
    item = [x for x in ruck[:l] if x in ruck[l:]][0]
    priority_sum += prio(item)

print(priority_sum)

# Part 2
i = 0
badge_priority_sum = 0
while i < len(sacks):
    badge = [x for x in sacks[i] if x in sacks[i+1] and x in sacks[i+2]][0]
    badge_priority_sum += prio(badge)
    i += 3
print(badge_priority_sum)