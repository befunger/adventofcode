# Parse input
with open("2022\Day 11\input.txt", "r") as file:
    inp = [monkey.split('\n') for monkey in file.read().split('\n\n')]

monkeys = []
for line in inp:
    monkey = {'inspected' : 0,
              'items' : [int(num) for num in line[1].strip('  Starting items: ').split(', ')],
              'test' : int(line[3].split(' ')[-1]),
              'true' : int(line[4][-1]),
              'false' : int(line[5][-1])}
    # Set worry function
    op, val = line[2].split(' ')[-2], line[2].split(' ')[-1]
    if val == 'old':
        monkey['worry'] = lambda worry_level: worry_level * worry_level
    elif op == '*':
        monkey['worry'] = lambda worry_level, C=int(val): worry_level * C
    else:
        monkey['worry'] = lambda worry_level, C=int(val): worry_level + C

    monkeys.append(monkey)


# Part 2 setup
prod_of_tests = 1
for monkey in monkeys:
    prod_of_tests *= monkey['test']


for n in range(10000):
    for i, monkey in enumerate(monkeys):
        for item in monkey['items']:
            # Monkey inspects item (worry function)
            item = monkey['worry'](item)
            monkey['inspected'] += 1
            
            # Part 1: Divide by 3 and round down
            # item = int(item/3)
            
            # Part 2: Modulo by product of all test-values (Could optimise by using Least Common Multiple)
            item = item % prod_of_tests

            if item % monkey['test']:
                monkeys[monkey['false']]['items'].append(item)
            else:
                monkeys[monkey['true']]['items'].append(item)
        
        monkey['items'] = [] # Empty this monkeys item list

# Find 2 most active monkeys
activities = sorted([monkey['inspected'] for monkey in monkeys])
print(activities[-1]*activities[-2])


