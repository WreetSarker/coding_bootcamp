// Implement an undirected adjacency list graph

class Graph {
    constructor() {
        this.adjacencyList = {};
    }

    addVertex(vertex) {
        if (!this.adjacencyList[vertex]) {
            this.adjacencyList[vertex] = [];
        }
    }

    addEdge(vertex1, vertex2) {
        this.adjacencyList[vertex1].push(vertex2);
        this.adjacencyList[vertex2].push(vertex1);
    }
}
g = new Graph();
g.addVertex('A')
console.log(g);
console.log(g.addVertex('B'));
g.addEdge('A', 'B')
console.log(g);