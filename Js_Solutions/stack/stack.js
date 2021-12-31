// Create a stack data structure.The stack
// should be a class that contains 'push' and 'pop'
// methods. 

class Node {
    constructor(val) {
        this.value = val;
        this.next = null;
    }
}

class Stack {
    constructor() {
        this.first = null;
        this.last = null;
        this.size = 0;
    }

    push(val) {
        const value = new Node(val);
        if (this.size === 0) {
            this.first = value;
            this.last = value;
        } else {
            const temp = this.first;
            this.first = value;
            this.first.next = temp;
        }
        this.size++;
    }

    pop() {
        if (this.size === 0) {
            return null;
        }
        const temp = this.first;
        if (this.size === 1) {
            this.first = null;
            this.last = null;
        } else {
            this.first = this.first.next;
        }
        this.size--;
        return temp.value;
    }
}

const s = new Stack();
s.push('a');
console.log(s);
s.push('b');
console.log(s);
s.push('c');
console.log(s);
console.log(s.pop());
console.log(s); 