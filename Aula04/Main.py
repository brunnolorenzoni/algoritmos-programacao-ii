from Queue import Queue
import random

fila = Queue()
loop_range = random.randint(1,100)

while (loop_range):
    binary = random.randint(0,1000)
    fila.add(binary)
    loop_range -= 1

fila.print()