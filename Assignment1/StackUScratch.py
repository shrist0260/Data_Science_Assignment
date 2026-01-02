#Stack without using library
class Stack:
    def __init__(self):
        self.items = []

    def push(self, value):
        self.items.append(value)

    def pop(self):
        return self.items.pop()

self= Stack()
self.push(10)
self.push(20)
print("Popped:", self.pop())