# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        result = None

        def inOrder(root):
            nonlocal result
            nonlocal k
            if not root or result is not None:
                return

            inOrder(root.left)
            k -= 1
            if k == 0:
                result = root.val
            inOrder(root.right)

        inOrder(root)
        return result