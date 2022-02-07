# Implement Dijkstra's shortest path algorithm

class Node:
    def __init__(self, val, priority):
        self.value = val
        self.priority = priority


class PriorityQueue:
    def __init__(self):
        self.values = []

    def enqueue(self, val, priority):
        newNode = Node(val, priority)
        self.values.append(newNode)
        self.bubbleUp()
        return self.values

    def bubbleUp(self):
        idx = len(self.values) - 1
        element = self.values[idx]
        while idx > 0:
            parentIdx = (idx-1)//2
            parent = self.values[parentIdx]
            if parent.priority < element.priority:
                break
            self.values[idx] = self.values[parentIdx]
            self.values[parentIdx] = element
            idx = parentIdx

    def dequeue(self):
        min_val = self.values[0]
        last = self.values.pop()
        if len(self.values) > 0:
            self.values[0] = last
            self.sinkDown()
        return min_val

    def sinkDown(self):
        idx = 0
        element = self.values[idx]
        length = len(self.values)

        while True:
            leftChildIdx = (2*idx) + 1
            rightChildIdx = (2*idx) + 2
            leftChild = None
            rightChild = None
            swap = None

            if leftChildIdx < length:
                leftChild = self.values[leftChildIdx]
                if leftChild.priority < element.priority:
                    swap = leftChildIdx

            if rightChildIdx < length:
                rightChild = self.values[rightChildIdx]
                if (swap is None and rightChild.priority < element.priority) or (swap is not None and rightChild.priority < leftChild.priority):
                    swap = rightChildIdx

            if swap is None:
                break
            self.values[idx] = self.values[swap]
            self.values[swap] = element
            idx = swap


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
            smallest = nodes.dequeue().value
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
print(g.Dijkstra("A", "E"))
