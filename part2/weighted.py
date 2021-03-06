import random
class WeightedNode:
    def __init__(self, value):
        self.val = value
        self.edges = {}

class WeightedGraph:
    def __init__(self):
        self.nodes = set()
    
    def addNode(self, nodeToAdd):
        self.nodes.add(nodeToAdd)

    def addUndirectedEdge(self, nodeOne, nodeTwo, weight):
        if nodeOne not in self.nodes or nodeTwo not in self.nodes:
            pass
        nodeOne.edges[nodeTwo] = weight
        nodeTwo.edges[nodeOne] = weight

    def removeUndirectedEdge(self, nodeOne, nodeTwo):
        if nodeOne not in self.nodes or nodeTwo not in self.nodes:
            pass
        if nodeTwo in nodeOne.edges:
            del nodeOne.edges[nodeTwo]
        if nodeOne in nodeTwo.edges:
            del nodeTwo.edges[nodeOne]

    def getAllNodes(self):
        return self.nodes

def createLinkedList(n):
    linkedList = WeightedGraph()

    prev = None
    for i in range(n):
        curr = WeightedNode(i)
        linkedList.addNode(curr)

        if prev != None:
            linkedList.addUndirectedEdge(curr, prev, 1)
            prev = curr

    return linkedList

def createRandomCompleteGraph(n):
    randomGraph = WeightedGraph()

    for i in range(n):
        randomGraph.addNode(WeightedNode(n))
        
    for node1 in randomGraph.nodes:
        for node2 in randomGraph.nodes:
            if node1 != node2:
                randWeight = random.randint(1, n)
                randomGraph.addUndirectedEdge(node1, node2, randWeight)
    return randomGraph

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

    #so i can actually understand the graph          
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

rando = createRandomCompleteGraph(10)
print(rando.nodes)

link = createLinkedList(20)
print(link.nodes)