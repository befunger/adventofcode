with open("2022\Day 13\input.txt", "r") as file:
    inp = [pair.split('\n') for pair in file.read().split('\n\n')]

'''Returns True if ordered, False if not, None if inconclusive.'''
def compareArr(left, right):
    # Both ints
    if type(left) is int and type(right) is int:
        return left < right if left != right else None
    
    # Compare lists index-wise
    elif type(left) is list and type(right) is list:
        for i in range(min(len(left), len(right))):
            res = compareArr(left[i], right[i])
            if not res is None:
                return res
        #  If lists are differing length, return true/false if left is smaller/larger
        return len(left) < len(right) if len(left) != len(right) else None

    else:
        left = [left] if type(left) is int else left
        right = [right] if type(right) is int else right
        return compareArr(left, right)
    
# Part 1: Recursive list comparator
index_sum = 0
for i, [left, right] in enumerate(inp):
    # Fuck it, unsafe exec() usage
    exec("left =" + left)
    exec("right =" + right)
    if compareArr(left, right):
        index_sum += i+1 # AoC wants 1-indexing
print(index_sum)


# Test recursive logic of compareArr
assert(compareArr([1, 1, 3, 1, 1], [1, 1, 5, 1, 1]))
assert(compareArr([[1],[2,3,4]], [[1],4]))
assert(not compareArr([9], [[8,7,6]]))
assert(compareArr([[4,4],4,4], [[4,4],4,4,4]))
assert(not compareArr([7,7,7,7], [7,7,7]))
assert(compareArr([], [3]))
assert(not compareArr([[[]]], [[]]))
assert(not compareArr([1,[2,[3,[4,[5,6,7]]]],8,9], [1,[2,[3,[4,[5,6,0]]]],8,9]))