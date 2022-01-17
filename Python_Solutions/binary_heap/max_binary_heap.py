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

    def extract_max(self):
        max_val = self.values[0]
        end = self.values.pop()
        if len(self.values) > 0:
            self.values[0] = end
            self.sink_down()
        return max_val

    def sink_down(self):
        idx = 0
        element = self.values[0]
        length = len(self.values)

        while True:
            left_child_idx = 2*idx + 1
            right_child_idx = 2*idx + 2
            left_child = None
            right_child = None
            swap = None

            if left_child_idx < length:
                left_child = self.values[left_child_idx]
                if left_child > element:
                    swap = left_child_idx

            if right_child_idx < length:
                right_child = self.values[right_child_idx]
                if (swap is None and right_child_idx > element) or (swap is not None and right_child > left_child):
                    swap = right_child_idx

            if swap is None:
                break
            self.values[idx] = self.values[swap]
            self.values[swap] = element
            idx = swap


heap = MaxBinaryHeap()
heap.insert(41)
heap.insert(39)
heap.insert(33)
heap.insert(18)
heap.insert(27)
heap.insert(12)
print(heap.insert(55))
print(heap.insert(1000))
print(heap.extract_max())
print(heap.values)
print(heap.extract_max())
print(heap.values)
heap.extract_max()
print(heap.values)
