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
        if not self.root:
            self.root = new_node
        else:
            current = self.root
            while current:
                if current.value > value:
                    if not current.left:
                        current.left = new_node
                        return True
                    current = current.left
                elif current.value < value:
                    if not current.right:
                        current.right = new_node
                        return True
                    current = current.right
                else:
                    return False

    def in_order_print(self, root):
        if root is None:
            return
        self.in_order_print(root.left)
        print(root.value)
        self.in_order_print(root.right)





my_tree = BinarySearchTree()
my_tree.insert(15)
my_tree.insert(13)
my_tree.insert(23)
my_tree.insert(12)
my_tree.insert(45)
my_tree.insert(345)
my_tree.insert(2)
my_tree.insert(79)

my_tree.in_order_print(my_tree.root)

"""
    THE LINES ABOVE CREATE THIS TREE:
                 2
                / \
               1   3
"""


print('Root:', my_tree.root.value)            
print('Root->Left:', my_tree.root.left.value)        
print('Root->Right:', my_tree.root.right.value)        



"""
    EXPECTED OUTPUT:
    ----------------
    Root: 2
    Root->Left: 1
    Root->Right: 3

"""