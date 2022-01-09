# Implement a doubly linked list data structure

class Node:
    def __init__(self, val):
        self.value = val
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def push(self, val):
        newNode = Node(val)
        if self.length == 0:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            newNode.prev = self.tail
            self.tail = newNode
        self.length += 1

    def pop(self):
        if self.length == 0:
            return None
        temp = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None
        self.length -= 1
        return temp

    def shift(self):
        if self.length == 0:
            return None
        temp = self.head
        if self.length == 1:
            self.head = 0
            self.tail = 0
        else:
            self.head = self.head.next
            self.head.prev = None
            temp.prev = None
        self.length -= 1
        return temp

    def unshift(self, val):
        newNode = Node(val)
        if self.length == 0:
            self.head = newNode
            self.tail = newNode
        else:
            self.head.prev = newNode
            newNode.next = self.head
            self.head = newNode
        self.length += 1


d = DoublyLinkedList()
d.push(1)
d.push(2)
print(d.pop().value)
print(d.pop().value)
print(d.pop())
d.push(1)
d.push(2)
d.push('Hello')
print(d.shift().value)
d.unshift('Hi there')
print(d.shift().value)
