# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        lo = float("-inf")
        hi = float("inf")

        result = True

        def dfs(node, l, h):
            nonlocal result
            if not node:
                return 

            if not (l < node.val < h):
                result = False
            
            dfs(node.left, l, node.val)
            dfs(node.right, node.val, h)


        dfs(root, lo, hi)
        return result
