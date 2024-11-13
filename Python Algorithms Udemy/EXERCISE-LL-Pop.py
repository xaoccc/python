class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        

class LinkedList:
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
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    def pop(self):
        if self.length == 0:
            return None

        node_to_remove = self.head

        if self.length == 1:
            self.length = 0
            self.head = None
            self.tail = None
            return node_to_remove

        new_last_node = node_to_remove
        # If the node does not have a next node, then it is the last one
        while (node_to_remove.next):
            # After the loop, we will have this node as the last one:
            new_last_node = node_to_remove
            node_to_remove = node_to_remove.next
        # Disconnect the new last node from the old last node
        self.tail = new_last_node
        self.tail.next = None
        self.length -= 1
        return node_to_remove


 


my_linked_list = LinkedList(1)
my_linked_list.append(2)

# (2) Items - Returns 2 Node
print(my_linked_list.pop().value)
# (1) Item -  Returns 1 Node
print(my_linked_list.pop().value)
# (0) Items - Returns None
print(my_linked_list.pop())


"""
    EXPECTED OUTPUT:
    ----------------
    2
    1
    None

"""