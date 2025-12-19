# Queue without using library 
class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, value):
        self.items.append(value)

    def dequeue(self):
        return self.items.pop(0)

q = Queue()
q.enqueue(10)
q.enqueue(20)
print("Dequeued:", q.dequeue())