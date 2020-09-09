from Node import Node

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def add(self, data):
        node = Node(data)
        if(self.head is None):
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.size += 1

    def pop(self):
        if(self.head is not None):
            self.head = self.head.next
            self.size -= 1

    def print(self):
        if(self.head is not None):
            print_text = ''
            current = self.head
            while(current):
                print_text += '[' + str(current.data) + ']'
                current = current.next
            print(print_text)
        else:
            print('Empty Queue')
    