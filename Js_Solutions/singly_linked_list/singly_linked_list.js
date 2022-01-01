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

}

s = new SinglyLinkedList();
s.push('Hi');
// console.log(s);
s.push('There');
// console.log(s);
s.push('Wreet');
// console.log(s);
console.log(s.shift());
console.log(s);
s.unshift('Mr.');
console.log(s);
s.unshift('Hello')
console.log(s);

// console.log(s.pop());