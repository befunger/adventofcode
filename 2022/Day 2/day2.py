score = 0
score2 = 0
f = open("2022\Day 2\input.txt", "r")
for line in f.readlines():
    ''' Part 1 '''
    # Reduces inputs to 0, 1, 2
    own = ord(line[2]) - ord('W')
    opp = ord(line[0]) - ord('@')

    # 0 if loss, 1 if draw, 2 if win 
    # Normally modulo 3 of the difference would give 0 if draw, 1 if win, 2 if loss, so we shift by + 1
    result = (own - opp + 1) % 3

    score += own        # From choice of hand
    score += 3 * result # From result

    ''' Part 2 '''
    opp = ord(line[0]) - ord('@')
    result = ord(line[2]) - ord('X')

    # Case 1: result = 0 => We should pick 1 lower
    # Case 2: result = 1 => we should pick same
    # case 3: result = 2 => we should pick 1 higher
    # Stupid and cursed
    own = ((opp - 1 + result - 1) % 3) + 1
    score2 += own + 3 * result

print(score)
print(score2)