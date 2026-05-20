# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def postOrderTraversal(node):
            if node == None:
                return node

            postOrderTraversal(node.left)
            postOrderTraversal(node.right)

            # Swap left & right child
            leftChild = node.left # temp storage variable
            node.left = node.right
            node.right = leftChild


        postOrderTraversal(root)

        return root
