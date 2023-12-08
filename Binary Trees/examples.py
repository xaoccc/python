
from collections import deque


class Node:
    def __init__(self, data):
        # left tree branch
        self.left = None
        # right tree branch
        self.right = None
        # head
        self.data = data

    def create(self, data):
        # if head has no data, we insert current data
        if self.data is None:
            self.data = data

        # then check left branch
        elif data < self.data:
            # if empty, populate it with data
            if self.left is None:
                self.left = Node(data)
            # if the branch has data, it becomes the head of a new branch, and we create the new branch.
            # recursively we search for an empty branch on the left until we find one
            else:
                self.left.create(data)

        # repeat the same check for the right branch
        elif data > self.data:
            if self.right is None:
                self.right = Node(data)
            else:
                self.right.create(data)

root = Node(4)
root.create(8)
root.create(5)
root.create(0)
root.create(1)
root.create(6)


def in_order_print(root):
    if root.right is not None:
        in_order_print(root.right)
    if root.left is not None:
        in_order_print(root.left)
    print(root.data)


def pre_order_print(root):
    print(root.data)
    if root.left is not None:
        pre_order_print(root.left)
    if root.right is not None:
        pre_order_print(root.right)


def post_order_print(root):
    if root.left is not None:
        post_order_print(root.left)
    if root.right is not None:
        post_order_print(root.right)
    print(root.data)


def draw_tree(root):
    tree = []
    tree.append(root.data)
    if root.left is not None:
        tree.append(draw_tree(root.left))

    if root.right is not None:
        tree.append(draw_tree(root.right))

    return tree

# print(draw_tree(root))


dict = {}
def tree_dict(root):
    if root is None:
        return

    dict[root.data] = []
    tree_dict(root.left)
    tree_dict(root.right)

    if root.left is not None:
        dict[root.data].append(root.left.data)

    if root.right is not None:
        dict[root.data].append(root.right.data)

    return dict


# print(tree_dict(root))


def bfs(td):
    # the first node is the root. We add it to the queue.
    queue = deque([root.data])
    # here we can store all nodes in bfs in a dictionary for better visualization
    visited = {}

    while queue:
        # We remove each first node, starting from the root.
        node = queue.popleft()
        # We add the node with its children in the dictionary
        visited[node] = [x for x in td[node]]
        # Then we add the children of the current node in the queue
        # Using the method of queue + append, ensures the bfs, in other words, we add nodes layer by layer
        [queue.append(x) for x in td[node]]
    return visited

# print(bfs(tree_dict(root)))

nodes_sums = []

def find_sums_of_each_subtree(node):
    if node is None:
        return

    left, right = 0, 0
    if node.left:
        left = find_sums_of_each_subtree(node.left)

    if node.right:
        right = find_sums_of_each_subtree(node.right)

    print(left, right, node.data)
    nodes_sum = left + right + node.data
    nodes_sums.append(nodes_sum)

    return node.data

# print(find_sums_of_each_subtree(root))
# print(nodes_sums)

# dfs method is different from bfs basically with the fact we use stack, instead of queue
def dfs(td):
    stack = [root.data]
    visited = {}
    while stack:
        # We remove each LAST node, starting from the root.
        # Thus, if the last node is lower level,
        #  - we use it as current node
        #  - remove it from the stack
        #  - continue moving down, until we find a node with no children
        #  - when find such node, we go up and look for unvisited nodes and check their children as well
        node = stack.pop()

        # here we have a condition, where we check if the node is visited,
        # so we do not add a node twice, while returning
        if node not in visited:
            visited[node] = [x for x in td[node]]
            stack += [x for x in td[node]]

    return visited
# print(dfs(tree_dict(root)))


# Breadth First Search taking just the root node as an argument
binary_tree_bfs = {}
def bfs_root(node):
    if node is None:
        return

    binary_tree_bfs[node.data] = []
    bfs_root(node.left)
    bfs_root(node.right)

    if node.left is not None:
        binary_tree_bfs[node.data].append(node.left.data)

    if node.right is not None:
        binary_tree_bfs[node.data].append(node.right.data)

    queue = deque([root.data])
    visited = {}

    while queue:
        node_to_check = queue.popleft()
        visited[node_to_check] = [x for x in binary_tree_bfs[node_to_check]]
        [queue.append(x) for x in binary_tree_bfs[node_to_check]]

    return visited

print(bfs_root(root))

binary_tree_dfs = {}

# Depth First Search taking just the root node as an argument
def dfs_root(node):
    if node is None:
        return

    binary_tree_dfs[node.data] = []
    dfs_root(node.left)
    dfs_root(node.right)

    if node.left is not None:
        binary_tree_dfs[node.data].append(node.left.data)

    if node.right is not None:
        binary_tree_dfs[node.data].append(node.right.data)

    stack = [root.data]
    visited = {}

    while stack:

        node_to_check = stack.pop()

        if node_to_check not in visited:
            visited[node_to_check] = [x for x in binary_tree_dfs[node_to_check]]
            stack += [x for x in binary_tree_dfs[node_to_check]]

    return visited

print(dfs_root(root))