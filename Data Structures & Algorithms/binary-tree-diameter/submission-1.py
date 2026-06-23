# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # Base case is if not root, return 0
        # We want a height() helper function that returns the height of each node + 1 to its parent
        # We don't care about the height but we will use it to update a global result variable
        # via result = max(result, l + r) where l, r respresent the height of l and r respectively
        # which represents the diameter of any node in the tree
        result = 0

        def height(root):
            nonlocal result
            if not root:
                return 0

            l = height(root.left)
            r = height(root.right)
            result = max(result, l+r)

            return 1 + max(l, r)

        height(root)
        return result