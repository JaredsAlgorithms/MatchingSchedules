class Stack:
    def __init__(self):
        self.container = []

    def pop(self):
        self.container.pop()

    def push(self, value):
        self.container.append(value)

    def peek(self):
        return self.container[-1]

    def empty(self):
        return len(self.container) == 0
