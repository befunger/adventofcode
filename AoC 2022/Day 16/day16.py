'''
INFO: 
Release as much pressure as possible in 30 minutes.
- It takes 1 minute to move to an adjacent room
- It takes 1 minute to open a valve
- Each valve releases the specified pressure EVERY MINUTE after opening (Open high flow ones earlier)

Ways to prune for brute force search (No pruning gives approx 3^30 = 2e14 end states)
Prune 1: Set all 0-valves to open so we don't bother with them (set to open in initialisation)
Prune 2: Disallow double back after walking (accomplishes nothing but wasting 2 mins)
    

IDEAS:
1. Remove zero flow points and link their "neighbours together with a travel distance of 2 minutes (weighted graph)
2. Convert into TSP-like structure. Instead of actions being "walk to adjacent" or "open" let possible actions be "go to unopened valve and open it" with whatever associated cost that has.
'''

import re
import time
from collections import deque
from collections import defaultdict

'''Turn input into a list of Valve objects'''
def parseInput(filename, dist_matrix=False):
    with open(filename, "r") as file:
        # lines = [line.strip("\n") for line in file.readlines()]
        # Keep all capital letters or digits (excluse the capital V at start of each line)
        lines = [re.findall('[A-Z]+|\d+', line[1:]) for line in file.readlines()]

    # Dict with name-flow pairs
    flows = {name:int(flow) for name,flow,*_ in lines}
    # Dict with name-state pairs for whether valve is open or closed (We set flow-0 ones to open so we cant open them later)
    states = {name:int(flow)==0 for name,flow,*_ in lines}

    
    # Make graph
    graph = {name:[{'name':neighbour, 'weight':1} for neighbour in neighbours] for name,_,*neighbours in lines}
    # Contract zero-valve points
    contractGraph(graph, flows, states)
    
    if dist_matrix:
        graph = bfs_distance_matrix(graph)

    return graph, flows, states


'''Removes all 0-flow nodes by binding all their neighbours together with an edge weight increase'''
def contractGraph(graph, flows, states):
    # print(graph)
    contracted = []
    for node in flows:
        # Keep 'AA' since it's the starting position.
        if flows[node] == 0 and node != 'AA':
            # print(f'Contracting {node}.')
            # Link up neighbours
            for i,neighbour1 in enumerate(graph[node]):
                for neighbour2 in graph[node][i+1:]:
                    n1, n2 = neighbour1['name'], neighbour2['name']
                    w1, w2 = neighbour1['weight'], neighbour2['weight']
                    # Add neighbours to each other
                    graph[n1].append({'name':n2, 'weight':w1+w2})
                    graph[n2].append({'name':n1, 'weight':w1+w2})
                    # Remove links to inbetween node
                    graph[n1].remove({'name':node, 'weight':w1})
                    graph[n2].remove({'name':node, 'weight':w2})
            contracted.append(node)

    # Delete contracted node from all records
    for node in contracted:
        del graph[node], flows[node], states[node]

'''Makes distance matrix by using BFS between points. Stored as dict of dicts. dist[point1][point2] gives shortest cost between the two'''
def bfs_distance_matrix(graph):
    num_nodes = len(graph)
    distance_matrix = [[float('inf')] * num_nodes for _ in range(num_nodes)]

    for i, start_node in graph.keys():
        visited = [False] * num_nodes
        visited[i] = True
        queue = deque([(start_node, 0)])  # (node, distance)

        while queue:
            current_node, current_distance = queue.popleft()
            distance_matrix[start_node][current_node] = current_distance

            for neighbor_info in graph[current_node]:
                neighbor = neighbor_info['name']
                edge_weight = neighbor_info['weight']
                neighbor_idx = ord(neighbor) - ord('A')  # Convert neighbor name to index

                if not visited[neighbor_idx]:
                    visited[neighbor_idx] = True
                    queue.append((neighbor_idx, current_distance + edge_weight))

    return distance_matrix

'''Counter function to check number of makeMove() calls'''
def counter():
    counter.counter += 1
counter.counter = 0


