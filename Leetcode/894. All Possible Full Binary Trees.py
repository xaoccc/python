# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        if n % 2 == 0:
            return []
        dp = {1 : [TreeNode()] }

        def find_nodes(n):
            if n in dp:
                return dp[n]

            nodes = []
            # l is the number of left branch nodes, r is the number of right branch nodes
            for l in range(n):
                r = n - l - 1
                left_tree, right_tree = find_nodes(l), find_nodes(r)
                for t1 in  left_tree:
                    for t2 in right_tree:
                        nodes.append(TreeNode(0, t1, t2))
            dp[n] = nodes
            return dp[n]
            
        return find_nodes(n)

# Full explanation here: https://www.youtube.com/watch?v=nZtrZPTTCAo
