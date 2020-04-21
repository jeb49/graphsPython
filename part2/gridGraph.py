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
        heuristicSet[gridNode.val] = aproximateDist

    return heuristicSet


def astar(gridGraph, src, dest):
    approxDist = calcHeuristic(gridGraph, src)
    actualDistances = {}
    astar = {}

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

        for node in gridGraph.getAllNodes():
            if node in gPlusH and node in finalized:
                del gPlusH[node]
            elif node in actualDistances and node in approxDist:
                gPlusH[node] = actualDistances[node] + approxDist[node]
        
        curr = min(gPlusH)
    
    return actualDistances[dest]
