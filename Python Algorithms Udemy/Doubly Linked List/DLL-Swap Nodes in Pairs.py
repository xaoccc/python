class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.length = 1

    def print_list(self):
        output = []
        current_node = self.head
        while current_node is not None:
            output.append(str(current_node.value))
            current_node = current_node.next
        print(" <-> ".join(output))

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = new_node
            new_node.prev = temp
        self.length += 1
        return True

    def swap_pairs(self):
        if self.length <= 1:
            return


        dummy = Node(0)
        dummy.next = self.head
        previous = dummy

        while self.head and self.head.next:
            first_node = self.head
            second_node = self.head.next

            previous.next = second_node
            first_node.next = second_node.next
            second_node.next = first_node
            second_node.prev = previous
            first_node.prev = second_node

            if first_node.next:
                first_node.next.prev = first_node
            self.head = first_node.next
            previous = first_node
        self.head = dummy.next
        if self.head:
            self.head.prev = None






    def swap_nodes_values(self):
        if self.length <= 1:
            return

        current = self.head

        for i in range(self.length // 2):
            current.value, current.next.value = current.next.value, current.value
            current = current.next.next




my_dll = DoublyLinkedList(1)
my_dll.append(2)
my_dll.append(3)
my_dll.append(4)
my_dll.append(5)
my_dll.append(6)

print('my_dll before swap_pairs:')
my_dll.print_list()

my_dll.swap_pairs()

print('my_dll after swap_pairs:')
my_dll.print_list()

"""
    EXPECTED OUTPUT:
    ----------------
    my_dll before swap_pairs:
    1 <-> 2 <-> 3 <-> 4
    ------------------------
    my_dll after swap_pairs:
    2 <-> 1 <-> 4 <-> 3

"""