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

    for x in range(n):
        print("boop")
        for y in range(n):
            randomVal = 3000 * random.randint(0, n)
            gridNodeToAdd = GridNode(randomVal, x, y)
            randomGraph.addGridNode(gridNodeToAdd)

    for node1 in randomGraph.nodes:
        for node2 in randomGraph.nodes:
            if node1 != node2:
                chance = random.randint(0, 1000)
                if len(node1.neighbors) < 4:
                    if node1.neighborCheck(node2) and chance%2 == 0:
                        print("hi")
                        randomGraph.addUndirectedEdge(node1, node2)
                else:
                    break
                    #     # print("added")
                    # else:
                    #     print("not added")
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
        # print(curr.x, curr.y, curr.neighbors)
        if curr == dest or curr == None: 
            break

        visted.add(curr)
        for neighbor in curr.neighbors:
            if neighbor not in visted:
                if neighbor not in distances or distances[neighbor] > distances[curr] + matthattenDistance(neighbor, dest):
                    distances[neighbor] = distances[curr] + matthattenDistance(neighbor, dest)
        
        curr = None
        maxNode = float('inf')
        for node in distances.keys():
            if node not in visted or distances[node] < maxNode:
                curr = node
                maxNode = distances[curr]
                print(node, node.neighbors, maxNode)
        
        # validPathCheck = 0
        # if curr != None:
        #     for neighbor in curr.neighbors:
        #         if neighbor in visted:
        #             validPathCheck += 1
        
        #     if validPathCheck == 4:
        #         break
        # print("im not crazy", validPathCheck)
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
mainGraph.addUndirectedEdge(nodeSix, nodeEight)
mainGraph.addUndirectedEdge(nodeThree, nodeTwo)
mainGraph.addUndirectedEdge(nodeFive, nodeSix)

rando = createRandomGridGraph(100)

print(astar(mainGraph, nodeOne, nodeThree))
print(nodeOne.neighbors)

# print(rando.nodes)

# startAndEnd = rando.getFirstAndLast(0, 99)


# print(startAndEnd[0].x, startAndEnd[0].y)
# print(startAndEnd[1].x, startAndEnd[1].y) 

# first ended up being last and last ended up being first

# print(astar(rando, startAndEnd[1], startAndEnd[0]))

for node in rando.nodes:
    print(node, node.neighbors)
