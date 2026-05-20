# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        def findDepth(node):
            if node == None:
                return 0

            left = findDepth(node.left) + 1
            right = findDepth(node.right) + 1

            return max(left, right)

        return findDepth(root)
