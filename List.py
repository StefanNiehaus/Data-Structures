import ctypes

class MyList:
    """Constructing a more beautiful list."""
    def __init__(self):
        self.size = 0
        self.capacity = 1
        self.data = self.make_array(self.capacity)

    def __len__(self):
        return self.size

    def __setitem__(self, index, value):
        if index < 0:
            index = len(self) + index
        if index >= self.size:
            raise IndexError("Invalid Index!")
        if index < 0:
            raise IndexError("Invalid Index!")
        self.data[index] = value

    def __getitem__(self, index):
        if index < 0:
            index = len(self) + index
        if index >= self.size:
            raise IndexError("Invalid Index!")
        if index < 0:
            raise IndexError("Invalid Index!")
        return self.data[index]

    def __str__(self):
        return '[' + ', '.join([str(self.data[index]) for index in range(self.size)]) + ']'

    def __repr__(self):
        return self.__str__()

    def __add__(self, other):
        new_MyList = MyList()
        new_MyList.extend(self)
        new_MyList.extend(other)
        return new_MyList

    def __iadd__(self, other):
        self.extend(other)
        return self

    def __mul__(self, rhs):
        new_lst = MyList()
        for i in range(rhs):
            new_lst.extend(self)
        return new_lst

    def __rmul__(self, lhs):
        return self * lhs

    def append(self, value):
        if self.size == self.capacity:
            self.resize(2 * self.capacity)
        self.data[self.size] = value
        self.size += 1

    def resize(self, new_capacity):
        """Resize array"""
        new_data = self.make_array(new_capacity)
        for index in range(self.size):
            new_data[index] = self.data[index]
        self.capacity = new_capacity
        self.data = new_data

    def make_array(self, capacity):
        return (capacity * ctypes.py_object)()

    def extend(self, other):
        """In-line extension of current list"""
        # Allow for lists
        if type(other) is list:
            othersize = len(other)
        else:
            othersize = other.size
        # Resize appropriately
        changed_capacity = False
        if (self.size + othersize) > self.capacity:
            self.capacity *= 2
            changed_capacity = True
        if changed_capacity:
            self.resize(self.capacity)
        # Perform extension
        for val in other:
            self.append(val)

    def insert(self, index, val):
        """
        myList.insert(0, x) inserts x at the front of the list,
        and myList.insert(len(myList), x) is equivalent to myList.append(x)
        """
        # Allow for negative indexing
        if index < 0:
            index = len(self) + index
        # Check for valid index
        if index > self.size or index < 0:
            raise IndexError("Out of Range")
        # Resize if necessary
        if self.size == self.capacity:
            self.resize(2 * self.capacity)
        if index == self.size:
            self.append(val)
            return
        data_copy_left = self.data[index]
        for shift_index in range(index+1, self.size+1):
            if shift_index == self.size:
                self.append(data_copy_left)
            data_copy_right = self.data[shift_index]
            self.data[shift_index] = data_copy_left
            data_copy_left = data_copy_right
        self.data[index] = val

    def pop(self):
        """Pop off the end element"""
        # Emptry list, raise error
        if self.size == 0:
            raise IndexError("Emptry list, no element to pop!")
        # Resize if necessary
        if self.size == self.capacity/4:
            self.resize(int(self.capacity/2))
        # Do the pop
        popped_value = self.data[self.size-1]
        self.data[self.size-1] == None
        self.size -= 1
        return popped_value
