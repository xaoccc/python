class Solution(object):
    # store the result in a class variable
    result = 0

    def averageOfSubtree(self, root):

        def tree(node):
            if not node:
                return 0, 0
            # look recursively in the left and on the right side of the tree:
            left = tree(node.left)
            right = tree(node.right)
            # for each subtree, we find the sum and the number of all nodes
            nodes_sum = left[0] + right[0] + node.val
            nodes_count = left[1] + right[1] + 1

            # check if the average node value is equal to the value of the root node
            if node.val == nodes_sum // nodes_count:
                # store each new success in the class variable
                self.result += 1

            return nodes_sum, nodes_count

        # call the function
        tree(root)
        return self.result
