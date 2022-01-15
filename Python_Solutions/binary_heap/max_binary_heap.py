# Implement a max binary heap data structure

class MaxBinaryHeap:
    def __init__(self):
        self.values = []

    def insert(self, val):
        self.values.append(val)
        self.bubbleUp()
        return self.values

    def bubbleUp(self):
        idx = len(self.values) - 1
        element = self.values[idx]
        while idx > 0:
            parentIdx = (idx-1)//2
            parent = self.values[parentIdx]
            if element <= parent:
                break
            self.values[parentIdx] = element
            self.values[idx] = parent
            idx = parentIdx


heap = MaxBinaryHeap()
heap.insert(12)
heap.insert(27)
heap.insert(18)
heap.insert(55)
heap.insert(33)
heap.insert(41)
print(heap.insert(39))
print(heap.insert(1000))
