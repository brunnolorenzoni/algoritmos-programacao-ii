class Stack:
    def __init__(self):
        self.list = list()

    def __len__(self):
        return len(self.list)

    def isEmpty(self):
        return self.__len__ == 0

    def peek(self):
        if(self.isEmpty() is False):
            return self.list[-1]
        else:
            return print('Stack Empty')

    def pop(self):
        if(self.isEmpty() is False):
            return self.list.pop()
        else:
            return print('Stack Empty')

    def push(self, data):
        return self.list.append(data)

    def printStack(self):
        #Print reverse
        return print(*self.list[::-1]) 