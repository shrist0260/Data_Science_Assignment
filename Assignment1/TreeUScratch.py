# Tree without using library 
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

root = Node(10)
root.left = Node(5)
root.right = Node(15)

print("Root:", root.value)
print("Left child:", root.left.value)
print("Right child:", root.right.value)