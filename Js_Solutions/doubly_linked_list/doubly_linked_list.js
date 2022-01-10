// Implement a doubly linked list data structure

class Node {
    constructor(val) {
        this.value = val;
        this.next = null;
        this.prev = null;
    }
}

class DoublyLinkedList {
    constructor() {
        this.head = null;
        this.tail = null;
        this.length = 0;
    }

    push(val) {
        const newNode = new Node(val);
        if (this.length === 0) {
            this.head = newNode;
            this.tail = newNode;
        } else {
            this.tail.next = newNode;
            newNode.prev = this.tail;
            this.tail = newNode;
        }
        this.length += 1;
        return true;
    }

    pop() {
        if (this.length === 0) {
            return undefined;
        }
        let temp = this.tail;
        if (this.length === 1) {
            this.head = null;
            this.tail = null;
        } else {
            this.tail = this.tail.prev;
            this.tail.next = null;
            temp.prev = null;
        }
        this.length--;
        return temp;
    }

    shift() {
        if (this.length === 0) {
            return undefined;
        }
        let temp = this.head;
        if (this.length === 1) {
            this.head = null;
            this.tail = null;
        } else {
            this.head = this.head.next;
            this.head.prev = null;
            temp.next = null;
        }
        this.length--;
        return temp;
    }

    unshift(val) {
        const newVal = new Node(val);
        if (this.head === 0) {
            this.head = newVal;
            this.tail = newVal;
        } else {
            this.head.prev = newVal;
            newVal.next = this.head;
            this.head = newVal;
        }
        this.length++;
        return true;
    }

    get(idx) {
        if (idx < 0 || idx >= this.length) {
            return null;
        }
        if (idx <= Math.floor(this.length / 2)) {
            let current = this.head;
            let count = 0;
            while (count != idx) {
                current = current.next;
                count++;
            }
            return current;
        } else {
            let current = this.tail;
            let count = this.length - 1;
            while (count != idx) {
                current = current.prev;
                count--;
            }
            return current;
        }
    }

    set(idx, val) {
        const found = this.get(idx);
        if (found !== null) {
            found.value = val;
            return true;
        }
        return false;
    }

    insert(idx, val) {
        if (idx < 0 || idx > this.length) {
            return false;
        }
        if (idx === 0) {
            return !!this.unshift(val);
        } else if (idx === this.length) {
            return !!this.push(val);
        } else {
            let newNode = new Node(val);
            let beforeNode = this.get(idx - 1);
            let afterNode = beforeNode.next;
            beforeNode.next = newNode;
            newNode.prev = beforeNode;
            newNode.next = afterNode;
            afterNode.prev = newNode;
        }
        this.length++;
        return true;
    }

    remove(idx) {
        if (idx < 0 || idx >= this.length) {
            return null;
        }
        if (idx === 0) {
            return this.shift();
        } else if (idx === this.length - 1) {
            return this.pop();
        } else {
            let removedNode = this.get(idx);
            let prevNode = removedNode.prev;
            let nextNode = removedNode.next;
            prevNode.next = nextNode;
            nextNode.prev = prevNode;
            this.length--;
            removedNode.prev = null;
            removedNode.next = null;
            return removedNode;
        }

    }
}

d = new DoublyLinkedList();
d.push(1)
d.push(2)
console.log(d);
// console.log(d.insert(1, 'hi'));
// console.log(d);
console.log(d.remove(1));
console.log(d);