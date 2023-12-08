# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):

    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        if root is None:
            return

        result = []

        if root.left is not None:
            result += self.inorderTraversal(root.left)

        result.append(root.val)
        if root.right is not None:
            result += self.inorderTraversal(root.right)

        return result