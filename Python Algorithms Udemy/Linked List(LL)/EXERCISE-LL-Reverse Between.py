class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.length = 1

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
        self.length += 1
        return True

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def make_empty(self):
        self.head = None
        self.length = 0

    def reverse_between(self, start, end):

        if self.length < 2:
            return
        # 1.2 Create dummy node with value 0
        dummy = Node(0)
        # 1.3 Point dummy node's next to head of list
        dummy.next = self.head
        #  1.4 Initialize previous_node to dummy node
        previous_node = dummy

        # 1.5 Loop for start_index times to find previous_node
        for i in range(start):
            # 1.5.1 Update previous_node to its next node
            previous_node = previous_node.next
        # 1.6 Initialize current_node to previous_node's next node
        current_node = previous_node.next


        #  1.7 Loop from 0 to (end_index - start_index) - flip two nodes in 4 steps
        for j in range(end - start):
            # 1.7.1 Initialize node_to_move to current_node's next
            node_to_move = current_node.next
            # 1.7.2 Update current_node's next to node_to_move's next
            current_node.next = node_to_move.next
            # 1.7.3 Update node_to_move's next to previous_node's next
            node_to_move.next = previous_node.next
            # 1.7.4 Update previous_node's next to node_to_move
            previous_node.next = node_to_move
        # 1.8 Update head to dummy_node's next node
        self.head = dummy.next




linked_list = LinkedList(1)
linked_list.append(2)
linked_list.append(3)
linked_list.append(4)
linked_list.append(5)

print("Original linked list: ")
linked_list.print_list()

# Reverse a sublist within the linked list
linked_list.reverse_between(2, 4)
print("Reversed sublist (2, 4): ")
linked_list.print_list()

# Reverse another sublist within the linked list
linked_list.reverse_between(0, 4)
print("Reversed entire linked list: ")
linked_list.print_list()

# Reverse a sublist of length 1 within the linked list
linked_list.reverse_between(3, 3)
print("Reversed sublist of length 1 (3, 3): ")
linked_list.print_list()

# Reverse an empty linked list
empty_list = LinkedList(0)
empty_list.make_empty()
empty_list.reverse_between(0, 0)
print("Reversed empty linked list: ")
empty_list.print_list()

"""
    EXPECTED OUTPUT:
    ----------------
    Original linked list: 
    1
    2
    3
    4
    5
    Reversed sublist (2, 4): 
    1
    2
    5
    4
    3
    Reversed entire linked list: 
    3
    4
    5
    2
    1
    Reversed sublist of length 1 (3, 3): 
    3
    4
    5
    2
    1
    Reversed empty linked list: 
    None

"""
