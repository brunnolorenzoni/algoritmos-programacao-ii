from Node import Node

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __len__(self):
        return self.size

    def add(self, data):
        if(self.head):
            aux = self.head
            prev = None
            while(aux.next):
                prev = aux
                aux = aux.next
            aux.next = Node(data)
            aux.next.prev = aux
            aux.prev = prev
            if(self.tail):
                self.tail = aux.next
        else:
            self.head = Node(data)
            self.tail = Node(data)
        
        self.size = self.size + 1

    def printList(self):
        aux = self.head
        print('Lista', '\n')
        while(aux):
            print(aux.data, '\n')
            aux = aux.next

    def printReverseList(self):
        aux = self.tail
        print('Lista', '\n')
        while(aux):
            print(aux.data, '\n')
            aux = aux.prev