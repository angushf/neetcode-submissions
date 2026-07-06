# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        count = 0

        def bst_search(root):
            nonlocal count
            if not root:
                return

            if low <= root.val <= high:
                print(f"adding {root.val}")
                count += root.val

            bst_search(root.left)
            bst_search(root.right)

            # return




        bst_search(root)

        return count

        