import random
from collections import deque

class Node:
    def __init__(self, val):
        self.val = val
        self.edges = []

class Graph:
    def __init__(self):
        self.nodes = set()
    
    def addNode(self, val):
        nodeToAdd = Node(val)
        self.nodes.add(nodeToAdd)

    def addUndirectedEdge(self, nodeOne, nodeTwo):
        #probably buggy
        if nodeTwo not in self.nodes[nodeOne]:
            nodeOne.edges.append(nodeTwo)
        if nodeOne not in self.nodes[nodeTwo]:
            nodeTwo.edges.append(nodeOne)

    def removeUndirectedEdge(self, nodeOne, nodeTwo):
        if nodeTwo in self.nodes[nodeOne]:
            self.nodes[nodeOne].remove(nodeTwo)
        if nodeOne in self.nodes[nodeTwo]:
            self.nodes[nodeTwo].remove(nodeOne)

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
    
    # for el in randList:
    #     randomGraph.addNode(el)
    #     if len(randomGraph.nodes) > 1:
    #         randomIndex = random.randint(0, len(randomGraph.edges))
    #         if randomIndex % 2 == 0:
    #             randVert = randomGraph[randVert]
    #             randomGraph.addUndirectedEdge(randVert, el)

    

def createLinkedList(n):
    randomGraph = Graph()
    randList = createRandomList(n)
    
    for i in range(n):
        curr = randList[i]
        el = Node(curr)
        if len(randomGraph.nodes) == 0:
            randomGraph.addNode(el)
            prev = curr
        else:
            randomGraph.addNode(el)
            randomGraph.addUndirectedEdge(el, prev)
            prev = curr
    

def dfsIter(start, end):
    s = []
    visitedArr = []
    for vertex in start.edges:
        if vertex in visitedArr:
            visitedArr.append(vertex)
            s.append(vertex)

            while s.isEmpty() != False:
                curr = s.pop()
                for vert in curr.edges:
                    if vert in visitedArr:
                        vert.visted = True
                        s.append(vert)
                        visitedArr.append(vertex)



def bftHelperRec(g, q, v):
    if q.isEmpty():
        return None
    
    curr = q.front()

    for vert in curr.edges:
        if vert not in v:
            q.append(vert)
    
    bftHelperRec(g, q)

def bftRecursive(g):
    q = []
    visted = []
    for v in g.edges:
        if v not in visted:
            q.append(v)
            bftHelperRec(g, q, visted)
    



def bftIter(g):
    q = []
    visitedArr = []
    for vertex in g.nodes:
        if vertex not in visitedArr:
            visitedArr.append(vertex)
            q.append(vertex)

            while len(q) != 0:
                curr = q.deque()
                for vert in curr.edges:
                    if vert not in visitedArr:
                        q.append(vert)
                        visitedArr.append(vertex)


def bftRecLinkedList(g):
    bftRecursive(g)

def bftIterLinkedList(g):
    bftIter(g)