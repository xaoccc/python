class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True
        temp = self.root
        while (True):
            if new_node.value == temp.value:
                return False
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else: 
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right

    def contains(self, value):
        temp = self.root
        while (temp is not None):
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else:
                return True
        return False 


    def __r_contains(self, current_node, value):
        if current_node == None: 
            return False      
        if value == current_node.value:
            return True 
        if value < current_node.value:
            return self.__r_contains(current_node.left, value) 
        if value > current_node.value:
            return self.__r_contains(current_node.right, value)

    def r_contains(self, value):
        return self.__r_contains(self.root, value)


    def __r_insert(self, current_node, value):
        if not current_node:
            return Node(value)
        if current_node.value > value:
            current_node.left = self.__r_insert(current_node.left, value)
        if current_node.value < value:
            current_node.right = self.__r_insert(current_node.right, value)
        return current_node

    def r_insert(self, value):
        if self.root is None:
            self.root = Node(value)
        self.__r_insert(self.root, value)




my_tree = BinarySearchTree()
my_tree.r_insert(2)
my_tree.r_insert(1)
my_tree.r_insert(6)


"""
    THE LINES ABOVE CREATE THIS TREE:
                 2
                / \
               1   3
"""


print('Root:', my_tree.root.value)            
print('Root -> Left:', my_tree.root.left.value)
print('Root -> Right:', my_tree.root.right.value)



"""
    EXPECTED OUTPUT:
    ----------------
	Root: 2
	Root -> Left: 1
	Root -> Right: 3

"""

