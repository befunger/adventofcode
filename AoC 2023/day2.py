with open("AoC 2023\inputs\day2.txt", "r") as file:
    inp = [line.split(": ")[1] for line in file.readlines()]

tot = 0
for x,game in enumerate(inp, start=1):
    viable = True
    draws = [item.strip('\n').split(" ") for turn in game.split("; ") for item in turn.split(", ")]
    for amount, color in draws:
        if (color == 'red' and int(amount) > 12)\
         or (color == 'green' and int(amount) > 13)\
         or (color == 'blue' and int(amount) > 14):
            viable = False
            break
    if viable:
        tot += x

print("Part 1:", tot)

tot = 0
for x,game in enumerate(inp, start=1):
    draws = [item.strip('\n').split(" ") for turn in game.split("; ") for item in turn.split(", ")]
    red = green = blue = 0
    for amount, color in draws:
        if color == 'red':
            red = max(red, int(amount))
        if color == 'green':
            green = max(green, int(amount))
        if color == 'blue':
            blue = max(blue, int(amount))
    tot += red*green*blue

print("Part 2:", tot)
