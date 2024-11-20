class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class Queue:
    def __init__(self, value):
        node = Node(value)
        self.first = node

    def print_queue(self):
        temp = self.first
        while temp is not None:
            print(temp.value)
            temp = temp.next




my_queue = Queue(4)

my_queue.print_queue()



"""
    EXPECTED OUTPUT:
    ----------------
    4

"""