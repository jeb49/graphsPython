import random

class GridNode:
    def __init__(self, val, xCoor, yCoor):
        self.val = val #node val can be theoretically be anything
        self.x = xCoor
        self.y = yCoor
        self.neighbors = set()
    
    def neighborCheck(self, nodeToCheck):
        xDiff = abs(self.x - nodeToCheck.x)
        yDiff = abs(self.y - nodeToCheck.y)

        if xDiff >= 1 and yDiff >= 1:
            return False
        else:
            return True

class GridGraph:
    def __init__(self):
        self.nodes = set()
    
    def addGridNode(self, nodeToAdd):
        self.nodes.add(nodeToAdd)
    
    def addUndirectedEdge(self, first, second):
        nodeCheckFirst = first.neighborCheck(second)
        nodeCheckSecond = second.neighborCheck(first)

        if nodeCheckFirst and len(first.neighbors) < 4:
            first.neighbors.add(second)
        if nodeCheckSecond and len(second.neighbors) < 4:
            second.neighbors.add(first)
    
    def removeUndirectedEdge(self, first, second):
        if second in first.neighbors:
            first.neighbors.remove(second)
        if first in second.neighbors:
            second.neighbors.remove(first)
    
    def getAllNodes(self):
        return self.nodes

    def getFirstAndLast(self, start, end):
        returnArr = []
        for node in self.nodes:
            if node.x ==  start and node.y == start:
                returnArr.append(node)
            if node.x == end and node.y == end:
                returnArr.append(node)

        return returnArr


"""
    returns the matthaten distance between two nodes
"""
def matthattenDistance(nodeOne, nodeTwo):
    return abs(nodeOne.x - nodeTwo.x) + abs(nodeOne.y - nodeTwo.y)

"""
    creates a random grid graph
"""

def createRandomGridGraph(n):
    randomGraph = GridGraph()
    matrix = [[0] * n for i in range(n)] #yes this causes more space, but i dont know what else to do at this point lol

    for x in range(n):
        print("boop")
        for y in range(n):
            randomVal = 3000 * random.randint(0, n)
            gridNodeToAdd = GridNode(randomVal, x, y)
            matrix[x][y] = gridNodeToAdd
            randomGraph.addGridNode(matrix[x][y])
            

    for node in randomGraph.nodes:
        xR = node.x + 1
        xL = node.x - 1
        yU = node.y + 1
        yD = node.y - 1

        upChance = random.randint(0,10)
        downChance = random.randint(0,10)
        leftChance = random.randint(0, 10)
        rightChance = random.randint(0, 10)

        if yU < n:
            if upChance % 2 == 0 and matrix[node.x][yU] not in node.neighbors:
                randomGraph.addUndirectedEdge(node, matrix[node.x][yU])
        if yD > 0:
            if downChance % 2 == 0 and matrix[node.x][yD] not in node.neighbors:
                randomGraph.addUndirectedEdge(node, matrix[node.x][yD])
        if xL > 0:
            if leftChance % 2 == 0 and matrix[xL][node.y] not in node.neighbors:
                randomGraph.addUndirectedEdge(node, matrix[xL][node.y])
        if xR < n:
            if rightChance % 2 == 0 and matrix[xR][node.y] not in node.neighbors:
                randomGraph.addUndirectedEdge(node, matrix[xR][node.y])

    return randomGraph
                    
"""
    returns the optimal path from a source node to it destination
"""

def astar(gridGraph, src, dest):
    distances = {}
    distances[src] = 0
    visted = set()
    path = []

    curr = src
    while curr != dest or curr != None:
        #this if statement stopped my infinite loop lol and idk why this works
        if curr == dest or curr == None: 
            break

        visted.add(curr)
        for neighbor in curr.neighbors:
            if neighbor not in visted:
                if neighbor not in distances or distances[neighbor] > distances[curr] + matthattenDistance(neighbor, dest):
                    distances[neighbor] = distances[curr] + matthattenDistance(curr, neighbor) 
        
        curr = None
        maxNode = float('inf')
        for node in distances.keys():
            if node not in visted or distances[node] < maxNode:
                curr = node
                maxNode = distances[curr]

        print(curr.val, dest.val, curr.x, curr.y)


        # for a in visted:
        #     print(a.val)

    actualDist = {} #so apparently python dictionaries are insertion ordered as of 3.6... but im going to return an ordered list anyways
    for key in distances.keys():
        path.append(key.val)
        actualDist[key.val] = distances[key]
    
    print(actualDist)    #so i can visually represent the distances
    return path

mainGraph = GridGraph()

nodeOne = GridNode(1, 0, 0)
nodeTwo = GridNode(2, 0, 1)
nodeThree = GridNode(3, 1, 1)
nodeFour = GridNode(4, 1, 0)
nodeFive = GridNode(5, 1, 2)
nodeSix = GridNode(6, 2, 1)
nodeSeven = GridNode(7, 1, 3)
nodeEight = GridNode(8, 2, 2)

mainGraph.addGridNode(nodeOne)
mainGraph.addGridNode(nodeTwo)
mainGraph.addGridNode(nodeThree)
mainGraph.addGridNode(nodeFour)
mainGraph.addGridNode(nodeFive)
mainGraph.addGridNode(nodeSix)
mainGraph.addGridNode(nodeSeven)
mainGraph.addGridNode(nodeEight)

mainGraph.addUndirectedEdge(nodeOne, nodeFour)
mainGraph.addUndirectedEdge(nodeOne, nodeTwo)
mainGraph.addUndirectedEdge(nodeThree, nodeTwo)
mainGraph.addUndirectedEdge(nodeSix, nodeEight)
mainGraph.addUndirectedEdge(nodeFive, nodeSix)

rando = createRandomGridGraph(100)

print(astar(mainGraph, nodeOne, nodeThree))
# result i get {1: 0, 4: 1, 2: 1, 3: 1}, [1, 4, 2, 3]

print(nodeOne.neighbors)

# print(rando.nodes)

startAndEnd = rando.getFirstAndLast(0, 99)


print(startAndEnd[0].x, startAndEnd[0].y)
print(startAndEnd[1].x, startAndEnd[1].y) 

# first ended up being last and last ended up being first
print(astar(rando, startAndEnd[1], startAndEnd[0]))
