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
    }
}

d = new DoublyLinkedList();
d.push(1)
d.push(2)
console.log(d);
console.log(d.pop());
console.log(d);
d.push(2);
d.push(3);
console.log(d);
console.log(d.shift());
console.log(d);
d.unshift(1);
d.unshift(0);
console.log(d);