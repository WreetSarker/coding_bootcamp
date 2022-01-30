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

    removeEdge(vertex1, vertex2) {
        let data1 = [];
        let data2 = [];
        for (let i = 0; i < this.adjacencyList[vertex1].length; i++) {
            if (this.adjacencyList[vertex1][i] !== vertex2) {
                data1.push(this.adjacencyList[vertex1][i]);
            }
        }
        this.adjacencyList[vertex1] = data1;

        for (let j = 0; j < this.adjacencyList[vertex2].length; j++) {
            if (this.adjacencyList[vertex2][j] !== vertex1) {
                data2.push(this.adjacencyList[vertex2][j]);
            }
        }
        this.adjacencyList[vertex2] = data2;
    }

    removeVertex(vertex) {
        for (let item of this.adjacencyList[vertex]) {
            this.removeEdge(item, vertex);
        }
        delete this.adjacencyList[vertex]
    }

    depthFirstSearchRec(start) {
        let results = [];
        let visited = {};
        const adjacencyList = this.adjacencyList;
        function dfs(vertex) {
            if (!vertex) return null;
            results.push(vertex);
            visited[vertex] = true;
            for (let neighbor of adjacencyList[vertex]) {
                if (!visited[neighbor]) {
                    dfs(neighbor)
                }
            }
        }
        dfs(start);
        return results;
    }

    depthFirstSearchIte(start) {
        let stack = [];
        let discovered = {};
        let vertex;
        let result = [];

        stack.push(start);
        while (stack.length > 0) {
            vertex = stack.pop();
            if (!discovered[vertex]) {
                discovered[vertex] = true;
                result.push(vertex);
                for (let neighbor of this.adjacencyList[vertex]) {
                    stack.push(neighbor);
                }
            }
        }
        return result;
    }

}
g = new Graph();
g.addVertex('A')
// console.log(g);
console.log(g.addVertex('B'));
g.addEdge('A', 'B')
g.addVertex('C');
g.addVertex('D');
g.addVertex('E');
g.addVertex('F');
g.addEdge('A', 'C');
g.addEdge('B', 'D');
g.addEdge('D', 'E');
g.addEdge('C', 'E');
g.addEdge('F', 'D');
g.addEdge('F', 'E');
// console.log(g);
// g.removeVertex('A')
console.log(g);
console.log(g.depthFirstSearchRec('A'));
console.log(g.depthFirstSearchIte('A'));