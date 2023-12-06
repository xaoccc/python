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

root = Node(5)
root.create(7)
root.create(3)
root.create(9)
root.create(23)
root.create(1)


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

# def bfs(root):
#     queue = {}
#     queue[root.data] = []
#     if root.left is not None:
#         queue[root.data].append(root.left.data)
#         bfs(root.left)
#
#     if root.right is not None:
#         queue[root.data].append(root.right.data)
#         bfs(root.right)
#
#     return queue

dict = {}
def bfs(root):
    if root is None:
        return

    dict[root.data] = []
    bfs(root.left)
    bfs(root.right)

    if root.left is not None:
        dict[root.data].append(root.left.data)

    if root.right is not None:
        dict[root.data].append(root.right.data)

    return dict


print(bfs(root))


def make_bfs_list(bfs):
    bfs_list = []
    for key, value in bfs.items():
        if key not in bfs_list:
            bfs_list.append(key)
            bfs_list += value
    return bfs_list


print(make_bfs_list(bfs(root)))
