class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insertAtBeginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insertAtEnd(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def insertAfter(self, data, after):
        temp = self.head
        while temp and temp.data != after:
            temp = temp.next
        if temp:
            new_node = Node(data)
            new_node.next = temp.next
            temp.next = new_node

    def deleteItem(self, key):
        temp = self.head
        if temp and temp.data == key:
            self.head = temp.next
            return
        prev = None
        while temp and temp.data != key:
            prev = temp
            temp = temp.next
        if temp:
            prev.next = temp.next

    def search(self, key):
        temp = self.head
        while temp:
            if temp.data == key:
                return True
            temp = temp.next
        return False

    def get_length(self):
        count = 0
        temp = self.head
        while temp:
            count += 1
            temp = temp.next
        return count

    def access(self, index):
        temp = self.head
        for _ in range(index):
            if temp is None:
                return None
            temp = temp.next
        return temp.data if temp else None

    def update(self, index, new_data):
        temp = self.head
        for _ in range(index):
            if temp is None:
                return
            temp = temp.next
        if temp:
            temp.data = new_data

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def sort(self):
        if self.head is None:
            return
        changed = True
        while changed:
            changed = False
            current = self.head
            while current.next:
                if current.data > current.next.data:
                    current.data, current.next.data = current.next.data, current.data
                    changed = True
                current = current.next

    def display(self):
        result = []
        temp = self.head
        while temp:
            result.append(temp.data)
            temp = temp.next
        print("LinkedList:", result)

