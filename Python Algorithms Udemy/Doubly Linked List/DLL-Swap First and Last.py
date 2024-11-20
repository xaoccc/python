class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True

    # Swap nodes
    # def swap_first_last(self):
    #     if self.length <= 1:
    #         return
    #     first = self.head
    #     last = self.tail
    #     second = self.head.next
    #     before_last = self.tail.prev
    #
    #     first.next = None
    #     first.prev = before_last
    #     before_last.next = first
    #     self.tail = first
    #
    #     last.prev = None
    #     last.next = second
    #     second.prev = last
    #     self.head = last

    # Swap nodes' values
    def swap_first_last(self):
        if self.length <= 1:
            return
        self.head.value, self.tail.value = self.tail.value, self.head.value




my_doubly_linked_list = DoublyLinkedList(1)
my_doubly_linked_list.append(2)
my_doubly_linked_list.append(3)
my_doubly_linked_list.append(4)
my_doubly_linked_list.append(5)

print('DLL before swap_first_last():')
my_doubly_linked_list.print_list()

my_doubly_linked_list.swap_first_last()

print('\nDLL after swap_first_last():')
my_doubly_linked_list.print_list()

"""
    EXPECTED OUTPUT:
    ----------------
    DLL before swap_first_last():
    1
    2
    3
    4

    DLL after swap_first_last():
    4
    2
    3
    1

"""

