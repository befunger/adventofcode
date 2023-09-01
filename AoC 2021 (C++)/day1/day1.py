with open('input.txt') as f:
    lines = f.readlines()

#lines = [2,3,5,7,5,10]

numIncreases = 0
prevNum = lines[0]

for line in lines[1:]:
    if int(line) > int(prevNum):
        numIncreases += 1
    prevNum = int(line)
print(numIncreases)