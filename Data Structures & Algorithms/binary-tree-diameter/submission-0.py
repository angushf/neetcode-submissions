# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0

        def postOrderTraversal(node):
            if node == None:
                return -1

            left = postOrderTraversal(node.left) + 1
            right = postOrderTraversal(node.right) + 1
            # Do something
            currentDiameter = left + right
            nonlocal diameter 
            diameter = max(diameter, currentDiameter)

            return max(left, right)

        postOrderTraversal(root)

        return diameter