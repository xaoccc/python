class Stack:
    def __init__(self):
        self.stack_list = []

    def print_stack(self):
        for i in range(len(self.stack_list) - 1, -1, -1):
            print(self.stack_list[i])

    def push(self, value):
        self.stack_list.append(value)


my_stack = Stack()
my_stack.push(1)
my_stack.push(2)
my_stack.push(3)

my_stack.print_stack()

"""
    EXPECTED OUTPUT:
    ----------------
    3 
    2
    1

"""