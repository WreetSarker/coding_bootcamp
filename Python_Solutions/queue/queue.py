# Create a queue data structure.The queue
# should be a class with methods 'add' and 'remove'.
# The added value should be store until it is removed.

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0

    def enqueue(self, val):
        value = Node(val)

        if self.size == 0:
            self.first = value
            self.last = value
        else:
            self.first.next = value
            self.last = value
        self.size += 1

    def dequeue(self):
        if self.size == 0:
            return None
        temp = self.first
        if self.size == 1:
            self.first = None
            self.last = None
        else:
            self.first = self.first.next
        self.size -= 1
        return temp.value


q = Queue()
q.enqueue(1)
print(q)
q.enqueue(2)
print(q)
print(q.dequeue())
print(q)
