# Implement a min binary heap

class MinBinaryHeap:
    def __init__(self):
        self.values = []
        
    def insert(self, val):
        self.values.append(val)
        self.bubbleUp()
        return self.values
    
    def bubbleUp(self):
        idx = len(self.values) -1
        element = self.values[idx]
        while idx > 0:
            parentIdx = (idx -1)//2
            parent = self.values[parentIdx]
            if parent <= element:
                break
            self.values[idx] = self.values[parentIdx]
            self.values[parentIdx] = element
            idx = parentIdx
            
    def extractMin(self):
        min_val = self.values[0]
        last = self.values.pop()
        if len(self.values) > 0:
            self.values[0] = last
            self.sinkDown()
        return min_val
    
    def sinkDown(self):
        idx = self.values[0]
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
                if leftChild < element:
                    swap = leftChildIdx
                    
            if rightChildIdx < length:
                rightChild = self.values[rightChildIdx]
                if (swap is None and rightChild < element) or (swap is not None and rightChild < leftChild):
                    swap = rightChildIdx
            
            if swap is None:
                break
            self.values[idx] = self.values[swap]
            self.values[swap] = element
            idx = swap