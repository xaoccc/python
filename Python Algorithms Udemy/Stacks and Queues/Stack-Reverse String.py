class Stack:
    def __init__(self):
        self.stack_list = []

    def print_stack(self):
        for i in range(len(self.stack_list)-1, -1, -1):
            print(self.stack_list[i])

    def is_empty(self):
        return len(self.stack_list) == 0

    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.stack_list[-1]

    def size(self):
        return len(self.stack_list)

    def push(self, value):
        self.stack_list.append(value)

    def pop(self):
        if self.is_empty():
            return None
        else:
            return self.stack_list.pop()



def reverse_string(my_string):
    my_string_to_stack = Stack()
    my_string_to_stack.stack_list = list(my_string)
    stack = Stack()
    while my_string_to_stack.stack_list:
        stack.push(my_string_to_stack.pop())

    return ''.join(stack.stack_list)




my_string = 'hello'

print ( reverse_string(my_string) )



"""
    EXPECTED OUTPUT:
    ----------------
    olleh

"""
