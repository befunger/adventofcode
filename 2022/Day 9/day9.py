with open("2022\Day 9\input.txt", "r") as file:
    inp = [line.strip('\n').split(' ') for line in file.readlines()]


'''Adjusts tail one step based on head position'''
def moveTail(head, tail):
    x, y = getOffset(head, tail)
    if (abs(x) > 1): 
        tail[0]+= x/abs(x) # Move in x
        if(abs(y) > 0): 
            tail[1]+= y/abs(y) # Add diagonal
    elif(abs(y) > 1): 
        tail[1]+= y/abs(y) # Move in y
        if (abs(x) > 0):
            tail[0]+= x/abs(x) # Add diagonal

'''Return offsets between head and tail'''
def getOffset(head, tail):
    return head[0] - tail[0], head[1] - tail[1]

# Part 1
head = [0, 0] 
tail = [0, 0]
visited = {'[0, 0]': 1}

# Part 2
tails = [[0, 0] for _ in range(9)]
visited2 = {'[0, 0]': 1}

for line in inp:
    # Move head
    match line[0]:
        case "U":
            head[1]+=int(line[1])
        case "D":
            head[1]-=int(line[1])
        case "L":
            head[0]-=int(line[1])
        case "R":
            head[0]+=int(line[1])

    # Part 1 (Update tail until it catches up with head)
    xOffset, yOffset = getOffset(head, tail)
    while(abs(xOffset) > 1 or abs(yOffset) > 1):
        moveTail(head, tail)
        xOffset, yOffset = getOffset(head, tail)
        visited[f'{tail}'] = 1

    # Part 2 (Update every tail segment sequentially, repeat until caught up)
    xOffset, yOffset = getOffset(head, tails[0])
    while(abs(xOffset) > 1 or abs(yOffset) > 1):
        for i, curr_tail in enumerate(tails):
            if i == 0:
                moveTail(head, curr_tail) # Use head
            else:
                moveTail(tails[i-1], curr_tail)
    
        xOffset, yOffset = getOffset(head, tails[0])
        visited2[f'{tails[8]}'] = 1

print(len(visited))
print(len(visited2))