# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
      #We need a variable in the function rangeSumBST to store the result in
        _sum = 0
        #We need to use a recursive function to make this work
        def traverse(n):
           #To access the variable _sum, we need to use nonlocal
            nonlocal _sum
            #What is n???
            if n:
                if low <= n.val <= high:
                    _sum += n.val
                traverse(n.left)
                traverse(n.right)
        #Why is this here and how does _sum adds its value???
        traverse(root)
        return _sum
