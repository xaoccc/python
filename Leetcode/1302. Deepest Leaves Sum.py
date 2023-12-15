# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def deepestLeavesSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return []

        queue = [root]
        deepest_leaves = []

        #  Number of loops are exactly as much as the number of tree levels.
        #  The last loop contains the deepest level nodes, then we exit the loop.
        while queue:
            nodes_num_at_current_level = len(queue)
            level_nodes = []

            for node in range(nodes_num_at_current_level):
                node = queue.pop(0)
                level_nodes.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            #  In each iteration, it essentially stores the values of the nodes at the deepest level encountered so far.
            deepest_leaves = level_nodes

        return sum(deepest_leaves)
