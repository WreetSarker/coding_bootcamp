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

    def depth_first_search_rec(self, start):
        result = []
        visited = dict()

        def dfs(vertex):
            if vertex is None:
                return None
            result.append(vertex)
            visited[vertex] = True
            for neighbor in self.adjacencyList[vertex]:
                if visited.get(neighbor) is not True:
                    dfs(neighbor)
        dfs(start)
        return result

    def depth_first_search_ite(self, start):
        result = []
        visited = {}
        stack = []
        vertex = None
        stack.append(start)

        while len(stack) > 0:
            vertex = stack.pop()
            if visited.get(vertex) is not True:
                result.append(vertex)
                visited[vertex] = True
                for neighbor in self.adjacencyList[vertex]:
                    stack.append(neighbor)
        return result

    def breadth_first_search(self, start):
        result = []
        queue = []
        queue.append(start)
        visited = {}
        visited[start] = True

        while len(queue) > 0:
            vertex = queue.pop(0)
            result.append(vertex)

            for neighbor in self.adjacencyList[vertex]:
                if visited.get(neighbor) is not True:
                    visited[neighbor] = True
                    queue.append(neighbor)

        return result


g = Graph()
g.addVertex('A')
g.addVertex('B')
g.addVertex('C')
g.addVertex('D')
g.addVertex('E')
g.addVertex('F')
g.addEdge('A', 'B')
g.addEdge('A', 'C')
g.addEdge('D', 'B')
g.addEdge('D', 'E')
g.addEdge('C', 'E')
g.addEdge('F', 'D')
g.addEdge('F', 'E')
# g.removeVertex('A')
print(g.depth_first_search_rec('A'))  # [ 'A', 'B', 'D', 'E', 'C', 'F' ]
print(g.depth_first_search_ite('A'))  # [ 'A', 'C', 'E', 'F', 'D', 'B' ]
print(g.breadth_first_search('A'))  # [ 'A', 'B', 'C', 'D', 'E', 'F' ]
