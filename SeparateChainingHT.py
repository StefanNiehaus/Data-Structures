"""
SeparateChainingMap
Implement a Map with a hash table, using separate chaining.
"""

class SeparateChaining:

    def __init__(self, length=10):
        self.table = [[] for _ in range(length)]
        self.size = 0

    def __len__(self):
        return self.size

    def __setitem__(self, key, value):
        print('inserting:', key, value)
        index = self._hash(key)
        for key_val in self.table[index]:
            if key == key_val[0]:
                key_val[1] = value
                return
        self.table[index].append([key, value])
        self.size += 1
        if self.size > len(self.table):
            self._resize(2*len(self.table))

    def __getitem__(self, key):
        index = self._hash(key)
        for k, v in self.table[index]:
            if key == k:
                return v
        raise KeyError

    def __delitem__(self, key):
        index = self._hash(key)
        for i in range(len(self.table[index])):
            if key is self.table[index][i][0]:
                self.table[index].pop(i)
                self.size -= 1
                return
        raise KeyError

    def __iter__(self):
        for bucket in self.table:
            for key, _ in bucket:
                yield key

    def __contains__(self, key):
        index = self._hash(key)
        for k, _ in self.table[index]:
            if key == k:
                return True
        return False

    def _hash(self, key):
        return hash(key) % len(self.table)

    def _resize(self, newsize):
        print('resizing')
        old_table = self.table
        self.table = [[] for _ in range(newsize)]
        for bucket in old_table:
            for key_value in bucket:
                #self[key] = value
                index = self._hash(key_value[0])
                self.table[index].append(key_value)

def print_map(map):
    for key in map:
        print(key, map[key])

if __name__ == '__main__':
    sc = SeparateChaining(3)
    print_map(sc)
    print(17 in sc)
    print('========')
    sc[17] = 'john'
    print_map(sc)
    print(17 in sc)
    print(sc[17])
    print('========')
    sc[42] = 'paul'
    print_map(sc)
    print(sc.table)
    print('========')
    sc[17] = 'george'
    print_map(sc)
    print(sc.table)
    print('========')
    del sc[17]
    print(sc.table)
    print_map(sc)
    print('========')
    sc[13] = 'ringo'
    print_map(sc)
    sc[25] = 'moe'
    sc[26] = 'larry'
    sc[27] = 'curly'
    sc[28] = 'groucho'
    print_map(sc)
    print(sc.table)
