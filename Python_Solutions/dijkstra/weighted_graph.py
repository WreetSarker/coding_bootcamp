# Implement Dijkstra's shortest path algorithm

class PriorityQueue:
    def __init__(self):
        self.values = []

    def enqueue(self, val, priority):
        self.values.append({'value': val, 'priority': priority})
        self.sort()

    def dequeue(self):
        return self.values.pop(0)

    def sort(self):
        self.values = sorted(self.values, key=lambda node: node['priority'])


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

q = PriorityQueue()
q.enqueue('A', 15)
q.enqueue('B', 12)
q.enqueue('C', 30)
print(q.values)
