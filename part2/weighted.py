class WeightedNode:
    def __init__(self, value):
        self.val = value
        self.edges = {}

class WeightedGraph:
    def __init__(self):
        self.edges = {}
        self.nodes = set()
    
    def addNode(self, nodeToAdd):
        self.nodes.add(nodeToAdd)

    def addUndirectedEdge(self, nodeOne, nodeTwo, weight):
        nodeOne.edges[nodeTwo] = weight
        nodeTwo.edges[nodeOne] = weight

    def removeUndirectedEdge(self, nodeOne, nodeTwo):
        if nodeTwo in nodeOne.edges:
            del nodeOne.edges[nodeTwo]
        if nodeOne in nodeTwo.edges:
            del nodeTwo.edges[nodeOne]

    def getAllNodes(self):
        return self.nodes

def dijkstra(graph, start):
    distances = {}
    visitedArr = []
    distances[start] = 0
    curr = start

    while curr != None and curr in distances:
        visitedArr.append(curr)
        for neighbor in curr.edges:
            if neighbor in visitedArr:
                continue

            currDistance = curr.edges[neighbor] + distances[curr]
            
            if neighbor not in distances:
                distances[neighbor] = currDistance
            elif currDistance < distances[neighbor]:
                distances[neighbor] = currDistance

        
        curr =  None

        for node in distances:
            if node in visitedArr:
                continue
            elif curr == None:
                curr = node
            elif distances[node] < distances[curr]:
                curr = node

    #so i can actually understand           
    newMap = {}
    for el in distances:
        newMap[el.val] = distances[el]

    return newMap

print("adding nodes")
mainGraph = WeightedGraph()

nodeOne = WeightedNode(1)
nodeTwo = WeightedNode(2)
nodeThree = WeightedNode(3)
nodeFour = WeightedNode(4)
nodeFive = WeightedNode(5)
nodeSix = WeightedNode(6)
nodeSeven = WeightedNode(7)
nodeEight = WeightedNode(8)

mainGraph.addNode(nodeOne)
mainGraph.addNode(nodeTwo)
mainGraph.addNode(nodeThree)
mainGraph.addNode(nodeFour)
mainGraph.addNode(nodeFive)
mainGraph.addNode(nodeSix)
mainGraph.addNode(nodeSeven)
mainGraph.addNode(nodeEight)

mainGraph.addUndirectedEdge(nodeOne, nodeEight, 8)
mainGraph.addUndirectedEdge(nodeFive, nodeEight, 4)
mainGraph.addUndirectedEdge(nodeThree, nodeSeven, 6)
mainGraph.addUndirectedEdge(nodeOne, nodeThree, 2)


print(dijkstra(mainGraph, nodeOne))
# print(mainGraph.nodes)