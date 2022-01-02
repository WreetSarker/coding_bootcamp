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

    def get(self, idx):
        if idx < 0 or idx >= self.length:
            return None
        count = 0
        current = self.head
        while count != idx:
            current = current.next
            count += 1
        return current

    def setValue(self, idx, value):
        if self.get(idx):
            currentNode = self.get(idx)
            currentNode.value = value
            return True
        return False

    def insert(self, idx, val):
        if idx < 0 or idx > self.length:
            return False
        if idx == 0:
            self.unshift(val)
        elif idx == self.length:
            self.push(val)
        else:
            newNode = Node(val)
            prevNode = self.get(idx - 1)
            temp = prevNode.next
            prevNode.next = newNode
            newNode.next = temp
            self.length += 1
        return True

    def remove(self, idx):
        if idx < 0 or idx >= 0:
            return None
        if idx == 0:
            return self.shift()
        elif idx == self.length - 1:
            return self.pop()
        else:
            prevNode = self.get(idx - 1)
            current = prevNode.next
            prevNode.next = current.next
            self.length -= 1
            return current.value


s = SinglyLinkedList()
s.push('Hi')
s.push('There')
s.push('Wreet')
print(s)
print(s.setValue(2, 'HAHA'))
print(s.get(2).value)
