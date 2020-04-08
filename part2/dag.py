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

    for vert in g.edges:
        for neigh in g.edges[vert]:
            if neigh not in inDegreeMap.keys():
                inDegreeMap[neigh] = 1
            else:
                inDegreeMap[neigh] += 1

    arr = []
    q =[]

    for el in inDegreeMap:
        q.append(el)
    while len(q) != 0:
        curr = q[0]
        arr.append(curr)

        #decrement the in-degrees of all dependents of curr
        for el in g.edges[curr]:
            inDegreeMap[el] -= 1

        #decrement the in-degree of curr to -1 (to avoid adding it back to Q)
        inDegreeMap[curr] = -1

        for neigh in g.edges[curr]:
            if inDegreeMap[neigh] == 0:
                q.append(neigh)
        q.pop(0)

    #output all nodes in q order
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
