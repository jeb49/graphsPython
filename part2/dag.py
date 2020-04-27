import random
class DirectedGraph:
    def __init__(self):
        self.nodes = set()
        self.edges = {}
    
    def addNode(self, nodeToAdd):
        self.nodes.add(nodeToAdd)
        self.edges[nodeToAdd] = set()

    def addDirectedEdge(self, nodeOne, nodeTwo):
        self.edges[nodeOne].add(nodeTwo)

    def removeDirectedEdge(self, nodeOne, nodeTwo):
        if nodeTwo in self.edges[nodeOne]:
            self.edges[nodeOne].remove(nodeTwo)

    def getAllNodes(self):
        return self.nodes

"""
    random graph
"""

def createRandomGraphDagIter(n):
    randomGraph = DirectedGraph()
    added = []
    for i in range(n):
        randInt = random.randint(0, n) * 1000
        randomGraph.addNode(randInt)
        chance = random.randint(0, 10)

        if chance%2 == 0 and len(added) != 0:          
            indexToAdd = random.randint(0, len(added) - 1)
            randomGraph.addDirectedEdge(randInt, added[indexToAdd])

        added.append(randInt)
    
    return randomGraph

"""
    khans algorithim
"""
def khans(g):
    inDegreeMap = {}
    arr = []
    q =[]

    #add all elements of M whose values are 0 to Q
    for vertex in g.edges:
        inDegreeMap[vertex] = 0
        for neighbor in g.edges[vertex]:
            if neighbor not in inDegreeMap.keys():
                inDegreeMap[neighbor] = 1
            else:
                inDegreeMap[neighbor] += 1

    for node in g.nodes:
        if inDegreeMap[node] == 0:
            q.append(node)

    while len(q) != 0:
        curr = q[0]
        q.pop(0)
        arr.append(curr)

        #decrement the in-degrees of all dependents of curr
        for edge in g.edges[curr]:
            inDegreeMap[edge] -= 1

        #decrement the in-degree of curr to -1 (to avoid adding it back to Q)
        inDegreeMap[curr] = -1

        for neighbor in g.edges[curr]:
            if inDegreeMap[neighbor] == 0:
                q.append(neighbor)

    return arr

"""
    modified dfs algorithim
"""

def mDFSHelper( graph, vert, vistedArr, stack):
    vistedArr.append(vert)
    for neigh in graph.edges[vert]:
        if neigh not in vistedArr:
            mDFSHelper(graph, neigh, vistedArr, stack)
    stack.append(vert)

def mDFS( g):
    stack = []
    vistedArr = []
    for vertex in g.edges:
        if vertex not in vistedArr:
            mDFSHelper(g, vertex, vistedArr, stack)
    #output all nodes in stack order
    return vistedArr


    

mainGraph = DirectedGraph()
mainGraph.addNode(1)
mainGraph.addNode(2)
mainGraph.addNode(4)
mainGraph.addNode(5)
mainGraph.addNode(7)
mainGraph.addNode(8)
mainGraph.addNode(12)
mainGraph.addNode(44)
mainGraph.addNode(21)
mainGraph.addNode(49)
mainGraph.addNode(401)

mainGraph.addDirectedEdge(1,2)
print(mainGraph.getAllNodes())
print(mainGraph.edges)
mainGraph.removeDirectedEdge(1,2)
print(mainGraph.edges)
mainGraph.addDirectedEdge(1,7)
mainGraph.addDirectedEdge(401,7)
mainGraph.addDirectedEdge(1,8)
print(mainGraph.edges)

print(khans(mainGraph))
print(mDFS(mainGraph))

rando = createRandomGraphDagIter(100)
print(rando.nodes) #confirm it works

print(mDFS(rando))

