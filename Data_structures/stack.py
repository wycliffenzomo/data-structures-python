class Stack:
    def __init__(self,items):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop() if not self.is_empty() else None

    def peek(self):
        return self.items[-1] if not self.is_empty() else None

    def is_empty(self):
        return len(self.items) == 0

    def display_stack(self):
        print("Stack:", self.items)

    def top(self):
        return self.peek()

    def isempty(self):
        return self.is_empty()

    def size(self):
        return len(self.items)
