# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        longestPath = 0

        def height(root):
            nonlocal longestPath
            if not root:
                return 0

            l = height(root.left)
            r = height(root.right)

            longestPath = max(longestPath, l+r)

            return max(l,r) + 1

        height(root)
        return longestPath