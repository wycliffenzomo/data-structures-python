class Queue:
    def __init__(self, max_size, para=None):
        if para is None:
            para = []
        self.queue = para
        self.max_size = max_size

    def peek(self):
        if not self.is_empty():
            return self.queue[0]
        return "Queue is empty"

    def enqueue(self, item):
        if not self.is_full():
            self.queue.append(item)
        else:
            return "Queue is full"

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        return "Queue is empty"

    def rear(self):
        if not self.is_empty():
            return self.queue[-1]
        return "Queue is empty"

    def is_full(self):
        return len(self.queue) >= self.max_size

    def is_empty(self):
        return len(self.queue) == 0
    def dequeue_asc(self):
      if not self.is_empty():
        min_val = min(self.queue)
        self.queue.remove(min_val)
        return min_val
      return "Queue is empty"

    def display_queue(self):
        print(self.queue)