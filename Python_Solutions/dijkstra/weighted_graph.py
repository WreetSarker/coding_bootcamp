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

    def Dijkstra(self, start, finish):
        distances = {}
        previous = {}
        nodes = PriorityQueue()
        path = []  # To return at the end
        smallest = None

        # Setting up initial values
        for vertex in self.adjacencyList.keys():
            if vertex == start:
                distances[vertex] = 0
                nodes.enqueue(vertex, 0)
            else:
                distances[vertex] = float('inf')
                nodes.enqueue(vertex, float('inf'))
            previous[vertex] = None

        # Loop until there is something to visit
        while len(nodes.values) > 0:
            smallest = nodes.dequeue()['value']
            if smallest == finish:
                while previous[smallest] is not None:
                    path.append(smallest)
                    smallest = previous[smallest]
                break
            if (smallest is not None) or distances[smallest] != float('inf'):
                for neighbor in self.adjacencyList[smallest]:
                    # Calculate new distance to neighbor node
                    candidate = distances[smallest] + neighbor['weight']
                    if candidate < distances[neighbor['node']]:
                        # update new distance to neighbor node
                        distances[neighbor['node']] = candidate
                        # update previous - How we got to neighbor
                        previous[neighbor['node']] = smallest
                        # Enqueue in priority queue with new priority
                        nodes.enqueue(neighbor['node'], candidate)

        path.append(smallest)
        return list(reversed(path))


g = WeightedGraph()
g.addVertex('A')
g.addVertex('B')
g.addVertex('C')
g.addVertex('D')
g.addVertex('E')
g.addVertex('F')
g.addEdge('A', 'B', 4)
g.addEdge('A', 'C', 2)
g.addEdge('B', 'E', 3)
g.addEdge('C', 'D', 2)
g.addEdge('C', 'F', 4)
g.addEdge('D', 'E', 3)
g.addEdge('D', 'F', 1)
g.addEdge('E', 'F', 1)
print(g.Dijkstra("B", "F"))
