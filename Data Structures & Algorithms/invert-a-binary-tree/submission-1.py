# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Base case is if not root or root has not children, then return root
        # Each call swaps the children and by the time we make it to the root node,
        # we'll have swapped all of the subtrees' children

        if not root:
            return root

        if not root.left and not root.right:
            return root

        self.invertTree(root.left)
        self.invertTree(root.right)
        root.left, root.right = root.right, root.left

        return root