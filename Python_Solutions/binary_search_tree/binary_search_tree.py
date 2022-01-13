# Implement a binary search tree

class Node:
    def __init__(self, val):
        self.value = val
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, val):
        newNode = Node(val)
        if self.root is None:
            self.root = newNode
        else:
            current = self.root
            while True:
                if current.value == val:
                    return False
                if val > current.value:
                    if current.right is None:
                        current.right = newNode
                        return True
                    else:
                        current = current.right
                elif val < current.value:
                    if current.left is None:
                        current.left = newNode
                        return True
                    else:
                        current = current.left

    def found(self, val):
        if self.root is None:
            return False
        current = self.root
        found = False

        while (current is not None) and not found:
            if val > current.value:
                current = current.right
            elif val < current.value:
                current = current.left
            else:
                found = True
        return found


tree = BinarySearchTree()
tree.insert(10)
tree.insert(4)
tree.insert(14)
tree.insert(3)
tree.insert(1)
tree.insert(13)
print(tree.found(2))
