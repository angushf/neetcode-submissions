# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        result = False

        def dfs(node, remaining):
            nonlocal result

            if not node:
                return

            if not node.left and not node.right:
                if node.val == remaining:
                    result = True
                return

            difference = remaining - node.val

            dfs(node.left, difference)
            dfs(node.right, difference)


        dfs(root, targetSum)
        return result