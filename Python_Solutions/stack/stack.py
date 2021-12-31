# Create a stack data structure.The stack
# should be a class that contains 'push' and 'pop'
# methods.

class Node:
    def __init__(self, val):
        self.value = val
        self.next = None


class Stack:
    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0

    def push(self, val):
        value = Node(val)

        if self.size == 0:
            self.first = value
            self.last = value
        else:
            temp = self.first
            self.first = value
            self.first.next = temp
        self.size += 1

    def pop(self):
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


s = Stack()
s.push('a')
print(s)
s.push('b')
s.push('c')
print(s.pop())
print(s.pop())
print(s.pop())
print(s.pop())
