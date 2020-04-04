import random
from collections import deque

class Node:
    def __init__(self, data):
        self.data = data
        self.edges = set()
        self.visited = False


class Graph:
    def __init__(self):
        self.edges = {}
        self.nodes = {}
    
    #todo

    def addNode(self, val):
        nodeToAdd = Node(val)
        self.edges[nodeToAdd] = []

    def addUndirectedEdge(self, nodeOne, nodeTwo):
        #probably buggy
        self[nodeOne].edges.add(nodeTwo)
        self[nodeTwo].edges.add(nodeOne)

    def removeUndirectedEdge(self, nodeOne, nodeTwo):
        #probably buggy
        self[nodeOne].edges.remove(nodeTwo)
        self[nodeTwo].edges.remove(nodeOne)

    def getAllNodes(self):
        return self.nodes

#todo main 

def createRandomList(n):
    returnList = [random.randrange(0, n) for i in range(n)]
    return returnList

def createRandomUnweightedGraph(n):
    randomGraph = Graph()

    #create random list
    randList = createRandomList(n)

    #not sure what i should do with this
    """
    for el in list:


    """
    

def createLinkedList(n):
    randomGraph = Graph()
    randList = createRandomList(n)
    """
    for i in range(n):
        curr = randList[i]
        if graph is empty
            randomGraph.addNode(el)
            prev = curr
        else:
            prev = randList[i - 1]
            randomeGraph.addNode(el)
            randomGraph.addUndirectedEdge(el, prev)
    """

def dfsIter(start, end):
    """"
    s = []
    visitedArr = []
    for vertex in start.edges:
        if vertex.visted == False:
            vertex.visted = true
            visitedArr.append(vertex)
            s.append(vertex)

            while S.isEmpty() != False:
                cur = s.pop()
                for vert in curr.edges:
                    if vert.visted == False:
                        vert.visted = true
                        s.append(vert)
                        visitedArr.append(vertex)

    """"

def bftRecursive(g):
    q = []
    for v in g.edges:
        if v.discovered == False:
            q.append(v)
            bfsHelperRec(g, q)
    



def bftHelperRec(g, q):
    """
    if q.isEmpty():
        return null
    
    curr = q.front()

    for vert in curr.edges:
        if vert.visited == False:
            vert.visted == True
            q.append(vert)
    
    bfsHelperRec(g, q)

    """


def bftIter(g):
    """"
    q = []
    visitedArr = []
    for vertex in start.edges:
        if vertex.visted == False:
            vertex.visted = true
            visitedArr.append(vertex)
            q.append(vertex)

            while S.isEmpty() != False:
                cur = q.deque()
                for vert in curr.edges:
                    if vert.visted == False:
                        vert.visted = true
                        q.append(vert)
                        visitedArr.append(vertex)
    """"

def bftRecLinkedList(g):
    bftRecursive(g)

def bftIterLinkedList(g):
    bftIter(g)