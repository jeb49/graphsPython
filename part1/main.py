import graph
traverse = graph.Traversal()

print("adding nodes")
mainGraph = graph.Graph()

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

print(traverse.createRandomList(10))
linkedListGraph = traverse.createLinkedList(7)
print(linkedListGraph.edges)

randomGraph = traverse.createRandomUnweightedGraph(7)
print(randomGraph.edges)

print(mainGraph.edges)
print(traverse.dfsIter(1, 99, mainGraph))

#they are the same thing
print(traverse.bftIter(mainGraph))
print(traverse.bftRecursive(mainGraph))

"""
linListIter = bftIterLinkedList(10000)
print(linListIter)

linListIter = bftRecLinkedList(10000)
print(linListIter)
"""