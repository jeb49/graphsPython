class GridNode:
    def __init__(self, val, xCoor, yCoor):
        self.val = val
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

        if nodeCheckFirst and len(first.neighbors) > 4:
            first.neighbors.add(second)
        if nodeCheckSecond and len(second.neighbors) > 4:
            second.neighbors.add(first)
    
    def removeUndirectedEdge(self, first, second):
        if second in first.neighbors:
            first.neighbors.remove(second)
        if first in second.neighbors:
            second.neighbors.remove(first)
    
    def getAllNodes(self):
        return self.nodes

"""
    returns the matthaten distance between two nodes
"""
def matthattenDistance(nodeOne, nodeTwo):
    return abs(nodeOne.x - nodeTwo.x) + abs(nodeOne.y - nodeTwo.y)

"""
    calculates the heuristic of the graph given a node
"""
def calcHeuristic(gridGraph, start):
    heuristicSet = {}

    for gridNode in gridGraph.nodes:
        aproximateDist = matthattenDistance(start, gridNode)
        heuristicSet[gridNode] = aproximateDist

    return heuristicSet


def astar(gridGraph, src, dest):
    approxDist = calcHeuristic(gridGraph, src)
    actualDistances = {}
    astar = {}
    gPlusH = {}
    finalized = []

    curr = src
    actualDistances[curr] = 0
    
    while curr != dest or curr != None:
        finalized.append(curr)

        for neighbor in curr.neighbors:
            #update distances
            if neighbor not in finalized:
                if approxDist[neighbor] < actualDistances[curr]: 
                    actualDistances[neighbor] = approxDist[curr] + actualDistances[neighbor]
                actualDistances[neighbor] = matthattenDistance(curr, neighbor)

        curr = None
        for node in approxDist:
            if node in finalized:
                continue
            elif node in actualDistances and node in approxDist:
                gPlusH[node] = actualDistances[node] + approxDist[node]

        print(actualDistances)
        print(approxDist)
        print(gPlusH)
        curr = min(gPlusH)
    
    return actualDistances[dest]

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

astar(mainGraph, nodeOne, nodeThree)