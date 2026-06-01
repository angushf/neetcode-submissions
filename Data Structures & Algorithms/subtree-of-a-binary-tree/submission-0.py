# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def preOrderTraversal(node):
            if node == None:
                return False

            
            # Do something
            if node.val == subRoot.val:
                print(f"comparing {node.val} to {subRoot.val}")
                if isSameTree(node, subRoot):
                    return True

            return preOrderTraversal(node.left) or preOrderTraversal(node.right)



        def isSameTree(root, subroot):
            if root and not subroot:
                return False
            elif not root and subroot:
                return False
            elif not root and not subroot:
                return True


            left = isSameTree(root.left, subroot.left)
            right = isSameTree(root.right, subroot.right)
            # two heads exist
            return left and right and root.val == subroot.val


        return preOrderTraversal(root)