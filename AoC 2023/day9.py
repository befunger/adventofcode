with open("AoC 2023\inputs\day9.txt", "r") as file:
    # Split input into list of int sequences
    sequences = [[int(num) for num in line.split()] for line in file.readlines()]

def differences(numbers : list[int]) -> list[int]:
    '''Returns array of length n-1 containing difference between each pair of numbers'''
    n = len(numbers)
    if n < 2:
        return [0]
    return [numbers[i+1]-numbers[i] for i in range(n-1)]

# Part 1
sum_of_next = 0
for sequence in sequences:
    # Go through each differentiation step and sum the rate of change
    next_in_sequence = 0
    while sum(abs(x) for x in sequence):
        next_in_sequence += sequence[-1]
        sequence = differences(sequence)
    sum_of_next += next_in_sequence

print("Part 1:", sum_of_next)

# Part 2
sum_of_prev = 0
for sequence in sequences:
    prev_in_sequence = 0
    # We alternate + and - with inverter to simulate the alternating signs of a-(b-(c-d)) = a-b+c-d
    inverter = 1
    while sum(abs(x) for x in sequence):
        prev_in_sequence += sequence[0] * inverter
        inverter *= -1
        sequence = differences(sequence)
    sum_of_prev += prev_in_sequence

print("Part 2:", sum_of_prev)
