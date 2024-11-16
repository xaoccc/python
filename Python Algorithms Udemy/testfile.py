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
        current = self.head
        while current:
            print(current.value)
            current = current.next

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

        temp = self.head
        self.length -= 1
        
        if self.length == 0:
            self.head = None
            self.tail = None
            return temp

        while temp.next:
            current = temp
            temp = temp.next
        self.tail = current
        self.tail.next = None
        return temp

    def prepend(self, value):
        new_node = Node(value)
        self.length += 1
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node            
        return True

    def pop_first(self):
        if self.length == 0:
            return None

        node_to_remove = self.head
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            node_to_remove.next = None
        return node_to_remove

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for i in range(self.length):
            if i == index:
                return temp
            temp = temp.next

    def set_value(self, index, value):
        if not self.get(index):
            return False
        self.get(index).value = value
        return True

    def insert(self, index, value):      
        if index < 0 or index > self.length:
            return False
        if index == 0:
            self.prepend(value)
        elif index == self.length:          
            self.append(value)
        else:
            new_node = Node(value)
            node_before = self.get(index - 1)            
            node_after = self.get(index)
            node_before.next = new_node            
            new_node.next = node_after
            self.length += 1
        return True

    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            self.pop_first(value)
        elif index == self.length - 1:          
            self.pop()
        else:
            node_before = self.get(index - 1)
            node_to_remove = self.get(index)
            node_before.next = node_to_remove.next
            node_to_remove.next = None
        self.length -= 1
        return node_to_remove

    def reverse(self):
        
        temp = self.head
        self.head = self.tail
        self.tail = temp

        after = temp.next
        before = None

        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after






linked_list = LinkedList(5)
print(f'length: {linked_list.length}')
linked_list.append(7)
print(f'length: {linked_list.length}')
linked_list.append(13)
print(f'length: {linked_list.length}')
linked_list.append(24)
print(f'length: {linked_list.length}')
linked_list.append(58)
print(f'length: {linked_list.length}')
linked_list.prepend(23)
print(f'length: {linked_list.length}')
linked_list.insert(6, 112)
print(f'length: {linked_list.length}')
print('Updated list:')
linked_list.print_list()

linked_list.reverse()

print('Updated list:')
linked_list.print_list()

