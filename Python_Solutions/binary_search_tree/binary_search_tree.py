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

    def breadth_first_search(self):
        data = []
        queue = []
        node = self.root
        queue.append(node)

        while len(queue) != 0:
            node = queue.pop(0)
            data.append(node.value)
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)
        return data

    def dfs_pre_order(self):
        data = []
        current = self.root

        def traverse(node):
            data.append(node.value)
            if node.left is not None:
                traverse(node.left)
            if node.right is not None:
                traverse(node.right)
        traverse(current)
        return data


tree = BinarySearchTree()
tree.insert(10)
tree.insert(6)
tree.insert(15)
tree.insert(3)
tree.insert(8)
tree.insert(20)
print(tree.breadth_first_search())
print(tree.dfs_pre_order())
