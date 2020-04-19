class WeightedGraph:
    def __init__(self):
        self.nodes = set()
        self.edges = {}
    
    def addNode(self, nodeToAdd):
        self.nodes.add(nodeToAdd)
        self.edges[nodeToAdd] = {}

    def addUndirectedEdge(self, nodeOne, nodeTwo, weight):
        if nodeTwo not in self.edges[nodeOne].keys:
            self.edges[nodeOne][nodeTwo] = weight
        if nodeOne not in self.edges[nodeTwo].keys:
            self.edges[nodeTwo][nodeOne] = weight

    def removeUndirectedEdge(self, nodeOne, nodeTwo):
        if nodeTwo in self.edges[nodeOne]:
            self.edges[nodeOne].remove(nodeTwo)

    def getAllNodes(self):
        return self.nodes

def dijkstra(graph, start):
    """
    distances = {}
    priority = []
    prev = p[]
    vistedArr = []
    for vertex in g:
        distance[vertex] = 0 #trying to simulate infinity
        prev[vertex] = None
        if vertex != start:
            priority[vertex] = graph.edges[vertex]
            distance[start] = 0
    
    while len(priority) != 0:
        currMin = priority.pop(min(priority))
        for neigh in graph.edges[currMin]:
            tempDist = distance[currMin] + graph.edges[currMin][neigh]
            distance[neigh] = temp
            prev[neigh] = currMin
    """