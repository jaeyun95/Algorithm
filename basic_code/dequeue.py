
class Deque:
    def __init__(self):
        self.items = []

    def enqueue_front(self, item):
        self.items.insert(0, item)

    def enqueue_back(self, item):
        self.items.append(item)

    def dequeue_front(self):
        if len(self.itmes) == 0:
            print("Deque is empty!!")
            exit()
        return self.items.pop(0)

    def dequeue_back(self):
        if len(self.itmes) == 0:
            print("Deque is empty!!")
            exit()
        return self.items.pop()

    def __len__(self):
        return len(self.items)

    def isEmpty(self):
        return True if (len(self.itmes) == 0) else False
