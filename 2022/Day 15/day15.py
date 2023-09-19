import re
import time
with open("2022\Day 15\input.txt", "r") as file:
    sensors = [[int(num) for num in re.findall(r'[-+]?\d+', text)] for text in file.readlines()]

'''Returns manhattan distance'''
def manhattan(sensor):
    return abs(sensor[0]-sensor[2]) + abs(sensor[1] - sensor[3]) 

'''Returns the perimeter of a sensors beacon range (all points 1 manhattan distance beyond the closest beacon)'''
def perimeter(sensor):
    dist = manhattan(sensor) + 1
    x, y = sensor[0], sensor[1]
    all = set({(x+i, y+j) for i in range(-dist, dist+1) for j in [abs(dist)-abs(i), abs(i)-abs(dist)]}) 
    return set({point for point in all if point[0] >= 0 and point[0] <= 4000000 and point[1] >= 0 and point[1] <= 4000000})

'''Iterates all sensors in range of the y-line and blocks all spaces within their range. Removes actual beacon/sensor positions as these do not count.'''
def part1(filename):
    with open(filename, "r") as file:
        sensors = [[int(num) for num in re.findall(r'[-+]?\d+', text)] for text in file.readlines()]
    y = 2000000
    blocked = set()
    for sensor in sensors:
        offset = manhattan(sensor) - abs(y-sensor[1]) # Distance to beacon minus distance to line in question
        if offset >= 0:
            blocked = blocked.union({i for i in range(sensor[0]-offset, sensor[0]+offset+1)})
    blocked -= {sensor[2] for sensor in sensors if sensor[1]==y or sensor[3]==y} # Remove actual beacon/sensor positions that block the line
    print("Part 1:", len(blocked))

'''Brute-force through all the perimeter locations of each sensor which are within 0 < x,y < 4e6 and return the first outside of all sensors ranges.
    We know that the correct spot must lie right outside a perimeter due to there only being a single correct solution.'''
def part2(filename):
    with open(filename, "r") as file:
        sensors = [[int(num) for num in re.findall(r'[-+]?\d+', text)] for text in file.readlines()]

    print("Checking", len(sensors), "sensors")
    for i, sensorToCheck in enumerate(sensors):
        # Get perimeter points
        print("Checking sensor", i)
        candidatePoints = perimeter(sensorToCheck)
        for point in candidatePoints:
            offsets = [manhattan(sensor) - (abs(point[0] - sensor[0]) + abs(point[1] - sensor[1])) for sensor in sensors]
            if max(offsets) < 0:
                print(point)
                print("Part 2:", 4000000*point[0]+point[1])
                return

start_time = time.time()
part1("2022\Day 15\input.txt")
print(f"{time.time() - start_time} seconds elapsed.")
start_time2 = time.time()
part2("2022\Day 15\input.txt")
print(f"{time.time() - start_time2} seconds elapsed.")


# 1.7 seconds for part 1
# 379 seconds for part 2