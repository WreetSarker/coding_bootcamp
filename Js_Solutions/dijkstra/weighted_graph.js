// Implement Dijkstra's shortest path algorithm

class WeightedGraph {
    constructor() {
        this.adjacencyList = {};
    }

    addVertex(vertex) {
        if (!this.adjacencyList[vertex]) {
            this.adjacencyList[vertex] = [];
        }
    }

    addEdge(vertex1, vertex2, weight) {
        this.adjacencyList[vertex1].push({ node: vertex2, weight });
        this.adjacencyList[vertex2].push({ node: vertex1, weight });
    }
}

g = new WeightedGraph();
g.addVertex('A');
g.addVertex('B');
g.addVertex('C');
g.addEdge('A', 'B', 15);
g.addEdge('A', 'C', 25);
console.log(g.adjacencyList);