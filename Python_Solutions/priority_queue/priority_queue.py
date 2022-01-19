# Implement a priority queue with min binary heap

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

            if element.priority >= parent.priority:
                break
            self.values[idx] = parent
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
            leftChildIdx = 2*idx + 1
            rightChildIdx = 2*idx + 2
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


priority = PriorityQueue()
priority.enqueue("common cold", 3)
priority.enqueue("wound", 1)
print(priority.enqueue("high fever", 2))
print(priority.dequeue())
print(priority.values)
