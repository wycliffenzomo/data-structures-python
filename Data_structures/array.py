class Array:
    def __init__(self, capacity):
        self.capacity = capacity
        self.data = []

    def insert(self, index, value):
        if len(self.data) >= self.capacity:
            print("Array is full. Cannot insert.")
            return
        if index < 0 or index > len(self.data):
            print("Index out of bounds.")
            return
        self.data.insert(index, value)

    def delete(self, index):
        if index < 0 or index >= len(self.data):
            print("Index out of bounds.")
            return
        self.data.pop(index)

    def access(self, index):
        if index < 0 or index >= len(self.data):
            return "Index out of bounds"
        return self.data[index]

    def update(self, index, value):
        if index < 0 or index >= len(self.data):
            print("Index out of bounds.")
            return
        self.data[index] = value

    def search(self, value):
        try:
            return self.data.index(value)
        except ValueError:
            return -1

    def is_full(self):
        return len(self.data) == self.capacity

    def is_empty(self):
        return len(self.data) == 0

    def display(self):
        print("Array contents:", self.data)
