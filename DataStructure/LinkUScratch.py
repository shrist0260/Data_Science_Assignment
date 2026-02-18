# linked_list without using library
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def display(self):
        temp = self.head
        while temp:
            print(temp.value)
            temp = temp.next

ll = LinkedList()
ll.insert(10)
ll.insert(20)
ll.insert(30)
ll.display()