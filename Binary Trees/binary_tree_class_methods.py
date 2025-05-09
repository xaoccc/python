class BinaryTree:
    def __init__(self, root):
        self.root = root
        self.left = None
        self.right = None
    def create(self, data):
        if not self.root:
            self.root = data
        elif data < self.root:
            if not self.left:
                self.left = BinaryTree(data)
            else:
                self.left.create(data)
        elif data > self.root:
            if not self.right:
                self.right = BinaryTree(data)
            else:
                self.right.create(data)
    def delete(self, data):
        if data < self.root:
            if self.left:
                self.left = self.left.delete(data)
        elif data > self.root:
            if self.right:
                self.right = self.right.delete(data)
        else:
            if not self.left and not self.right:
                # Returning None instead of BinaryTree(None) prevents from having phantom nodes between other nodes
                return None
            if not self.left:
                return self.right
            if not self.right:
                return self.left
            min_larger_node = self.right.get_min()
            self.root = min_larger_node.root
            self.right = self.right.delete(min_larger_node.root)

        return self
    def get_min(self):
        current = self
        while current.left:
            current = current.left
        return current

    def get_max(self):
        current = self
        while current.right:
            current = current.right
        return current

    def print_in_order(self):
        if self.left:
            self.left.print_in_order()
        print(self.root)
        if self.right:
            self.right.print_in_order()

    def reversed_print(self):
        if self.right:
            self.right.reversed_print()
        print(self.root)
        if self.left:
            self.left.reversed_print()

    def find_node(self, data):
        current = self
        steps = 0
        while current:
            steps += 1
            if current.root == data:
                print(f'steps: {steps}')
                return current
            elif current.root > data:
                current = current.left
            elif current.root < data:
                current = current.right
        print(f'steps: {steps}')
        return False

    def sum_subtree(self, data):
        subtree = self.find_node(data)
        def sum_subtree_values(node):
            sum_values = node.root
            if node.left:
                sum_values += sum_subtree_values(node.left)
            if node.right:
                sum_values += sum_subtree_values(node.right)
            return sum_values
        return sum_subtree_values(subtree)










# We can use also external function, just replace self with the instance of the binary tree:
def get_max(binary_tree):
    current = binary_tree
    while current.right:
        current = current.right
    return current


binary_tree = BinaryTree(5)
# delete method returns the updated binary tree, so we wee to assign, not just execute
binary_tree = binary_tree.delete(5)
print(binary_tree)
binary_tree = BinaryTree(17)
binary_tree.create(15)
binary_tree.create(12)
binary_tree.create(13)
binary_tree.create(14)
binary_tree.create(10)
binary_tree.create(8)
binary_tree.create(3)
binary_tree.create(4)
binary_tree = binary_tree.delete(12)

# print(binary_tree.left.left.root)
binary_tree = binary_tree.delete(13)
# print(binary_tree.left.left.root)
binary_tree.create(45)
# print(binary_tree.get_max().root)
binary_tree.create(87)
# print(binary_tree.get_max().root)
binary_tree.create(204)
# Using the method:
# print(binary_tree.get_max().root)

# Using the external function:
# print(get_max(binary_tree).root)

binary_tree.print_in_order()
print(binary_tree.find_node(4))
binary_tree.reversed_print()
print(binary_tree.sum_subtree(17))
