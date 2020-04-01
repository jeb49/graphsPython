class Node:
    def __init__(self, data):
        self.data = data
        self.nextTo = set()


class Graph:
    def __init__(self):
        self.edges = {}
        self.nodes = {}
    
    #todo

    def addNode(self, val):
        nodeToAdd = Node(val)
        self.edges[nodeToAdd] = []

    def addUndirectedEdge(self, nodeOne, nodeTwo):
        self[nodeOne].edges.add(nodeTwo)
        self[nodeTwo].edges.add(nodeOne)

    def removeUndirectedEdge(self, nodeOne, nodeTwo):
        self[nodeOne].edges.remove(nodeTwo)
        self[nodeTwo].edges.remove(nodeOne)

    def getAllNodes(self):
        return self.nodes

#todo main 

# def createRandomUnweightedGraph():

# def createLinkedList():

# def dfsIter():

# def bftRec():

# def bftRec():

# def bftRecLinkedList():

# def bftIterLinkedList():
