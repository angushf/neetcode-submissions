# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Base case is if not node then return 0
        # Each call returns 1 + max(maxDepth(node.left), maxDepth(node.right))

        if not root:
            return 0

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))