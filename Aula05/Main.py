from Stack import Stack

stack = Stack()

stack.push(0)
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.printStack()
print('Topo: ' + str(stack.peek()))
stack.printStack()
print('Removido: ' + str(stack.pop()))
stack.printStack()