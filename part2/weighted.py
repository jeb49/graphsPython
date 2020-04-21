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
        if nodeOne in self.edges[nodeTwo]:
            self.edges[nodeTwo].remove(nodeOne)

    def getAllNodes(self):
        return self.nodes

    def dijkstra(self, graph, start):
        distances = {}
        priority = []
        prev = []
        vistedArr = []

        for neighbor in g.edges[start]:
            distance[neighbor] = 0 #trying to simulate infinity
            prev[neighbor] = None
            if neighbor != start:
                priority[neighbor] = graph.edges[neighbor]
                distance[neighbor] = 0
        
        while len(priority) != 0:
            currMin = priority.pop(min(priority))
            for neigh in graph.edges[currMin]:
                tempDist = distances[currMin] + graph.edges[currMin][neigh]
                distance[neigh] = tempDist
                prev[neigh] = currMin