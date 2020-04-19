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
    
    def addGridNode(self, val, x, y):
        nodeToAdd = GridNode(val, x, y)
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

def matthattenDistance(nodeOne, nodeTwo):
    return abs(nodeOne.x - nodeTwo.x) + abs(nodeOne.y - nodeTwo.y)


def calcHeuristic(gridGraph, start):
    heuristicSet = {}
    for gridNode in gridGraph.nodes:
        aproximateDist = matthattenDistance(start, gridNode)
        heuristicSet[gridNode.val] = aproximateDist

    return heuristicSet


#innefficient


def astar(gridGraph, src, dest):
    print("a star")
    approxDist = calcHeuristic(gridGraph, src)
    actualDistances = {}
    astar = {}

    for node in gridGraph.getAllNodes():
        actualDistances[node] = None #problematic i know

    originNode = GridNode("origin", 0, 0)
    finalized = []
    aproxOrginDist = matthattenDistance(originNode, src)

    curr = originNode #not sure about this

    gPlusH = {}

    while curr != dest:
        finalized.append(curr)

        for neighbor in curr:
            #update distances
            if neighbor not in curr:
                #TODO: fix this
                if approxDist[neighbor] < actualDistances[curr]: 
                    actualDistances[neighbor] = approxDist[curr] + actualDistances[neighbor]
                approxDist[neighbor] = matthattenDistance(curr, neighbor)

            #TODO: set curr to the next min node g[curr] + h[node] not yet finalized

        for node in gridGraph.getAllNodes():
            if node in gPlusH and node in finalized:
                del gPlusH[node]
            else:
                gPlusH[node] = actualDistances[node] + approxDist[node]
        
        curr = min(gPlusH)
    
    return actualDistances[dest]
