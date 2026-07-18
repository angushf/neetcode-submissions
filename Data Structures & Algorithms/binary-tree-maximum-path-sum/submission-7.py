# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        result = float("-inf")

        def height(node):
            nonlocal result
            if not node:
                return 0

            l = height(node.left)
            r = height(node.right)

            result = max(result, l + node.val + r)

            return max(node.val + max(l,r,0), 0)
            # return max(node.val,0) + max(l,r,0)


        height(root)
        return result