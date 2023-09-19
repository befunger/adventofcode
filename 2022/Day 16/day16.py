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

'''Turn input into a list of Valve objects'''
def parseInput(filename, contract=True):
    with open(filename, "r") as file:
        # lines = [line.strip("\n") for line in file.readlines()]
        # Keep all capital letters or digits (excluse the capital V at start of each line)
        lines = [re.findall('[A-Z]+|\d+', line[1:]) for line in file.readlines()]

    # Dict with name-flow pairs
    flows = {name:int(flow) for name,flow,*_ in lines}
    # Dict with name-state pairs for whether valve is open or closed (We set flow-0 ones to open so we cant open them later)
    states = {name:int(flow)==0 for name,flow,*_ in lines}


    graph = {name:[{'name':neighbour, 'weight':1} for neighbour in neighbours] for name,_,*neighbours in lines}
    if contract:
        # Contract zero-valve points
        graph = contractGraph(graph, flows, states)
    
    return graph, flows, states
'''
     CC
     |
BB - AA - DD   Contract AA: Link BB to CC,DD,EE.
     |
     EE
'''


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

    return graph

def myfunction():
    myfunction.counter += 1
myfunction.counter = 0

'''Performs a move and recursively returns the max flow given best future moves'''
def makeMove(minsLeft, pos, graph, flows, states, prevRoom="None"):
    myfunction()
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
    
   
    



def part1(filename):
    graph, flows, states = parseInput(filename)
    print("Part 1:", makeMove(30, 'AA', graph, flows, states))
    print(f'{myfunction.counter} calls')

def part2(filename):
    print("Part 2:")
    # graph, flows, states = parseInput(filename)
    

start_time = time.time()
part1("2022\Day 16\input.txt")
print(f"{time.time() - start_time} seconds elapsed.")