// Implement Dijkstra's shortest path algorithm

class PriorityQueue {
    constructor() {
        this.values = [];
    }

    enqueue(val, priority) {
        this.values.push({ val, priority });
        this.sort();
    }

    dequeue() {
        return this.values.shift();
    }

    sort() {
        this.values.sort((a, b) => a.priority - b.priority);
    }
}

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

    Dijkstra(start, finish) {
        const nodes = new PriorityQueue();
        const distances = {};
        const previous = {};
        let smallest;
        const path = []; // to return at the end

        // Build up initial state
        for (let vertex in this.adjacencyList) {
            if (vertex === start) {
                distances[vertex] = 0;
                nodes.enqueue(vertex, 0);
            } else {
                distances[vertex] = Infinity;
                nodes.enqueue(vertex, Infinity);
            }
            previous[vertex] = null;
        }

        // Loop until there is something to visit
        while (nodes.values.length > 0) {
            smallest = nodes.dequeue().val;
            if (smallest === finish) {
                while (previous[smallest]) {
                    path.push(smallest);
                    smallest = previous[smallest]
                }
                break;
            }
            if (smallest || distances[smallest] !== Infinity) {
                for (let neighbor of this.adjacencyList[smallest]) {
                    // Calculate new distance to neighboring node
                    let candidate = distances[smallest] + neighbor.weight;
                    if (candidate < distances[neighbor.node]) {
                        // updating new smallest distance to neighbor
                        distances[neighbor.node] = candidate;
                        // updating previous - How we got to neighbor
                        previous[neighbor.node] = smallest;
                        // Enqueue in priority queue with new priority
                        nodes.enqueue(neighbor.node, candidate);
                    }
                }
            }

        }
        return path.concat(smallest).reverse()
    }

}

g = new WeightedGraph();
g.addVertex('A');
g.addVertex('B');
g.addVertex('C');
g.addVertex('D');
g.addVertex('E');
g.addVertex('F');
g.addEdge('A', 'B', 4);
g.addEdge('A', 'C', 2);
g.addEdge('B', 'E', 3);
g.addEdge('C', 'D', 2);
g.addEdge('C', 'F', 4);
g.addEdge('D', 'E', 3);
g.addEdge('D', 'F', 1);
g.addEdge('E', 'F', 1);
console.log(g.Dijkstra("D", "F"));
