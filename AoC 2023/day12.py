def recbad(line, hints):
    # Move until ?
    ptr = 0
    prior_springs = 0
    # Find first ? while recording prior #s
    while line[ptr] != '?' and ptr < len(line):
        prior_springs = prior_springs + 1 if line[ptr] == '#' else 0
        ptr += 1

    print(f"Found first ? at {ptr} with {prior_springs} preceeding springs.")

    if prior_springs > 0:
        # We must add more springs until matching first hint
        print(f"Adding {hints[0]-prior_springs} more springs, and then a .")
        while hints[0] - prior_springs > 0:
            print(f"Replacing at {ptr} with spring")
            line[ptr] = '#'
            prior_springs += 1
            ptr += 1
        print(f"Closing # group with . at {ptr}")
        line[ptr] = '.'
    return 0

def rec(line, hints, prior_springs = 0):
    # If no more hints, it's a success if the rest of the line has no #
    # print(line, hints)
    if len(hints) == 0:
        if '#' in line:
            # print("No more hints but too many #")
            return 0
        else:
            # print(" Finished correctly.")
            return 1
    if len(line) == 0:
        # print("End of line but didnt detect finishing hints")
        return 0

    # Not enough space left to fill out
    if len(line) + prior_springs < sum(hints) + len(hints)-1:
        return 0

    # Move past a .
    if line[0] == ".":
        # print("Hit a .")
        if prior_springs > 0:
            # print("  Closed a group just now.")
            if prior_springs == hints[0]:
                # print("    Group finished correctly!")
                return rec(line[1:], hints[1:])
            else:
                # print("    Invalid group closing, aborting.")
                return 0
        else:
            return rec(line[1:], hints)
    # Move past a # but record springs prior
    if line[0] == "#":
        # print("Hit a #")
        if prior_springs == hints[0]:
            # print("Too many # for current group")
            return 0
        else:
            return rec(line[1:], hints, prior_springs+1)

    # print("Hit a ?")
    # If we hit a ? but with #s prior, we have to finish the group first
    if prior_springs > 0:
        # print("  We have an unresolved group")
        if prior_springs < hints[0]:
            # print("    Replacing with #")
            return rec(line[1:], hints, prior_springs+1)
        elif prior_springs == hints[0]:
            # print("    Closing group with .")
            return rec(line[1:], hints[1:])

    # print("  We can either start new group or block with .")
    # Adding a # (new group began)
    # print("    Adding # and recursing")
    spring_options = rec(line[1:], hints, 1)
    # print(f"    {spring_options} options with # as first on {line}")
    # Adding a . (no new group)
    # print("    Adding . and recursing")
    dot_options = rec(line[1:], hints)
    # print(f"    {dot_options} options with . as first on {line}")

    return dot_options + spring_options



with open("AoC 2023\inputs\day12.txt", "r") as file:
    # Split input into list of chars and list of ints
    lines = [(line.split(" ")[0],
              [int(num) for num in line.split(" ")[1].split(",")])
              for line in file.read().splitlines()]


part_1_total = 0
part_2_total = 0
for line, hint in lines:
    part_1_arrs = rec(line+'.', hint)
    print(f'Line gives {part_1_arrs} arrangements.')
    part_1_total += part_1_arrs

    part_2_arrs = rec("?".join([line]*5)+'.', hint*5)
    print(f'Line gives {part_2_arrs} part 2 arrangements.')
    part_2_total += part_2_arrs


print("Part 1:", part_1_total)
print("Part 2:", part_2_total)



# test_line = (list("?###????????"), [3,2,1])
# print(rec(test_line[0]+['.'], test_line[1]))
