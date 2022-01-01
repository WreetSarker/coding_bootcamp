# Implement a singly linked list.

class Node:
    def __init__(self, val):
        self.value = val
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def push(self, value):
        value = Node(value)
        if self.length == 0:
            self.head = value
            self.tail = value
        else:
            self.tail.next = value
            self.tail = value
        self.length += 1

    def pop(self):
        if self.length == 0:
            return None

        current = self.head
        newTail = current

        while current.next:
            newTail = current
            current = current.next

        self.tail = newTail
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return current.value

    def shift(self):
        if self.length == 0:
            return None
        temp = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
        self.length -= 1
        return temp.value

    def unshift(self, value):
        val = Node(value)
        if self.length == 0:
            self.head = val
            self.tail = val
        else:
            temp = self.head
            self.head = val
            self.head.next = temp

        self.length += 1


s = SinglyLinkedList()
s.push('Hi')
s.push('There')
s.push('Wreet')
print(s)
print(s.pop())
print(s.pop())
print(s.pop())
print(s.pop())
