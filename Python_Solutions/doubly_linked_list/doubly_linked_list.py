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
        return True

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
        return True

    def get(self, idx):
        if idx < 0 or idx >= self.length:
            return None
        if idx <= self.length // 2:
            current = self.head
            count = 0
            while count != idx:
                current = current.next
                count += 1
            return current
        else:
            current = self.tail
            count = self.length - 1
            while count != idx:
                current = current.prev
                count -= 1
            return current

    def set_val(self, idx, val):
        found = self.get(idx)
        if found is not None:
            found.value = val
            return True
        return False

    def insert(self, idx, val):
        if idx < 0 or idx > self.length:
            return False
        if idx == 0:
            return self.unshift(val)
        elif idx == self.length:
            return self.push(val)
        else:
            newNode = Node(val)
            beforeNode = self.get(idx-1)
            afterNode = beforeNode.next
            beforeNode.next = newNode
            newNode.prev = beforeNode
            newNode.next = afterNode
            afterNode.prev = newNode
            self.length += 1
            return True

    def remove(self, idx):
        if idx < 0 or idx >= self.length:
            return None
        if idx == 0:
            return self.shift()
        elif idx == self.length - 1:
            return self.pop()
        else:
            removedNode = self.get(idx)
            prevNode = removedNode.prev
            nextNode = removedNode.next
            prevNode.next = nextNode
            nextNode.prev = prevNode
            removedNode.prev = None
            removedNode.next = None
            self.length -= 1
            return removedNode


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
