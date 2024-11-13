class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        node = Node(value)
        self.head = node
        self.tail = node
        self.length = 1

    def print_list(self):
        temp = self.head
        while (temp is not None):
            print(temp.value)
            temp = temp.next





my_ll = LinkedList(4)
my_ll.append(7)
my_ll.append(13)
my_ll.append(23)
my_ll.append(56)
my_ll.append(12)

my_ll.print_list()
my_ll.pop()

my_ll.print_list()