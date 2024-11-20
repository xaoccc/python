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
        # Creating a dummy and a previous separately is because dummy will stay here, but previous node will be changed
        dummy.next = self.head
        previous = dummy

        while self.head and self.head.next:
            first_node = self.head
            second_node = self.head.next
            # Main logic
            # Point the dummy node to the second node (the new first node)
            previous.next = second_node
            # Point the first node to the third node (second_node.next) (previously it pointed to the second node)
            first_node.next = second_node.next
            # Point the second node to the first node (previously it pointed to the third node)
            second_node.next = first_node
            # Point the second node to the previous (which equals dummy only at the first iteration)
            second_node.prev = previous
            # Point the first node to the second but not as next, but as previous, e.g. first is now after second
            first_node.prev = second_node

            # Check if we've reached the last pair
            if first_node.next:
                first_node.next.prev = first_node
            # Update the head pointer on each iteration, so that first_node and second_node are the nodes of the new pair
            self.head = first_node.next
            # Update previous pointer as well, but dummy still points to the head
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