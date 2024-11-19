class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node

        
    def append(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        return True
        

    def find_middle_node(self):
        slow_node = self.head
        fast_node = self.head
        while fast_node.next:
            slow_node = slow_node.next
            # For even number of nodes we return the first node of the second half
            # If We should have returned the last node of the first half, we should move slow_node = slow_node.next aftre the if condition
            if not fast_node.next.next:
                break
            fast_node = fast_node.next.next            
        return slow_node    

linked_list = LinkedList(1)
linked_list.append(2)
linked_list.append(3)
linked_list.append(4)
linked_list.append(5)
linked_list.append(6)
linked_list.append(7)
linked_list.append(8)
linked_list.find_middle_node()