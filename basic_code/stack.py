
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if len(self.itmes) == 0:
            print("Stack is empty!!")
            exit()
        return self.items.pop()

    def __len__(self):
        return len(self.items)

    def isEmpty(self):
        return True if (len(self.itmes) == 0) else False
