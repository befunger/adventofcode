with open("2022\Day 7\input.txt", "r") as file:
    lines = [line.strip('\n').split(' ') for line in file.readlines()]

'''Node class for directory datapoints'''
class Node:
    def __init__(self, parent, name, value=0):
        self.parent = parent
        self.name = name
        self.value = value
        self.children = {}

'''Directory class for storing full directory.'''
class Directory:
    def __init__(self):
        self.root = Node(None, '/', 0)
        self.current = self.root

    # Update current to '/', dir above, or dir below. Create new dir if needed.
    def cd(self, name):
        if name == '/':
            self.current = self.root
        elif name == '..':
            self.current = self.current.parent
        else: 
            if not name in self.current.children:
                new_child = Node(self.current, name) 
                self.current.children[name] = new_child
            self.current = self.current.children[name]
        return self.current
    
    # Adds new discovered file/dir and updates values
    def ls(self, name, size):
        # Don't add value to files, only necessary for updating directory sizes
        self.current.children[name] = Node(self.current, name, 0)
        self._updateValues(self.current, size)

    # Update node values recursively for parents
    def _updateValues(self, node, value):
        node.value += value
        if not node.parent is None:
            self._updateValues(node.parent, value)

    # Print whole directory with basic formatting
    def printDirectory(self, node=None, prefix=''):
        if node is None:
            node = self.root

        print(prefix + node.name, node.value)
        for child in node.children.values():
            self.printDirectory(child, prefix+' ')

    # Gets sum of directories of size smaller than threshold
    def getSumOfSmallest(self, threshold, node=None):
        if node is None:
            node = self.root
        tot = 0 if node.value > threshold else node.value
        for child in node.children.values():
            tot += self.getSumOfSmallest(threshold, child)
        return tot

    # Finds smallest directory that is larger than threshold
    def findSmallestOfSize(self, threshold, node=None):
        if node is None:
            node = self.root
        if node.value < threshold:
            return 1e100 # Dumb big value
        else:
            return min([node.value]+[self.findSmallestOfSize(threshold, child) for child in node.children.values()])


# Process input into directory object
dir = Directory()
last_cmd = None
for line in lines:
    if line[0] == '$' and line[1] == 'cd':
        dir.cd(line[2])
    elif line[0] != '$':
        dir.ls(line[1], 0 if line[0] == 'dir' else int(line[0]))

# Part 1
print(dir.getSumOfSmallest(threshold=1e5))

# Part 2
space_needed = 3e7 - (7e7 - dir.root.value)
print(dir.findSmallestOfSize(space_needed))