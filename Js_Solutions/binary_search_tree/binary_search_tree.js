// Implement a binary search tree

class Node {
    constructor(val) {
        this.value = val;
        this.left = null;
        this.right = null;
    }
}

class BinarySearchTree {
    constructor() {
        this.root = null;
    }

    insert(val) {
        const newNode = new Node(val);
        if (!this.root) {
            this.root = newNode;
            return true;
        } else {
            let current = this.root;
            while (true) {
                if (val === current.value) return false;
                if (val > current.value) {
                    if (current.right === null) {
                        current.right = newNode;
                        return true;
                    } else {
                        current = current.right;
                    }
                } else if (val < current.value) {
                    if (current.left === null) {
                        current.left = newNode;
                        return true;
                    } else {
                        current = current.left;
                    }
                }
            }
        }
    }

    find(val) {
        if (!this.root) {
            return false;
        } else {
            let current = this.root;
            let found = false;
            while (current && !found) {
                // if (val === current.value) return true;
                if (val > current.value) {
                    current = current.right;
                } else if (val < current.value) {
                    current = current.left;
                } else {
                    found = true;
                }
            }
            return found;
        }
    }

    breadthFirstSearch() {
        let data = [];
        let node = this.root;
        let queue = [];
        queue.push(node);
        while (queue.length) {
            node = queue.shift();
            data.push(node.value);
            if (node.left) queue.push(node.left);
            if (node.right) queue.push(node.right)
        }
        return data;
    }

    dfsPreOrder() {
        let data = [];
        let current = this.root;

        function traverse(node) {
            data.push(node.value);
            if (node.left) traverse(node.left);
            if (node.right) traverse(node.right);
        }
        traverse(current);
        return data;
    }
}

tree = new BinarySearchTree();
tree.insert(10);
// console.log(tree);
tree.insert(6);
// console.log(tree);
tree.insert(15);
// console.log(tree);
tree.insert(3);
tree.insert(8);
tree.insert(20);
// console.log(tree);
// console.log(tree.find(13));
console.log(tree.breadthFirstSearch());
console.log(tree.dfsPreOrder());