'''Performs a move and recursively returns the max flow given best future moves'''
def makeMove(minsLeft, pos, graph, flows, states, prevRoom="None"):
    counter()
    # A minute passes
    if minsLeft == 0:
        return 0
        
    # Append the best result from each possible move
    possibleFlows = []
    
    # Open valve in current room if not open
    if not states[pos]:
        # Copy states to not mess with other branches (shallow copy is enough since all keys/values are strings and integers)
        newStates = states.copy()
        newStates[pos] = True
        # flows[pos] * (minsLeft-1) pre-calculates the total flow from an opened valve instead of calculating flow of all open valves at every minute
        possibleFlows.append(flows[pos] * (minsLeft-1) + makeMove(minsLeft-1, pos, graph, flows, newStates)) 
    
    # Move to all adjacent rooms if we did not come from there
    for adjacent in graph[pos]:
        # Don't go back to the exact same place we came from, and don't go further than possible in minsLeft
        if adjacent['name'] != prevRoom and minsLeft >= adjacent['weight']: 
            # Decrease time by the edge weight of the moved path
            possibleFlows.append(makeMove(minsLeft-adjacent['weight'], adjacent['name'], graph, flows, states, prevRoom=pos))

    # If no valid moves exist or all valves are open, the outcome will never change.
    if len(possibleFlows) == 0 or not False in states.values():
        return 0
    else: # Return the maximum yield from subsequent moves
        return max(possibleFlows)
    
   
'''Only considers 'composite moves', which consist of moving to an open valve and closing it'''
def makeCompositeMove(minsLeft, pos, distances, flows, states):
    counter()
    # A minute passes
    if minsLeft == 0 or not False in states.values():
        return 0
        
    # Append the best result from each possible move
    possibleFlows = []

    for room in [name for name,state in states.items() if not state]:
        # Time left after moving and opening valve (-1 for opening valve)
        timeLeft = minsLeft - distances[pos][room] - 1
        if timeLeft > 0: # Maybe >=
            # print(f'Move from {pos} to {room} reduces time from {minsLeft} to {timeLeft} and gains {flows[room]}*{timeLeft}={flows[room]*timeLeft} flow')
            newStates = states.copy()
            newStates[room] = True
            possibleFlows.append(flows[room] * timeLeft + makeCompositeMove(timeLeft, room, distances, flows, states))
        
    
    if len(possibleFlows) == 0: # No valve reachable in remaining time
        return 0
    else: # Return the maximum yield from possible moves
        return max(possibleFlows)



    
def bfs(graph, start):
    visited, queue = set(), deque([start])
    distances = defaultdict(int)
    while queue:
        vertex = queue.popleft()
        for neighbor in graph[vertex]:
            if neighbor['name'] not in visited:
                visited.add(neighbor['name'])
                queue.append(neighbor['name'])
                distances[neighbor['name']] = distances[vertex] + neighbor['weight']
    return distances



def part1(filename):
    graph, flows, states = parseInput(filename)
    print("Part 1:", makeMove(3, 'AA', graph, flows, states))
    print(f'{counter.counter} calls')

def part2(filename):
    print("Part 2:")
    # graph, flows, states = parseInput(filename)

def part1new(filename):
    graph, flows, states = parseInput(filename)
    distance_matrix = {}
    for node in graph:
        distance_matrix[node] = bfs(graph, node)
    
    # [print(name, node) for name, node in distance_matrix.items()]
    print("Part 1:", makeCompositeMove(30, 'AA', distance_matrix, flows, states))
    print(f'{counter.counter} calls')


# start_time = time.time()
# part1("2022\Day 16\input.txt")
# print(f"{time.time() - start_time} seconds elapsed.")

part1new("2022\Day 16\small.txt")


# start_time2 = time.time()
# part2("2022\Day 16\small.txt")
# print(f"{time.time() - start_time2} seconds elapsed.")

# Part 1: 421.8832404613495 seconds (Prune 1 and 2)
# Part 1  353.96296739578247 seconds (Contract graph)

# Part 2: TBD