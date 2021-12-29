// Create a queue data structure.The queue
// should be a class with methods 'add' and 'remove'.
// The added value should be store until it is removed.

// Node implementation

class Node {
    constructor(value) {
        this.value = value;
        this.next = null;
    }
}

class Queue {
    constructor() {
        this.first = null;
        this.last = null;
        this.size = 0;
    }

    enqueue(value) {
        const val = new Node(value);
        if (this.size === 0) {
            this.first = val;
            this.last = val;
            this.size = 1
        } else {
            this.first.next = val;
            this.last = val;
            this.size += 1
        }
    }

    dequeue() {
        if (this.size === 0) {
            return null;
        }
        const temp = this.first;
        if (this.size === 1) {
            this.first = null;
            this.last = nul;
        } else {
            this.first = this.first.next;
        }
        this.size--;
        return temp.value;
    }
}


// Queue with array
// class Queue {
//     constructor() {
//         this.data = [];
//     }

//     enqueue(val) {
//         this.data.unshift(val)
//     }

//     dequeue() {
//         return this.data.pop();
//     }
// }

q = new Queue();
q.enqueue(1);
console.log(q);
q.enqueue(2)
console.log(q);
console.log(q.dequeue());
console.log(q);