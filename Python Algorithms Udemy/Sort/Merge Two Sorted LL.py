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
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def merge(self, other_list):
        current_one = self.head
        current_two = other_list.head
        merged_list = LinkedList(0)
        merged_list_current = merged_list.head

        while current_one and current_two:
            if current_one.value > current_two.value:
                merged_list_current.next = Node(current_two.value)
                current_two = current_two.next
            else:
                merged_list_current.next = Node(current_one.value)
                current_one = current_one.next
            merged_list_current = merged_list_current.next
            merged_list.length += 1

        while current_one:
            merged_list_current.next = Node(current_one.value)
            current_one = current_one.next

        while current_two:
            merged_list_current.next = Node(current_two.value)
            current_two = current_two.next

        self.head = merged_list.head.next
        merged_list.head.next = None
        self.tail = merged_list_current
        self.length = merged_list.length

        # def merge(self, other_list):
        #     other_head = other_list.head
        #     dummy = Node(0)
        #     current = dummy
        #
        #     while self.head is not None and other_head is not None:
        #         if self.head.value < other_head.value:
        #             current.next = self.head
        #             self.head = self.head.next
        #         else:
        #             current.next = other_head
        #             other_head = other_head.next
        #         current = current.next
        #
        #     if self.head is not None:
        #         current.next = self.head
        #     else:
        #         current.next = other_head
        #         self.tail = other_list.tail
        #
        #     self.head = dummy.next
        #     self.length += other_list.length





l1 = LinkedList(1)
l1.append(3)
l1.append(5)
l1.append(7)

l2 = LinkedList(1)
l2.append(3)
l2.append(6)
l2.append(8)

l1.merge(l2)

l1.print_list()

"""
    EXPECTED OUTPUT:
    ----------------
    1 
    2 
    3 
    4 
    5 
    6 
    7
    8

"""