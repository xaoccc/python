class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None # This is the difference from the LL
        
class DoublyLinkedList:
    def __init__(self, value):
        node = Node(value)
        self.head = node
        self.tail = node
        self.length = 1
  



my_doubly_linked_list = DoublyLinkedList(7)

print('Head:', my_doubly_linked_list.head.value)
print('Tail:', my_doubly_linked_list.tail.value)
print('Length:', my_doubly_linked_list.length)



"""
    EXPECTED OUTPUT:
    ----------------
    Head: 7
    Tail: 7
    Length: 1

"""
