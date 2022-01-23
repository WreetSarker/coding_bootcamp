# Implement a hash table

class HashTable:
    def __init__(self, size=53):
        self.keyMap = [None for i in range(size)]

    def _hash(self, key):
        total = 0
        FIXED_PRIME = 31
        for i in range(min(len(key), 100)):
            value = ord(key[i]) - 96
            total = (total * FIXED_PRIME + value) % len(self.keyMap)
        return total

    def set_val(self, key, val):
        idx = self._hash(key)
        if self.keyMap[idx] is None:
            self.keyMap[idx] = []
        self.keyMap[idx].append([key, val])
        return True

    def get(self, key):
        idx = self._hash(key)
        if self.keyMap[idx] is not None:
            for i in range(len(self.keyMap[idx])):
                if self.keyMap[idx][i][0] == key:
                    return self.keyMap[idx][i][1]
        return None

    def keys(self):
        result = []
        for i in range(len(self.keyMap)):
            if self.keyMap[i] is not None:
                for j in range(len(self.keyMap[i])):
                    result.append(self.keyMap[i][j][0])
        return result

    def values(self):
        result = []
        for i in range(len(self.keyMap)):
            if self.keyMap[i] is not None:
                for j in range(len(self.keyMap[i])):
                    result.append(self.keyMap[i][j][1])
        return result

    def items(self):
        result = []
        for i in range(len(self.keyMap)):
            if self.keyMap[i] is not None:
                for j in range(len(self.keyMap[i])):
                    result.append(self.keyMap[i][j])
        return result


h = HashTable()
h.set_val('pink', 123)
print(h.set_val('cyan', 231))
print(h.set_val('tomato', 111))
print(h.set_val('orange', 1))
print(h.set_val('hello world', 2))
print(h.get('orange'))
print(h.keys())
print(h.values())
print(h.items())
