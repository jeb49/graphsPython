class DirectedGraph:
    def __init__(self):
        self.nodes = set()
        self.edges = {}
    
    def addNode(self, nodeToAdd):
        self.nodes.add(nodeToAdd)
        self.edges[nodeToAdd] = []

    def addUndirectedEdge(self, nodeOne, nodeTwo):
        if nodeTwo not in self.edges[nodeOne]:
            self.edges[nodeOne].append(nodeTwo)


    def removeUndirectedEdge(self, nodeOne, nodeTwo):
        if nodeTwo in self.edges[nodeOne]:
            self.edges[nodeOne].remove(nodeTwo)

    def getAllNodes(self):
        return self.nodes

def khans(g):
    inDegreeMap = {}

    for vertex in g.edges:
        for neighbor in g.edges[vertex]:
            if neighbor not in inDegreeMap.keys():
                inDegreeMap[neighbor] = 1
            else:
                inDegreeMap[neighbor] += 1

    arr = []
    q =[]

    for edge in inDegreeMap:
        q.append(edge)

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

def mDFS(g):
    stack = []
    vistedArr = []
    for vertex in g.edges:
        if vertex not in vistedArr:
            mDFSHelper(g, vertex, vistedArr, stack)
    #output all nodes in stack order
    return vistedArr

    
def mDFSHelper(graph, vert, vistedArr, stack):
    vistedArr.append(vert)
    for neigh in graph.edges[vert]:
        if neigh not in vistedArr:
            mDFSHelper(graph, neigh, vistedArr, stack)
    stack.append(vert)
