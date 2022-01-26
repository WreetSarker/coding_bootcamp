# Implement an undirected adjacency list graph

class Graph:
    def __init__(self):
        self.adjacencyList = dict()

    def addVertex(self, vertex):
        if self.adjacencyList.get(vertex) is None:
            self.adjacencyList[vertex] = []

    def addEdge(self, vertex1, vertex2):
        self.adjacencyList[vertex1].append(vertex2)
        self.adjacencyList[vertex2].append(vertex1)

    def removeEdge(self, vertex1, vertex2):
        data1 = []
        data2 = []
        for vertex in self.adjacencyList[vertex1]:
            if vertex != vertex2:
                data1.append(vertex)
        self.adjacencyList[vertex1] = data1

        for vertex in self.adjacencyList[vertex2]:
            if vertex != vertex1:
                data2.append(vertex)
        self.adjacencyList[vertex2] = data2

    def removeVertex(self, vertex):
        for ver in self.adjacencyList[vertex]:
            self.removeEdge(ver, vertex)
        del self.adjacencyList[vertex]


g = Graph()
g.addVertex('A')
g.addVertex('B')
g.addVertex('C')
g.addVertex('D')
g.addVertex('E')
g.addEdge('A', 'B')
g.addEdge('A', 'C')
g.addEdge('D', 'B')
g.addEdge('D', 'E')
g.addEdge('C', 'E')
print(g.adjacencyList)
g.removeVertex('A')
print(g.adjacencyList)
