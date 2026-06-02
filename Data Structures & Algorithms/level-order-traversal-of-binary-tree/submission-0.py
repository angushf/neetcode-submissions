# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return []
            
        q = []
        level = 1
        q.append((root, level))

        result = []

        arr = []
        while len(q) != 0:
            item = q.pop(0)

            node = item[0]
            currLevel = item[1]

            arr.append(node.val)

            if node.left:
                q.append((node.left, currLevel + 1))
            if node.right:
                q.append((node.right, currLevel + 1))

            if q and q[0][1] != currLevel:
                result.append(arr)
                arr = []

        result.append(arr)
        return result

        
