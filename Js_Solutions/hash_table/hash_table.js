// Implement a hash table

class HashTable {
    constructor(size = 53) {
        this.keyMap = new Array(size);
    }

    _hash(key) {
        let total = 0;
        const WEIRD_PRIME = 31;
        for (let i = 0; i < Math.min(key.length, 100); i++) {
            let char = key[i];
            let value = char.charCodeAt(0) - 96;
            total = (total * WEIRD_PRIME + value) % this.keyMap.length;
        }
        return total;
    }

    set(key, val) {
        let idx = this._hash(key);
        if (!this.keyMap[idx]) {
            this.keyMap[idx] = [];
        }
        this.keyMap[idx].push([key, val])
        return this.keyMap;
    }

    get(key) {
        let idx = this._hash(key);
        if (this.keyMap[idx]) {
            for (let i = 0; i < this.keyMap[idx].length; i++) {
                if (this.keyMap[idx][i][0] === key) {
                    return this.keyMap[idx][i][1];
                }
            }
        }
        return undefined;
    }

    keys() {
        let result = [];
        for (let i = 0; i < this.keyMap.length; i++) {
            if (this.keyMap[i]) {
                for (let j = 0; j < this.keyMap[i].length; j++) {
                    result.push(this.keyMap[i][j][0])
                }
            }
        }
        return result;
    }

    values() {
        let result = [];
        for (let i = 0; i < this.keyMap.length; i++) {
            if (this.keyMap[i]) {
                for (let j = 0; j < this.keyMap[i].length; j++) {
                    if (!result.includes(this.keyMap[i][j][1])) {
                        result.push(this.keyMap[i][j][1])
                    }
                }
            }
        }
        return result;
    }

    items() {
        let result = [];
        for (let i = 0; i < this.keyMap.length; i++) {
            if (this.keyMap[i]) {
                for (let j = 0; j < this.keyMap[i].length; j++) {
                    result.push(this.keyMap[i][j]);
                }
            }
        }
        return result;
    }
}

h = new HashTable();
h.set('pink', 123);
console.log(h.set('cyan', 231));
console.log(h.set('tomato', 111));
console.log(h.set('orange', 1));
console.log(h.set('hello world', 2));
console.log(h.get('orange'));
console.log(h.keys());
console.log(h.values());
console.log(h.items());