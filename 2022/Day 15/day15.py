import re
with open("2022\Day 15\input.txt", "r") as file:
    sensors = [[int(num) for num in re.findall(r'[-+]?\d+', text)] for text in file.readlines()]

'''Returns manhattan distance'''
def manhattan(sensor):
    return abs(sensor[0]-sensor[2]) + abs(sensor[1] - sensor[3]) 

y = 2000000
blocked = set()

for sensor in sensors:
    offset = manhattan(sensor) - abs(y-sensor[1]) # Distance to beacon minus distance to line in question
    if offset >= 0:
        blocked = blocked.union({i for i in range(sensor[0]-offset, sensor[0]+offset+1)})

blocked -= {sensor[2] for sensor in sensors if sensor[1]==y or sensor[3]==y} # Remove actual beacon/sensor positions that block the line
print(len(blocked))