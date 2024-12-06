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

    def bubble_sort(self):
        if self.length <= 1:
            return
        current_node = self.head
        helper_list = []
        while current_node:
            helper_list.append(current_node.value)
            current_node = current_node.next

        for i in range(len(helper_list) - 1, 0, -1):
            for j in range(len(helper_list) - 1):
                if helper_list[j] > helper_list[j + 1]:
                    temp = helper_list[j]
                    helper_list[j] = helper_list[j + 1]
                    helper_list[j + 1] = temp

        current_node = self.head
        for k in range(len(helper_list)):
            current_node.value = helper_list[k]
            current_node = current_node.next
            
    # Directly on the LL
    # def bubble_sort(self):
    #     if self.length < 2:
    #         return
    #
    #     sorted_until = None
    #
    #     while sorted_until != self.head.next:
    #         current = self.head
    #         while current.next != sorted_until:
    #             next_node = current.next
    #             if current.value > next_node.value:
    #                 current.value, next_node.value = next_node.value, current.value
    #             current = current.next
    #         sorted_until = current









my_linked_list = LinkedList(4)
my_linked_list.append(2)
my_linked_list.append(6)
my_linked_list.append(5)
my_linked_list.append(1)
my_linked_list.append(3)

print("Linked List Before Sort:")
my_linked_list.print_list()

my_linked_list.bubble_sort()

print("\nSorted Linked List:")
my_linked_list.print_list()

"""
    EXPECTED OUTPUT:
    ----------------
    Linked List Before Sort:
    4
    2
    6
    5
    1
    3

    Sorted Linked List:
    1
    2
    3
    4
    5
    6

"""

