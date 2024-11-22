class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        

class BinarySearchTree:
    def __init__(self):
        self.root = None







my_tree = BinarySearchTree()

print(my_tree.root)

my_tree.append(10)
print(my_tree.root.value)
my_tree.append(15)
my_tree.append(12)
print(my_tree.root.right.left.value)
 
"""
    EXPECTED OUTPUT:
    ----------------
    None

"""