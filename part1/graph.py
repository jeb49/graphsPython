import random
from collections import deque

class Node:
    def __init__(self, val):
        self.val = val
        self.edges = []

class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = {}
    
    def addNode(self, nodeToAdd):
        self.nodes.add(nodeToAdd)
        self.edges[nodeToAdd] = []

    def addUndirectedEdge(self, nodeOne, nodeTwo):
        if nodeTwo not in self.edges[nodeOne]:
            self.edges[nodeOne].append(nodeTwo)
        if nodeOne not in self.edges[nodeTwo]:
            self.edges[nodeTwo].append(nodeOne)

    def removeUndirectedEdge(self, nodeOne, nodeTwo):
        if nodeTwo in self.edges[nodeOne]:
            self.edges[nodeOne].remove(nodeTwo)
        if nodeOne in self.edges[nodeTwo]:
            self.edges[nodeTwo].remove(nodeOne)

    def getAllNodes(self):
        return self.nodes


#todo main

def createRandomList(n):
    returnList = [random.randrange(0, n * 100000) for i in range(n)]
    return returnList

def createRandomUnweightedGraph(n):
    randomGraph = Graph()
    #create random list
    randList = createRandomList(n)

    for i in range(n):
        curr = randList[i]
        if len(randomGraph.nodes) == 0:
            randomGraph.addNode(curr)
        else:
            randomGraph.addNode(curr)
            if i%2 == 0:
                randomGraph.addUndirectedEdge(randList[random.randrange(0, i )], curr)
    return randomGraph

    

def createLinkedList(n):
    randomGraph = Graph()
    randList = createRandomList(n)
    
    for i in range(n):
        curr = randList[i]
        if len(randomGraph.nodes) == 0:
            randomGraph.addNode(curr)
            prev = curr
        else:
            randomGraph.addNode(curr)
            randomGraph.addUndirectedEdge(curr, prev)
            prev = curr

    return randomGraph

def dfsIter(start, end, graph):
    s = []
    visitedArr = []
    visitedArr.append(start)
    for vertex in graph.edges[start]:
        print(graph.edges[start])
        if vertex not in visitedArr:
            visitedArr.append(vertex)
            s.append(vertex)

            while len(s) != 0:
                curr = s.pop()
                for vert in graph.edges[curr]:
                    if vert not in visitedArr:
                        visitedArr.append(vert)
                        s.append(vert)

    return visitedArr



def bftHelperRec(g, q, visted):
    if len(q) == 0:
        return visted
    
    curr = q.pop(0)

    for vert in g.edges[curr]:
        if vert not in visted:
            visted.append(vert)
            q.append(vert)

    
    bftHelperRec(g, q, visted)

def bftRecursive(g):
    q = []
    visted = []
    for v in g.edges:
        if v not in visted:
            visted.append(v)
            q.append(v)
            bftHelperRec(g, q, visted)
    return visted 



def bftIter(g):
    q = []
    visitedArr = []
    for vertex in g.edges:
        if vertex not in visitedArr:
            visitedArr.append(vertex)
            q.append(vertex)

            while len(q) != 0:
                curr = q.pop(0)
                for vert in g.edges[curr]:
                    if vert not in visitedArr:
                        q.append(vert)
                        visitedArr.append(vert)
    return visitedArr


def bftRecLinkedList(g):
    bftRecursive(g)

def bftIterLinkedList(g):
    bftIter(g)

#testing

print("adding nodes")
mainGraph = Graph()
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
mainGraph.addNode(67)
mainGraph.addNode(81)
mainGraph.addNode(99)

print(mainGraph.getAllNodes())
print('\n')

print("adding and removing undirected edges")

mainGraph.addUndirectedEdge(1,2)
print(mainGraph.getAllNodes())
print(mainGraph.edges)
mainGraph.removeUndirectedEdge(1,2)
print(mainGraph.edges)
mainGraph.addUndirectedEdge(1,7)
mainGraph.addUndirectedEdge(401,7)
mainGraph.addUndirectedEdge(1,8)

print("linked list and random graph")

print(createRandomList(10))
linkedListGraph = createLinkedList(7)
print(linkedListGraph.edges)

randomGraph = createRandomUnweightedGraph(7)
print(randomGraph.edges)

print(mainGraph.edges)
print(dfsIter(1, 99, mainGraph))
print(bftIter(mainGraph))
print(bftRecursive(mainGraph))