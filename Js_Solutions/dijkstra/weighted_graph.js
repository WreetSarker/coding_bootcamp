// Implement Dijkstra's shortest path algorithm

class Node {
    constructor(val, priority) {
        this.value = val;
        this.priority = priority;
    }
}

class PriorityQueue {
    constructor() {
        this.values = [];
    }

    enqueue(val, priority) {
        const newNode = new Node(val, priority);
        this.values.push(newNode);
        this.bubbleUp();
        return true;
    }

    bubbleUp() {
        let idx = this.values.length - 1;
        const element = this.values[idx];
        while (idx > 0) {
            let parentIdx = Math.floor((idx - 1) / 2);
            let parent = this.values[parentIdx];
            if (parent.priority < element.priority) {
                break;
            }
            this.values[idx] = this.values[parentIdx];
            this.values[parentIdx] = element;
            idx = parentIdx;
        }
    }

    dequeue() {
        const min_val = this.values[0];
        const last = this.values.pop();
        if (this.values.length > 0) {
            this.values[0] = last;
            this.sinkDown();
        }
        return min_val;
    }

    sinkDown() {
        let idx = 0;
        const element = this.values[idx];
        const length = this.values.length;

        while (true) {
            let leftChildIdx = (2 * idx) + 1;
            let rightChildIdx = (2 * idx) + 2;
            let leftChild, rightChild;
            let swap = null;

            if (leftChildIdx < length) {
                leftChild = this.values[leftChildIdx];
                if (leftChild.priority < element.priority) {
                    swap = leftChildIdx;
                }
            }

            if (rightChildIdx < length) {
                rightChild = this.values[rightChildIdx];
                if ((swap === null && rightChild.priority < element.priority) || (swap !== null && rightChild.priority < leftChild.priority)) {
                    swap = rightChildIdx;
                }
            }

            if (swap === null) {
                break;
            }
            this.values[idx] = this.values[swap];
            this.values[swap] = element;
            idx = swap;
        }
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

    removeEdge(vertex1, vertex2) {
        let data1 = [];
        let data2 = [];
        for (let neighbor of this.adjacencyList[vertex1]) {
            if (neighbor !== vertex2) {
                data1.push(neighbor);
            }
        }
        this.adjacencyList[vertex1] = data1;
        for (let neighbor of this.adjacencyList[vertex2]) {
            if (neighbor !== vertex1) {
                data2.push(neighbor);
            }
        }
        this.adjacencyList[vertex2] = data2;
    }

    removeVertex(vertex) {
        for (let neighbor of this.adjacencyList[vertex]) {
            this.removeEdge(neighbor, vertex);
        }
        delete this.adjacencyList[vertex];
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
            smallest = nodes.dequeue().value;
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
console.log(g.Dijkstra("A", "E"));
