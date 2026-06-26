# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        best = float('-inf')

        def height(root):
            nonlocal best
            if not root:
                return 0

            l = height(root.left)
            r = height(root.right)
            best = max(best, root.val + max(l, 0) + max(r,0))

            return max(root.val, root.val + max(l, r))


        height(root)
        return best

            