// Implement a min binary heap data structure

class MinBinaryHeap {
    constructor() {
        this.values = []
    }

    insert(val) {
        this.values.push(val);
        this.bubbleUp();
        return this.values;
    }

    bubbleUp() {
        let idx = this.values.length - 1;
        let element = self.values[idx];
        while (idx > 0) {
            let parentIdx = Math.floor((idx - 1) / 2);
            let parent = this.values[parentIdx];
            if (element >= parent) {
                break;
            }
            this.values[idx] = this.values[parentIdx];
            this.values[parentIdx] = element;
            idx = parentIdx;
        }
    }

    extractMin() {
        let min = this.values[0];
        const last = this.values.pop();
        if (this.values.length > 0) {
            this.values[0] = last;
            this.sinkDown();
        }
        return min;
    }

    sinkDown() {
        let idx = 0;
        const element = this.values[idx];
        const length = this.values.length;

        while (true) {
            let leftChildIdx = 2 * idx + 1;
            let rightChildIdx = 2 * idx + 2;
            let leftChild, rightChild;
            let swap = null;

            if (leftChildIdx < length) {
                leftChild = this.values[leftChildIdx];

                if (leftChild < element) {
                    swap = leftChildIdx;
                }
            }

            if (rightChildIdx < length) {
                rightChild = this.values[rightChildIdx];

                if ((swap === null && rightChild < element) || (swap !== null && rightChild < leftChild)) {
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