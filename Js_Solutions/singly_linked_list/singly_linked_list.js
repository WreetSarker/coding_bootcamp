// Implement a singly linked list
class Node {
    constructor(val) {
        this.value = val;
        this.next = null;
    }
}

class SinglyLinkedList {
    constructor() {
        this.head = null;
        this.tail = null;
        this.length = 0;
    }

    push(val) {
        const value = new Node(val);
        if (this.length === 0) {
            this.head = value;
            this.tail = value;
        } else {
            this.tail.next = value;
            this.tail = value;
        }
        this.length++;
    }

    pop() {
        if (this.length === 0) {
            return undefined;
        }
        let current = this.head;
        let newTail = current;
        while (current.next) {
            newTail = current;
            current = current.next;
        }
        this.tail = newTail;
        this.tail.next = null;
        this.length--;
        if (this.length === 0) {
            this.head = null;
            this.tail = null;
        }
        return current.value;
    }

    shift() {
        if (this.length === 0) return undefined;
        let temp = this.head;
        if (this.length === 1) {
            this.head = null;
            this.tail = null;
        } else {
            this.head = this.head.next;
        }
        this.length--;
        return temp.value;
    }

    unshift(value) {
        const val = new Node(value);
        if (this.length === 0) {
            this.head = val;
            this.tail = val;
        } else {
            const temp = this.head;
            this.head = val;
            this.head.next = temp;
        }
        this.length++;
    }

    get(idx) {
        if (idx < 0 || idx >= this.length) {
            return null;
        }
        let count = 0;
        let current = this.head;
        while (count !== idx) {
            current = current.next;
            count++
        }
        return current;
    }

    set(idx, value) {
        if (this.get(idx)) {
            const node = this.get(idx);
            node.value = value;
            return true;
        }
        return false;
    }

    insert(idx, value) {
        if (idx < 0 || idx > this.length) {
            return false;
        }
        if (idx === 0) {
            this.unshift(value);
        } else if (idx === this.length) {
            this.push(value);
        } else {
            const prevNode = this.get(idx - 1);
            let temp = prevNode.next;
            const newNode = new Node(value);
            prevNode.next = newNode;
            newNode.next = temp;
            this.length++;
        }
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
            let prevNode = this.get(idx - 1);
            let currentNode = this.get(idx);
            prevNode.next = currentNode.next;
            this.length--;
            return currentNode.value;
        }
    }

    reverse() {
        if (this.length === 0) {
            return null;
        }
        let node = this.head;
        this.head = this.tail;
        this.tail = node;
        let next;
        let prev = null;

        for (let i = 0; i < this.length; i++) {
            next = node.next;
            node.next = prev;
            prev = node;
            node = next;
        }
        return this;
    }

    print() {
        const arr = [];
        let current = this.head;
        while (current) {
            arr.push(current.value);
            current = current.next;
        }
        console.log(arr);
    }
}

s = new SinglyLinkedList();
s.push('Hi');
s.push('There');
s.push('Wreet');
s.shift()
s.unshift('Mr.');
s.unshift('Hello')
console.log(s.get(3));
console.log(s.insert(1, 'Haha'));
console.log(s);
// console.log(s.remove(4));
console.log(s);
s.print();
s.reverse();
s.print();

// console.log(s.pop());