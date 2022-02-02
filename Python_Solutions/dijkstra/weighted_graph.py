# Implement Dijkstra's shortest path algorithm

class WeightedGraph:
    def __init__(self):
        self.adjacencyList = {}

    def addVertex(self, vertex):
        if self.adjacencyList.get(vertex) is None:
            self.adjacencyList[vertex] = []

    def addEdge(self, vertex1, vertex2, weight):
        self.adjacencyList[vertex1].append({'node': vertex2, 'weight': weight})
        self.adjacencyList[vertex2].append({'node': vertex1, 'weight': weight})


g = WeightedGraph()
g.addVertex('A')
g.addVertex('B')
g.addVertex('C')
g.addEdge('A', 'B', 15)
g.addEdge('A', 'C', 25)
print(g.adjacencyList)
