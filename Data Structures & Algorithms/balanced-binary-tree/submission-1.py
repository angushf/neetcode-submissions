# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        result = True

        def postOrderTraversal(node):
            if node == None:
                return -1

            left = postOrderTraversal(node.left) + 1
            right = postOrderTraversal(node.right) + 1
            # Do work on parent node
            heightDifference = abs(left - right)
            nonlocal result
            if heightDifference > 1:
                result = False
            
            return max(left, right)

        postOrderTraversal(root)

        return result