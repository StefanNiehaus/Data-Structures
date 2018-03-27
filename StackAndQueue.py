class Empty(Exception):
    pass

class ArrayStack:
    def __init__(self):
        self.data = []

    def __len__(self):
        return len(self.data)

    def is_empty(self):
        return len(self.data) == 0

    def push(self, val):
        self.data.append(val)

    def top(self):
        if self.is_empty():
            raise Empty("Stack is empty")
        return self.data[-1]

    def pop(self):
        if self.is_empty():
            raise Empty("Stack is empty")
        return self.data.pop()

class ArrayQueue:
    def __init__(self, n=10):
        self.data = [None] * n
        self.front = 0
        self.num_of_elems = 0

    def __len__(self):
        return self.num_of_elems

    def is_empty(self):
        return self.num_of_elems == 0

    def enqueue(self, val):
        if self.num_of_elems == len(self.data):
            self.resize(2 * len(self.data))
        back = (self.front + self.num_of_elems) % len(self.data)
        self.data[back] = val
        self.num_of_elems += 1

    def dequeue(self):
        if self.is_empty():
            raise Empty("Empty Queue!")
        result = self.data[self.front]
        self.data[self.front] = None
        self.front = (self.front + 1) % len(self.data)
        self.num_of_elems -= 1
        if self.num_of_elems < len(self.data) // 4:
            self.resize(len(self.data) // 2)
        return result

    def first(self):
        if self.is_empty():
            raise Empty("Queue is empty")
        return self.data[self.front]

    def last(self):
        if self.is_empty():
            raise Empty("Queue is empty")
        back = (self.front + self.num_of_elems) % len(self.data)
        return self.data[back]

    def resize(self, capacity):
        old_data = self.data
        self.data = [None] * capacity
        for index in range(self.num_of_elems):
            self.data[index] = old_data[(self.front + index) % len(old_data)]
        self.front = 0

class ArrayDEQ:
    def __init__(self, n=10):
        self.data = [None] * n
        self.front = 0
        self.num_of_elems = 0

    def __len__(self):
        return self.num_of_elems

    def is_empty(self):
        return self.num_of_elems == 0

    def first(self):
        if self.is_empty():
            raise Empty("Queue is empty")
        return self.data[self.front]

    def last(self):
        if self.is_empty():
            raise Empty("Queue is empty")
        back = (self.front + self.num_of_elems) % len(self.data)
        return self.data[back]

    def add_first(self, val):
        if self.num_of_elems == len(self.data):
            self.resize(2 * len(self.data))
        self.front = (self.front - 1) % len(self.data)
        self.data[self.front] = val
        self.num_of_elems += 1

    def add_last(self, val):
        """enqueue"""
        if self.num_of_elems == len(self.data):
            self.resize(2 * len(self.data))
        back = (self.front + self.num_of_elems) % len(self.data)
        self.data[back] = val
        self.num_of_elems += 1

    def delete_first(self):
        """dequeue"""
        if self.is_empty():
            raise Empty("Empty Queue!")
        result = self.data[self.front]
        self.data[self.front] = None
        self.front = (self.front + 1) % len(self.data)
        self.num_of_elems -= 1
        if (self.num_of_elems < len(self.data) // 4):
            self.resize(len(self.data) // 2)
        return result

    def delete_last(self):
        if self.is_empty():
            raise Empty("Empty Queue!")
        back_index = (self.front + self.num_of_elems - 1) % len(self.data)
        result = self.data[back_index]
        self.data[back_index] = None
        self.num_of_elems -= 1
        if (self.num_of_elems < len(self.data) // 4):
            self.resize(len(self.data) // 2)
        return result

    def resize(self, new_capacity):
        old_data = self.data
        self.data = [None] * new_capacity
        for index in range(self.num_of_elems):
            self.data[index] = old_data[(self.front + index) % len(old_data)]
        self.front = 0
