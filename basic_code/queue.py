
class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        if len(self.itmes) == 0:
            print("Queue is empty!!")
            exit()
        return self.items.pop()

    def __len__(self):
        return len(self.items)

    def isEmpty(self):
        return True if (len(self.itmes) == 0) else False
