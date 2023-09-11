with open("2022\Day 10\input.txt", "r") as file:
    inp = [line.strip('\n').split(' ') for line in file.readlines()]

x = 1
cycle = 1
signal_sum = 0
draw_string = ['#']
for cmd in inp:
    cycle += 1 # Always pass one cycle
    signal_sum += x*cycle if (cycle+20)%40==0 else 0 # Part 1
    draw_string.append('#' if cycle%40 in (x, x+1, x+2) else '.') # Part 2
    if cmd[0] == "addx": 
        cycle += 1
        x += int(cmd[1])
        signal_sum += x*cycle if (cycle+20)%40==0 else 0 # Part 1
        draw_string.append('#' if cycle%40 in (x, x+1, x+2) else '.') # Part 2

print(signal_sum)
for i, x in enumerate(draw_string):
    if i%40 == 0:
        print("")
    print(x, end="")