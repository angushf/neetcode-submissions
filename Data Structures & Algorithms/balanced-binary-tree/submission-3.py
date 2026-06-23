# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # Base case is if not root, return 0
        # We want a helper function height() that tracks height for both root.left and root.right
        # This will allow us to check for the balance condition at every node using the post-order traversal
        # if height of root.left is > abs(1) then we return False immediately.
        # return True at the end
        result = True

        def height(root):
            nonlocal result
            if not root:
                return 0

            l = height(root.left)
            r = height(root.right)

            if abs(l-r) > 1:
                result = False

            return 1 + max(l, r)



        height(root)

        return result