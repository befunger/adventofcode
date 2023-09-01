f = open("2022\Day 1\input.txt", "r")
list_of_elves = f.read().split("\n\n")

cal_counts = [sum([int(cal) for cal in list_of_items.split("\n")]) for list_of_items in list_of_elves[:-1]]

# Part 1 solution
print(max(cal_counts))

# Part 2 solution
print(sum(sorted(cal_counts)[-3:]))