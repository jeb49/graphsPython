import random
from collections import deque
class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = {}
    
    def addNode(self, nodeToAdd):
        #node can theoretically be anything
        if nodeToAdd not in self.nodes:
            self.nodes.add(nodeToAdd)
            self.edges[nodeToAdd] = set()

    def addUndirectedEdge(self, nodeOne, nodeTwo):
        self.edges[nodeOne].add(nodeTwo)
        self.edges[nodeTwo].add(nodeOne)

    def removeUndirectedEdge(self, nodeOne, nodeTwo):
        if nodeTwo in self.edges[nodeOne]:
            self.edges[nodeOne].remove(nodeTwo)
        if nodeOne in self.edges[nodeTwo]:
            self.edges[nodeTwo].remove(nodeOne)

    def getAllNodes(self):
        return self.nodes

class Traversal:
    def __init__(self):
        pass
    
    def createRandomList(self, n):
        returnList = [random.randrange(0, n * 100000) for i in range(n)]
        return returnList

    def createRandomUnweightedGraph(self, n):
        randomGraph = Graph()
        #create random list
        randList = self.createRandomList(n)

        for i in range(n):
            curr = randList[i]
            if len(randomGraph.nodes) == 0:
                randomGraph.addNode(curr)
            else:
                randomGraph.addNode(curr)
                if i%2 == 0:
                    randomGraph.addUndirectedEdge(randList[random.randrange(0, i )], curr)
        return randomGraph

    def createLinkedList(self,n):
        randomGraph = Graph()
        randList = self.createRandomList(n)
        
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

    def dfsIter(self, start, end, graph):
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


    def bftHelperRec(self, g, q, visted):
        if len(q) == 0:
            return visted
        
        curr = q.pop(0)

        for vert in g.edges[curr]:
            if vert not in visted:
                visted.append(vert)
                q.append(vert)
        
        self.bftHelperRec(g, q, visted)

    def bftRecursive(self, g):
        q = []
        visted = []
        for v in g.edges:
            if v not in visted:
                visted.append(v)
                q.append(v)
                self.bftHelperRec(g, q, visted)
        return visted 



    def bftIter(self, g):
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


    def bftRecLinkedList(self, n):
        linkedList = self.createLinkedList(n)
        return self.bftIter(linkedList)

    def bftIterLinkedList(self, n):
        linkedList = self.createLinkedList(n)
        return self.bftRecursive(linkedList)